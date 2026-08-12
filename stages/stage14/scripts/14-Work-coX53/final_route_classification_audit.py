from pathlib import Path

repo = Path(__file__).resolve().parents[4]

checks = {
    repo / 'stages/stage14/14-Work-coX53/result.md': [
        'COMPLETE_FINAL_STAGE14_ROUTE_CLASSIFICATION_AND_EXTERNAL_GATE_PARK',
        'FINAL_S_XQ_CLASSIFICATION_AUDIT_CONSUMED=true',
        'ALL_ACTIVE_STAGE14_ANALYTIC_ROUTES_PARKED=true',
        'STAGE14_ANALYTIC_AUTOMATIC_NEXT=NONE',
        'Q27_NEEDED=false',
        'Q27_CREATED=false',
        'TH34_NEEDED=false',
        'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
        'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    ],
    repo / 'docs/stage14-toolbox/work-coX53-final-route-classification.md': [
        'S_FINAL_DECISION=PARKED_EXTERNAL_GATE',
        'NEW_S7_165_ALLOWED=false',
        'ALL_ACTIVE_STAGE14_ANALYTIC_ROUTES_PARKED=true',
        'STAGE14_ANALYTIC_RESTART_REQUIRES_MATERIAL_NEW_INPUT=true',
    ],
    repo / 'stages/stage14/14-s7-164/result.md': [
        'S_FINAL_XQ_AUDIT_NEEDED=true',
        'Q27_NEEDED=false',
        'NEW_S7_165_ALLOWED=false',
        'S_ROUTE_NEXT=NONE',
    ],
    repo / 'stages/stage14/14-q26/result.md': [
        'Q27_NEEDED=false',
    ],
}

for path, tokens in checks.items():
    text = path.read_text(encoding='utf-8')
    for token in tokens:
        assert token in text, f'{token} missing from {path}'

print('Stage14-Work-coX53 final route classification audit: PASS')
