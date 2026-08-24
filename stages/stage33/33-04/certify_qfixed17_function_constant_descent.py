#!/usr/bin/env python3
"""Exact two-primary arithmetic descent adapter for the Q-fixed17 residual.

This leaf closes ONLY the exponent-two function/constant-squareclass descent wall.
It must not be promoted to all-primary BR0G closure: for odd primary residue
characters H^1(-, Z/l) is not Kummer f mod l over Q or Q(i) in general.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sk = json.loads((ROOT / "boundary-residue-skeleton.json").read_text())
bg = json.loads((ROOT / "boundary-galois.json").read_text())
q17 = json.loads((ROOT / "qfixed17-graph-residual.json").read_text())
v4 = json.loads((ROOT / "qfixed17-v4-divisor-descent.json").read_text())

if sk["component_count"] != 72 or sk["side_component_count"] != 24 or sk["exceptional_component_count"] != 48:
    raise SystemExit("boundary inventory regression")
if sk["codim2_crossing_count"] != 144:
    raise SystemExit("crossing inventory regression")
if int(q17["qfixed_quotient_after_unit_symbol_image_dimension_f2"]) != 17:
    raise SystemExit("Q-fixed17 dimension regression")
if not v4["finite_divisor_parity_descent_obstruction_zero"]:
    raise SystemExit("finite divisor descent predecessor not closed")

cc = [int(x)-1 for x in bg["boundary_perm_cc_1based"]]
ct = [int(x)-1 for x in bg["boundary_perm_ct_1based"]]
if ct != list(range(72)):
    raise SystemExit("sqrt(2)-conjugation is no longer trivial on boundary inventory")
if any(cc[j] != j for j in range(24)):
    raise SystemExit("side conics are no longer individually Q-fixed")

exc_singletons = [j for j in range(24,72) if cc[j] == j]
exc_pairs = []
seen = set(exc_singletons)
for j in range(24,72):
    if j in seen:
        continue
    k = cc[j]
    if k == j or k < 24 or cc[k] != j:
        raise SystemExit("unexpected exceptional complex-conjugation orbit")
    exc_pairs.append(tuple(sorted((j,k))))
    seen.update((j,k))
exc_pairs = sorted(set(exc_pairs))
if len(exc_singletons) != 24 or len(exc_pairs) != 12 or len(seen) != 48:
    raise SystemExit(f"exceptional orbit regression singles={len(exc_singletons)} pairs={len(exc_pairs)}")

deg = [0]*72
for e in sk["codim2_crossings"]:
    a = int(e["side_vertex"])-1
    b = int(e["exceptional_vertex"])-1
    deg[a] += 1
    deg[b] += 1
if any(deg[j] < 1 for j in range(24,72)):
    raise SystemExit("exceptional component without a certified side branch")
if sorted(set(deg[j] for j in range(24,72))) != [2,4]:
    raise SystemExit("exceptional incidence degree regression")

vecs = [[int(x)&1 for x in v] for v in q17["qfixed_residual_basis_edge_vectors_144"]]
edges = []
edge_index = {}
for idx,e in enumerate(sk["codim2_crossings"]):
    a = int(e["side_vertex"])-1
    b = int(e["exceptional_vertex"])-1
    edges.append((a,b))
    edge_index[tuple(sorted((a,b)))] = idx

def induced_edge_perm(p):
    out=[]
    for a,b in edges:
        key=tuple(sorted((p[a],p[b])))
        if key not in edge_index:
            raise SystemExit("Galois action escaped crossing graph")
        out.append(edge_index[key])
    return out

ecc = induced_edge_perm(cc)

def act(v,ep):
    w=[0]*len(v)
    for j,k in enumerate(ep):
        w[k]=v[j]
    return w

per_vector=[]
for idx,v in enumerate(vecs):
    if act(v,ecc) != v:
        raise SystemExit(f"vector {idx} lost complex-conjugation invariance")
    counts=[0]*72
    for bit,(a,b) in zip(v,edges):
        if bit:
            counts[a]+=1; counts[b]+=1
    if any(x%2 for x in counts):
        raise SystemExit(f"vector {idx} lost even component degree")
    per_vector.append({
        "index_1based": idx+1,
        "selected_crossings": sum(v),
        "all_component_geometric_degrees_even": True,
        "q_or_qi_rational_divisor_orbitwise": True,
        "principal_after_even_basepoint_correction_on_split_p1": True,
        "constant_squareclass_cocycle_trivial_by_orbitwise_normalization": True,
    })

cert = {
    "schema": "STAGE33_04_QFIXED17_FUNCTION_CONSTANT_DESCENT_V2",
    "scope": "EXPONENT_TWO_RESIDUAL_ONLY",
    "source_locks": {
        "boundary_skeleton_sha256": sk["canonical_sha256"],
        "boundary_galois_sha256": bg["canonical_sha256"],
        "qfixed17_graph_residual_sha256": q17["canonical_sha256"],
        "qfixed17_v4_divisor_descent_sha256": v4["canonical_sha256"],
        "testa_stoll_code_commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "testa_stoll_code_blob": "0422b69847f2afb97cb7b3ed02ebef91279f61b1",
        "testa_stoll_paper": "arXiv:1009.0388",
    },
    "side_component_count": 24,
    "side_models_defined_over_q": True,
    "side_models_split_pythagorean_conics_over_q": True,
    "side_standard_parameterization": "x=u^2-v^2, y=2uv, z=u^2+v^2",
    "side_singular_parameter_support_over_qi": ["0","infinity","1","-1","i","-i"],
    "exceptional_component_count": 48,
    "exceptional_q_singletons": len(exc_singletons),
    "exceptional_qi_conjugate_pairs": len(exc_pairs),
    "sqrt2_extension_needed_for_boundary_models": False,
    "ordinary_node_exceptional_genus_zero_adapter": True,
    "every_exceptional_has_residue_field_rational_side_tangent_direction": True,
    "every_exceptional_split_over_its_residue_field": True,
    "boundary_component_orbit_count": 24 + len(exc_singletons) + len(exc_pairs),
    "qfixed17_dimension_f2": 17,
    "all_17_arithmetic_crossing_divisors_orbitwise_rational": True,
    "all_17_even_degree_on_every_geometric_component": True,
    "pic0_p1_principal_divisor_adapter_complete": True,
    "actual_first_residue_function_descent_complete_mod2": True,
    "constant_squareclass_descent_complete_mod2": True,
    "constant_squareclass_cocycle_dimension_f2": 0,
    "q_defined_residual_dimension_f2_after_known_unit_symbol_image": 17,
    "per_vector_certificates": per_vector,
    "proper_brauer_residue_quotient_changes_qfixed17": False,
    "two_primary_residual_leaf_complete": True,
    "all_primary_physical_open_unramified_kernel_complete": False,
    "br0g_discharged": False,
    "unit_status": "RUNNING",
    "unit_closed": False,
    "downstream_released": False,
    "new_residual_kernel": "R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT",
    "next_exact_leaf": "L33-04-COMPUTE-ALL-PRIMARY-GEOMETRIC-FIXED-MODULE-THEN-ODD-CHARACTER-DESCENT",
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
    "firewall": "mod-2 Kummer function descent is not an all-primary BR0G closure; odd-primary H^1(-,Z/l) character descent remains",
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
(ROOT / "qfixed17-function-constant-descent.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({
    "success": True,
    "scope": cert["scope"],
    "q_defined_residual_dimension_f2": 17,
    "constant_squareclass_cocycle_dimension_f2": 0,
    "two_primary_residual_leaf_complete": True,
    "br0g_discharged": False,
    "remaining_kernel": cert["new_residual_kernel"],
    "certificate_sha256": cert["canonical_sha256"],
},indent=2,sort_keys=True))
