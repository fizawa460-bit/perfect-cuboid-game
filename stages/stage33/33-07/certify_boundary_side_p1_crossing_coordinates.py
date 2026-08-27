#!/usr/bin/env python3
"""Certify explicit P1 coordinates for all 24 physical side conics.

The current arithmetic-HS repair needs actual geometric first-residue
functions, not only parity vectors on the boundary dual graph.  This leaf
source-locks the first constructive layer: every physical side conic is given
an explicit Pythagorean P1 parametrization and each of its six crossings with
the exceptional boundary is identified with t=0,infinity,+/-1,+/-i.

The computation is performed in the pinned Testa--Stoll model.  Magma checks
that every displayed point is one of the exact 48 singular points, lies on the
claimed conic, and exhausts that conic's full singular-point set.  It also
recomputes the cc/ct permutations from the defining equations.

This is deliberately not a Gersten lift and does not compute any entry of the
14x26 L-squareclass tensor.
"""

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

from stoll_cuboid_source import load_pinned_source, run_magma


HERE = Path(__file__).resolve().parent
OUT = HERE / "boundary-side-p1-crossing-coordinates.json"
PARAMETERS = ["0", "infinity", "1", "-1", "i", "-i"]


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


_, core, blob, _source_attempt = load_pinned_source()
code = core + r'''
uvs := [[L|0,1],[L|1,0],[L|1,1],[L|-1,1],[L|i,1],[L|-i,1]];
for j in [1..24] do
  fam := (j-1) div 8;
  r := (j-1) mod 8;
  e1 := [1,-1][(r div 4)+1];
  e2 := [1,-1][((r div 2) mod 2)+1];
  e3 := [1,-1][(r mod 2)+1];
  found := [];
  for z in [1..6] do
    u:=uvs[z][1]; v:=uvs[z][2];
    X:=u^2-v^2; Y:=2*u*v; Z:=u^2+v^2;
    if fam eq 0 then
      p:=Pr6![0,-e1*X,-e2*Y,-e3*Z,Y,X,Z];
    elif fam eq 1 then
      p:=Pr6![-e2*Y,0,-e1*X,X,-e3*Z,Y,Z];
    else
      p:=Pr6![-e1*X,-e2*Y,0,Y,X,-e3*Z,Z];
    end if;
    pos:=Position(pts,p);
    assert pos ne 0 and p in Cs[j];
    Append(~found,pos);
    printf "MAP|%o|%o|%o|%o|%o|%o|%o\n",j,fam+1,e1,e2,e3,z,pos;
  end for;
  assert #Seqset(found) eq 6;
  assert #Cpts[j] eq 6;
  assert forall{p : p in Cpts[j] | Position(pts,p) in found};
end for;

ccL := hom<L -> L | -i>;
ccPL := hom<R -> R | ccL*Bang(L,R), [R.j : j in [1..7]]>
  where R := CoordinateRing(Pr6);
actcc := func<C | Curve(Pr6, [ccPL(e) : e in DefiningEquations(C)])>;
permccC := [Position(C1s, actcc(C)) : C in C1s[1..24]];
permccP := [Position(pts, Pr6![ccL(a) : a in Eltseq(pt)]) : pt in pts];

ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL := hom<R -> R | ctL*Bang(L,R), [R.j : j in [1..7]]>
  where R := CoordinateRing(Pr6);
actct := func<C | Curve(Pr6, [ctPL(e) : e in DefiningEquations(C)])>;
permctC := [Position(C1s, actct(C)) : C in C1s[1..24]];
permctP := [Position(pts, Pr6![ctL(a) : a in Eltseq(pt)]) : pt in pts];

assert permccC eq [1..24] and permctC eq [1..24];
assert permctP eq [1..48];
for j in [1..24] do
  printf "GAL|CCC|%o|%o\n",j,permccC[j];
  printf "GAL|CTC|%o|%o\n",j,permctC[j];
end for;
for j in [1..48] do
  printf "GAL|CCP|%o|%o\n",j,permccP[j];
  printf "GAL|CTP|%o|%o\n",j,permctP[j];
end for;
'''

