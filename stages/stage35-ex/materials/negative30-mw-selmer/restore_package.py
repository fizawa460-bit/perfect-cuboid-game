"""Restore one complete original archive package to a new directory."""
import argparse
from pathlib import Path, PurePosixPath

from verify_migration import ROOT, original_bytes, require, verify


def restore(row, destination):
    inventory = verify()
    packages = [a for a in inventory['archives'] if a['row'] == row]
    require(len(packages) == 1, 'Unknown row')
    target = destination.resolve()
    require(target != ROOT and ROOT not in target.parents,
            'Restore outside the frozen material directory')
    require(not target.exists(), 'Destination must be a new directory')
    # Validate every source before creating or writing the destination.
    prepared = []
    for item in packages[0]['members']:
        rel = PurePosixPath(item['member'])
        require(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe source member')
        prepared.append((rel, original_bytes(item)))
    target.mkdir(parents=True)
    for rel, data in prepared:
        path = target / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    print(f'PASS restored row{row}: {len(prepared)} exact original files to {target}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--row', type=int, required=True)
    parser.add_argument('--destination', type=Path, required=True)
    args = parser.parse_args()
    restore(args.row, args.destination)
