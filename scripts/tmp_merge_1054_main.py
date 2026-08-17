#!/usr/bin/env python3
import json, subprocess
from pathlib import Path

P = Path('stages/stage27/27-controller.json')
branch = json.loads(Path('/tmp/controller-r5ah.json').read_text())
main = json.loads(subprocess.check_output(['git','show','origin/main:stages/stage27/27-controller.json'], text=True))

# Start from live main so all parallel Stage20 additions are retained.
merged = main

# Apply only the Stage19 r5 lifecycle/progression surface from the PR branch.
merged['status'] = branch['status']
merged['checkpoint_status']['40'] = branch['checkpoint_status']['40']
for key in ('Stage27-19-r5af-r5ag', 'Stage27-19-r5ah-r5ai'):
    merged['derived_routes'][key] = branch['derived_routes'][key]

# The global state currently belongs to the Stage19 r5 main-batch controller contract.
# Preserve any keys added by main, then overlay the r5 state fields.
state = dict(main.get('state', {}))
state.update(branch.get('state', {}))
merged['state'] = state
if 'next_expected_command' in branch:
    merged['next_expected_command'] = branch['next_expected_command']

P.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + '\n')
json.loads(P.read_text())

# Guard the two parallel lanes explicitly.
check = json.loads(P.read_text())
assert 'Stage27-20-r301t-v' in check['derived_routes']
assert check['derived_routes']['Stage27-19-r5af-r5ag']['audit_status'] == 'PASS'
assert check['derived_routes']['Stage27-19-r5ah-r5ai']['audit_status'] == 'PENDING'
assert check['state']['CURRENT_CHECKPOINT'] == 40
print('controller merge guard PASS')
