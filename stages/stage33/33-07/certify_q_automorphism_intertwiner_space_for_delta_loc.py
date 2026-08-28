#!/usr/bin/env python3
"""Constrain the 26x16 finite localization map by Q-defined automorphisms.

The actual localization connecting homomorphism is functorial for automorphisms
of the pair (S,boundary).  The pinned Testa--Stoll model has eight elementary
automorphisms defined over Q that preserve the physical 72-component boundary:
2 coordinate transpositions and 6 coordinate sign flips.

This leaf computes, in the already-locked Stage33-07 coordinates,

  * their action on the 26-dimensional residue source A[2];
  * their action on K=Br(Sbar)[2] and hence H^1(V4,K)=F2^16; and
  * the exact F2 dimension of the intertwiner space containing delta_loc.

No arbitrary extension class is selected.  If the intertwiner space is zero,
naturality itself forces the finite V4 connecting map to vanish; otherwise the
remaining dimension is the new exact ambiguity size.
"""
import ast
import hashlib
import json
import re
import runpy
from pathlib import Path

from stoll_cuboid_source import load_pinned_source, run_magma

HERE = Path(__file__).resolve().parent
BASE_SCRIPT = HERE / "materialize_order2_first_residue_functions.py"
IB_PATH = HERE / "two-primary-residue-invariant-basis.json"
BR2_PATH = HERE / "proper-brauer2-from-discriminant.json"
RECEIVER_PATH = HERE / "order2-localization-receiver.json"
OUTPUT = HERE / "q-automorphism-delta-loc-intertwiner-space.json"

EXPECTED_IB = "f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939"
EXPECTED_BR2 = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_RECEIVER = "9280846c6e7ae8a043e36c7b5498f11476901567b229b94e953b79afab891bda"
AUTO_NAMES = [
    "swap_a1_a2_b1_b2",
    "swap_a1_a3_b1_b3",
    "sign_a1",
    "sign_a2",
    "sign_a3",
    "sign_b1",
    "sign_b2",
    "sign_b3",
]
N = 14
QDIM = 26
H1DIM = 16


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.get("canonical_sha256")
    body = dict(obj)
    body.pop("canonical_sha256", None)
    actual = canonical_sha256(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"source lock moved for {path.name}: {claimed} {actual}")
    return obj


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def row_basis(rows, ncols):
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    if any(len(row) != ncols for row in a):
        raise SystemExit("GF2 row width regression")
    r = 0
    pivots = []
    for c in range(ncols):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = xor(a[i], a[r])
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a[:r], pivots


def rank2(rows, ncols):
    return len(row_basis(rows, ncols)[0])


def build_solver(basis):
    pivots = {}
    for i, row in enumerate(basis):
        x = sum((int(b) & 1) << j for j, b in enumerate(row))
        coord = 1 << i
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                bx, bc = pivots[p]
                x ^= bx
                coord ^= bc
            else:
                pivots[p] = (x, coord)
                break
        if not x:
            raise SystemExit("coordinate basis is dependent")

    def solve(row):
        x = sum((int(b) & 1) << j for j, b in enumerate(row))
        coord = 0
        while x:
            p = x.bit_length() - 1
            if p not in pivots:
                raise SystemExit("target escaped coordinate span")
            bx, bc = pivots[p]
            x ^= bx
            coord ^= bc
        return [(coord >> i) & 1 for i in range(len(basis))]

    return solve


def rowmul_z(v, M):
    return [sum(int(v[k]) * int(M[k][j]) for k in range(len(v))) for j in range(len(M[0]))]


def rowmul2(v, M):
    return [sum((int(v[k]) & 1) * (int(M[k][j]) & 1) for k in range(len(v))) & 1 for j in range(len(M[0]))]


def matmul2(A, B):
    return [rowmul2(row, B) for row in A]


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def transpose(A):
    return [list(col) for col in zip(*A)]


def permute_vector(row, perm, modulus):
    out = [0] * len(row)
    for i, value in enumerate(row):
        out[perm[i]] = int(value) % modulus
    return out


def rank_bitmasks(rows):
    pivots = {}
    for x in rows:
        x = int(x)
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


# Reconstruct the exact boundary source lattice and quotient basis.
ns = runpy.run_path(str(BASE_SCRIPT))
edges = ns["edges"]
edge_index = ns["edge_index"]
U44 = ns["U44"]
R17 = ns["R17"]
O4 = ns["O4"]
solve61 = ns["solve61"]
br0g = ns["br0g"]

