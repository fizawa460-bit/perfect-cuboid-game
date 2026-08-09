from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PROOF = ROOT / "stages/stage13/13-13fn/stage13-r06-canonical-proof.md"
RESULT = ROOT / "stages/stage13/13-13fn/result.md"

proof = PROOF.read_text(encoding="utf-8")
result = RESULT.read_text(encoding="utf-8")

required = [
    "SUM_IQ_ANALYTIC_PROOF_COMPLETE=true",
    "PROOF_TO_HLR_INDEX=k_HLR=2*ell",
    "PRINCIPAL_POLE_SECTOR=KER_REDUCED_POLE_SIGNATURE_MAP",
    "TAGGED_FACTOR_TWO_UPPER_BOUND_PROVED=true",
    "NONPRINCIPAL_POLE_LOSS_PROVED=true",
    "WIENER_MIXED_TERM_EXPLICIT=true",
    "P5_EXPLICIT_FINITE_BOUND_LT=432",
    "RETAINED_ELL_MIN=1",
    "LAMBDA_3=1",
    "GELFAND_LERAY_RADIAL_FACTOR=1/(P/d)",
    "OE_EE_FACE_INDEPENDENCE_BRANCHWISE=true",
    "BOX_COUNT_DERIVATION_EXPLICIT=true",
    "HARMONIC_EXPONENT_DECOMPOSED=true",
    "VAALER_ENDPOINT_CONVENTION_EXPLICIT=true",
    "THETA_VARTTHETA_SEPARATION=true",
    "KAPPA_ABSOLUTE_CONVERGENCE_EXPANSION_EXPLICIT=true",
    "NEXT=13-13fo",
]

missing = [token for token in required if token not in proof + "\n" + result]
if missing:
    raise SystemExit(f"missing lock tokens: {missing}")

# Exact Wiener arithmetic.
assert Fraction(3465625, 6561) < 529
assert Fraction(10799919009, 25000000) < 432

# Exceptional inert prime and contraction range.
def lam(p: int) -> Fraction:
    return Fraction(p + 5, 2 * (p + 1))

assert lam(3) == 1
for p in (7, 11, 19, 23, 31, 43):
    assert lam(p) <= Fraction(3, 4)

# Harmonic exponent ledger: L=(log B)^4 contributes 4(C_H+1),
# two positive base channels contribute +2.
for c_h in range(6):
    for d_h in range(6):
        lhs = 4 * (c_h + 1) + d_h + 2
        rhs = 4 * c_h + d_h + 6
        assert lhs == rhs

# The proof must not retain the ambiguous R05 Hecke indexing phrase.
forbidden = [
    "Stage13 `k=8ell`",
    "L(s,\\Xi_{8\\ell})",
    "Hecke k=8 ell",
]
for token in forbidden:
    if token in proof:
        raise SystemExit(f"stale ambiguous Hecke normalization: {token}")

# Finite-data scope must be explicit.
assert "Finite data are neither proof of convergence nor a refutation" in proof
assert "numerical quadrature is validation only" in proof

print("STAGE13_13FN_AUDIT=PASS")
print("DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY")
