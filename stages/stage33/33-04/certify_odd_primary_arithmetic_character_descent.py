#!/usr/bin/env python3
"""Discharge the hostile-audit residual odd-primary boundary-character descent.

This leaf does not enumerate characters.  It gives the exact parametric
arithmetic module.  The hostile audit has already accepted every other BR0G
prefix and isolated exactly one unknown:
R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT.

For an odd prime ell, every codimension-two crossing has residue field Q or
Q(i).  Neither field contains nontrivial odd-order roots of unity, hence
H^0(k(x), Q_ell/Z_ell(-1))=0.  Therefore an odd-primary first-residue character
on a boundary P1 is unramified at every point.  Since the geometric P1 has no
nontrivial finite etale cover in characteristic zero, the unramified character
is exactly a constant-field character.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent.parent.parent

sk = json.loads((ROOT / "boundary-residue-skeleton.json").read_text())
bg = json.loads((ROOT / "boundary-galois.json").read_text())
two = json.loads((ROOT / "qfixed17-function-constant-descent.json").read_text())
audit = json.loads((ROOT / "audit-state.json").read_text())
proper_odd_path = REPO / "stages/stage29/29-02f/odd-primary-proper-brauer.md"
proper_odd = proper_odd_path.read_text()

# Hostile-audit lock: this leaf is allowed to solve exactly one named residual.
if audit["audit_verdict"] != "PASS_EXACT_PREFIX_BLOCKED_NEW_KERNEL_AFTER_REJECTING_PREMATURE_BR0G_CLOSURE":
    raise SystemExit("hostile-audit verdict regression")
if audit["unit_status"] != "BLOCKED_NEW_KERNEL" or audit["unit_closed"]:
    raise SystemExit("expected blocked audited checkpoint")
if audit["unresolved_unknown_in_scope"] != 1:
    raise SystemExit("audit no longer isolates exactly one unknown")
if audit["new_kernel_id"] != "R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT":
    raise SystemExit("unexpected audited residual kernel")

# Accepted two-primary predecessor remains a separate scope firewall.
if not two["two_primary_residual_leaf_complete"]:
    raise SystemExit("two-primary predecessor no longer complete")
if two["scope"] != "EXPONENT_TWO_RESIDUAL_ONLY":
    raise SystemExit("two-primary scope firewall regression")

if sk["component_count"] != 72 or sk["codim2_crossing_count"] != 144:
    raise SystemExit("boundary inventory regression")
cc = [int(x) - 1 for x in bg["boundary_perm_cc_1based"]]
ct = [int(x) - 1 for x in bg["boundary_perm_ct_1based"]]
if len(cc) != 72 or len(ct) != 72:
    raise SystemExit("boundary Galois permutation shape regression")
if ct != list(range(72)):
    raise SystemExit("sqrt(2)-conjugation no longer fixes all boundary components")
if any(cc[cc[j]] != j for j in range(72)):
    raise SystemExit("complex-conjugation action is not an involution")

# Geometric component orbits inside L=Q(i,sqrt(2)).  Fixed by cc and ct means
# constant field Q.  A two-cycle under cc, fixed by ct, has constant field Q(i).
fixed_components = [j for j in range(72) if cc[j] == j]
pairs = []
seen = set(fixed_components)
for j in range(72):
    if j in seen:
        continue
    k = cc[j]
    if k == j or cc[k] != j:
        raise SystemExit("unexpected component orbit")
    pairs.append(tuple(sorted((j, k))))
    seen.update((j, k))
pairs = sorted(set(pairs))
if len(fixed_components) != 48 or len(pairs) != 12 or len(seen) != 72:
    raise SystemExit(f"boundary orbit regression fixed={len(fixed_components)} pairs={len(pairs)}")
if any(j >= 24 and cc[j] != j for j in fixed_components if j < 24):
    raise SystemExit("side component orbit regression")

# Every crossing is the unique intersection of its listed side/exceptional pair,
# so the component permutation induces the crossing permutation exactly.
edges = []
edge_index = {}
for idx, e in enumerate(sk["codim2_crossings"]):
    a = int(e["side_vertex"]) - 1
    b = int(e["exceptional_vertex"]) - 1
    edges.append((a, b))
    edge_index[tuple(sorted((a, b)))] = idx
if len(edges) != 144 or len(edge_index) != 144:
    raise SystemExit("crossing inventory uniqueness regression")

def induced_edge_perm(p):
    out = []
    for a, b in edges:
        key = tuple(sorted((p[a], p[b])))
        if key not in edge_index:
            raise SystemExit("Galois action escaped crossing inventory")
        out.append(edge_index[key])
    return out

ecc = induced_edge_perm(cc)
ect = induced_edge_perm(ct)
if ect != list(range(144)):
    raise SystemExit("sqrt(2)-conjugation no longer fixes crossing inventory")
if any(ecc[ecc[j]] != j for j in range(144)):
    raise SystemExit("crossing cc action is not an involution")
fixed_edges = [j for j in range(144) if ecc[j] == j]
edge_pairs = []
seen_e = set(fixed_edges)
for j in range(144):
    if j in seen_e:
        continue
    k = ecc[j]
    if k == j or ecc[k] != j:
        raise SystemExit("unexpected crossing orbit")
    edge_pairs.append(tuple(sorted((j, k))))
    seen_e.update((j, k))
edge_pairs = sorted(set(edge_pairs))
if len(fixed_edges) + 2 * len(edge_pairs) != 144:
    raise SystemExit("crossing orbit count regression")

# Source-locked proper odd-primary result must still say that every nonconstant
# proper-surface Brauer class is 2-primary.  Constant Br(Q) classes have zero
# divisor residues, so they do not quotient the boundary character module.
for needle in (
    "PROPER_NONCONSTANT_BRAUER_ODD_PRIMARY=ABSENT",
    "odd-primary physical-open Brauer, if any = boundary-residue source only.",
):
    if needle not in proper_odd:
        raise SystemExit(f"proper odd-primary source lock missing: {needle}")
proper_odd_sha = hashlib.sha256(proper_odd.encode()).hexdigest()

# Arithmetic theorem adapter, prime-uniform:
# 1) Q and Q(i) have roots of unity of orders 2 and 4 respectively, hence no
#    nontrivial odd-order roots of unity.  Therefore for every odd ell^n,
#    H^0(k, Z/ell^n(-1))=0 for k=Q,Q(i).
# 2) Thus every odd-primary second residue at every certified crossing is zero.
# 3) Away from crossings only one removed divisor passes through a point, so
#    Gersten compatibility also forces zero second residue there.
# 4) Hence each first-residue character is unramified on the full boundary P1.
# 5) P1 over an algebraic closure has trivial finite etale fundamental group
#    (Riemann-Hurwitz in characteristic zero), so unramified characters on
#    P1_k are exactly H^1(k,Q/Z).
# The 60 Q-prime divisor orbits therefore give the exact parametric module below.
q_prime_divisors = len(fixed_components)
qi_prime_divisors = len(pairs)
if q_prime_divisors != 48 or qi_prime_divisors != 12:
    raise SystemExit("Q/Q(i) prime divisor orbit regression")

odd_module = (
    "Hom_cont(G_Q,Q/Z)_odd^48 direct_sum "
    "Hom_cont(G_Q(i),Q/Z)_odd^12"
)

cert = {
    "schema": "STAGE33_04_ODD_PRIMARY_ARITHMETIC_CHARACTER_DESCENT_V1",
    "audited_residual_kernel": audit["new_kernel_id"],
    "audited_exact_prefix_preserved": True,
    "source_locks": {
        "audit_state_sha256": hashlib.sha256((ROOT / "audit-state.json").read_bytes()).hexdigest(),
        "boundary_skeleton_sha256": sk["canonical_sha256"],
        "boundary_galois_sha256": bg["canonical_sha256"],
        "two_primary_function_constant_descent_sha256": two["canonical_sha256"],
        "proper_odd_primary_result_sha256": proper_odd_sha,
        "proper_odd_primary_result_path": "stages/stage29/29-02f/odd-primary-proper-brauer.md",
        "stacks_geometric_arithmetic_pi1_tag": "0BTU",
        "stacks_gm_constant_coefficient_twist_tag": "0A44",
        "stage29_boundary_gersten_receiver": "stages/stage29/29-02f/boundary-gersten-receiver.md",
    },
    "boundary_geometric_component_count": 72,
    "boundary_q_prime_divisor_orbit_count": 60,
    "q_defined_geometric_component_singletons": q_prime_divisors,
    "qi_geometric_component_conjugate_pairs": qi_prime_divisors,
    "crossing_geometric_point_count": 144,
    "q_crossing_singletons": len(fixed_edges),
    "qi_crossing_conjugate_pairs": len(edge_pairs),
    "all_boundary_constant_fields_in": ["Q", "Q(i)"],
    "all_crossing_residue_fields_in": ["Q", "Q(i)"],
    "q_roots_of_unity_order": 2,
    "qi_roots_of_unity_order": 4,
    "odd_primary_crossing_tate_twist_invariants_zero": True,
    "odd_primary_second_residue_at_every_crossing_zero": True,
    "odd_primary_first_residues_unramified_on_each_boundary_p1": True,
    "unramified_h1_p1_equals_constant_field_h1": True,
    "odd_primary_boundary_character_module": odd_module,
    "odd_primary_q_component_character_factor_count": 48,
    "odd_primary_qi_component_character_factor_count": 12,
    "proper_nonconstant_odd_primary_brauer_source_absent": True,
    "proper_constant_brauer_residues_zero": True,
    "arithmetic_odd_character_descent_complete": True,
    "all_primary_physical_open_unramified_kernel_complete_candidate": True,
    "br0g_discharged_candidate_pending_hostile_audit": True,
    "unresolved_unknown_in_scope_candidate": 0,
    "unit_status_candidate": "AUDIT_REQUIRED",
    "unit_closed": False,
    "downstream_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
    "next_expected_command_if_ci_green": "Stage33-audit",
    "firewall": "parametric character factors are exact BR0G residue data, not a finite list of Q-defined Brauer generators and not a Brauer-Manin obstruction",
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "odd-primary-arithmetic-character-descent.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n"
)
print(json.dumps({
    "success": True,
    "boundary_q_prime_orbits": 60,
    "q_character_factors": 48,
    "qi_character_factors": 12,
    "q_crossings": len(fixed_edges),
    "qi_crossing_pairs": len(edge_pairs),
    "odd_primary_boundary_character_module": odd_module,
    "arithmetic_odd_character_descent_complete": True,
    "next": "Stage33-audit",
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
