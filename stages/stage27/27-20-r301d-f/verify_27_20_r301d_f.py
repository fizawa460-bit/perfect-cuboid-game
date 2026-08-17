#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]

def must(path, *needles):
    text=(ROOT/path).read_text(encoding='utf-8')
    for n in needles:
        assert n in text, (path,n)

must('stages/stage27/27-20-r301d/result.md',
     'STATUS=AUDITED_PASS_MERGED',
     'AUDIT_STATUS=PASS',
     'SPACE_DIAGONAL_STATE_G_REDUCTION_PROVED=true',
     'SPACE_DIAGONAL_LOCAL_BLOCKER_MASS_FORMULA_PROVED=true',
     'SPACE_DIAGONAL_DELTA_2=2/9',
     'SPACE_DIAGONAL_DELTA_P=2(p-chi4(p))/(p^2+6p+1)',
     'ALL_STAGE20_LOCAL_FACTORS_TRANSFER=false',
     'STRICT_SUB_SQRT_UPPER_PROVED=false')

must('stages/stage27/27-20-r301e/result.md',
     'STATUS=AUDITED_PASS_MERGED',
     'FINAL_AUDIT_VERDICT=PASS',
     'PREVIOUS_AUDIT_VERDICT=FAIL_PENDING_SOURCE_JUSTIFICATION',
     'R301E_SOURCE_JUSTIFICATION=REPAIRED_BY_IDENTICAL_BAD_SUBSET_AND_SET_INCLUSION',
     'SAME_BAD_SUBSET_B_P_ON_COMMON_HOST=true',
     'EQUAL_MASS_ALONE_USED=false',
     'P_SP_SUBSET_OF_E11_SIFTED_AMBIENT_SET=true',
     'PREDICATE_SPECIFIC_REMAINDER_TRANSFER_REQUIRED=false',
     'SPACE_DIAGONAL_GROWING_PRIME_SIEVE_TRANSFER_PROVED=true',
     'SPACE_DIAGONAL_HOST_SIEVE_BOUND=B(log B)^5/(log log B)^2',
     'HOST_SIEVE_BOUND_BEATS_CURRENT_HALF_POWER=false',
     'SIEVE_FACTOR_MULTIPLIED_WITH_HALF_POWER=false',
     'FRESH_REAUDIT_REQUIRED=false',
     'STRICT_SUB_SQRT_UPPER_PROVED=false')

must('stages/stage27/27-20-r301e/source-justification.md',
     'SOURCE_JUSTIFICATION_REPAIRED=true',
     'HUANG_SOURCE_LEVEL_CHECK_COMPLETED=true',
     'HUANG_THEOREM_3_11_ARBITRARY_OPEN_CLOSED_FAMILY=true',
     'HUANG_THEOREM_3_11_UNIFORM_IN_LOCAL_FAMILY=true',
     'HUANG_REMAINDER_USES_EE_AND_COVERING_EXPONENT=true',
     'HUANG_REMAINDER_USES_THIRD_FACE_PREDICATE=false',
     'HUANG_COROLLARY_3_13_FULL_FAMILY_BY_SET_INCLUSION=true',
     'R301E_FINAL_SOURCE_OBJECTION_RESOLVED=true',
     'SAME_BAD_SUBSET_B_P_ON_COMMON_HOST=true',
     'EQUAL_MASS_ALONE_USED=false',
     'P_SP_SUBSET_OF_E11_SIFTED_AMBIENT_SET=true',
     'PREDICATE_SPECIFIC_REMAINDER_TRANSFER_REQUIRED=false',
     'FINAL_SOURCE_AUDIT=PASS',
     'FRESH_REAUDIT_REQUIRED=false')

