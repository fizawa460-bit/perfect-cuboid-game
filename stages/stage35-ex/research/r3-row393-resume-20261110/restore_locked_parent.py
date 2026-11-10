"""Restore the exact locked row393 members, without certifying the publication manifest."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath
import tempfile


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--destination', required=True, type=Path)
    parser.add_argument('--materials', type=Path, help='classgroup-and-different materials directory')
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    materials = (args.materials or here.parents[1] / 'materials/classgroup-and-different').resolve()
    repo = materials.parents[3]
    archive = next(a for a in json.loads((materials / 'SOURCE-INVENTORY.json').read_text())['archives']
                   if a['row'] == 393)
    lock = json.loads((here / 'PARENT-SHA256.json').read_text())
    members = archive['members']
    names = [m['member'] for m in members]
    if len(names) != len(set(names)) or set(names) != set(lock):
        raise RuntimeError('Row393 inventory does not match the 123 locked names')
    destination = args.destination.resolve()
    if destination.exists():
        raise RuntimeError('Destination already exists')
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='row393-restore-', dir=destination.parent) as tmp:
        tmp = Path(tmp)
        for item in members:
            name = PurePosixPath(item['member'])
            source = PurePosixPath(item['path'])
            if name.is_absolute() or '..' in name.parts or source.is_absolute() or '..' in source.parts:
                raise RuntimeError('Unsafe inventory path')
            src = (repo / source).resolve()
            if repo not in src.parents:
                raise RuntimeError('Source outside repository')
            data = src.read_bytes()
            if 'stored_sha256' in item and (sha(data) != item['stored_sha256'] or len(data) != item['stored_bytes']):
                raise RuntimeError('Stored-byte mismatch: ' + str(source))
            if item['encoding'] == 'gzip':
                data = gzip.decompress(data)
            elif item['encoding'] != 'identity':
                raise RuntimeError('Unknown encoding')
            if sha(data) != item['sha256'] or len(data) != item['bytes'] or sha(data) != lock[str(name)]:
                raise RuntimeError('Original or parent lock mismatch: ' + str(name))
            target = tmp / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        lines = (tmp / archive['manifest_member']).read_text().splitlines()
        sums = {}
        for line in lines:
            if line.strip():
                digest, name = line.split(maxsplit=1)
                name = name.lstrip('*')
                if name in sums:
                    raise RuntimeError('Duplicate original manifest entry')
                sums[name] = digest
        if set(sums) != set(names) - {archive['manifest_member']}:
            raise RuntimeError('Original manifest coverage mismatch')
        if any(sha((tmp / name).read_bytes()) != digest for name, digest in sums.items()):
            raise RuntimeError('Original manifest digest mismatch')
        tmp.rename(destination)
    print(f'PASS locked row393 restoration: {len(names)} parent locks; {len(sums)} original manifest entries')
    print('Publication-wide frozen-manifest verification NOT performed by this helper.')


if __name__ == '__main__':
    main()
