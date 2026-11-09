"""Replay fixed existing certificates; do not run discovery or new research."""
import argparse
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time
from restore_package import restore
from verify_migration import ROOT, digest, load, require, verify


def run_job(job, inventory):
    archive = next(a for a in inventory['archives'] if a['row'] == job['row'])
    with tempfile.TemporaryDirectory(prefix='stage35ex-materials03-replay-') as tmp:
        target = Path(tmp)
        restore(archive, target)
        expected = ((target / job['expected']).read_bytes() if 'expected' in job else None)
        command = [sys.executable, job['script']]
        started = time.monotonic()
        result = subprocess.run(command, cwd=target, capture_output=True)
        receipt = {'id': job['id'], 'row': job['row'], 'script': job['script'],
                   'exit_code': result.returncode,
                   'seconds': round(time.monotonic() - started, 3),
                   'stdout_sha256': digest(result.stdout), 'stderr_sha256': digest(result.stderr),
                   'stdout_tail': result.stdout.decode(errors='replace')[-1800:],
                   'stderr_tail': result.stderr.decode(errors='replace')[-1200:]}
        require(result.returncode == 0, json.dumps(receipt, ensure_ascii=False))
        require(job['comparison'] in ('json_identity', 'author_assertions'), 'Unknown comparison')
        if job['comparison'] == 'json_identity':
            require(json.loads(result.stdout) == json.loads(expected),
                    job['id'] + ': regenerated JSON differs')
            receipt['retained_json_identity'] = True
        receipt['comparison'] = job['comparison']
        return receipt


def main(args):
    require(not sys.flags.optimize and os.environ.get('PYTHONOPTIMIZE') in (None, '', '0'),
            'Run without -O/PYTHONOPTIMIZE: original scripts use assert')
    output = args.output.resolve()
    require(output != ROOT and ROOT not in output.parents, 'Receipt must be outside frozen payload')
    inventory = verify()
    versions = {p: importlib.metadata.version(p) for p in ('python-flint', 'mpmath')}
    require(versions == {'python-flint': '0.9.0', 'mpmath': '1.3.0'}, 'Use pinned dependencies')
    all_jobs = load('REPLAY-JOBS.json')['jobs']
    jobs = [j for j in all_jobs if j['id'] in args.job] if args.job else all_jobs
    require(jobs and set(args.job) <= {j['id'] for j in all_jobs}, 'Unknown or empty job selection')
    identity = digest((ROOT / 'MANIFEST.json').read_bytes())
    if args.resume and output.exists():
        receipt = json.loads(output.read_text())
        require(receipt['manifest_sha256'] == identity, 'Resume receipt belongs to another payload')
    else:
        receipt = {'schema': 1, 'purpose': 'EXISTING_CERTIFICATE_ARITHMETIC_REPLAY',
                   'independent_mathematical_audit': False, 'manifest_sha256': identity,
                   'environment': {'python': sys.version, 'platform': platform.platform(),
                                   'packages': versions}, 'results': []}
    done = {r['id'] for r in receipt['results'] if r['exit_code'] == 0}
    output.parent.mkdir(parents=True, exist_ok=True)
    for job in jobs:
        if job['id'] in done:
            print('REUSE ' + job['id'], flush=True)
            continue
        print('RUN ' + job['id'], flush=True)
        result = run_job(job, inventory)
        receipt['results'].append(result)
        output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
        print('PASS ' + job['id'] + ' (' + str(result['seconds']) + 's)', flush=True)
    verify()
    print('PASS selected arithmetic replay; original source bytes unchanged.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--job', action='append', default=[])
    main(parser.parse_args())
