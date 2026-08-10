#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
FROZEN=ROOT/'stages/stage14/data/14-t80/projective_gauss_dual_frozen.json'
def main():
    d=json.loads(FROZEN.read_text())
    assert d['stage']=='14-t80'
    assert d['reciprocal_states']==560 and d['invisible_states']==419
    assert d['physical_unit_checks']==419 and d['physical_affine_prime_checks']==1370
    assert d['local_primes']==16 and d['local_split_primes']==7 and d['local_inert_primes']==9
    assert d['local_nonprincipal_characters']==424 and d['local_nonzero_frequency_checks']==15938
    assert d['max_observed_weil_ratio_to_2sqrtp']<1.0
    assert d['max_zero_frequency_identity_error']<1e-10 and d['max_parseval_error']<1e-10
    assert d['independent_crt_squarefree_moduli']==610 and d['independent_crt_zero_support_checks']==2289
    b=d['boundary']
    assert b['MERGED_TH22_IMPORTED'] is True and b['MERGED_X13_SQRT_LEDGER_IMPORTED'] is True
    assert b['PROJECTIVE_ADDITIVE_DUAL_MODULUS']=='d'
    assert b['PROJECTIVE_CHARACTER_KERNEL_BECOMES_INVERSE_FRACTION_ADDITIVE_KERNEL'] is True
    assert b['CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT']=='1/2'
    assert b['SQRT_B_UPPER_BOUND_PROVED'] is True and b['STRICT_SUBSQRT_POWER_SAVING_PROVED'] is False
    assert b['TH23_NEEDED'] is True
    print('Stage14-t80 frozen boundary OK')
if __name__=='__main__':main()
