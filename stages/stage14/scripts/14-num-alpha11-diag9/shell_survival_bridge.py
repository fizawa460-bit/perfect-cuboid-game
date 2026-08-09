#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SRC = ROOT / 'stages/stage14/data/14-num-alpha11-diag8/extended_denominator_summary.json'

STAGE13_LIMIT = [0.5347369332313988, 0.24535917783225203, 0.21990388893634913]
TARGET_SURVIVAL_REL = [0.5483166899967721, 0.8962529581293825, 1.0]
TARGET_ENDPOINT_433 = [0.4, 0.3, 0.3]


def normalize(v):
    s = sum(v)
    if s <= 0:
        raise ArithmeticError('cannot normalize non-positive vector')
    return [x / s for x in v]


def bridge(source_prop, survival):
    return normalize([source_prop[i] * survival[i] for i in range(3)])


def l1(a, b):
    return sum(abs(a[i] - b[i]) for i in range(3))


def l2(v):
    return math.sqrt(sum(x*x for x in v))


def sub(a, b):
    return [a[i] - b[i] for i in range(3)]


def add(a, b):
    return [a[i] + b[i] for i in range(3)]


def scale(c, v):
    return [c*x for x in v]


def endpoint_to_pair(endpoint_prop):
    e0, e1, e2 = endpoint_prop
    return [e0 + e1 - e2, e0 + e2 - e1, e1 + e2 - e0]


def rms_spread(vectors, weights=None):
    if weights is None:
        weights = [1.0] * len(vectors)
    sw = sum(weights)
    mean = [sum(weights[j] * vectors[j][i] for j in range(len(vectors))) / sw for i in range(3)]
    return math.sqrt(sum(weights[j] * sum((vectors[j][i] - mean[i])**2 for i in range(3)) for j in range(len(vectors))) / sw)


def close_vec(a, b, tol=1e-12):
    return all(abs(a[i] - b[i]) <= tol for i in range(3))