ib = load_locked(IB_PATH, EXPECTED_IB)
br2 = load_locked(BR2_PATH, EXPECTED_BR2)
receiver = load_locked(RECEIVER_PATH, EXPECTED_RECEIVER)

if len(edges) != 144 or len(U44) != 44 or len(R17) != 17 or len(O4) != 12:
    raise SystemExit("boundary raw basis shape regression")
if receiver["finite_source_order2_dimension_f2"] != QDIM:
    raise SystemExit("source dimension regression")
if receiver["finite_receiver_H1_dimension_f2"] != H1DIM:
    raise SystemExit("receiver H1 dimension regression")

# ---------------------------------------------------------------------------
# Magma: compute the same eight Q-defined automorphisms on the physical
# boundary and on A_T[2] in the frozen compact-discriminant Smith basis.
# ---------------------------------------------------------------------------
_, core, upstream_blob, source_attempt = load_pinned_source()
extra = r'''
actperm := func<g, perm | qPic(Big![e[perm[j]] : j in [1..#e]]) where e := Eltseq(g @@ qPic)>;
act := func<sch, subs | Curve(Pr6, [Evaluate(e, subs) : e in DefiningEquations(sch)])>;
function actpt(pt, subs)
  i0 := 1; while pt[i0] eq 0 do i0 +:= 1; end while;
  pteqns := [Pr6.j*pt[i0] - Pr6.i0*pt[j] : j in [1..7] | j ne i0];
  return Rep(Points(Scheme(Pr6, [Evaluate(e, subs) : e in pteqns])));
end function;

ccL := hom<L -> L | -i>;
ccPL := hom<R -> R | ccL*Bang(L,R), [R.j : j in [1..7]]> where R := CoordinateRing(Pr6);
actcc := func<C | Curve(Pr6, [ccPL(e) : e in DefiningEquations(C)])>;
permcc := [Position(C1s, actcc(C)) : C in C1s]
 cat [#C1s+Position(C2s, actcc(C)) : C in C2s]
 cat [#C1s+#C2s+Position(C3s, actcc(C)) : C in C3s]
 cat [#Cs+Position(pts, Pr6![ccL(a) : a in Eltseq(pt)]) : pt in pts];
Gcc := Matrix(Integers(), [Eltseq(actperm(Pic.j, permcc)) : j in [1..64]]);

ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL := hom<R -> R | ctL*Bang(L,R), [R.j : j in [1..7]]> where R := CoordinateRing(Pr6);
actct := func<C | Curve(Pr6, [ctPL(e) : e in DefiningEquations(C)])>;
permct := [Position(C1s, actct(C)) : C in C1s]
 cat [#C1s+Position(C2s, actct(C)) : C in C2s]
 cat [#C1s+#C2s+Position(C3s, actct(C)) : C in C3s]
 cat [#Cs+Position(pts, Pr6![ctL(a) : a in Eltseq(pt)]) : pt in pts];
Gct := Matrix(Integers(), [Eltseq(actperm(Pic.j, permct)) : j in [1..64]]);

D, _, V := SmithForm(pmPic : Optimize := false);
diag := [Abs(Integers()!D[j,j]) : j in [1..64]];
pos := [j : j in [1..64] | diag[j] gt 1];
mods := [diag[j] : j in pos];
assert mods eq [2 : j in [1..4]] cat [4 : j in [1..6]] cat [8 : j in [1..4]];
scales := [m div 2 : m in mods];
Vin := V^-1;

function AT2Rows(G)
  B := Vin * Transpose(G^-1) * V;
  assert IsIntegral(B);
  rows := [];
  for a in [1..14] do
    row := [];
    for b in [1..14] do
      num := scales[a] * Integers()!B[pos[a],pos[b]];
      assert num mod scales[b] eq 0;
      Append(~row, (num div scales[b]) mod 2);
    end for;
    Append(~rows,row);
  end for;
  return rows;
end function;

cc2 := AT2Rows(Gcc); ct2 := AT2Rows(Gct);
for a in [1..14] do
  printf "GALCC_ROW_%o=%o\n",a,cc2[a];
  printf "GALCT_ROW_%o=%o\n",a,ct2[a];
end for;

subs := [
 [a2,a1,a3,b2,b1,b3,c],
 [a3,a2,a1,b3,b2,b1,c],
 [-a1,a2,a3,b1,b2,b3,c],
 [a1,-a2,a3,b1,b2,b3,c],
 [a1,a2,-a3,b1,b2,b3,c],
 [a1,a2,a3,-b1,b2,b3,c],
 [a1,a2,a3,b1,-b2,b3,c],
 [a1,a2,a3,b1,b2,-b3,c]
];
I64 := IdentityMatrix(Integers(),64);
for z in [1..#subs] do
  su := subs[z];
  sidep := [Position(C1s, act(C,su)) : C in C1s[1..24]];
  assert forall{x : x in sidep | 1 le x and x le 24};
  pointp := [Position(pts, actpt(pt,su)) : pt in pts];
  assert Seqset(pointp) eq {1..48};
  pfull := [Position(C1s, act(C,su)) : C in C1s]
    cat [#C1s+Position(C2s, act(C,su)) : C in C2s]
    cat [#C1s+#C2s+Position(C3s, act(C,su)) : C in C3s]
    cat [#Cs+Position(pts, actpt(pt,su)) : pt in pts];
  G := Matrix(Integers(), [Eltseq(actperm(Pic.j,pfull)) : j in [1..64]]);
  assert G*pmPic*Transpose(G) eq pmPic;
  assert G^2 eq I64;
  assert G*Gcc eq Gcc*G and G*Gct eq Gct*G;
  rows := AT2Rows(G);
  printf "AUTO_%o_SIDE=%o\n",z,sidep;
  printf "AUTO_%o_POINT=%o\n",z,pointp;
  for a in [1..14] do
    printf "AUTO_%o_AT2_ROW_%o=%o\n",z,a,rows[a];
  end for;
end for;
printf "STAGE33_Q_AUTOMORPHISM_DONE\n";
'''
code = "SetColumns(0);\nquick := true;\n" + core + "\n" + extra
stdout, magma_attempt = run_magma(
    code,
    300,
    "Stage33-07 Q-automorphism delta_loc naturality",
    user_agent="perfect-cuboid-stage33/3.3",
)
if "STAGE33_Q_AUTOMORPHISM_DONE" not in stdout or any(
    marker in stdout for marker in ("Runtime error", "Internal error", "Assertion failed")
):
    print(stdout)
    raise SystemExit("Q-automorphism Magma certificate failed")


