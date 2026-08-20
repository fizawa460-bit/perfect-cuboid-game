from pathlib import Path

here = Path(__file__).resolve().parent
stage27 = here.parent
m = (stage27 / '27-20-r302m' / 'result.md').read_text(encoding='utf-8')
n = (stage27 / '27-20-r302n' / 'result.md').read_text(encoding='utf-8')
o = (stage27 / '27-20-r302o' / 'result.md').read_text(encoding='utf-8')
registry = (here / 'batch-registry.json').read_text(encoding='utf-8')

checks = [
    ('m receiver', 'SAME_MEASURE_QUADRATIC_FORM_RECEIVER_DERIVED=true' in m),
    ('m no false theorem', 'PUBLISHED_LARGE_SIEVE_APPLICABILITY_PROVED=false' in m),
    ('n diagonal firewall', 'GRAM_DIAGONAL_CANNOT_BE_IGNORED=true' in n),
    ('n offdiag alone false', 'OFFDIAGONAL_CANCELLATION_ALONE_SUFFICIENT=false' in n),
    ('o continue policy', 'FREEZE_FOR_STRUCTURE_RADAR=false' in o),
    ('o checkpoint gate', 'ADVANCE_TO_CHECKPOINT50=false' in o),
    ('registry range', '"range": "r302m-r302o"' in registry),
    ('registry unfrozen', '"freeze_for_structure_radar": false' in registry),
]
for name, ok in checks:
    assert ok, name
print('Stage27-20-r302m-o verifier: PASS')
