"""Check archived native sources and reversible extraction, not new theorem credit."""
from pathlib import Path, PurePosixPath
import ast
import gzip
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[3]
PRIOR_SHA = 'd84545a9f0a002f218e525978d75203a31fd455bbbbb9645eb0f40168ccfc0a7'


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
    require(len(b) == item['stored_bytes'] and digest(b) == item['stored_sha256'],
            'Stored source bytes changed')
    require(item['encoding'] in ('identity', 'gzip'), 'Unknown source encoding')
    if item['encoding'] == 'gzip':
        b = gzip.decompress(b)
    require(len(b) == item['bytes'] and digest(b) == item['sha256'], 'Native export bytes changed')
    return b


def extracted(source, item):
    text = source.decode('utf-8-sig').replace('\r\n', '\n')
    if item['marker']:
        marks = list(re.finditer(r'^NATIVE SOURCE[^\n]*$', text, re.M))
        index = next((i for i, m in enumerate(marks)
                      if m.group(0).strip() == 'NATIVE SOURCE ' + item['marker']), None)
        require(index is not None and index + 1 < len(marks), 'Native source marker missing')
        text = text[marks[index].end():marks[index + 1].start()].strip('\n') + '\n'
    require(item['kind'] in ('python', 'json'), 'Unknown extraction type')
    if item['kind'] == 'python':
        ast.parse(text)
        return text.encode()
    return (json.dumps(json.loads(text), ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode()


def verify():
    manifest = load('MANIFEST.json')['files']
    present = {p.relative_to(REPO).as_posix() for p in ROOT.rglob('*')
               if p.is_file() and '__pycache__' not in p.parts
               and p.name not in ('MANIFEST.json', 'LOCAL-REPLAY.json')}
    require(set(manifest) == present, 'Frozen migration file set changed')
    for name, expected in manifest.items():
        b = safe_path(name).read_bytes()
        require(len(b) == expected['bytes'] and digest(b) == expected['sha256'],
                'Frozen publication changed: ' + name)
    inv = load('SOURCE-INVENTORY.json')
    require(len(inv['sources']) == 24 and len({s['id'] for s in inv['sources']}) == 24,
            'Native source coverage changed')
    sources = {s['key']: original_bytes(s) for s in inv['sources']}
    require(len(sources) == 24, 'Duplicate source key')
    require(all(s['id'] != '1weMNOpPRuYDOC_J_iXhkkPyYAYjc0UCgGmQjAQ1K8cw'
                for s in inv['sources']), 'Mutable CURRENT link treated as frozen history')
    require(len(inv['derived']) == 12, 'Extraction coverage changed')
    for item in inv['derived']:
        b = safe_path(item['path']).read_bytes()
        require(len(b) == item['bytes'] and digest(b) == item['sha256'], 'Derived bytes changed')
        require(b == extracted(sources[item['source_key']], item),
                'Extracted artifact differs from native source')
        if item['original_sha256_when_recovered']:
            require(digest(b) == item['original_sha256_when_recovered'],
                    'Recovered historical-byte checksum changed')
    require(digest((ROOT / 'inputs/prior44D.json').read_bytes()) == PRIOR_SHA,
            'Original 44D input checksum changed')
    require(PRIOR_SHA in sources['R3_p3_manifest'].decode('utf-8-sig') and
            PRIOR_SHA in sources['R3_rank1_manifest'].decode('utf-8-sig'),
            'Historical checksum evidence missing')
    claims = load('CLAIMS.json')
    require(claims['research_paused_after_row'] == 393 and
            claims['new_mathematical_credit'] == 0 and claims['formal_promotion'] is False,
            'Publication scope changed')
    require(claims['retained_HCS_rank_scope'] == 'INHERITED_PROVISIONAL_RESEARCH_ONLY',
            'Historical rank scope promoted')
    for key in ('new_external_hostile_audit', 'all_odd_indices_globally_excluded',
                'finite_tamagawa_tests_prove_uniform_theorem', 'offcycle_points_are_physical_packets',
                'finite_local_squares_imply_global_fourth_square', 'new_signed_source_exclusion'):
        require(claims[key] is False, 'Unproved conclusion promoted: ' + key)
    require(claims['branch_B'] == claims['LOW'] == 'OPEN' and
            claims['row393_source_theorem_verification'] == 'PENDING',
            'Current research limitations changed')
    control = json.loads((ROOT.parent / 'MIGRATION-STATUS.json').read_text())
    require(control['active_publication_pr'] == 1854 and control['create_new_pr'] is False,
            'Single-PR policy changed')
    for name, expected in [('AGENTS.md', 'a65d4672e07181dfe38f628c5befe6f6ac39f8c2'),
                           ('stages/stage35-ex/MAIN-STATE.json', '1435c1cb05b1f6e59649b8e3d1768135ae6ab000')]:
        b = (REPO / name).read_bytes()
        require(hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest() == expected,
                'Protected authority changed')
    print(f'PASS migration: {len(present)} frozen files; 24 native source exports; '
          '12 deterministic extractions; original 44D SHA256 recovered; no authority promotion.')
    return inv


if __name__ == '__main__':
    verify()
