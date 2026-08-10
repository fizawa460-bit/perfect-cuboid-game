#!/usr/bin/env python3
import json, subprocess
from pathlib import Path

root=Path(__file__).resolve().parents[4]
frozen=json.loads((root/'data/14-t82/fixed_u_selector_divisor_frozen.json').read_text())
out=json.loads(subprocess.check_output(['python',str(root/'scripts/14-t/t82_fixed_u_selector_divisor_audit.py')],text=True))
for k in ['local_projective_selector_checks','selector_divisor_checks','nonselector_partition_checks','fixed_u_host_checks','synthetic_packets','max_selector_over_m']:
    assert out[k]==frozen[k], (k,out[k],frozen[k])
assert out['boundary']==frozen['boundary']
print('Stage14-t82 frozen validation: OK')
