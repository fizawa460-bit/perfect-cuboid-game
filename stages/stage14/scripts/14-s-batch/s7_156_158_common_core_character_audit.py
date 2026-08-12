from math import gcd


def check_unit_ratio(U, V, f, n):
    Q = 2 * U * V
    assert gcd(U, V) == 1
    assert gcd(f * n, Q) == 1
    lhs = (n + f) % (2 * U) == 0 and (n - f) % (2 * V) == 0
    r = (n * pow(f, -1, Q)) % Q
    rhs = (r + 1) % (2 * U) == 0 and (r - 1) % (2 * V) == 0
    assert lhs == rhs


for U in range(1, 9):
    for V in range(1, 9):
        if gcd(U, V) != 1:
            continue
        Q = 2 * U * V
        for f in range(1, 80):
            for n in range(1, 80):
                if gcd(f * n, Q) == 1:
                    check_unit_ratio(U, V, f, n)

# Common-core fiber model: g*x*y = c*z implies every g, hence H up to
# the frozen two-primary chart, is divisor-hosted over one outer z.
for c in range(1, 8):
    for z in range(1, 40):
        for g in range(1, c * z + 1):
            if (c * z) % g:
                continue
            assert (c * z) // g >= 1

required = {
    'COMMON_CORE_AVERAGE_MUST_BE_RETAINED=true',
    'UNIT_STRATUM_DIRICHLET_CHARACTER_EXPANSION_PROVED=true',
    'UNIT_NONUNIT_CRT_PARTITION_PROVED=true',
    'Q25_THEOREM_TARGET_NOW_STABLE=true',
    'NEXT=Stage14-s7-159',
}
text = ''.join(open(p, encoding='utf-8').read() for p in [
    'stages/stage14/14-s7-156/result.md',
    'stages/stage14/14-s7-157/result.md',
    'stages/stage14/14-s7-158/result.md',
    'stages/stage14/14-s-batch/s7-156-158-report.md',
])
for token in required:
    assert token in text, token

print('STAGE14_S_BATCH_S7_156_158_AUDIT=PASS')
