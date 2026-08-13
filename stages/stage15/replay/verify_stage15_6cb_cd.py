from pathlib import Path
base=Path('stages/stage15')
cb=(base/'15-6cb/result.md').read_text()
cc=(base/'15-6cc/result.md').read_text()
cd=(base/'15-6cd/result.md').read_text()
assert 'BLIND_REDISCOVERY_REQUIRED=true' in cb
assert 'BLIND_REDISCOVERY_COMPLETE=true' in cc
for cls in ['LIVE','UNTESTED','EQUIVALENT','DOMINATED','BLOCKED']:
    assert cls in cd
assert 'CYCLE_PARKING_AUDIT_COMPLETE=true' in cd
assert 'AUDIT_REQUIRED=true' in cd and 'MERGE_ALLOWED=false' in cd
print('Stage15-6 main-batch cb-cd: PASS')
