"""Check migration bytes and scope; this is not a new mathematical audit."""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[3]
ROWS = list(range(385, 394))


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
    require(digest(data) == item['sha256'] and len(data) == item['bytes'],
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
        require(digest(data) == expected['sha256'] and len(data) == expected['bytes'],
                'Frozen publication changed: ' + name)
    inv = load('SOURCE-INVENTORY.json')
    require([a['row'] for a in inv['archives']] == ROWS, 'Archive row coverage changed')
    mappings = 0
    for archive in inv['archives']:
        members = {m['member']: m for m in archive['members']}
        require(len(members) == len(archive['members']), 'Duplicate source member')
        sums = {}
        for line in original_bytes(members[archive['manifest_member']]).decode().splitlines():
            if line.strip():
                h, name = line.split(maxsplit=1)
                require(name.lstrip('*') not in sums, 'Duplicate checksum entry')
                sums[name.lstrip('*')] = h
        require(set(sums) == set(members) - {archive['manifest_member']},
                'Original source manifest is incomplete')
        require(archive['manifest_verified'] == len(sums), 'Source coverage changed')
        for name, expected in sums.items():
            rel = PurePosixPath(name)
            require(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe archive member')
            require(digest(original_bytes(members[name])) == expected,
                    'Original member checksum mismatch')
        mappings += len(members)
    require(len(inv['files']) == 18, 'Proof/audit coverage changed')
    for item in inv['files']:
        require(original_bytes(item).lstrip(bytes.fromhex('efbbbf')).strip(),
                'Unexpected empty proof/audit')
        mappings += 1
    source = load('R3-SOURCE-RECORDS.json')['records']
    claims = load('CLAIMS.json')
    require([s['row'] for s in source] == ROWS, 'Owner snapshot coverage changed')
    require([r['row'] for r in claims['records']] == ROWS, 'Claim row coverage changed')
    for record, old in zip(claims['records'], source):
        require(record['reported_summary'] == old['reported_summary'] and
                record['reported_audit_status'] == old['latest_status_field_D'],
                'Owner summary or audit status changed')
    require(claims['research_paused_after_row'] == 393 and
            claims['new_mathematical_credit'] == 0 and
            claims['independent_mathematical_audit'] is False and
            claims['formal_promotion'] is False, 'Publication scope changed')
    for field in ('class_group_generation_certified', 'formal181_is_classgroup_rank_or_bound',
                  'qstar_computed', 'true_Sel4_decided', 'unconditional_minus30_exclusion',
                  'whole_Jacobian_three_class_classification', 'conic_failure_proves_nonlift'):
        require(claims[field] is False, 'Unproved conclusion promoted: ' + field)
    require(claims['row393_source_theorem_verification'] == 'PENDING' and
            'SOURCE_THEOREM_VERIFICATION_PENDING' in claims['records'][-1]['reported_audit_status'],
            'Source theorem qualifier missing')
    require(claims['LOW'] == claims['branch_B'] == 'OPEN', 'Scope incorrectly closed')
    control = json.loads((ROOT.parent / 'MIGRATION-STATUS.json').read_text())
    require(control['active_publication_pr'] == 1854 and control['create_new_pr'] is False,
            'Single-PR publication policy changed')
    formal = (REPO / 'stages/stage35-ex/MAIN-STATE.json').read_bytes()
    require(hashlib.sha1(b'blob ' + str(len(formal)).encode() + b'\0' + formal).hexdigest()
            == '1435c1cb05b1f6e59649b8e3d1768135ae6ab000', 'Formal state changed')
    print(f'PASS migration: {len(present)} frozen files; {mappings} exact source mappings; '
          '9 records and 9 audits; theorem-source check pending; one active PR #1854.')
    return inv


if __name__ == '__main__':
    verify()
