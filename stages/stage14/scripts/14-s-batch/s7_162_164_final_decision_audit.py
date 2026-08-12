from fractions import Fraction
from pathlib import Path


stage14 = Path(__file__).resolve().parents[2]
repo = stage14.parent.parent

checks = {
    stage14 / '14-s7-162/result.md': [
        'FAIL_NO_UNIFORM_BO1_COLLAPSE',
        'VALUATION_PATTERN_BO1_IMPLIES_CHARACTER_FAMILY_BO1=false',
        'UNIT_PATTERN_CHARACTER_COUNT=phi_Q',
        'FULL_PHYSICAL_PACKET_PRESERVED=true',
        'NEXT=Stage14-s7-163',
    ],
    stage14 / '14-s7-163/result.md': [
        'PASS_EXACT_RESIDUE_MEAN',
        'FAIL_LOSSES_PHI_QNU',
        'FAIL_VARIANCE_NOT_TARGET_CLASS_LOWER_BOUND',
        'ORTHOGONALITY_ONLY_ZERO_TARGET_RESIDUE_COUNTERMODEL=true',
        'FULL_PHYSICAL_MAIN_TERM_DOMINANCE_PROVED=false',
        'NEXT=Stage14-s7-164',
    ],
    stage14 / '14-s7-164/result.md': [
        'COMPLETE_FINAL_S_DECISION_PARKED_EXTERNAL_GATE',
        'VALID_EXISTING_THEOREM_ADAPTER_PROVED=false',
        'S_FINAL_DECISION=PARKED_EXTERNAL_GATE',
        'S_ROUTE_NEXT=NONE',
        'Q27_NEEDED=false',
        'NEW_S7_165_ALLOWED=false',
    ],
    stage14 / '14-s-batch/s7-162-164-report.md': [
        'BATCH_START_MAIN_SHA=9632d760afcf529aeae5e56a40820b6cfbced44c',
        'BATCH_SUBSTANTIVE_STAGE_COUNT=3',
        'BATCH_STOP_REASON=final_decision_parked_external_gate',
        'S_FINAL_XQ_AUDIT_NEEDED=true',
        'STAGE14_AUTOMATION_SAFE=true',
        'STAGE14_ROUTE=s',
    ],
    stage14 / 'roadmap.md': [
        'S_FINAL_DECISION_RECORDED=true',
        'S_FINAL_DECISION=PARKED_EXTERNAL_GATE',
        'S_FINAL_DECISION_STAGE=Stage14-s7-164',
        'S_ROUTE_CURRENT_STATE=PARKED_EXTERNAL_GATE',
        'S_ROUTE_NEXT=NONE',
    ],
    stage14 / '14-s7-161/result.md': [
        'UNIT_NONUNIT_SEPARATE_ARITHMETIC_GATES_SUPERSEDED=true',
        'Q26_THEOREM_TARGET_NOW_STABLE=true',
        'NEXT=Stage14-s7-162',
    ],
    stage14 / '14-q26/result.md': [
        'Q26_REDUCED_MODULUS_CHARACTER_FAMILY_COMPLEXITY_TEST -> Stage14-s7-162',
        'Q27_NEEDED=false',
    ],
}

for path, tokens in checks.items():
    text = path.read_text(encoding='utf-8')
    for token in tokens:
        assert token in text, f'{token} missing from {path}'

# Exact toy witness that nonnegativity plus residue-class Fourier identities do
# not imply strict principal domination.  Four unit classes, all mass off target.
residue_mass = [Fraction(0), Fraction(1), Fraction(0), Fraction(0)]
phi_q = len(residue_mass)
target = 0
a0 = sum(residue_mass)
principal = a0 / phi_q
joint = residue_mass[target]
error = joint - principal
assert joint == 0
assert principal > 0
assert error == -principal
assert abs(error) == principal

assert not (stage14 / '14-s7-165').exists(), 's7-165 is forbidden after final park'

print('Stage14 s7-162..164 final decision audit: PASS')
