#!/usr/bin/env python3
"""Local-only bounded dispatcher. Atomic status, no retries, fail-closed carry."""
import argparse
import ctypes
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
from verify_local_support_qbc_receipt import validate

HERE = Path(__file__).resolve().parent


class MemoryStatus(ctypes.Structure):
    _fields_ = [('length', ctypes.c_ulong), ('load', ctypes.c_ulong)] + [(n, ctypes.c_ulonglong) for n in ('total_phys', 'avail_phys', 'total_page', 'avail_page', 'total_virtual', 'avail_virtual', 'avail_extended')]


def available_ram():
    stat = MemoryStatus()
    stat.length = ctypes.sizeof(stat)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
        raise OSError('cannot measure available RAM')
    return stat.avail_phys


def atomic(path, obj):
    tmp = path.with_suffix('.tmp')
    with tmp.open('w', encoding='utf8', newline='\n') as f:
        json.dump(obj, f, sort_keys=True, indent=2)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo-root', type=Path, required=True)
    ap.add_argument('--source-root', type=Path, required=True)
    ap.add_argument('--durable', type=Path, required=True)
    ap.add_argument('--before', required=True)
    ap.add_argument('--head', required=True)
    args = ap.parse_args()
    key = json.loads((HERE/'SUPPORT-QBC-LOCAL-WAVE-RUNKEY.json').read_text())
    assert key['armed'] and key['local_only'] and key['github_artifact_upload_bytes'] == 0
    assert 1 <= key['planned_local_concurrency'] <= 4
    args.durable.mkdir(parents=True, exist_ok=True)
    # Persistent launch sentinel: even an abnormal dispatcher exit never silently reruns.
    with (args.durable/'launch.lock').open('x') as f:
        json.dump({'pid': os.getpid(), 'head': args.head, 'started_unix': time.time()}, f)
    units = [(r,b) for b in key['authorized_b'] for r in key['authorized_rows'] if [r,b] not in key['excluded_completed_units']]
    assert len(set(units)) == len(units) == key['expected_authorized_units']
    started = time.monotonic()
    running, completed, failed = {}, {}, []
    queue = []
    def receipt(unit):
        return args.durable/f'row{unit[0]:03d}-b{unit[1]:03d}.json'
    for unit in units:
        p = receipt(unit)
        if p.exists():
            result = validate(p, args.source_root)
            assert (result['row_index'], result['b']) == unit
            completed[unit] = result
        else:
            queue.append(unit)
    reason = None
    while True:
        for unit, job in list(running.items()):
            proc, out, err, launch = job
            code = proc.poll()
            if code is None:
                continue
            out.close()
            err.close()
            del running[unit]
            try:
                assert code == 0, f'worker exit {code}'
                result = validate(receipt(unit), args.source_root)
                assert (result['row_index'], result['b']) == unit
                completed[unit] = result
            except Exception as exc:
                failed.append({'unit': unit, 'exit_code': code, 'error': repr(exc)})
                reason = 'FAIL_CLOSED_NO_NEW_DISPATCH'
        saving = sum(int(r['saving']) for r in completed.values())
        elapsed = time.monotonic()-started
        ram = available_ram()
        disk = shutil.disk_usage(args.durable).free
        evidence_bytes = sum(p.stat().st_size for p in args.durable.iterdir() if p.is_file())
        if saving >= int(key['stop_new_dispatch_at_exact_reduction']):
            reason = reason or 'ONE_PERCENT_EXACT_CANDIDATE_REACHED'
        if elapsed >= key['max_elapsed_hours']*3600:
            reason = reason or 'DISPATCH_TIME_BUDGET_REACHED'
        if disk < 2*1024**3 or evidence_bytes > key['projected_local_evidence_bytes']:
            reason = reason or 'RESOURCE_STOP_NO_NEW_DISPATCH'
        if ram < 512*1024**2:
            reason = reason or 'LOW_MEMORY_NO_NEW_DISPATCH'
        # Start at two; expand to four only after first measured completions and RAM headroom.
        limit = key['planned_local_concurrency'] if len(completed) >= 2 else min(2, key['planned_local_concurrency'])
        if reason is None and queue and len(running) < limit and ram >= 1024**3:
            unit = queue.pop(0)
            p = receipt(unit)
            assert not p.exists()
            out = p.with_suffix('.stdout.log').open('xb')
            err = p.with_suffix('.stderr.log').open('xb')
            cmd = [sys.executable, '-u', str(HERE/'run_hpadj22_support_qbc_local_row_b.py'), '--repo-root', str(args.repo_root), '--source-root', str(args.source_root), '--before', args.before, '--head', args.head, '--row-index', str(unit[0]), '--b', str(unit[1]), '--output', str(p)]
            proc = subprocess.Popen(cmd, stdout=out, stderr=err, cwd=args.repo_root)
            running[unit] = (proc, out, err, time.time())
        finished = not running and (reason is not None or not queue)
        status = {
            'schema': 'STAGE32_178_LOCAL_SUPPORT_QBC_WAVE_STATUS_V1', 'supervisor_pid': os.getpid(),
            'execution_head': args.head, 'authorization_before': args.before, 'updated_unix': time.time(),
            'elapsed_seconds': elapsed, 'status': ('STOPPED' if reason else 'COMPLETE') if finished else 'RUNNING',
            'stop_reason': reason, 'remaining_units': len(queue), 'completed': list(completed.values()),
            'failed': failed, 'exact_disjoint_reduction': str(saving), 'main_credit': 0,
            'global_authority': '138652739800650593494', 'hostile_audit_required': True,
            'running': [{'row_index': u[0], 'b': u[1], 'pid': j[0].pid, 'started_unix': j[3]} for u,j in running.items()],
            'available_ram_bytes': ram, 'free_disk_bytes': disk, 'evidence_bytes': evidence_bytes,
            'unknown_units_not_credited': len(queue)+len(running)+len(failed),
        }
        atomic(args.durable/'status.json', status)
        if finished:
            return 1 if failed else 0
        time.sleep(5)


if __name__ == '__main__':
    sys.exit(main())
