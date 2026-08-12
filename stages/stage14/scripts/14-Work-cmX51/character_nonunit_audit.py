from pathlib import Path

root = Path(__file__).resolve().parents[3]

checks = {
    root / '14-Work-cmX51/result.md': [
        'COMPLETE_COMMON_CORE_AVERAGED_UNIT_CHARACTER_NONUNIT_LOCALIZATION',
        'S_UNIT_NONUNIT_THEOREM_SPECIES_COUNT=4',
        'UNIT_CHARACTER_PRINCIPAL_DOMINATION_PROVED=false',
        'NONUNIT_Q_SUPPORTED_VALUATION_GATE_PROVED=false',
        'TH34_NEEDED=false',
        'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    ],
    root / '14-q25/result.md': [
        'COMPLETE_UNIT_CHARACTER_NONUNIT_VALUATION_LITERATURE_RADAR',
        'DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0',
        'UNIT_CHARACTER_PRINCIPAL_DOMINATION_DIRECT_THEOREM_FOUND=false',
        'NONUNIT_Q_SUPPORTED_VALUATION_DIRECT_THEOREM_FOUND=false',
    ],
    root.parent.parent / 'docs/stage14-toolbox/work-cmX51-receiver-matrix.md': [
        'COMMON_CORE_AVERAGE_MUST_BE_RETAINED=true',
        'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
    ],
}

for path, tokens in checks.items():
    text = path.read_text(encoding='utf-8')
    for token in tokens:
        assert token in text, f'{token} missing from {path}'

print('Stage14-Work-cmX51/q25 audit: PASS')
