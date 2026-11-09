"""Restore original archive paths in temporary directories and replay selected checks.

Run without -O. Full expensive checks are available through --job, while the
default selection is frozen in REPLAY-JOBS.json. Receipts are written outside
the published payload; previously completed jobs can be resumed explicitly.
"""
import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path, PurePosixPath
import platform
import subprocess
import sys
import tempfile
import time

from verify_migration import ROOT, digest, load, original_bytes, require, verify


def clean(value, ignored):
    if isinstance(value, dict):
        return {k: clean(v, ignored) for k, v in value.items() if k not in ignored}
    if isinstance(value, list):
        return [clean(v, ignored) for v in value]
    return value


def run_job(job, inventory):
    archive = next(a for a in inventory['archives'] if a['row'] == job['row'])
    with tempfile.TemporaryDirectory(prefix='stage35ex-migrate-replay-') as temp:
        target = Path(temp)
        for item in archive['members']:
            rel = PurePosixPath(item['member'])
            require(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe archive path')
            path = target / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(original_bytes(item))
        # All archived files, including their original checksum manifest, are
        # restored byte for byte before any author code is executed.
        expected_bytes = ((target / job['expected']).read_bytes()
                          if 'expected' in job else None)
        command = [sys.executable, job['script'], *job.get('arguments', [])]
        start = time.monotonic()
        result = subprocess.run(command, cwd=target, capture_output=True)
        receipt = {'id': job['id'], 'row': job['row'], 'script': job['script'],
                   'arguments': job.get('arguments', []), 'exit_code': result.returncode,
                   'seconds': round(time.monotonic() - start, 3),
                   'stdout_sha256': digest(result.stdout), 'stderr_sha256': digest(result.stderr),
                   'stdout_tail': result.stdout.decode(errors='replace')[-1600:],
                   'stderr_tail': result.stderr.decode(errors='replace')[-1600:]}
        require(result.returncode == 0, json.dumps(receipt, ensure_ascii=False))
        kind = job.get('comparison', 'author_assertions_only')
        if kind in ('stdout_json', 'written_json'):
            expected = json.loads(expected_bytes)
            actual = json.loads(result.stdout if kind == 'stdout_json' else
                                (target / job['actual']).read_bytes())
            ignored = job.get('ignore_runtime_keys', [])
            require(clean(actual, ignored) == clean(expected, ignored),
                    job['id'] + ': regenerated JSON differs')
            receipt['json_identity'] = True
            receipt['ignored_runtime_keys'] = ignored
        elif kind == 'stdout_bytes':
            require(result.stdout == expected_bytes,
                    job['id'] + ': stdout bytes differ')
            receipt['stdout_byte_identity'] = True
        else:
            require(kind == 'author_assertions_only', 'Unknown output comparison')
        receipt['comparison'] = kind
        return receipt


def main(args):
    require(not sys.flags.optimize and os.environ.get('PYTHONOPTIMIZE') in (None, '', '0'),
            'Run without -O/PYTHONOPTIMIZE: retained scripts use assert')
    output = args.output.resolve()
    require(output != ROOT and ROOT not in output.parents, 'Receipt must be outside frozen payload')
    inventory = verify()
    versions = {p: importlib.metadata.version(p) for p in ('sympy', 'python-flint')}
    require(versions == {'sympy': '1.14.0', 'python-flint': '0.9.0'}, 'Use pinned dependencies')
    jobs = load('REPLAY-JOBS.json')['jobs']
    chosen = [j for j in jobs if args.all or (j['id'] in args.job if args.job else j['default'])]
    require(chosen and set(args.job) <= {j['id'] for j in jobs}, 'Unknown or empty job selection')
    if args.resume and output.exists():
        receipt = json.loads(output.read_text())
        require(receipt['manifest_sha256'] == digest((ROOT / 'MANIFEST.json').read_bytes()),
                'Resume receipt belongs to another frozen payload')
    else:
        receipt = {'schema': 1, 'purpose': 'SELECTED_EXISTING_ARITHMETIC_REPLAY',
                   'independent_mathematical_audit': False,
                   'manifest_sha256': digest((ROOT / 'MANIFEST.json').read_bytes()),
                   'environment': {'python': sys.version, 'platform': platform.platform(),
                                   'packages': versions}, 'results': []}
    done = {r['id'] for r in receipt['results'] if r['exit_code'] == 0}
    output.parent.mkdir(parents=True, exist_ok=True)
    for job in chosen:
        if job['id'] in done:
            print('REUSE ' + job['id'], flush=True)
            continue
        print('RUN ' + job['id'], flush=True)
        result = run_job(job, inventory)
        receipt['results'].append(result)
        output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
        print('PASS ' + job['id'] + ' (' + str(result['seconds']) + 's)', flush=True)
    verify()
    print('PASS selected arithmetic replay; original published source bytes unchanged.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--job', action='append', default=[])
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--resume', action='store_true')
    main(parser.parse_args())
