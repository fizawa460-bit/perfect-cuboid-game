from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

# Finite exact check of the parity/gcd lemma used in s7-153.
for R in range(1, 80):
    for S in range(R + 1, 80):
        if gcd(R, S) != 1:
            continue
        for g in range(1, 40):
            if (g * (S + R)) % 2 or (g * (S - R)) % 2:
                continue
            cp = g * (S + R) // 2
            dq = g * (S - R) // 2
            both_odd = (R % 2 == 1 and S % 2 == 1)
            delta2 = 1 if both_odd else 2
            assert g % delta2 == 0
            H = g // delta2
            assert gcd(cp, dq) == H
            Cplus, Cminus = cp // H, dq // H
            assert gcd(Cplus, Cminus) == 1

checks = {
    'stages/stage14/14-s7-153/result.md': [
        'FIRST_REVERSE_EXACT_COMMON_GCD_PROVED=true',
        'FIRST_REVERSE_COPRIME_SIDE_FACTORS_PROVED=true',
    ],
    'stages/stage14/14-s7-154/result.md': [
        'PQ_COMMON_PRIME_SUPPORT_LOCALIZED_TO_H=true',
        'PQ_COPRIME_SIDE_MOVERS_PROVED=true',
        'COMMON_CORE_IS_MOVING_NOT_FIXED=true',
    ],
    'stages/stage14/14-s7-155/result.md': [
        'MOVING_COMMON_CORE_TWO_COPRIME_SIDE_NORMAL_FORM_PROVED=true',
        'Q24_THEOREM_TARGET_NOW_STABLE=true',
        'NEXT=Stage14-s7-156',
    ],
    'stages/stage14/14-s-batch/s7-153-155-report.md': [
        'BATCH_STOP_REASON=receiver_change',
        'BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3',
        'Q24_NEEDED=true',
    ],
}
for rel, tokens in checks.items():
    text = (ROOT / rel).read_text()
    for token in tokens:
        assert token in text, (rel, token)

print('STAGE14_S_BATCH_S7_153_155_AUDIT=PASS')