def main():
    src = json.loads(SRC.read_text())
    cumulative = src['rows']

    target_endpoint = bridge(STAGE13_LIMIT, TARGET_SURVIVAL_REL)
    if not close_vec(target_endpoint, TARGET_ENDPOINT_433):
        raise ArithmeticError(f'target bridge failed: {target_endpoint}')

    prev_raw = [0, 0, 0]
    prev_pair = [0, 0, 0]
    prev_endpoint = [0, 0, 0]
    lo = 0
    shells = []
    actual_series = []
    source_only_series = []
    survival_only_series = []
    weights = []

    for row in cumulative:
        hi = row['B']
        raw = [row['raw'][i] - prev_raw[i] for i in range(3)]
        pair = [row['pair'][i] - prev_pair[i] for i in range(3)]
        endpoint = [row['endpoint'][i] - prev_endpoint[i] for i in range(3)]
        n2 = sum(pair)

        if sum(endpoint) != 2*n2:
            raise ArithmeticError(f'endpoint total != 2N2 in shell {(lo,hi)}')
        if min(raw) <= 0 or min(endpoint) < 0 or min(pair) < 0:
            raise ArithmeticError(f'non-positive shell difference {(lo,hi)}')

        raw_prop = normalize(raw)
        pair_prop = normalize(pair)
        endpoint_prop = normalize(endpoint)
        survival = [endpoint[i] / raw[i] for i in range(3)]
        survival_rel = [x / survival[2] for x in survival]

        actual = bridge(raw_prop, survival)
        if not close_vec(actual, endpoint_prop):
            raise ArithmeticError(f'bridge identity failed {(lo,hi)}')
        if not close_vec(endpoint_to_pair(endpoint_prop), pair_prop):
            raise ArithmeticError(f'endpoint/pair inverse failed {(lo,hi)}')

        source_only = bridge(raw_prop, TARGET_SURVIVAL_REL)
        survival_only = bridge(STAGE13_LIMIT, survival)

        # Two-factor Shapley decomposition of the endpoint residual from 4:3:3.
        # This is vector-additive even though L1 norms need not add because the
        # source and survival effects can partially cancel.
        source_shapley = scale(0.5, add(sub(source_only, target_endpoint), sub(actual, survival_only)))
        survival_shapley = scale(0.5, add(sub(survival_only, target_endpoint), sub(actual, source_only)))
        if not close_vec(add(source_shapley, survival_shapley), sub(actual, target_endpoint)):
            raise ArithmeticError(f'Shapley decomposition failed {(lo,hi)}')

        shells.append({
            'lo': lo,
            'hi': hi,
            'N2': n2,
            'raw': raw,
            'raw_proportion': raw_prop,
            'pair_a_b_c': pair,
            'pair_proportion': pair_prop,
            'endpoint_ab_ac_bc': endpoint,
            'endpoint_proportion': endpoint_prop,
            'survival_relative_to_bc': survival_rel,
            'endpoint_L1_to_4_3_3': l1(endpoint_prop, target_endpoint),
            'source_only_counterfactual_endpoint': source_only,
            'source_only_L1_to_4_3_3': l1(source_only, target_endpoint),
            'survival_only_counterfactual_endpoint': survival_only,
            'survival_only_L1_to_4_3_3': l1(survival_only, target_endpoint),
            'source_shapley_vector': source_shapley,
            'survival_shapley_vector': survival_shapley,
            'source_shapley_L2': l2(source_shapley),
            'survival_shapley_L2': l2(survival_shapley),
        })
        actual_series.append(actual)
        source_only_series.append(source_only)
        survival_only_series.append(survival_only)
        weights.append(n2)

        prev_raw = row['raw']
        prev_pair = row['pair']
        prev_endpoint = row['endpoint']
        lo = hi

    unweighted = {
        'actual_endpoint_shell_RMS': rms_spread(actual_series),
        'source_only_counterfactual_shell_RMS': rms_spread(source_only_series),
        'survival_only_counterfactual_shell_RMS': rms_spread(survival_only_series),
    }
    unweighted['survival_to_source_RMS_ratio'] = (
        unweighted['survival_only_counterfactual_shell_RMS'] /
        unweighted['source_only_counterfactual_shell_RMS']
    )
    weighted = {
        'actual_endpoint_shell_RMS': rms_spread(actual_series, weights),
        'source_only_counterfactual_shell_RMS': rms_spread(source_only_series, weights),
        'survival_only_counterfactual_shell_RMS': rms_spread(survival_only_series, weights),
    }
    weighted['survival_to_source_RMS_ratio'] = (
        weighted['survival_only_counterfactual_shell_RMS'] /
        weighted['source_only_counterfactual_shell_RMS']
    )

    raw_axis_ranges = []
    for i in range(3):
        vals = [s['raw_proportion'][i] for s in shells]
        raw_axis_ranges.append({'min': min(vals), 'max': max(vals), 'range': max(vals)-min(vals)})

    report = {
        'stage': '14-num-alpha11-diag9',
        'classification': 'SHELL_SECOND_FACE_SURVIVAL_DRIFT_AND_BRIDGE_RESIDUAL_DECOMPOSITION',
        'source': str(SRC.relative_to(ROOT)),
        'target': {
            'Stage13_direction_limit_ab_ac_bc': STAGE13_LIMIT,
            'hypothetical_pair_2_2_1_required_survival_rel_bc': TARGET_SURVIVAL_REL,
            'equivalent_endpoint_4_3_3': target_endpoint,
        },
        'shells': shells,
        'raw_source_proportion_axis_ranges': raw_axis_ranges,
        'shell_volatility_unweighted': unweighted,
        'shell_volatility_N2_weighted': weighted,
        'decision': {
            'SHELL_DECOMPOSITION_COMPLETE': True,
            'RAW_SOURCE_SHELL_PROPORTION_STABLE_AT_PERCENT_SCALE': max(x['range'] for x in raw_axis_ranges) < 0.01,
            'SURVIVAL_SIDE_COUNTERFACTUAL_VOLATILITY_DOMINATES_SOURCE_SIDE': unweighted['survival_to_source_RMS_ratio'] > 10,
            'N2_WEIGHTED_SURVIVAL_SIDE_VOLATILITY_DOMINATES_SOURCE_SIDE': weighted['survival_to_source_RMS_ratio'] > 10,
            'SHELL_N2_SMALL_ENOUGH_THAT_SAMPLING_NOISE_REMAINS_A_MAJOR_ALTERNATIVE': min(weights) < 30,
            'ASYMPTOTIC_SECOND_FACE_SURVIVAL_PROFILE_CLAIM': False,
            'ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM': False,
            'NEXT': 'Stage14-num-alpha11-diag10 quantify whether shell survival heterogeneity exceeds finite-count sampling noise using the diag9 conditional panel',
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
