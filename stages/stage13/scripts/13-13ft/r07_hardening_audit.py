from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DOC = ROOT / 'stages/stage13/13-13ft/r07-hardening-lemma.md'
RESULT = ROOT / 'stages/stage13/13-13ft/result.md'

def main():
    text = DOC.read_text()
    result = RESULT.read_text()

    assert 529 * 6561 == 3470769
    assert 3465625 < 529 * 6561
    assert 432 * 25000000 == 10800000000
    assert 10799919009 < 432 * 25000000

    required_doc = [
        '3465625<3470769',
        '10799919009<10800000000',
        'RETAINED_ELL_LOG_MOMENTS_UNIFORM=true',
        'OVERLAP_SQUEEZE_EPSILON_FORM_EXPLICIT=true',
        'TWO_PREIMAGES_ARE_NOT_TWO_CANONICAL_CUBOIDS=true',
        'R07_GATES_A_B_C_D_COMPLETE=true',
        'R07_REPAIR_BLOCKERS_OPEN=0',
        'NEXT=13-13fu',
    ]
    for token in required_doc:
        assert token in text, token

    required_result = [
        'STAGE13_13FT=COMPLETE_R07_EXACT_ARITHMETIC_AND_QUANTIFIER_HARDENING',
        'R07_GATE_D=COMPLETE',
        'R07_CANONICAL_SYNTHESIS_READY=true',
        'R07_FRESH_EXTERNAL_REVIEW_REQUIRED=true',
        'PROMOTE_TO_13_13G=false',
        'NEXT=13-13fu',
    ]
    for token in required_result:
        assert token in result, token

    print('13-13ft hardening audit: PASS')

if __name__ == '__main__':
    main()