def grab(name):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing Magma output {name}")
    return ast.literal_eval(m.group(1))


cc2 = [[int(x) & 1 for x in grab(f"GALCC_ROW_{r}")] for r in range(1, 15)]
ct2 = [[int(x) & 1 for x in grab(f"GALCT_ROW_{r}")] for r in range(1, 15)]
if cc2 != br2["A_T_two_torsion_cc_action_f2"] or ct2 != br2["A_T_two_torsion_ct_action_f2"]:
    raise SystemExit("Magma Smith basis moved relative to frozen proper Br2 certificate")

# H1 quotient-coordinate solver.
b1 = [[int(x) & 1 for x in row] for row in receiver["finite_receiver_B1_basis_f2_28"]]
h1 = [[int(x) & 1 for x in row] for row in receiver["finite_receiver_H1_quotient_representatives_f2_28"]]
if rank2(b1 + h1, 28) != 20:
    raise SystemExit("B1+H1 coordinate frame regression")
solve_h1 = build_solver(b1 + h1)

T = [[int(x) for x in row] for row in ib["smith_right_unimodular_T"]]
diag29 = [int(x) for x in ib["smith_diagonal"]]
if diag29 != [1] * 3 + [2] * 23 + [4] * 3:
    raise SystemExit("Smith diagonal regression")
source_basis = receiver["finite_source_basis"]
if len(source_basis) != QDIM:
    raise SystemExit("source basis length regression")
support_to_source = {}
for source_index, rec in enumerate(source_basis):
    smith = [int(x) for x in rec["smith_coordinates_Z29"]]
    support = [j for j, x in enumerate(smith) if x]
    if len(support) != 1:
        raise SystemExit("A2 Smith basis support regression")
    support_to_source[support[0]] = (source_index, smith[support[0]])
if len(support_to_source) != QDIM:
    raise SystemExit("A2 Smith supports not distinct")

relation29 = [[int(x) for x in row] for row in br0g["diagnostic_quotient_by_U44_relation_matrix_29x29"]]
if len(relation29) != 29 or any(len(row) != 29 for row in relation29):
    raise SystemExit("29-generator relation matrix regression")

