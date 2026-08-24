#!/usr/bin/env python3
"""Compute the exact all-primary geometric Galois-fixed boundary cycle module.

For the integral rank-73 cycle lattice L, ct acts trivially and cc is an
involution.  The fixed subgroup of L \otimes Q/Z is ker(cc-I on (Q/Z)^73).
Smith normal form of cc-I determines this group uniformly at all primes.
"""
import hashlib
import json
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parent
cg = json.loads((ROOT / "boundary-cycle-galois.json").read_text())
bg = json.loads((ROOT / "boundary-galois.json").read_text())

Ccc = sp.Matrix(cg["cycle_lattice"]["cc_matrix"])
Cct = sp.Matrix(cg["cycle_lattice"]["ct_matrix"])
if Ccc.shape != (73,73) or Cct.shape != (73,73):
    raise SystemExit("cycle action shape regression")
I = sp.eye(73)
if Cct != I:
    raise SystemExit("ct is no longer trivial on integral cycle lattice")
if Ccc*Ccc != I:
    raise SystemExit("cc is no longer an involution")
A = Ccc-I
rank = int(A.rank())
D = smith_normal_form(A, domain=ZZ)
nonzero = [abs(int(D[i,i])) for i in range(73) if D[i,i] != 0]
if rank != 12 or len(nonzero) != 12:
    raise SystemExit(f"cc-I rank regression rank={rank} smith={len(nonzero)}")
if any(d != 1 for d in nonzero):
    raise SystemExit(f"unexpected finite torsion in fixed Q/Z module: {nonzero}")
free_divisible_rank = 73-rank
if free_divisible_rank != 61:
    raise SystemExit("fixed divisible rank regression")

cert = {
    "schema": "STAGE33_04_ALL_PRIMARY_GEOMETRIC_CYCLE_INVARIANTS_V1",
    "source_locks": {
        "cycle_galois_sha256": cg["canonical_sha256"],
        "boundary_galois_sha256": bg["canonical_sha256"],
    },
    "integral_cycle_rank": 73,
    "ct_action_identity": True,
    "cc_involution": True,
    "rank_cc_minus_identity": rank,
    "smith_nonzero_invariant_factors_cc_minus_identity": nonzero,
    "smith_cokernel_torsion_nontrivial": False,
    "galois_fixed_geometric_cycle_module": "(Q/Z)^61",
    "galois_fixed_geometric_cycle_divisible_rank": 61,
    "odd_primary_fixed_module": "direct_sum_{ell odd} (Q_ell/Z_ell)^61",
    "two_primary_geometric_fixed_module": "(Q_2/Z_2)^61",
    "uniform_prime_power_fixed_rank": 61,
    "all_primary_geometric_fixed_module_complete": True,
    "arithmetic_odd_character_descent_complete": False,
    "br0g_discharged": False,
    "new_residual_kernel": "R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT",
    "next_exact_leaf": "L33-04-ODD-PRIMARY-ONE-VARIABLE-CHARACTER-DESCENT-ON-Q-AND-QI-BOUNDARY-ORBITS",
    "theorem_credit": False,
    "endpoint_credit": False,
    "firewall": "geometric Galois-fixed residue cycles are not automatically arithmetic H^1(K(D),Q/Z) residue characters",
}
canonical = json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "all-primary-geometric-cycle-invariants.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({
    "success": True,
    "smith_nonzero_factors": nonzero,
    "fixed_module": cert["galois_fixed_geometric_cycle_module"],
    "remaining_kernel": cert["new_residual_kernel"],
    "certificate_sha256": cert["canonical_sha256"],
},indent=2,sort_keys=True))
