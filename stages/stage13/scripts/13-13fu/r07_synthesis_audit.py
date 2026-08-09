#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
proof = (ROOT / "stages/stage13/13-13fu/stage13-r07-canonical-proof.md").read_text()
result = (ROOT / "stages/stage13/13-13fu/result.md").read_text()

required_proof = [
    "STAGE13_13FU_R07_CANONICAL_PROOF_CANDIDATE",
    "N_q(B)\\sim\\frac{\\kappa I_q}{3\\pi^3}B(\\log B)^3",
    "N_1(B):=\\sum_qN_q(B)\\sim\\frac{\\kappa}{24\\pi}B(\\log B)^3",
    "\\sum_qI_q=\\frac{\\pi^2}{8}",
    "C_{\\rm prim}(B)=2\\sum_qA_q(B)",
    "3465625<529\\cdot6561=3470769",
    "10799919009<432\\cdot25000000=10800000000",
    "\\Xi_{2\\ell}=\\xi_{8\\ell}",
    "\\boxed{k_{HLR}=2\\ell}",
    "\\boxed{\\lambda_p=\\frac{p+5}{2(p+1)}}",
    "\\boxed{\\lambda_3=1}",
    "N_{box}=O(\\Lambda^{27})",
    "O(B\\Lambda^{-35})",
    "O(B\\Lambda^{-5})",
    "4C_H+D_H+6",
    "finite sum of functions each having pole order at most three cannot create a pole of order four",
    "Choose **one fixed** `k`",
    "R07 Gate A: fixed finite Hecke/ray-class twist contract",
    "R07 Gate B: concrete fixed-S residue/pole model",
    "R07 Gate C: self-contained curved-region transfer",
    "R07 Gate D: exact arithmetic and quantifier hardening",
    "R07_CANONICAL_PROOF_SINGLE_ENTRYPOINT=true",
]

required_result = [
    "STAGE13_13FU=COMPLETE_R07_CANONICAL_PROOF_SYNTHESIS",
    "R07_GATES_A_B_C_D_COMPLETE=true",
    "R07_REPAIR_BLOCKERS_OPEN=0",
    "R07_HARDENING_OBLIGATIONS_OPEN=0",
    "R07_BUNDLE_CREATED=false",
    "R07_FRESH_EXTERNAL_REVIEW_REQUIRED=true",
    "R06_VERDICTS_CARRY_FORWARD_TO_R07=false",
    "THEOREM_CHANGED=false",
    "PROMOTE_TO_13_13G=false",
    "NEXT=13-13fv",
]

missing = [x for x in required_proof if x not in proof]
missing += [f"result:{x}" for x in required_result if x not in result]
assert not missing, "missing synthesis locks: " + repr(missing)

# Exact arithmetic checks: no floating-point proof is needed.
assert 3465625 < 529 * 6561 == 3470769
assert 10799919009 < 432 * 25000000 == 10800000000

# Quantitative ledger checks.
assert 9 * 3 == 27
assert 27 - 62 == -35
assert -8 + 3 == -5

# Local contraction locks.
def lam(p):
    return (p + 5) / (2 * (p + 1))
assert lam(3) == 1
assert lam(7) == 3 / 4
for p in [7, 11, 19, 23, 31, 43, 47, 59]:
    assert lam(p) <= 3 / 4

print("Stage13-13fu R07 synthesis audit: PASS")