records = []
constraint_rows = []
progressive = []
for auto_index, name in enumerate(AUTO_NAMES, 1):
    sidep = [int(x) - 1 for x in grab(f"AUTO_{auto_index}_SIDE")]
    pointp = [int(x) - 1 for x in grab(f"AUTO_{auto_index}_POINT")]
    if sorted(sidep) != list(range(24)) or sorted(pointp) != list(range(48)):
        raise SystemExit(f"{name}: boundary permutation regression")
    vertex_perm = sidep + [24 + x for x in pointp]
    edge_perm = [edge_index[(vertex_perm[a], vertex_perm[b])] for a, b in edges]
    if sorted(edge_perm) != list(range(144)):
        raise SystemExit(f"{name}: crossing permutation regression")

    # U44 is an intrinsic unit-symbol subspace and must be preserved exactly.
    for u in U44:
        coords = solve61(permute_vector(u, edge_perm, 2))
        if any(coords[44:]):
            raise SystemExit(f"{name}: U44 escaped itself")

    # Action on the 17 order-two quotient generators.
    r_action = []
    for row in R17:
        coords = solve61(permute_vector(row, edge_perm, 2))
        r_action.append([int(x) & 1 for x in coords[44:]])

    # The twelve oriented Q(i)-component order-four generators are permuted,
    # possibly with inversion.  Fail closed if an R17 correction appears.
    o_action = []
    for j, row in enumerate(O4):
        image = permute_vector(row, edge_perm, 4)
        matches = []
        for k, target in enumerate(O4):
            if image == target:
                matches.append((k, 1))
            if image == [(-int(x)) % 4 for x in target]:
                matches.append((k, -1))
        if len(matches) != 1:
            raise SystemExit(f"{name}: O4_{j+1} is not a unique signed O4 generator: {matches}")
        o_action.append(matches[0])

    A29 = []
    for i in range(17):
        A29.append(r_action[i] + [0] * 12)
    for j in range(12):
        row = [0] * 29
        target, sign = o_action[j]
        row[17 + target] = sign
        A29.append(row)

    # Check the geometric raw action descends through the exact retained
    # relation lattice, using the frozen Smith quotient.
    for rel in relation29:
        image_rel = rowmul_z(rel, A29)
        smith_rel = rowmul_z(image_rel, T)
        if any(smith_rel[j] % diag29[j] for j in range(29)):
            raise SystemExit(f"{name}: relation lattice not preserved")

    # Restrict the 29-generator action to the exact A[2] Smith basis.
    source_action = []
    for rec in source_basis:
        original = [int(x) for x in rec["original_R17_O12_coordinates_Z29"]]
        image = rowmul_z(original, A29)
        smith = rowmul_z(image, T)
        out = [0] * QDIM
        for j, d in enumerate(diag29):
            value = smith[j] % d
            if value == 0:
                continue
            if j not in support_to_source:
                raise SystemExit(f"{name}: image hit trivial Smith coordinate {j}")
            source_index, basis_value = support_to_source[j]
            if value != basis_value % d:
                raise SystemExit(f"{name}: A2 image is not order-two basis-valued at Smith {j}: {value}")
            out[source_index] ^= 1
        source_action.append(out)
    if rank2(source_action, QDIM) != QDIM or matmul2(source_action, source_action) != eye(QDIM):
        raise SystemExit(f"{name}: source A2 action is not an involutive automorphism")

    at2 = [[int(x) & 1 for x in grab(f"AUTO_{auto_index}_AT2_ROW_{r}")] for r in range(1, 15)]
    proper = transpose(at2)
    if matmul2(proper, proper) != eye(N):
        raise SystemExit(f"{name}: proper Br2 action is not involutive")
    if matmul2(proper, br2["proper_Br2_cc_action_f2"]) != matmul2(br2["proper_Br2_cc_action_f2"], proper):
        raise SystemExit(f"{name}: proper action does not commute with cc")
    if matmul2(proper, br2["proper_Br2_ct_action_f2"]) != matmul2(br2["proper_Br2_ct_action_f2"], proper):
        raise SystemExit(f"{name}: proper action does not commute with ct")

    # Induced action on H^1(V4,K): apply the proper-Br2 automorphism to both
    # cocycle values and reduce modulo the frozen B1 basis.
    h1_action = []
    for z in h1:
        transformed = rowmul2(z[:N], proper) + rowmul2(z[N:], proper)
        coeff = solve_h1(transformed)
        h1_action.append(coeff[4:])
    if rank2(h1_action, H1DIM) != H1DIM or matmul2(h1_action, h1_action) != eye(H1DIM):
        raise SystemExit(f"{name}: H1 action is not an involutive automorphism")

    # Naturality for D: A2 -> H1 in row convention is S*D = D*R.
    local_equations = []
    for i in range(QDIM):
        for j in range(H1DIM):
            mask = 0
            for k in range(QDIM):
                if source_action[i][k]:
                    mask ^= 1 << (k * H1DIM + j)
            for ell in range(H1DIM):
                if h1_action[ell][j]:
                    mask ^= 1 << (i * H1DIM + ell)
            if mask:
                local_equations.append(mask)
    constraint_rows.extend(local_equations)
    total_rank = rank_bitmasks(constraint_rows)
    remaining = QDIM * H1DIM - total_rank
    progressive.append({
        "after_generator": name,
        "constraint_rank_f2": total_rank,
        "intertwiner_dimension_f2": remaining,
    })
    records.append({
        "name": name,
        "boundary_side_permutation_1based": [x + 1 for x in sidep],
        "boundary_exceptional_permutation_1based": [x + 1 for x in pointp],
        "source_A2_action_f2": source_action,
        "proper_Br2_action_f2": proper,
        "finite_H1_action_f2": h1_action,
        "O4_signed_permutation": [
            {"source_1based": j + 1, "target_1based": target + 1, "sign": sign}
            for j, (target, sign) in enumerate(o_action)
        ],
    })