stdout, _magma_attempt = run_magma(
    code,
    240,
    "Stage33 side-P1 crossing coordinate certificate",
    user_agent="perfect-cuboid-stage33/3.1",
)

rows = []
perms = {}
for raw in stdout.splitlines():
    line = raw.strip().replace("\\n", "")
    if line.startswith("MAP|"):
        values = [int(x) for x in line.split("|")[1:]]
        if len(values) != 7:
            raise SystemExit(f"bad MAP row: {line}")
        rows.append(values)
    elif line.startswith("GAL|"):
        _, tag, source, image = line.split("|")
        source, image = int(source), int(image)
        perms.setdefault(tag, {})[source] = image

if len(rows) != 24 * 6:
    raise SystemExit(f"expected 144 side-crossing rows, got {len(rows)}")
if set(perms) != {"CCC", "CCP", "CTC", "CTP"}:
    raise SystemExit(f"missing Galois permutations: {sorted(perms)}")
perms = {
    tag: [mapping[j] for j in range(1, (24 if tag.endswith("C") else 48) + 1)]
    for tag, mapping in perms.items()
}
if perms["CCC"] != list(range(1, 25)) or perms["CTC"] != list(range(1, 25)):
    raise SystemExit(
        "physical side conics are no longer individually fixed: "
        f"cc={perms['CCC']} ct={perms['CTC']}"
    )
if perms["CTP"] != list(range(1, 49)):
    raise SystemExit("sqrt(2) unexpectedly moves a physical singular point")
ccp = perms["CCP"]
if sorted(ccp) != list(range(1, 49)) or any(ccp[ccp[j] - 1] != j + 1 for j in range(48)):
    raise SystemExit("complex-conjugation point permutation is not an involution")

by_side = defaultdict(list)
incidence = defaultdict(list)
for side, family, e1, e2, e3, z, point in rows:
    if not (1 <= side <= 24 and 1 <= family <= 3 and 1 <= z <= 6 and 1 <= point <= 48):
        raise SystemExit("MAP row escaped expected ranges")
    by_side[side].append((family, e1, e2, e3, z, point))
    incidence[point].append((side, z))

family_names = {1: "A1", 2: "A2", 3: "A3"}
formulas = {
    1: "[0,-e1*(u^2-v^2),-e2*(2uv),-e3*(u^2+v^2),2uv,u^2-v^2,u^2+v^2]",
    2: "[-e2*(2uv),0,-e1*(u^2-v^2),u^2-v^2,-e3*(u^2+v^2),2uv,u^2+v^2]",
    3: "[-e1*(u^2-v^2),-e2*(2uv),0,2uv,u^2-v^2,-e3*(u^2+v^2),u^2+v^2]",
}
side_records = []
for side in range(1, 25):
    entries = sorted(by_side[side], key=lambda x: x[4])
    if len(entries) != 6 or [x[4] for x in entries] != list(range(1, 7)):
        raise SystemExit(f"side {side} did not receive all six parameters")
    family, e1, e2, e3 = entries[0][:4]
    if any(x[:4] != (family, e1, e2, e3) for x in entries):
        raise SystemExit(f"side {side} sign/family regression")
    side_records.append({
        "side_id": f"SIDE_{family_names[family]}_{side - 8 * (family - 1):03d}",
        "upstream_C1s_index_1based": side,
        "family": family_names[family],
        "signs": {"e1": e1, "e2": e2, "e3": e3},
        "homogeneous_parameter": "t=u/v",
        "coordinate_order": ["a1", "a2", "a3", "b1", "b2", "b3", "c"],
        "parametrization": formulas[family],
        "crossings": [
            {"parameter": PARAMETERS[z - 1], "exceptional_id": f"EXC_{point:03d}"}
            for _, _, _, _, z, point in entries
        ],
    })

degree_histogram = Counter(len(incidence[j]) for j in range(1, 49))
if degree_histogram != Counter({2: 24, 4: 24}):
    raise SystemExit(f"exceptional incidence histogram regression: {degree_histogram}")

