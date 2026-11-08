"""Restore one original evidence package without changing retained source bytes."""
import argparse
from pathlib import Path, PurePosixPath
from verify_migration import original_bytes, require, verify


def restore(archive, destination):
    for item in archive['members']:
        rel = PurePosixPath(item['member'])
        require(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe archive member')
        path = destination / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(original_bytes(item))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--row', type=int, choices=range(385, 394), required=True)
    parser.add_argument('--destination', type=Path, required=True)
    args = parser.parse_args()
    inventory = verify()
    target = args.destination.resolve()
    require(not target.exists(), 'Choose a new, nonexistent destination')
    target.mkdir(parents=True)
    archive = next(a for a in inventory['archives'] if a['row'] == args.row)
    restore(archive, target)
    print(f"PASS restored row{args.row}: {len(archive['members'])} exact original files.")