must('stages/stage27/27-20-r301f/result.md',
     'STATUS=AUDITED_PASS_MERGED',
     'AUDIT_STATUS=PASS',
     'SPACE_DIAGONAL_TORUS_FACTORIZATION_PROVED=true',
     'SPACE_DIAGONAL_SQUARECLASS_RECEIVER_DERIVED=true',
     'GAUSSIAN_NORM_FACTOR_STRUCTURE_IDENTIFIED=true',
     'SQUARECLASS_SUPPORT_FIXED_POWER_BOUND_PROVED=false',
     'STRICT_SUB_SQRT_UPPER_PROVED=false')

must('stages/stage27/27-20-r301d-f/audit.md',
     'AUDIT_VERDICT=PASS',
     'MATHEMATICAL_AUDIT=PASS',
     'CI_AUDIT=PASS',
     'SOURCE_PR=1043',
     'SOURCE_MERGE_COMMIT=11bab78346d6535ba17fb268b42c89defff9a7eb',
     'ADVANCE_TO_CHECKPOINT50=false',
     'STRICT_SUB_SQRT_UPPER_PROVED=false')

reg=json.loads((ROOT/'stages/stage27/27-20-r301d-f/batch-registry.json').read_text())
assert reg['routes']==['Stage27-20-r301d','Stage27-20-r301e','Stage27-20-r301f']
assert reg['audit_status']=='PASS'
assert reg['final_status']=='AUDITED_PASS_MERGED'
assert reg['final_audit_verdict']=='PASS'
assert reg['previous_audit_verdict']=='FAIL_PENDING_SOURCE_JUSTIFICATION'
assert reg['pr']==1043
assert reg['merge_commit']=='11bab78346d6535ba17fb268b42c89defff9a7eb'
assert reg['merge_allowed'] is True
assert reg['advance_to_checkpoint50'] is False
assert reg['fresh_reaudit_required'] is False
assert reg['claims']['r301e_source_justification_repaired'] is True
assert reg['claims']['r301e_source_justification_audited_pass'] is True
assert reg['claims']['r301e_same_bad_subset_on_common_host'] is True
assert reg['claims']['r301e_equal_mass_alone_used'] is False
assert reg['claims']['r301e_predicate_specific_remainder_transfer_required'] is False
assert reg['claims']['host_sieve_beats_half_power'] is False
assert reg['claims']['strict_sub_sqrt_upper_proved'] is False
assert reg['next_derived_route']=='27-20-r301g'

ctl=json.loads((ROOT/'stages/stage27/27-controller.json').read_text())
for key in ['Stage27-20-r301','Stage27-20-r301a','Stage27-20-r301b','Stage27-20-r301c','Stage27-20-r301d','Stage27-20-r301e','Stage27-20-r301f']:
    assert key in ctl['derived_routes'], key
for key in ['Stage27-20-r301','Stage27-20-r301a','Stage27-20-r301b','Stage27-20-r301c']:
    assert ctl['derived_routes'][key]['audit_status']=='PASS'
for key in ['Stage27-20-r301d','Stage27-20-r301e','Stage27-20-r301f']:
    r=ctl['derived_routes'][key]
    assert r['status']=='AUDITED_PASS_MERGED'
    assert r['audit_status']=='PASS'
    assert r['audit_record']=='stages/stage27/27-20-r301d-f/audit.md'
    assert r['pr']==1043
    assert r['merge_commit']=='11bab78346d6535ba17fb268b42c89defff9a7eb'
    assert r['merge_allowed'] is True
    assert r['advance_allowed'] is True
    assert r['advance_to_checkpoint50'] is False
    assert r['strict_sub_sqrt_upper_proved'] is False
assert ctl['state']['CURRENT_CHECKPOINT']==40
assert ctl['state']['NEXT_CHECKPOINT']==40
assert ctl['derived_routes']['Stage27-20-r301e']['host_sieve_beats_current_half_power'] is False
assert ctl['derived_routes']['Stage27-20-r301f']['next_derived_route']=='27-20-r301g'
print('Stage27-20-r301d-f verifier: PASS')