final_rank = rank_bitmasks(constraint_rows)
remaining_dim = QDIM * H1DIM - final_rank
finite_delta_forced_zero = remaining_dim == 0

cert = {
    "schema": "STAGE33_07_Q_AUTOMORPHISM_DELTA_LOC_INTERTWINER_SPACE_V1",
    "source_locks": {
        "upstream_testa_stoll_git_blob_sha1": upstream_blob,
        "two_primary_residue_invariant_basis_sha256": EXPECTED_IB,
        "proper_brauer2_from_discriminant_sha256": EXPECTED_BR2,
        "order2_localization_receiver_sha256": EXPECTED_RECEIVER,
        "submitted_magma_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    },
    "execution": {
        "source_fetch_attempt": source_attempt,
        "magma_request_attempt": magma_attempt,
    },
    "naturality_statement": {
        "q_defined_automorphism_generators_used": AUTO_NAMES,
        "generator_count": len(AUTO_NAMES),
        "all_generators_preserve_the_24_physical_side_curves_and_48_exceptional_curves": True,
        "all_generators_commute_with_V4_galois_action": True,
        "all_generators_preserve_U44_and_the_exact_29_generator_residue_quotient": True,
        "connecting_map_equivariance_equation": "S_phi * D = D * R_phi for D in Mat_{26x16}(F2)",
    },
    "progressive_intertwiner_reduction": progressive,
    "final_intertwiner": {
        "ambient_matrix_space_dimension_f2": QDIM * H1DIM,
        "naturality_constraint_rank_f2": final_rank,
        "intertwiner_dimension_f2": remaining_dim,
        "compatible_connecting_map_count": "1" if finite_delta_forced_zero else f"2^{remaining_dim}",
        "finite_v4_delta_loc_forced_zero_by_q_automorphism_naturality": finite_delta_forced_zero,
    },
    "automorphism_records": records,
    "exact_consequence": {
        "all_26_source_columns_treated_uniformly": True,
        "arbitrary_endpoint_compatible_extension_dimension_f2_before_naturality": 416,
        "remaining_extension_ambiguity_dimension_f2_after_q_automorphism_naturality": remaining_dim,
        "connecting_matrix_columns_explicitly_materialized": 0,
        "middle_gersten_module_action_materialized": False,
        "finite_v4_delta_loc_computed_without_explicit_middle_module": finite_delta_forced_zero,
        "absolute_delta_loc_computed": False,
        "project_14x26_L_squareclass_tensor_materialized": False,
        "arithmetic_HS_closed": False,
    },
    "next_exact_leaf": (
        "L33-07-PROMOTE-FINITE-V4-DELTA-LOC-ZERO-THEN-ATTACK-14x26-GL-SQUARECLASS-TENSOR"
        if finite_delta_forced_zero
        else "L33-07-ADD-REMAINING-Q-DEFINED-AUTOMORPHISM-NATURALITY-OR-GEOMETRIC-MIDDLE-DATA-TO-RESOLVE-INTERTWINER"
    ),
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_existence_claim": False,
    "perfect_cuboid_nonexistence_claim": False,
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUTPUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "q_defined_automorphism_generators": len(AUTO_NAMES),
    "ambient_extension_dimension_f2": 416,
    "naturality_constraint_rank_f2": final_rank,
    "remaining_intertwiner_dimension_f2": remaining_dim,
    "finite_v4_delta_loc_forced_zero": finite_delta_forced_zero,
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
