#!/usr/bin/env python3
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def read(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def audit_quadratic_root_equivalence():
    # The equivalence is tested on every unit divisor for several small exact
    # packets.  It uses only gcd(f,2UV)=1, the K-free condition used in 4gg.
    packets = [
        (3, 5, 1, 1, 11 * 13),
        (3, 5, 2, 7, 11 * 17),
        (5, 7, 3, 4, 11 * 13 * 17),
    ]
    for U, V, Gm, Gp, N in packets:
        for f in divisors(N):
            assert gcd(f, 2 * U * V) == 1
            fp = N // f
            crt = (
                (Gp * fp + Gm * f) % (2 * U) == 0
                and (Gp * fp - Gm * f) % (2 * V) == 0
            )
            quadratic = (
                (Gm * f * f + Gp * N) % (2 * U) == 0
                and (Gm * f * f - Gp * N) % (2 * V) == 0
            )
            assert crt == quadratic


def audit_nested_divisor_shape():
    m = 11 * 13 * 17
    tuples = []
    for tp in divisors(m):
        for tq in divisors(m):
            N = tp * tq
            for f in divisors(N):
                tuples.append((tp, tq, f, N // f))
                assert tp * tq == f * (N // f)
    assert tuples
    # This is genuinely more data than one divisor choice of m.
    assert len(tuples) > len(divisors(m))


def audit_tokens():
    target = read('stages/stage14/14-4gh/h-target.md')
    result = read('stages/stage14/14-4ghH/result.md')
    literature = read('stages/stage14/14-4ghH/literature.md')
    report = read('stages/stage14/14-4-batch/4ghH-report.md')

    for token in [
        'H_STAGE=Stage14-4ghH',
        'SOURCE_SNAPSHOT_SHA=79393f83b1110b7e66b41a23c51596a10bc6c7ef',
        'TARGET_FREEZES_AT_DISPATCH=true',
        'DO_NOT_REPLACE_EVERY_PRINCIPAL_CELL_BY_ALMOST_ALL_MODULI=true',
    ]:
        assert token in target, token

    for token in [
        'EXACT_QUADRATIC_DIVISOR_ROOT_NORMAL_FORM_DERIVED=true',
        'EXACT_TWO_CRT_CONGRUENCES_RETAINED=true',
        'OFF_THE_SHELF_THEOREM_APPLICABLE=false',
        'DIRECT_TRANSFER_PROVED=false',
        'FIRST_MOMENT_FULL_EXPONENT_PROVED=false',
        'FIRST_MOMENT_FIXED_POWER_DEFICIT_PROVED=false',
        'PARAMETER_DICHOTOMY_PROVED=false',
        'MAINLINE_BLOCKED_BY_H=true',
        'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
        'STAGE14_4GI_EXECUTED=false',
    ]:
        assert token in result, token

    for token in [
        'DIRECT_FULL_TARGET_THEOREM_COUNT=0',
        'EVERY_PRINCIPAL_CELL_UNIFORMITY_SUPPLIED=false',
        'EXACT_TWO_CRT_CONGRUENCES_RETAINED_IN_ANY_CANDIDATE=false',
    ]:
        assert token in literature, token

    for token in [
        'BATCH_START_MAIN_SHA=72e747a7680d01f490ce549b4a8acbf38c368912',
        'BATCH_FIRST_STAGE=Stage14-4ghH',
        'BATCH_LAST_STAGE=Stage14-4ghH',
        'BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=1',
        'BATCH_INTEGRATED_H_UNITS=Stage14-4ghH',
        'BATCH_STOP_REASON=unresolved_external_gate',
        'STAGE14_MAIN_BATCH=STOPPED_EARLY',
        'PUBLICATION_MAIN_RECHECK_COMPLETE=true',
    ]:
        assert token in report, token


if __name__ == '__main__':
    audit_quadratic_root_equivalence()
    audit_nested_divisor_shape()
    audit_tokens()
    print('Stage14-main-batch 4ghH deterministic audit: PASS')
