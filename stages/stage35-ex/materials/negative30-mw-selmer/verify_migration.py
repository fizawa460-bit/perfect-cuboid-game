"""Verify the frozen migration and retained source bytes using the standard library.

This checks publication integrity and claim boundaries, not new mathematical
correctness or an independent hostile-audit verdict.
"""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[3]
ROWS = [370, 371, 372, 373, 374, 375, 377, 378, 379, 380, 381, 382, 383, 384]


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def safe_path(name):
    rel = PurePosixPath(name)
    require(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe retained path')
    path = (REPO / rel).resolve()
    require(REPO.resolve() in path.parents, 'Retained path leaves repository')
    return path


def original_bytes(item):
    data = safe_path(item['path']).read_bytes()
    if 'stored_sha256' in item:
        require(digest(data) == item['stored_sha256'] and len(data) == item['stored_bytes'],
                'Stored-byte mismatch: ' + item['path'])
    require(item['encoding'] in ('identity', 'gzip'), 'Unknown storage encoding')
    if item['encoding'] == 'gzip':
        data = gzip.decompress(data)
    require(len(data) == item['bytes'] and digest(data) == item['sha256'],
            'Original-byte mismatch: ' + item['path'])
    return data


def verify():
    manifest = load('MANIFEST.json')
    present = {p.relative_to(REPO).as_posix() for p in ROOT.rglob('*')
               if p.is_file() and '__pycache__' not in p.parts
               and p.name not in ('MANIFEST.json', 'LOCAL-REPLAY.json')}
    require(set(manifest['files']) == present, 'Frozen migration file set changed')
    for name, expected in manifest['files'].items():
        data = safe_path(name).read_bytes()
        require(len(data) == expected['bytes'] and digest(data) == expected['sha256'],
                'Frozen publication changed: ' + name)
    inv = load('SOURCE-INVENTORY.json')
    require([a['row'] for a in inv['archives']] == ROWS, 'Archive row coverage changed')
    mappings = 0
    for archive in inv['archives']:
        require(archive['manifest_verified'] == len(archive['members']) - 1,
                'Source manifest coverage changed')
        members = {m['member']: m for m in archive['members']}
        require(len(members) == len(archive['members']), 'Duplicate source member')
        manifest_name = archive['manifest_member']
        raw = original_bytes(members[manifest_name])
        if manifest_name.endswith('.json'):
            sums = json.loads(raw)
        else:
            sums = {line.split(maxsplit=1)[1].lstrip('*'): line.split(maxsplit=1)[0]
                    for line in raw.decode().splitlines() if line.strip()}
        prefix = str(PurePosixPath(manifest_name).parent)
        prefix = '' if prefix == '.' else prefix + '/'
        require({prefix + n for n in sums} == set(members) - {manifest_name},
                'Original source manifest is incomplete')
        for name, expected in sums.items():
            require(digest(original_bytes(members[prefix + name])) == expected,
                    'Original member checksum mismatch')
        mappings += len(members)
    missing = []
    for item in inv['files']:
        if item['path'] is None:
            require(item['row'] == 377 and item['role'] == 'audit' and item['bytes'] == 3
                    and item['sha256'] == digest(bytes.fromhex('efbbbf')),
                    'Unexpected unretained source')
            missing.append(item['row'])
        else:
            original_bytes(item)
            mappings += 1
    require(missing == [377], 'Audit availability gap changed')
    availability = load('AUDIT-AVAILABILITY.json')
    require(availability['missing_readable_report'] == [377] and
            len(availability['readable_reports']) == 13, 'Audit coverage misreported')
    claims = load('CLAIMS.json')
    require(claims['research_paused_after_row'] == 393, 'Research pause changed')
    require(claims['new_mathematical_credit'] == 0 and claims['formal_promotion'] is False
            and claims['independent_audit_performed_by_this_migration'] is False,
            'Publication incorrectly promotes credit')
    for key in ('minus30_unconditional_exclusion', 'c_Cl_zero_unconditionally_proved',
                'ZF2_proved', 'delta_star_Sel4_nonlift_proved'):
        require(claims[key] is False, 'Unproved conclusion promoted: ' + key)
    require(claims['branch_B'] == claims['LOW'] == 'OPEN', 'Scope incorrectly closed')
    require([r['row'] for r in claims['rows']] == ROWS, 'Claim row coverage changed')
    source_rows = load('R3-SOURCE-RECORDS.json')['records']
    require([r['row'] for r in source_rows] == ROWS, 'Owner snapshot coverage changed')
    for row, source in zip(claims['rows'], source_rows):
        require(row['owner_reported_summary'] == source['reported_summary'] and
                row['owner_reported_audit_status'] == source['latest_status_field_D'],
                'Owner summary or audit qualifier changed')
        require(row['unconditional_new_signed_exclusions'] == 0, 'Unconditional exclusion invented')
        require(row['audit_report_available'] == (row['row'] != 377), 'Audit availability changed')
        require(safe_path(row['proof_path']).is_file(), 'Proof is missing')
        if row['audit_path']:
            require(safe_path(row['audit_path']).is_file(), 'Audit report is missing')
    require('GRH' in claims['row381_condition'] and 'not each character' in claims['row384_condition'],
            'Conditional or averaged-character qualifier missing')
    formal = REPO / 'stages/stage35-ex/MAIN-STATE.json'
    data = formal.read_bytes()
    require(hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            == '1435c1cb05b1f6e59649b8e3d1768135ae6ab000', 'Formal state changed')
    print(f'PASS migration: {len(present)} frozen files; {mappings} exact source mappings; '
          '14 rows; 13 readable audit reports; row377 gap explicit; no unconditional -30 exclusion.')
    return inv


if __name__ == '__main__':
    verify()
