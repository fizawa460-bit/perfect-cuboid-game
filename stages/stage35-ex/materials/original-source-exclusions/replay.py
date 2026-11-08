"""Replay the unchanged author arithmetic in isolated temporary copies.

This checks retained arithmetic and byte identity, not the whole mathematical
dependency chain or the independent-audit verdicts. No network or Actions.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent


def run_all() -> dict:
    if sys.flags.optimize or os.environ.get('PYTHONOPTIMIZE') not in (None, '', '0'):
        raise RuntimeError('Run replay.py without -O/PYTHONOPTIMIZE: rows368/369/376 use assert.')
    integrity = subprocess.run([sys.executable, str(ROOT / 'verify_migration.py')],
                               capture_output=True, text=True)
    if integrity.returncode:
        raise RuntimeError(integrity.stdout + integrity.stderr)
    versions = {name: importlib.metadata.version(name)
                for name in ('sympy', 'numpy', 'python-flint')}
    expected_versions = {'sympy': '1.14.0', 'numpy': '2.5.4', 'python-flint': '0.9.0'}
    if versions != expected_versions:
        raise RuntimeError(f'Replay uses pinned versions: expected {expected_versions}; got {versions}')
    jobs = [
        ('row365-normal', 'parents/row365', 'math/verify_dyadic_frame.py', []),
        ('row365-optimized', 'parents/row365', 'math/verify_dyadic_frame.py', ['-O']),
        ('row367-normal', 'row367', 'math/verify_source_obstruction.py', []),
        ('row367-optimized', 'row367', 'math/verify_source_obstruction.py', ['-O']),
        ('row368', 'row368', 'verify_row368.py', []),
        ('row369', 'row369', 'verify_row369.py', []),
        ('row376', 'row376', 'verify_row376.py', []),
    ]
    results = []
    for label, folder, script, options in jobs:
        print(f'RUN {label}', flush=True)
        with tempfile.TemporaryDirectory(prefix='stage35ex-replay-') as temp:
            target = Path(temp) / 'evidence'
            shutil.copytree(ROOT / folder, target,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            command = [sys.executable, *options, str(target / script)]
            start = time.monotonic()
            child = subprocess.run(command, cwd=target, capture_output=True)
            result = {'label': label, 'source': f'{folder}/{script}', 'python_options': options,
                      'exit_code': child.returncode, 'stdout_sha256': hashlib.sha256(child.stdout).hexdigest(),
                      'stderr_sha256': hashlib.sha256(child.stderr).hexdigest(),
                      'stdout': child.stdout.decode('utf-8', errors='replace'),
                      'stderr': child.stderr.decode('utf-8', errors='replace'),
                      'seconds': round(time.monotonic() - start, 3)}
            if child.returncode:
                raise RuntimeError(json.dumps(result, ensure_ascii=False, indent=2))
            if label in ('row368', 'row369'):
                name = f'{label}_exact.json'
                if (target / name).read_bytes() != (ROOT / folder / name).read_bytes():
                    raise RuntimeError(label + ': regenerated JSON differs byte for byte')
                result['regenerated_json_byte_identity'] = True
            if label == 'row376':
                expected = json.loads((ROOT / folder / 'row376_exact.json').read_text())
                if json.loads(child.stdout) != expected:
                    raise RuntimeError('row376: stdout JSON differs from frozen certificate')
                result['stdout_json_object_identity'] = True
            results.append(result)
            print(f'PASS {label} ({result["seconds"]}s)', flush=True)
    integrity_after = subprocess.run([sys.executable, str(ROOT / 'verify_migration.py')],
                                    capture_output=True, text=True)
    if integrity_after.returncode:
        raise RuntimeError(integrity_after.stdout + integrity_after.stderr)
    return {'schema': 1, 'purpose': 'LOCAL_ARITHMETIC_REPLAY_OF_EXISTING_CERTIFICATES',
            'independent_mathematical_audit': False,
            'environment': {'python': sys.version, 'platform': platform.platform(), 'packages': versions},
            'temporary_copy_execution': True,
            'retained_files_unchanged': True,
            'integrity_before': integrity.stdout.strip(),
            'integrity_after': integrity_after.stdout.strip(), 'results': results,
            'scope': 'Seven runs of five unchanged author verifiers, including immediate row365 parent. Deeper parent completeness/theory remains inherited.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True,
                        help='Write the local replay receipt outside this frozen material directory.')
    args = parser.parse_args()
    output = args.output.resolve()
    if output == ROOT or ROOT in output.parents:
        raise RuntimeError('--output must be outside the frozen material directory')
    receipt = run_all()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print('PASS all seven arithmetic replays; frozen source bytes unchanged.', flush=True)
