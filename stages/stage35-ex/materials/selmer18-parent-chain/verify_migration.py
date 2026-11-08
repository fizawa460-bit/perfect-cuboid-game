"""Verify retained signed18 parent evidence and its publication scope."""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[3]
EXPECTED_KEYS = ['row361', 'row363', 'row364', 'ROW360_ORIGINAL_EVIDENCE',
                 'ROW359_ORIGINAL_TRUE_SELMER14_EVIDENCE', 'ROW358_ORIGINAL_FINITE_EVEN_EVIDENCE',
                 'ROW357_ORIGINAL_SCLASS_EVIDENCE', 'ROW356_INDEPENDENT_AUDIT_EVIDENCE',
                 'ROW356_ORIGINAL_FOUR_CUTS_EVIDENCE', 'PARENT_ROW345_LOCAL_DIMENSIONS',
                 'PARENT_ROW352_INFINITY_RANK7', 'ROW355_INDEPENDENT_AUDIT_EVIDENCE']


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
    p = (REPO / rel).resolve()
    require(REPO.resolve() in p.parents, 'Retained path leaves repository')
    return p


def original_bytes(item):
    b = safe_path(item['path']).read_bytes()
    if 'stored_sha256' in item:
        require(len(b) == item['stored_bytes'] and digest(b) == item['stored_sha256'],
                'Stored-byte mismatch: ' + item['path'])
    require(item['encoding'] in ('identity', 'gzip'), 'Unknown storage encoding')
    if item['encoding'] == 'gzip':
        b = gzip.decompress(b)
    require(len(b) == item['bytes'] and digest(b) == item['sha256'],
            'Original-byte mismatch: ' + item['path'])
    return b


def verify():
    frozen = load('MANIFEST.json')['files']
    present = {p.relative_to(REPO).as_posix() for p in ROOT.rglob('*')
               if p.is_file() and '__pycache__' not in p.parts
               and p.name not in ('MANIFEST.json', 'LOCAL-REPLAY.json')}
    require(set(frozen) == present, 'Frozen migration file set changed')
    for path, expected in frozen.items():
        b = safe_path(path).read_bytes()
        require(len(b) == expected['bytes'] and digest(b) == expected['sha256'],
                'Frozen publication changed: ' + path)
    inv = load('SOURCE-INVENTORY.json')
    require([a['key'] for a in inv['archives']] == EXPECTED_KEYS, 'Archive coverage changed')
    by_key = {a['key']: a for a in inv['archives']}
    selected = omitted = 0
    for archive in inv['archives']:
        members = {m['member']: m for m in archive['members']}
        require(len(members) == len(archive['members']), 'Duplicate source member')
        if archive['manifest_member']:
            raw = json.loads(original_bytes(members[archive['manifest_member']]))
            raw = raw['files'] if 'files' in raw and 'algorithm' in raw else raw
            sums = {k: v if isinstance(v, str) else v['sha256'] for k, v in raw.items()}
            require(set(sums) == set(members) - {archive['manifest_member']},
                    'Original manifest coverage changed')
            require(archive['original_manifest_verified'] == len(sums), 'Source count changed')
            for name, h in sums.items():
                require(members[name]['sha256'] == h, 'Source manifest digest mismatch')
        else:
            parent = archive['embedded_in']
            outer = next(a for a in inv['archives'] if a['sha256'] == parent['package'])
            bound = next(m for m in outer['members'] if m['member'] == parent['member'])
            require(bound['sha256'] == archive['sha256'], 'Unbound nested source archive')
        for name, item in members.items():
            rel = PurePosixPath(name)
            require(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe archive member')
            if item['path'] is not None:
                original_bytes(item)
                selected += 1
            else:
                omitted += 1
                if item['omission'] == 'nested archive contents mapped separately':
                    require(name.endswith('.zip') and
                            by_key[item['child_archive']]['sha256'] == item['sha256'],
                            'Nested archive mapping mismatch')
                else:
                    require(item['omission'] == 'administrative writeback snapshot retained in source Drive ZIP'
                            and name.startswith('record_updates/')
                            and not name.startswith('record_updates/parent'),
                            'Undeclared evidence omission')
            require(not name.startswith('math/') or item['path'] is not None
                    or 'child_archive' in item,
                    'Mathematical input omitted')
    expected_files = {(361, 'proof'), (363, 'proof'), (364, 'proof'),
                      (363, 'audit'), (364, 'audit'), (364, 'audit_code')}
    require({(f['row'], f['role']) for f in inv['files']} == expected_files
            and len(inv['files']) == 6, 'Primary proof/audit coverage changed')
    for item in inv['files']:
        require(original_bytes(item).strip(), 'Empty primary source')
    claims = load('CLAIMS.json')
    require(claims['research_paused_after_row'] == 393 and claims['new_mathematical_credit'] == 0
            and claims['formal_promotion'] is False and claims['independent_mathematical_audit'] is False,
            'Publication scope changed')
    require(claims['signed18_root_field_degree'] == 36 and claims['minus30_root_field_degree'] == 105,
            'Field scope changed')
    for key in ('class_one_transferred_to_minus30', 'whole_MW_rank7_proved_by_this_batch',
                'true_Selmer9_identified_with_MW_rank9', 'CT_entry_computed',
                'whole_MW_p163_U_constructed', 'new_source_exclusion_by_this_batch'):
        require(claims[key] is False, 'Unproved conclusion promoted: ' + key)
    require(claims['row362_audit_status'] == 'DEPENDENT_COROLLARY_INDEPENDENT_AUDIT_PENDING'
            and claims['row361_standalone_audit_report'] == 'NOT_LOCATED',
            'Historical audit scope promoted')
    source = load('R3-SOURCE-RECORDS.json')['records']
    require([r['row'] for r in claims['records']] == [r['row'] for r in source], 'Owner rows changed')
    for record, old in zip(claims['records'], source):
        require(record['reported_summary'] == old['reported_summary'] and
                record['reported_audit_status'] == old['latest_status_field_D'], 'Owner fields changed')
    require(claims['LOW'] == claims['branch_B'] == 'OPEN' and
            claims['row393_source_theorem_verification'] == 'PENDING', 'Current limitations changed')
    control = json.loads((ROOT.parent / 'MIGRATION-STATUS.json').read_text())
    require(control['active_publication_pr'] == 1854 and control['create_new_pr'] is False,
            'Single-PR publication policy changed')
    b = (REPO / 'stages/stage35-ex/MAIN-STATE.json').read_bytes()
    require(hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
            == '1435c1cb05b1f6e59649b8e3d1768135ae6ab000', 'Formal state changed')
    print(f'PASS migration: {len(present)} frozen files; 12 source packages; '
          f'{selected + 6} retained source mappings; {omitted} declared omissions; '
          'signed18 field36 only; one active PR #1854.')
    return inv


if __name__ == '__main__':
    verify()
