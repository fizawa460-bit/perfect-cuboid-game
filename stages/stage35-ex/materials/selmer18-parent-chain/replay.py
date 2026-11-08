"""Replay fixed archived certificates. Discovery scripts are never selected."""
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
from verify_migration import ROOT, digest, load, original_bytes, require, verify


def stable(value):
    if isinstance(value, dict):
        return {k: stable(v) for k, v in value.items() if k not in ('seconds', 'elapsed_seconds')}
    if isinstance(value, list):
        return [stable(v) for v in value]
    return value


def run_job(job, inv):
    archive = next(a for a in inv['archives'] if a['key'] == job['package'])
    with tempfile.TemporaryDirectory(prefix='stage35ex-selmer18-replay-') as tmp:
        target = Path(tmp)
        restore(archive, target)
        if job.get('audit_code'):
            item = next(f for f in inv['files'] if f['role'] == 'audit_code' and f['row'] == 364)
            (target / job['script']).write_bytes(original_bytes(item))
        expected = json.loads((target / job['expected']).read_text()) if 'expected' in job else None
        options = job.get('python_options', [])
        require(options in ([], ['-O']), 'Unknown Python options')
        command = [sys.executable, *options, job['script'], *job.get('arguments', [])]
        environment = dict(os.environ)
        environment.pop('STAGE35EX_DEPS', None)
        started = time.monotonic()
        result = subprocess.run(command, cwd=target, env=environment, capture_output=True)
        receipt = {'id': job['id'], 'package': job['package'], 'script': job['script'],
                   'arguments': job.get('arguments', []), 'python_options': options,
                   'exit_code': result.returncode, 'seconds': round(time.monotonic() - started, 3),
                   'stdout_sha256': digest(result.stdout), 'stderr_sha256': digest(result.stderr),
                   'stdout_tail': result.stdout.decode(errors='replace')[-2000:],
                   'stderr_tail': result.stderr.decode(errors='replace')[-1500:]}
        require(result.returncode == 0, json.dumps(receipt, ensure_ascii=False))
        parsed = []
        for line in result.stdout.decode().splitlines():
            try:
                parsed.append(json.loads(line))
            except json.JSONDecodeError:
                pass
        if expected is not None:
            require(any(stable(v) == stable(expected) for v in parsed),
                    job['id'] + ': retained JSON differs; output=' + result.stdout.decode()[-2200:])
            receipt['retained_json_identity_except_runtime'] = True
        for key, value in job.get('required_fields', {}).items():
            require(any(isinstance(v, dict) and v.get(key) == value for v in parsed),
                    job['id'] + ': required result field differs: ' + key)
        receipt['comparison'] = 'retained_json_except_timing' if expected is not None else 'original_checks_and_listed_fields'
        return receipt


def main(args):
    require(not sys.flags.optimize and os.environ.get('PYTHONOPTIMIZE') in (None, '', '0'),
            'Run the orchestrator without -O/PYTHONOPTIMIZE')
    output = args.output.resolve()
    require(output != ROOT and ROOT not in output.parents, 'Receipt must be outside frozen payload')
    inv = verify()
    versions = {p: importlib.metadata.version(p) for p in ('python-flint', 'sympy', 'cypari2')}
    require(versions == {'python-flint': '0.9.0', 'sympy': '1.14.0', 'cypari2': '2.2.4'},
            'Use pinned dependencies')
    from cypari2 import Pari
    pari_version = str(Pari().version())
    jobs = load('REPLAY-JOBS.json')['jobs']
    selected = [j for j in jobs if j['id'] in args.job] if args.job else jobs
    require(selected and set(args.job) <= {j['id'] for j in jobs}, 'Unknown job selection')
    identity = digest((ROOT / 'MANIFEST.json').read_bytes())
    if args.resume and output.exists():
        receipt = json.loads(output.read_text())
        require(receipt['manifest_sha256'] == identity, 'Resume receipt belongs to another payload')
    else:
        receipt = {'schema': 1, 'purpose': 'EXISTING_SIGNED18_PARENT_CERTIFICATE_REPLAY',
                   'independent_mathematical_audit': False, 'manifest_sha256': identity,
                   'environment': {'python': sys.version, 'platform': platform.platform(),
                                   'packages': versions, 'PARI': pari_version}, 'results': []}
    done = {r['id'] for r in receipt['results'] if r['exit_code'] == 0}
    output.parent.mkdir(parents=True, exist_ok=True)
    for job in selected:
        if job['id'] in done:
            print('REUSE ' + job['id'], flush=True)
            continue
        print('RUN ' + job['id'], flush=True)
        result = run_job(job, inv)
        receipt['results'].append(result)
        output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
        print('PASS ' + job['id'] + ' (' + str(result['seconds']) + 's)', flush=True)
    verify()
    print('PASS retained mathematical certificate replay; no discovery or new mathematical credit.')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--resume', action='store_true')
    p.add_argument('--job', action='append', default=[])
    main(p.parse_args())
