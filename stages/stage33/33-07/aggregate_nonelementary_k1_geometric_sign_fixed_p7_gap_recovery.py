#!/usr/bin/env python3
"""Run the exact mixed K1 aggregate after repairing expired old32 artifacts, then relock provenance."""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'k1-gap-recovery-manifest.json'
BASE_OUT = HERE / 'nonelementary-k1-geometric-sign-fixed-p7-rescue128-census.json'
OUT = HERE / 'nonelementary-k1-geometric-sign-fixed-p7-gap-recovery-census.json'
EXPECTED_SOURCE_RUNS = {
    'source_old32_run_id': 33004278066,
    'source_p7_run_id': 33013524879,
    'source_support_run_id': 32971195642,
    'source_endpoint_run_id': 32934384807,
}
MAX_RECOVERY_GAPS = 48

manifest = json.loads(MANIFEST.read_text())
if manifest.get('schema') != 'STAGE33_07_K1_GAP_RECOVERY_MANIFEST_V1':
    raise SystemExit('gap-recovery manifest schema regression')
for key, expected in EXPECTED_SOURCE_RUNS.items():
    if int(manifest.get(key, -1)) != expected:
        raise SystemExit(f'gap-recovery provenance regression for {key}')
missing = [tuple(map(int, x)) for x in manifest['missing_old32_coordinates']]
if len(missing) != len(set(missing)) or not missing:
    raise SystemExit('gap-recovery coordinate uniqueness/emptiness regression')
if len(missing) > MAX_RECOVERY_GAPS:
    raise SystemExit('gap-recovery coordinate cap regression')
if any(p == 7 or not (0 <= p < 15 and 0 <= s < 32) for p, s in missing):
    raise SystemExit('gap-recovery coordinate range regression')
if int(manifest['base_old32_live_count']) + len(missing) != 448:
    raise SystemExit('gap-recovery old32 accounting regression')
if int(manifest['p7_live_count']) != 128:
    raise SystemExit('gap-recovery P7 accounting regression')
if int(manifest.get('snapshot_support_count', -1)) != 15:
    raise SystemExit('gap-recovery support snapshot regression')
if manifest.get('stage33_progress') != '6/11':
    raise SystemExit('gap-recovery Stage33 progress regression')
if manifest.get('actual_index512_glue_identified') or manifest.get('arithmetic_HS_closed'):
    raise SystemExit('gap-recovery manifest promotion firewall regression')

subprocess.run(
    ['python', str(HERE / 'aggregate_nonelementary_k1_geometric_sign_fixed_p7_rescue128.py')],
    cwd=HERE,
    check=True,
)
cert = json.loads(BASE_OUT.read_text())
if not cert.get('all_14x32_old_and_P7x128_rescue_subshards_present_exactly_once'):
    raise SystemExit('base exact mixed coverage did not certify')
if not cert.get('all_support_orbit_representative_lifts_checked_exactly_once'):
    raise SystemExit('base exact representative coverage did not certify')
if int(cert.get('weighted_H_checked', -1)) != 1311205952:
    raise SystemExit('base weighted-H coverage regression')
if cert.get('actual_index512_glue_identified') or cert.get('arithmetic_HS_closed'):
    raise SystemExit('Stage33 promotion firewall regression')
if cert.get('stage33_progress') != '6/11':
    raise SystemExit('Stage33 progress firewall regression')

cert.pop('canonical_sha256', None)
cert['schema'] = 'STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SIGN_FIXED_GAP_RECOVERY_CENSUS_V1'
cert.pop('source_rescue32_workflow_run_id_for_P_not_7', None)
cert['source_old32_base_workflow_run_id'] = int(manifest['source_old32_run_id'])
cert['source_p7_rescue128_workflow_run_id'] = int(manifest['source_p7_run_id'])
cert['source_support_workflow_run_id'] = int(manifest['source_support_run_id'])
cert['source_endpoint_workflow_run_id'] = int(manifest['source_endpoint_run_id'])
cert['old32_base_live_artifact_count_at_snapshot'] = int(manifest['base_old32_live_count'])
cert['old32_gap_repaired_artifact_count'] = len(missing)
cert['old32_gap_repaired_coordinates'] = [list(x) for x in missing]
cert['all_old32_artifact_expiry_gaps_repaired_exactly_once'] = True
cert['P7_rescue128_reused_without_recomputation'] = True
cert['artifact_expiry_recovery_only_no_mathematical_shortcut'] = True
raw = json.dumps(cert, sort_keys=True, separators=(',', ':')).encode()
cert['canonical_sha256'] = hashlib.sha256(raw).hexdigest()
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + '\n')
print(json.dumps({
    'success': True,
    'base_old32_live': manifest['base_old32_live_count'],
    'repaired_old32': len(missing),
    'p7_reused': manifest['p7_live_count'],
    'representative_sections_checked': cert['representative_lift_sections_checked'],
    'weighted_H_checked': cert['weighted_H_checked'],
    'survivors': cert['representative_section_survivors'],
    'weighted_survivors': cert['weighted_H_survivors'],
    'k1_rejected': cert['k1_nonelementary_type_rejected'],
    'sha256': cert['canonical_sha256'],
    'next': cert['next_exact_leaf'],
}, indent=2, sort_keys=True))
