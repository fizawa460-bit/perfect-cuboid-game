"""Restore the retained mathematical paths; admin writebacks remain on Drive."""
import argparse
from pathlib import Path, PurePosixPath
from verify_migration import original_bytes, require, verify


def restore(archive, target):
    count = 0
    for item in archive['members']:
        if item['path'] is None:
            continue
        rel = PurePosixPath(item['member'])
        require(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe archive member')
        p = target / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(original_bytes(item))
        count += 1
    return count


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--package', required=True)
    p.add_argument('--destination', type=Path, required=True)
    args = p.parse_args()
    inventory = verify()
    archive = next((a for a in inventory['archives'] if a['key'] == args.package), None)
    require(archive is not None, 'Unknown retained package')
    target = args.destination.resolve()
    require(not target.exists(), 'Choose a new, nonexistent destination')
    target.mkdir(parents=True)
    print(f'PASS restored {restore(archive, target)} retained mathematical/source paths.')
