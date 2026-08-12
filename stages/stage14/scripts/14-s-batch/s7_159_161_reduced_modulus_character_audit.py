from pathlib import Path

root = Path(__file__).resolve().parents[2]
checks = {
    root/'14-s7-159/result.md': [
        'Q25_UNIT_CHARACTER_PRINCIPAL_DOMINATION_NORMAL_FORM_TEST=PASS_EXACT_PRINCIPAL_PLUS_NONPRINCIPAL_DISCREPANCY',
        'UNIT_CHARACTER_PRINCIPAL_NONPRINCIPAL_EXACT_DECOMPOSITION_PROVED=true',
    ],
    root/'14-s7-160/result.md': [
        'Q25_NONUNIT_Q_VALUATION_STRATIFICATION_TEST=PASS_REDUCED_MODULUS_UNIT_RESIDUE_AFTER_LOCAL_STRIPPING',
        'NONUNIT_REDUCED_MODULUS_Q_NU_PROVED=true',
    ],
    root/'14-s7-161/result.md': [
        'Q25_UNIT_NONUNIT_RECOMBINATION_TEST=PASS_EXACT_REDUCED_MODULUS_CHARACTER_RECOMBINATION',
        'UNIT_NONUNIT_SEPARATE_ARITHMETIC_GATES_SUPERSEDED=true',
        'Q26_THEOREM_TARGET_NOW_STABLE=true',
    ],
    root/'14-s-batch/s7-159-161-report.md': [
        'BATCH_STOP_REASON=receiver_change',
        'NEXT=Stage14-s7-162',
        'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    ],
}
for path, tokens in checks.items():
    text = path.read_text()
    for token in tokens:
        assert token in text, (path, token)
print('s7-159..161 reduced-modulus character audit: PASS')
