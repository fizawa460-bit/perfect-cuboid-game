#!/usr/bin/env python3
"""Research-only end-to-end replay; never affirms surface/effectivity sources."""
import copy
import hashlib
from pathlib import Path
import sys
import tempfile
import types
from unittest.mock import patch

import source_locked_known_curve_scalar as source
from producer_protocol import replay, validate
from picard_pairing_scalar_producer import produce


def reject(call):
    try:
        call()
    except ValueError:
        return
    raise AssertionError('invalid input accepted')


def main():
    # For each locked dependency, inject code with an observable side effect.
    # All lock checks must finish before ANY dependency code can execute.
    original_locks = source.LOCKS.copy()
    for target in original_locks:
        with tempfile.TemporaryDirectory() as temp:
            marker = Path(temp) / 'executed'
            poisoned = Path(temp) / 'dependency.py'
            poisoned.write_text('from pathlib import Path\nPath('+repr(str(marker))+').touch()\n')
            changed = {(poisoned if p == target else p): h for p,h in original_locks.items()}
            with patch.object(source, 'LOCKS', changed), patch('builtins.exec') as execute:
                reject(source.load)
                assert not execute.called, 'dependency executed before all locks passed'
            assert not marker.exists()

    # Preloaded names must not override verified source bytes.
    with patch.dict(sys.modules, {'pairing_prefix_engine': types.ModuleType('poison')}):
        record = source.produce_known_curve(1)
    validate(record)
    _, P, G, _, _ = source.load()
    plain = lambda matrix: [[int(v) for v in row] for row in matrix.tolist()]
    P, G = plain(P), plain(G)
    locks = {str(p.relative_to(source.ROOT)): h for p,h in original_locks.items()}
    replay(record, P, G, locks)
    assert (record['d'],record['C2'],record['negative_hperp_square_N']) == (2,-4,272)

    # RR consumer is also locked BEFORE execution; no surface credit asserted.
    path = source.HERE.parent / 'hperp_norm_rr_adapter.py'
    raw = path.read_bytes()
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == '069e9215305fe4fa34d9949c871914b5ee17f19d'
    consumer = types.ModuleType('scalar_e2e_rr')
    with patch.dict(sys.modules, {'scalar_e2e_rr': consumer}):
        exec(compile(raw,str(path),'exec'),consumer.__dict__)
    result = consumer.classify_from_norm(record['d'],record['negative_hperp_square_N'],source_affirmed=False)
    assert result.C2 == record['C2'] and result.m == record['m']
    assert result.status == 'RR_INCONCLUSIVE_SOURCE_NOT_AFFIRMED'
    assert not result.effective_divisor_certified

    for key in ('terminal_identity','picard64_coordinates','witness_source_locks'):
        bad = copy.deepcopy(record); del bad[key]
        reject(lambda: replay(bad,P,G,locks))
    for key in ('d','m','C2','negative_hperp_square_N'):
        bad = copy.deepcopy(record); bad[key] += 1
        reject(lambda: replay(bad,P,G,locks))
        bad[key] = 2.0
        reject(lambda: replay(bad,P,G,locks))
    for key in ('picard64_coordinates','selected64_pairings'):
        bad = copy.deepcopy(record); bad[key][0] += 1
        reject(lambda: replay(bad,P,G,locks))
    bad = copy.deepcopy(record); bad['witness_source_locks'] = {'drift':'x'}
    reject(lambda: replay(bad,P,G,locks))
    bad = copy.deepcopy(record)
    bad['C2'] += 2; bad['negative_hperp_square_N'] -= 2*bad['m']**2
    reject(lambda: replay(bad,P,G,locks))  # coherent scalar forgery, wrong Gram square
    bad = copy.deepcopy(record); bad['gram64_sha256'] = 'drift'
    reject(lambda: replay(bad,P,G,locks))
    reject(lambda: source.produce_known_curve(0))
    reject(lambda: produce('test',2,'test',[0.5]*64,P,G,locks))
    print('PASS_32_02_SCALAR_E2E_LOCK_BEFORE_IMPORT_PROTOCOL_REPLAY_RR')
    print('KNOWN_CURVE d=2 C2=-4 N=272; RR_INCONCLUSIVE_SOURCE_NOT_AFFIRMED; credit=0')


if __name__ == '__main__':
    main()
