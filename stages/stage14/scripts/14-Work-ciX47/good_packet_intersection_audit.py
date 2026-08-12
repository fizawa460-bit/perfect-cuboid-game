from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def text(rel):
    return (ROOT / rel).read_text()


result = text('stages/stage14/14-Work-ciX47/result.md')
matrix = text('docs/stage14-toolbox/work-ciX47-receiver-matrix.md')
qradar = text('docs/stage14-q21-literature-radar.md')
qsummary = text('docs/stage14-q21-summary.md')
s143 = text('stages/stage14/14-s7-143/result.md')

required_result = [
    'STAGE14_WORK_CIX47=COMPLETE_Q17_GOOD_PACKET_INTERSECTION_SUPPORT_LOCALIZATION_AND_Q21_TRIGGER',
    'GOOD_PACKET_INTERSECTION_SUPPORT_CONSUMED=true',
    'GOOD_PACKET_HIT_WITNESS_EXPONENT_EQUIVALENCE_CONSUMED=true',
    'UPPER_FIBER_PLUS_LARGE_GOOD_SET_DOES_NOT_FORCE_LARGE_INTERSECTION=true',
    'S_Q17_GOOD_INTERSECTION_THEOREM_SPECIES_COUNT=2',
    'Q17_INNER_KERNEL_DEFICIT_RECHARGED=false',
    'POST_MASK_REMAINS_SEPARATELY_CHARGED=true',
    'Q_COMPONENT=COMPLETE',
    'Q21_NEEDED=true',
    'TH34_NEEDED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
]
for token in required_result:
    assert token in result, token

required_matrix = [
    'UniformScalarFilteredTau3Q17GoodPacketPushforwardIntersectionLowerCoverage',
    'UniformPolynomialOuterPairFilteredTau3Q17GoodPacketPushforwardIntersectionLowerCoverage',
    'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
]
for token in required_matrix:
    assert token in matrix, token

required_q = [
    'DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0',
    'Q17_GOOD_PUSHFORWARD_INTERSECTION_DIRECT_THEOREM_FOUND=false',
    'Q21_GOOD_PACKET_INDICATOR_CORRELATION_ENCODING_TEST',
    'Q21_INTERSECTION_FIRST_SECOND_MOMENT_TEST',
    'Q21_POST_MASK_SEARCHED=false',
]
for token in required_q:
    assert token in qradar or token in qsummary, token

assert 'Q21_THEOREM_TARGET_NOW_STABLE=true' in s143
assert 'RECEIVER_MATERIALLY_CHANGED=true' in s143

# Pure set-theoretic no-go: upper fibers do not imply overlap.
Theta = set(range(20))
G = set(range(10))
P = set(range(10, 20))
assert len(G) == len(P) == 10
assert len(G & P) == 0

# Packet/witness exponent-equivalence finite analogue with bounded fibers.
fibers = {theta: list(range(theta % 3 + 1)) for theta in range(7)}
H = set(fibers)
Lambda_H_count = sum(len(fibers[t]) for t in H)
assert len(H) <= Lambda_H_count <= 3 * len(H)

print('Stage14-Work-ciX47 good-packet intersection audit: PASS')
