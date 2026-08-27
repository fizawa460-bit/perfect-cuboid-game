#!/usr/bin/env python3
"""Certify the order-two coefficient action and finite/absolute H^1 firewall.

K=Br(Sbar)[2] is the 14-dimensional F2 module already derived from the exact
endpoint discriminant certificate.  The producer provenance is pinned to the
Testa--Stoll model over L=Q(i,sqrt(2)); its two matrices are the actions of the
two generators of Gal(L/Q)=V4.  Therefore the *coefficient action* of G_Q on K
factors through this V4 and N=G_L acts trivially on K.

That factorization does NOT identify H^1(G_Q,K) with H^1(V4,K).  This script
independently recomputes H^1(V4,K) and H^2(V4,K) from the full inhomogeneous bar
complex and records the exact inflation--restriction segment

  0 -> H^1(V4,K) -> H^1(G_Q,K)
    -> Hom_cont(G_L,K)^V4 -> H^2(V4,K).

Thus a finite 16x26 delta_loc matrix captures only the inflated V4 component.
The restriction of the actual localization cocycle to G_L remains genuine
representative-level geometric lift data and is not manufactured here.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BR2 = HERE / "proper-brauer2-from-discriminant.json"
RECEIVER = HERE / "order2-localization-receiver.json"
PICDISC = HERE / "picard-discriminant-compact.json"
PRODUCER = HERE / "certify_proper_brauer2_from_discriminant.py"
EXTRACTOR = HERE / "extract_picard_discriminant_compact.py"
PIN_HELPER = HERE / "stoll_cuboid_source.py"
OUT = HERE / "order2-absolute-h1-inflation-restriction.json"
KDIM = 14
GORDER = 4
EXPECTED_UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_PICDISC = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"


def die(msg):
    raise SystemExit(msg)


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_locked(path, label):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.get("canonical_sha256")
    if not claimed:
        die(f"{label}: missing canonical_sha256")
    body = dict(obj)
    body.pop("canonical_sha256")
    actual = canonical_sha256(body)
    if actual != claimed:
        die(f"{label}: canonical hash mismatch claimed={claimed} actual={actual}")
    return obj


def binary_matrix(x, n, label):
    if not isinstance(x, list) or len(x) != n:
        die(f"{label}: expected {n} rows")
    out = []
    for row in x:
        if not isinstance(row, list) or len(row) != n:
            die(f"{label}: expected {n}x{n}")
        rr = [int(v) for v in row]
        if any(v not in (0, 1) for v in rr):
            die(f"{label}: non-binary entry")
        out.append(rr)
    return out


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x & y for x, y in zip(row, col)) & 1 for col in bt] for row in a]


def rank_bits(vectors):
    pivots = {}
    for value in vectors:
        v = int(value)
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)


def xor_image(vector, basis_images):
    out = 0
    v = int(vector)
    while v:
        low = v & -v
        i = low.bit_length() - 1
        out ^= basis_images[i]
        v ^= low
    return out


def put_row(out, block, row):
    base = block * KDIM
    for j, bit in enumerate(row):
        if bit:
            out ^= 1 << (base + j)
    return out


def basis_row(i):
    return [1 if j == i else 0 for j in range(KDIM)]


br2 = load_locked(BR2, "proper Br2")
receiver = load_locked(RECEIVER, "order2 localization receiver")
picdisc = load_locked(PICDISC, "Picard discriminant")
if picdisc["canonical_sha256"] != EXPECTED_PICDISC:
    die("Picard discriminant source lock moved")
if br2.get("source_locks", {}).get("picard_discriminant_compact_sha256") != EXPECTED_PICDISC:
    die("proper Br2 no longer locks the accepted Picard discriminant")
if br2.get("proper_geometric_Br2_dimension_f2") != KDIM:
    die("proper Br2 dimension regression")
if receiver.get("finite_receiver_module_dimension_f2") != KDIM:
    die("receiver module dimension regression")

# Provenance firewall for the coefficient action.  The accepted discriminant
# extraction is obtained from the pinned Testa--Stoll model over
# L=Q(i,sqrt(2)); cc and ct are exactly i->-i and sqrt(2)->-sqrt(2).
helper_text = PIN_HELPER.read_text(encoding="utf-8")
extractor_text = EXTRACTOR.read_text(encoding="utf-8")
producer_text = PRODUCER.read_text(encoding="utf-8")
required_helper = [
    f'UPSTREAM_BLOB="{EXPECTED_UPSTREAM_BLOB}"',
    'Cuboids/cuboids.magma',
]
required_extractor = [
    'ccL := hom<L -> L | -i>;',
    'ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;',
    'Gcc := Matrix(Integers()',
    'Gct := Matrix(Integers()',
    'assert Gcc^2 eq I64 and Gct^2 eq I64 and Gcc*Gct eq Gct*Gcc;',
]
required_producer = [
    'The Picard discriminant action is source-locked through the',
    'V4 splitting field Q(i,sqrt(2)).',
    "'equivariant_identification':'T/2T ~= A_T[2] via x mod 2T -> x/2 mod T'",
]
for s in required_helper:
    if s not in helper_text:
        die(f"pinned-source provenance moved: {s}")
for s in required_extractor:
    if s not in extractor_text:
        die(f"discriminant Galois-action provenance moved: {s}")
for s in required_producer:
    if s not in producer_text:
        die(f"proper-Br2 provenance moved: {s}")

cc = binary_matrix(br2["proper_Br2_cc_action_f2"], KDIM, "cc action")
ct = binary_matrix(br2["proper_Br2_ct_action_f2"], KDIM, "ct action")
I = eye(KDIM)
if matmul(cc, cc) != I or matmul(ct, ct) != I:
    die("pinned V4 generators are not involutions")
if matmul(cc, ct) != matmul(ct, cc):
    die("pinned V4 generators do not commute")

# Elements are 1, cc, ct, cc*ct; multiplication is xor on exponents.
elements = [(0, 0), (1, 0), (0, 1), (1, 1)]
index = {g: i for i, g in enumerate(elements)}
actions = [I, cc, ct, matmul(cc, ct)]


def mul(g, h):
    a, b = elements[g]
    c, d = elements[h]
    return index[(a ^ c, b ^ d)]


# Full inhomogeneous bar cochains, including identity arguments.
C0 = KDIM
C1 = GORDER * KDIM
C2 = GORDER * GORDER * KDIM
C3 = GORDER * GORDER * GORDER * KDIM

# d0(m)(g) = m.g + m.
d0 = []
for i in range(KDIM):
    out = 0
    e = basis_row(i)
    for g in range(GORDER):
        row = [x ^ y for x, y in zip(actions[g][i], e)]
        out = put_row(out, g, row)
    d0.append(out)

# d1(f)(g,h) = f(g).h + f(h) + f(gh).
d1 = []
for source_g in range(GORDER):
    for i in range(KDIM):
        out = 0
        e = basis_row(i)
        for g in range(GORDER):
            for h in range(GORDER):
                block = g * GORDER + h
                row = [0] * KDIM
                if g == source_g:
                    row = [x ^ y for x, y in zip(row, actions[h][i])]
                if h == source_g:
                    row = [x ^ y for x, y in zip(row, e)]
                if mul(g, h) == source_g:
                    row = [x ^ y for x, y in zip(row, e)]
                out = put_row(out, block, row)
        d1.append(out)

# d2(c)(g,h,k) = c(g,h).k + c(gh,k) + c(g,hk) + c(h,k).
d2 = []
for source_g in range(GORDER):
    for source_h in range(GORDER):
        for i in range(KDIM):
            out = 0
            e = basis_row(i)
            for g in range(GORDER):
                for h in range(GORDER):
                    for k in range(GORDER):
                        block = (g * GORDER + h) * GORDER + k
                        row = [0] * KDIM
                        if g == source_g and h == source_h:
                            row = [x ^ y for x, y in zip(row, actions[k][i])]
                        if mul(g, h) == source_g and k == source_h:
                            row = [x ^ y for x, y in zip(row, e)]
                        if g == source_g and mul(h, k) == source_h:
                            row = [x ^ y for x, y in zip(row, e)]
                        if h == source_g and k == source_h:
                            row = [x ^ y for x, y in zip(row, e)]
                        out = put_row(out, block, row)
            d2.append(out)

if len(d0) != C0 or len(d1) != C1 or len(d2) != C2:
    die("bar-complex basis cardinality regression")
if any(xor_image(v, d1) for v in d0):
    die("bar complex regression: d1*d0 != 0")
if any(xor_image(v, d2) for v in d1):
    die("bar complex regression: d2*d1 != 0")

r0 = rank_bits(d0)
r1 = rank_bits(d1)
r2 = rank_bits(d2)
ker1 = C1 - r1
ker2 = C2 - r2
h1 = ker1 - r0
h2 = ker2 - r1
if (r0, r1, r2, h1, h2) != (4, 36, 166, 16, 22):
    die(f"finite V4 bar-complex regression {(r0,r1,r2,h1,h2)}")
if receiver.get("finite_receiver_H1_dimension_f2") != h1:
    die("independent bar H1 disagrees with localization receiver")
if br2.get("finite_v4_H1_proper_Br2", {}).get("H1_dimension_f2") != h1:
    die("independent bar H1 disagrees with proper-Br2 certificate")

cert = {
    "schema": "STAGE33_07_ORDER2_ABSOLUTE_H1_INFLATION_RESTRICTION_V2",
    "source_locks": {
        "proper_brauer2_sha256": br2["canonical_sha256"],
        "picard_discriminant_compact_sha256": picdisc["canonical_sha256"],
        "order2_localization_receiver_sha256": receiver["canonical_sha256"],
        "testa_stoll_upstream_git_blob_sha1": EXPECTED_UPSTREAM_BLOB,
        "stoll_cuboid_source_py_sha256": file_sha256(PIN_HELPER),
        "extract_picard_discriminant_compact_py_sha256": file_sha256(EXTRACTOR),
        "certify_proper_brauer2_from_discriminant_py_sha256": file_sha256(PRODUCER),
    },
    "coefficient_module": "K=Br(Sbar)[2]",
    "coefficient_dimension_f2": KDIM,
    "coefficient_action_factorization": {
        "splitting_field": "L=Q(i,sqrt(2))",
        "quotient": "Gal(L/Q)=V4=<cc,ct>",
        "cc": "i -> -i, sqrt(2) fixed",
        "ct": "sqrt(2) -> -sqrt(2), i fixed",
        "kernel": "N=G_L=Gal(Qbar/L)",
        "N_action_on_K": "TRIVIAL",
        "absolute_GQ_action_on_K_factors_through_V4": True,
        "scope": "COEFFICIENT_MODULE_ONLY; no factorization of the lift torsor/ambient extension is inferred",
    },
    "bar_complex": {
        "convention": "full inhomogeneous cochains; row-vector/right-action; characteristic two",
        "C0_dimension_f2": C0,
        "C1_dimension_f2": C1,
        "C2_dimension_f2": C2,
        "C3_dimension_f2": C3,
        "rank_d0_f2": r0,
        "rank_d1_f2": r1,
        "rank_d2_f2": r2,
        "kernel_d1_dimension_f2": ker1,
        "kernel_d2_dimension_f2": ker2,
        "d1_after_d0_zero": True,
        "d2_after_d1_zero": True,
        "H1_V4_K_dimension_f2": h1,
        "H2_V4_K_dimension_f2": h2,
    },
    "independent_finite_receiver_consistency": {
        "existing_receiver_H1_dimension_f2": receiver["finite_receiver_H1_dimension_f2"],
        "proper_br2_certificate_H1_dimension_f2": br2["finite_v4_H1_proper_Br2"]["H1_dimension_f2"],
        "bar_complex_H1_dimension_f2": h1,
        "all_equal": True,
    },
    "inflation_restriction": {
        "hypothesis_status": "CERTIFIED_FOR_THE_COEFFICIENT_ACTION",
        "exact_segment": "0 -> H^1(V4,K) -> H^1(G_Q,K) -> Hom_cont(G_L,K)^V4 -> H^2(V4,K)",
        "finite_inflated_subspace_dimension_f2": h1,
        "transgression_target_dimension_f2": h2,
        "restriction_term": "Hom_cont(G_L,K)^V4",
        "restriction_term_certified_zero": False,
        "interpretation": "finite V4 H1 is the exact inflated subspace, but G_L-character classes may contribute to absolute H1 subject to transgression",
    },
    "project_status": {
        "absolute_GQ_action_factorization_through_this_V4_certified": True,
        "absolute_H1_identified_with_finite_V4_H1": False,
        "finite_16x26_delta_loc_is_absolute_delta_loc": False,
        "finite_delta_loc_adapter_scope": "INFLATED_FINITE_V4_COMPONENT_ONLY",
        "real_project_ambient_gersten_v4_extension_materialized": False,
        "project_finite_v4_delta_loc_matrix_computed": False,
        "restriction_of_project_localization_cocycle_to_G_L_computed": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_hs_closed": False,
        "stage33_progress": "6/11",
    },
    "remaining_exact_inputs": [
        "representative-level geometric Gersten lift torsor with exact G_Q action, sufficient to materialize the real finite V4 extension component",
        "restriction of each project localization cocycle to G_L, equivalently the Hom_cont(G_L,K)^V4 component, or an exact proof that all 26 restrictions vanish",
    ],
    "new_smallest_exact_kernel": "R33-BR2A-REAL-GEOMETRIC-LIFT-GQ-EXTENSION-AND-GL-CHARACTER-DATA",
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "rank_d0": r0,
    "rank_d1": r1,
    "rank_d2": r2,
    "H1_V4_K_dimension_f2": h1,
    "H2_V4_K_dimension_f2": h2,
    "absolute_GQ_action_factorization_through_V4_certified": True,
    "absolute_H1_identified_with_finite_V4_H1": False,
    "G_L_restriction_component_computed": False,
    "absolute_delta_loc_computed": False,
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
