"""Check frozen publication bytes, provenance mappings and explicit scope.

This is an import-integrity check, not a mathematical proof or hostile audit.
Python standard library only; -O does not disable checks.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def main():
    manifest = load('MANIFEST.json')
    excluded = {'MANIFEST.json', 'LOCAL-REPLAY.json'}
    present = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()
               and '__pycache__' not in p.parts and p.relative_to(ROOT).as_posix() not in excluded}
    require(present == set(manifest['files']), 'frozen material file set changed')
    for name, info in manifest['files'].items():
        path = Path(name)
        require(not path.is_absolute() and '..' not in path.parts, 'unsafe manifest path')
        data = (ROOT / path).read_bytes()
        require(len(data) == info['bytes'], 'size mismatch: ' + name)
        require(hashlib.sha256(data).hexdigest() == info['sha256'], 'hash mismatch: ' + name)

    inventory = load('provenance/SOURCE-INVENTORY.json')
    imported = []
    for archive in inventory['archives']:
        require(archive['zip_crc_verified'], 'source archive CRC not checked')
        if archive.get('manifest_kind') == 'whole_archive_hash_only':
            require(archive['key'] == 'C3508zip' and
                    archive['archive_sha256'] == archive['expected_archive_sha256'] ==
                    '853b92b62982b95e0c3a7a3e03c28d3f6873a1655900a2c9a2f101a61d2a08f2' and
                    len(archive['members']) == 6 and
                    all(x['path'] is not None for x in archive['members']),
                    'C35-08 whole-archive/source-member lock changed')
        else:
            require(archive['original_manifest_verified'] == len(archive['members']) - 1,
                    'original source archive manifest coverage changed')
        imported.extend(x for x in archive['members'] if x['path'] is not None)
    imported.extend(inventory['files'])
    for source in imported:
        item = manifest['files'].get(source['path'])
        require(item is not None, 'missing imported source: ' + source['path'])
        require(item['bytes'] == source['bytes'] and item['sha256'] == source['sha256'],
                'imported bytes no longer equal recorded source: ' + source['path'])

    claims = load('CLAIMS.json')
    require(claims['research_paused_after_row'] == 393, 'research pause changed')
    require(claims['formal_promotion'] is False and claims['new_mathematical_credit'] == 0,
            'publication incorrectly promotes mathematical credit')
    require(claims['branch_B'] == 'OPEN' and claims['R3_07_LOW'] == 'OPEN', 'scope broadened')
    by_row = {c['row']: c for c in claims['claims']}
    expected = {367: ([18], ['+', '-'], 2),
                368: ([24,36,54,56,64,66,84,94,96,104,114,124,126,144,32,80,88,92,122,128,152], ['+', '-'], 42),
                369: ([48,78,90,120,132], ['+', '-'], 10), 376: ([30], ['+'], 1)}
    require(set(by_row) == set(expected), 'result groups changed')
    for n, (indices, signs, count) in expected.items():
        c = by_row[n]
        require(c['absolute_indices'] == indices and c['signs'] == signs and
                c['newly_excluded_signed_slots'] == count, 'signed scope changed: row' + str(n))
        require(c['proof'] in present and c['audit_file'] in present, 'missing proof or audit')
    require(by_row[376]['minus30'] == 'OPEN' and
            by_row[376]['whole_absolute_index30_excluded'] is False, 'minus30 wrongly excluded')
    require(by_row[376]['row375_full_cantor_chain_required_for_this_result'] is False,
            'row376 parent scope changed')
    erratum = load('SOURCE-ERRATA.json')['items'][0]
    require('1fuws-yuFyWEKQ24dgOqZPCf9EoREzAo9/' in erratum['verified_url'],
            'C35-12 verified locator changed')
    baseline = load('row369/ROW368_BASELINE.json')
    row368 = load('row368/row368_exact.json')
    projection = ('remaining_abs', 'remaining_signed', 'remaining_B_even_abs')
    require(all(k in baseline and k in row368 and row368[k] == baseline[k] for k in projection),
            'row369 baseline no longer equals row368 projection')
    freshness = load('provenance/SOURCE-FRESHNESS.json')
    require(freshness['all_unchanged'] is True and len(freshness['files']) == 18 and
            all(x['unchanged'] is True and
                x['current']['modified_time'] == x['recorded']['modified_time']
                for x in freshness['files']), 'Drive source freshness record changed')
    print(f'PASS migration integrity: {len(present)} frozen files; {len(imported)} byte-exact source mappings; four scoped result groups; research paused at row393.')


if __name__ == '__main__':
    main()
