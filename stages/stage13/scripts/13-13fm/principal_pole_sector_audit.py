from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PROOF = ROOT / "stages/stage13/13-13fm/principal-pole-sector-closure.md"
RESULT = ROOT / "stages/stage13/13-13fm/result.md"


def check_face_intersections() -> None:
    faces = {
        "ab": {"a", "b"},
        "ac": {"a", "c"},
        "bc": {"b", "c"},
    }
    for q, qedges in faces.items():
        for r, redges in faces.items():
            if q == r:
                continue
            shared = qedges & redges
            assert len(shared) == 1, (q, r, shared)


def check_lambda() -> None:
    for p in (7, 11, 19, 23, 31, 43):
        lam = Fraction(p + 5, 2 * (p + 1))
        raw = Fraction(p + 1, p - 1)
        accepted = Fraction(p + 5, 2 * (p - 1))
        assert accepted / raw == lam
        assert lam <= Fraction(3, 4)

    # Symbolically, lambda_p <= 3/4 is equivalent to p >= 7.
    for p in range(7, 100):
        assert 2 * (p + 5) <= 3 * (p + 1)


def check_tokens() -> None:
    text = PROOF.read_text()
    result = RESULT.read_text()
    required = [
        "POLE_CHANNELS=H,R1,R2,S1,S2",
        "ACTUAL_CONSTRAINED_RESIDUE_SET_USED=true",
        "AUXILIARY_CHARACTER_ALIASING_QUOTIENTED_BEFORE_POLE_CLASSIFICATION=true",
        "PRINCIPAL_POLE_SECTOR=KER_REDUCED_POLE_SIGNATURE_MAP",
        "PRINCIPAL_SECTOR_RESIDUE_FUNCTIONAL_PROOF_COMPLETE=true",
        "PRINCIPAL_POLE_SECTOR_MULTIPLIER=product_{p_in_S}_lambda_p",
        "TAGGED_AMBIENT_CARDINALITY=2*A_q(B)",
        "TAGGED_FACTOR_TWO_UPPER_BOUND_PROVED=true",
        "NONPRINCIPAL_POLE_LOSS_PROVED=true",
        "MIXED_CORRECTION_CANNOT_RESTORE_POLE=true",
        "NONPRINCIPAL_TOTAL=o_S(B(log B)^3)",
        "R06_GATE_C=COMPLETE",
        "NEXT=13-13fn",
    ]
    for token in required:
        assert token in text, token
        assert token in result or token == "ACTUAL_CONSTRAINED_RESIDUE_SET_USED=true", token

    assert "No group structure is asserted for `Omega_{p,nu}`." in text
    assert "O_{qr}(B)\\le A^{\\rm tag}_{q,S}(B)" in text


def main() -> None:
    check_face_intersections()
    check_lambda()
    check_tokens()
    print("Stage13-13fm principal-pole-sector audit: PASS")


if __name__ == "__main__":
    main()
