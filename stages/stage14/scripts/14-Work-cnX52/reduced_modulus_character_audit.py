from pathlib import Path

root = Path(__file__).resolve().parents[3]

checks = {
    root / '14-Work-cnX52/result.md': [
        'COMPLETE_VALUATION_AVERAGED_REDUCED_MODULUS_CHARACTER_LOCALIZATION',
        'UNIT_NONUNIT_RECOMBINATION_CONSUMED=true',
        'S_REDUCED_MODULUS_CHARACTER_THEOREM_SPECIES_COUNT=2',
        'REDUCED_MODULUS_AGGREGATE_DISCREPANCY_BOUND_PROVED=false',
        'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
        'TH34_NEEDED=false',
        'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    ],
    root / '14-q26/result.md': [
        'COMPLETE_REDUCED_MODULUS_CHARACTER_DISCREPANCY_LITERATURE_RADAR',
        'DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0',
        'REDUCED_MODULUS_AGGREGATE_CHARACTER_DOMINATION_DIRECT_THEOREM_FOUND=false',
        'Q27_NEEDED=false',
    ],
    root.parent.parent / 'docs/stage14-toolbox/work-cnX52-receiver-matrix.md': [
        'COMMON_CORE_AVERAGE_MUST_BE_RETAINED=true',
        'UNIT_NONUNIT_SEPARATE_ARITHMETIC_GATES_SUPERSEDED=true',
        'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
    ],
}

for path, tokens in checks.items():
    text = path.read_text(encoding='utf-8')
    for token in tokens:
        assert token in text, f'{token} missing from {path}'

print('Stage14-Work-cnX52/q26 audit: PASS')
