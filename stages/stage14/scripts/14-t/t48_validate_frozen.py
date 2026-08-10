#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
FULL = ROOT / 'stages/stage14/data/14-t48/physical_row_correlation.json'
FROZEN = ROOT / 'stages/stage14/data/14-t48/physical_row_correlation_summary.json'

full = json.loads(FULL.read_text())
frozen = json.loads(FROZEN.read_text())
w = full['row_l2']['worst']
compact = {
    'stage': full['stage'],
    'physical_character_bridge': {
        'test_primes': full['physical_character_bridge']['test_primes'],
        'all_test_primes_split_mod4': full['physical_character_bridge']['all_test_primes_split_mod4'],
        'canonical_square_normalization_checks': full['physical_character_bridge']['canonical_square_normalization_checks'],
        'product_character_checks': full['physical_character_bridge']['product_character_checks'],
    },
    'fixed_direction_structure': {
        'directions': full['fixed_direction_structure']['directions'],
        'reciprocal_quotient_fixed_direction_squareclass_injective': full['fixed_direction_structure']['reciprocal_quotient_fixed_direction_squareclass_injective'],
    },
    'finite_coherence': {
        k: full['finite_coherence'][k] for k in (
            'largest_abs_global_G', 'largest_abs_global_pair',
            'max_abs_endpoint_canonical_contribution_sum',
            'max_abs_single_direction_cell_on_top_pairs',
            'max_abs_single_common_packet_cell_on_top_pairs', 'top_pair_count')
    },
    'row_l2': {
        'direction_partition_cells': full['row_l2']['direction_partition_cells'],
        'common_packet_partition_cells': full['row_l2']['common_packet_partition_cells'],
        'worst_prime': w['prime'],
        'worst_actual_offdiag_l2': w['actual_offdiag_l2'],
        'worst_direction_local_l2_sum': w['direction_local_l2_sum'],
        'worst_direction_cauchy_upper': w['direction_cauchy_upper'],
        'worst_common_packet_local_l2_sum': w['common_packet_local_l2_sum'],
        'worst_common_packet_cauchy_upper': w['common_packet_cauchy_upper'],
        'top8_prime_actual': [[r['prime'], r['actual_offdiag_l2']] for r in full['row_l2']['top8']],
    },
    'decision': {k: full['decision'][k] for k in frozen['decision']},
}
assert compact == frozen

d = full['decision']
assert d['STAGE14_T48'] == 'COMPLETE_PHYSICAL_ROW_CORRELATION_BRIDGE_AND_DIFFUSE_COHERENCE_AUDIT'
for k in (
    'T47_GRAM_IS_NORMALIZED_PHYSICAL_FOUR_LINEAR_CHARACTER_SUM',
    'ALL_CANONICAL_TEST_PRIMES_SPLIT',
    'T32_TWO_PRIME_ANGULAR_COMPLETION_REUSED',
    'FIXED_DIRECTION_KERNEL_INJECTIVITY_AFTER_RECIPROCAL_QUOTIENT',
    'SIGNED_COMMON_REFINEMENT_AGGREGATION_REQUIRED'):
    assert d[k] is True
assert d['TOP_FROZEN_ROW_CORRELATIONS_SINGLE_CELL_EXCEPTIONAL'] is False
for k in (
    'UNIFORM_PHYSICAL_ROW_CORRELATION_POWER_SAVING_PROVED',
    'GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED',
    'GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED',
    'CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED',
    'A_11_POWER_SAVING_PROVED', 'T_O_SQRT_B_PROVED',
    'PERFECT_CUBOID_NONEXISTENCE_PROVED', 'TH14_NEEDED'):
    assert d[k] is False

print('Stage14-t48 frozen compact ledger and locked boundary: PASS')
