#!/usr/bin/env python3
"""Materialize the seven retained Picard coordinate-sign row certificates."""
import json
from pathlib import Path
from picard_coordinate_sign_rows_retained import load
HERE=Path(__file__).resolve().parent
x=load()
if x['canonical_sha256']!='5cd64ca89ee9f3ec76d275bc4082349764ac8a5cb4647a9bb9a4eaf267b76ab9':
    raise SystemExit('retained seven-sign lock moved')
for n in x['coordinate_order']:
    out={
      'schema':'STAGE33_07_PICARD_COORDINATE_SIGN_ACTION_ROWS_RETAINED_PROXY_V1',
      'coordinate':n,
      'upstream_git_blob_sha1':x['upstream_git_blob_sha1'],
      'source_run_id':x['source_run_id'],
      'source_head_sha':x['source_head_sha'],
      'source_artifact_id':x['artifact_ids'][n],
      'source_artifact_zip_sha256':x['artifact_zip_sha256'][n],
      'picard_action_64x64':x['picard_actions_64x64'][n],
      'canonical_sha256':x['action_certificate_sha256'][n],
      'retained_bundle_sha256':x['canonical_sha256'],
    }
    (HERE/f'picard-action-sign-{n}.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'coordinate_count':7,'retained_bundle_sha256':x['canonical_sha256'],'action_certificate_sha256':x['action_certificate_sha256']},indent=2,sort_keys=True))