# Parameter conjugation is t -> conjugate(t); only +/-i are exchanged.
parameter_cc = [1, 2, 3, 4, 6, 5]
for side in side_records:
    lookup = {PARAMETERS.index(x["parameter"]) + 1: int(x["exceptional_id"][4:])
              for x in side["crossings"]}
    for z in range(1, 7):
        if ccp[lookup[z] - 1] != lookup[parameter_cc[z - 1]]:
            raise SystemExit(f"side parameter/cc mismatch on {side['side_id']} at {PARAMETERS[z-1]}")

exceptional_records = []
for point in range(1, 49):
    exceptional_records.append({
        "exceptional_id": f"EXC_{point:03d}",
        "incident_side_parameter_pairs": [
            {"side_index_1based": side, "parameter": PARAMETERS[z - 1]}
            for side, z in sorted(incidence[point])
        ],
        "complex_conjugate_exceptional_id": f"EXC_{ccp[point - 1]:03d}",
        "sqrt2_conjugate_exceptional_id": f"EXC_{point:03d}",
    })

cert = {
    "schema": "STAGE33_07_BOUNDARY_SIDE_P1_CROSSING_COORDINATES_V1",
    "source_locks": {
        "testa_stoll_commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "testa_stoll_cuboids_magma_blob_sha1": blob,
        "stoll_cuboid_source_py_sha256": hashlib.sha256(
            (HERE / "stoll_cuboid_source.py").read_bytes()
        ).hexdigest(),
    },
    "field": "L=Q(i,sqrt(2))",
    "physical_side_count": 24,
    "singular_point_exceptional_count": 48,
    "side_exceptional_crossing_count": 144,
    "parameter_support": PARAMETERS,
    "parameter_complex_conjugation_1based": parameter_cc,
    "parameter_sqrt2_conjugation_1based": list(range(1, 7)),
    "exceptional_complex_conjugation_1based": ccp,
    "exceptional_sqrt2_conjugation_1based": perms["CTP"],
    "exceptional_incidence_degree_histogram": {str(k): v for k, v in sorted(degree_histogram.items())},
    "side_models": side_records,
    "exceptional_incidence": exceptional_records,
    "exact_checks": {
        "all_24_side_parametrizations_checked_in_pinned_surface": True,
        "all_144_parameter_points_are_pinned_singular_points": True,
        "every_side_full_singular_set_exhausted": True,
        "all_side_parameter_points_distinct": True,
        "all_side_conics_individually_q_defined": True,
        "sqrt2_fixes_all_physical_side_and_exceptional_components": True,
        "complex_conjugation_matches_t_to_conjugate_t": True,
        "exceptional_incidence_histogram_matches_24_degree2_plus_24_degree4": True,
    },
    "constructive_progress": {
        "physical_side_first_residue_function_coordinates_materialized": True,
        "exceptional_P1_tangent_coordinates_materialized": False,
        "order2_source_first_residue_functions_materialized": False,
        "project_14x26_L_squareclass_tensor_materialized": False,
        "absolute_delta_loc_computed": False,
    },
    "next_exact_leaf": "L33-07-MATERIALIZE-48-EXCEPTIONAL-P1-TANGENT-COORDINATES-THEN-26-FIRST-RESIDUE-FUNCTIONS",
    "new_smallest_exact_kernel": "R33-BR2A-EXPLICIT-EXCEPTIONAL-P1-COORDINATES-AND-GLOBAL-GERSTEN-LIFTS",
    "arithmetic_hs_closed": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
    "execution": {
        "submitted_magma_sha256": hashlib.sha256(code.encode()).hexdigest(),
        "network_retry_counts_excluded_from_canonical_certificate": True,
    },
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "physical_side_count": 24,
    "crossing_count": 144,
    "exceptional_degree_histogram": cert["exceptional_incidence_degree_histogram"],
    "project_squareclass_tensor_materialized": False,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
