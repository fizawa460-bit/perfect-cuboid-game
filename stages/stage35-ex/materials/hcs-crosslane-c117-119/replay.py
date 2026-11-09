"""Replay six retained historical programs on isolated source-bound inputs."""
import argparse
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
from verify_migration import ROOT, digest, load, require, verify


def run(job):
    with tempfile.TemporaryDirectory(prefix='stage35ex-hcs-replay-') as tmp:
        target = Path(tmp)
        source = ROOT / job['code']
        shutil.copyfile(source, target / source.name)
        for item in job.get('inputs', []):
            p = target / item['target']
            p.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / item['source'], p)
        started = time.monotonic()
        result = subprocess.run([sys.executable, source.name], cwd=target, capture_output=True)
        receipt = {'id': job['id'], 'exit_code': result.returncode,
                   'seconds': round(time.monotonic() - started, 3),
                   'stdout_sha256': digest(result.stdout), 'stderr_sha256': digest(result.stderr),
                   'stdout_tail': result.stdout.decode(errors='replace')[-1800:],
                   'stderr_tail': result.stderr.decode(errors='replace')[-1500:]}
        require(result.returncode == 0, json.dumps(receipt, ensure_ascii=False))
        raw = ((target / job['actual']).read_bytes() if job.get('actual') else result.stdout)
        actual = json.loads(raw)
        if job.get('expected'):
            require(actual == json.loads((ROOT / job['expected']).read_text()),
                    job['id'] + ': declared evidence JSON differs')
            receipt['declared_evidence_json_identity'] = True
        for key, value in job.get('required_fields', {}).items():
            require(actual.get(key) == value, job['id'] + ': result scope field differs: ' + key)
        receipt['comparison'] = 'declared_json_identity' if job.get('expected') else 'original_assertions_and_scope_fields'
        return receipt


def main(args):
    require(not sys.flags.optimize and os.environ.get('PYTHONOPTIMIZE') in (None, '', '0'),
            'Run without -O/PYTHONOPTIMIZE: archived programs use assert')
    output = args.output.resolve()
    require(output != ROOT and ROOT not in output.parents, 'Receipt must be outside frozen payload')
    verify()
    version = importlib.metadata.version('sympy')
    require(version == '1.14.0', 'Use SymPy 1.14.0')
    jobs = load('REPLAY-JOBS.json')['jobs']
    selected = [j for j in jobs if j['id'] in args.job] if args.job else jobs
    require(selected and set(args.job) <= {j['id'] for j in jobs}, 'Unknown job selection')
    identity = digest((ROOT / 'MANIFEST.json').read_bytes())
    if args.resume and output.exists():
        receipt = json.loads(output.read_text())
        require(receipt['manifest_sha256'] == identity, 'Resume receipt belongs to another payload')
    else:
        receipt = {'schema': 1, 'purpose': 'REPLAY_OF_EXISTING_C117_C119_CERTIFICATES',
                   'independent_mathematical_audit': False, 'manifest_sha256': identity,
                   'environment': {'python': sys.version, 'platform': platform.platform(),
                                   'sympy': version}, 'results': []}
    done = {r['id'] for r in receipt['results'] if r['exit_code'] == 0}
    output.parent.mkdir(parents=True, exist_ok=True)
    for job in selected:
        if job['id'] in done:
            print('REUSE ' + job['id'], flush=True)
            continue
        print('RUN ' + job['id'], flush=True)
        receipt['results'].append(run(job))
        output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
        print('PASS ' + job['id'], flush=True)
    verify()
    print('PASS six historical program replays; no new theorem or audit promotion.')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--resume', action='store_true')
    p.add_argument('--job', action='append', default=[])
    main(p.parse_args())
