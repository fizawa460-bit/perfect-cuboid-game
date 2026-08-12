from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

def must(path, tokens):
    text = (ROOT / path).read_text(encoding='utf-8')
    for token in tokens:
        assert token in text, (path, token)

must('stages/stage14/14-s7-140/result.md', [
    'S_PUSHFORWARD_POINTWISE_UPPER_ENVELOPE=Bo1',
    'S_Q17_GOOD_PACKET_COVERAGE_PROVED=false',
    'Q17_INNER_KERNEL_DEFICIT_RECHARGED=false',
])
must('stages/stage14/14-Work-chX46/result.md', [
    'PUSHFORWARD_UPPER_ENVELOPE_DOES_NOT_IMPLY_LOWER_COVERAGE=true',
    'S_PUSHFORWARD_LOWER_COVERAGE_THEOREM_SPECIES_COUNT=2',
    'Q21_NEEDED=false',
])
must('stages/stage14/14-s7-141/result.md', [
    'S_Q17_GOOD_PUSHFORWARD_INTERSECTION_DEFINED=true',
    '#G = #H + #M',
    'PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false',
])
must('stages/stage14/14-s7-142/result.md', [
    '#H <= #Lambda_H <= B^o(1) #H',
    'S_GOOD_HIT_PACKET_TO_WITNESS_SUPPORT_EQUIVALENCE_PROVED=true',
    'S_Q17_GOOD_PACKET_HIT_DEFICIT_DEFINED=true',
])
must('stages/stage14/14-s7-143/result.md', [
    'UniformScalarFilteredTau3Q17GoodPacketPushforwardIntersectionLowerCoverage',
    'UniformPolynomialOuterPairFilteredTau3Q17GoodPacketPushforwardIntersectionLowerCoverage',
    'S_PUSHFORWARD_WEIGHT_COMPARISON_AS_FINAL_TARGET_SUPERSEDED=true',
    'Q21_THEOREM_TARGET_NOW_STABLE=true',
    'NEXT=Stage14-s7-144',
])
must('stages/stage14/14-s-batch/s7-141-143-report.md', [
    'BATCH_START_MAIN_SHA=43ed9a782d57986791644f8b9c1a9aa451445dbf',
    'BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3',
    'BATCH_STOP_REASON=receiver_change',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    'NEXT=Stage14-s7-144',
])

print('STAGE14_S_BATCH_S7_141_143_AUDIT=PASS')
