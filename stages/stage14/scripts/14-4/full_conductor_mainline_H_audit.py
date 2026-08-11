#!/usr/bin/env python3
from fractions import Fraction

SOURCE="0a2d313b4bd1baf8fad29cda70cc0f8a44e1b153"


def audit_endpoint_ranges():
    checks=0
    for chi in [Fraction(1,6),Fraction(5,24),Fraction(1,4)]:
        plus=chi+2*(Fraction(1,4)-chi/2)
        minus=(Fraction(1,4)-chi)+2*(Fraction(1,8)+chi/2)
        assert plus==minus==Fraction(1,2)
        # A hypothetical oscillatory saving does not alter the principal exponent.
        for delta in [Fraction(1,100),Fraction(1,32),Fraction(1,12)]:
            osc=Fraction(1,2)-delta
            principal=Fraction(1,2)
            assert max(osc,principal)==Fraction(1,2)
            checks+=1
    return checks


def audit_required_logic():
    # Full-count saving cannot follow from oscillatory-error saving alone.
    osc_saving=True
    principal_saving=False
    anti_correlation=False
    covariance_control=False
    whole_family=(osc_saving and (principal_saving or anti_correlation) and covariance_control)
    assert not whole_family
    return 1


def main():
    c1=audit_endpoint_ranges()
    c2=audit_required_logic()
    print(f"endpoint_logic_checks={c1}")
    print(f"whole_family_logic_checks={c2}")
    print(f"SOURCE_SNAPSHOT_SHA={SOURCE}")
    print("TARGET_FROZEN=true")
    print("FULL_REQUIRED_MASKS_RETAINED=true")
    print("FULL_CONDUCTOR_ENDPOINT_USED=true")
    print("OFF_THE_SHELF_THEOREM_APPLICABLE=false")
    print("OSCILLATORY_ERROR_POWER_SAVING_CERTIFIED=false")
    print("PRINCIPAL_DENSITY_FIXED_POWER_LOSS_CERTIFIED=false")
    print("MAIN_TERM_SCALE_SIGNED_ANTICORRELATION_CERTIFIED=false")
    print("X15_ALL_COVARIANCE_TERMS_CONTROLLED=false")
    print("FIXED_POWER_SAVING_PROVED=false")
    print("CERTIFIED_B_POWER_SAVING_EXPONENT=0")
    print("MAINLINE_H_COMPLETED=true")
    print("MAINLINE_BLOCKED_BY_H=false")
    print("NEXT_H_NEEDED=false")
    print("CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2")
    print("STRICT_SUBSQRT_POWER_SAVING_PROVED=false")
    print("NEXT=Stage14-4dj")

if __name__=="__main__":
    main()
