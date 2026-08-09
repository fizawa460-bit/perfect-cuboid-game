#!/usr/bin/env python3
import json
import math
import random
from pathlib import Path

TRIALS = 50000
SEED_PATH = 14110011
SEED_ENDPOINT = 14110012

ROOT = Path(__file__).resolve().parents[4]
SRC = ROOT / "stages/stage14/data/14-num-alpha11-diag8/extended_denominator_summary.json"
source = json.loads(SRC.read_text())
rows = source["rows"]
checkpoints = [r["B"] for r in rows]
plugin_survival = list(rows[-1]["survival_rel_bc"])
hyp_target = list(source["required_relative_survival_if_stage13_limit_plus_hypothetical_221"])


def vec_sub(a, b):
    return [a[i] - b[i] for i in range(len(a))]


def pair_to_endpoint(pair):
    a, b, c = pair
    return [a + b, a + c, b + c]


def relative_survival(raw, pair):
    endpoint = pair_to_endpoint(pair)
    rates = [endpoint[i] / raw[i] for i in range(3)]
    return [rates[i] / rates[2] for i in range(3)]


def shape(v):
    s = sum(v)
    return [x / s for x in v]


def l1(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def pair_probs_from_raw(raw, survival):
    e = [raw[i] * survival[i] for i in range(3)]
    a = (e[0] + e[1] - e[2]) / 2.0
    b = (e[0] + e[2] - e[1]) / 2.0
    c = (e[1] + e[2] - e[0]) / 2.0
    if min(a, b, c) <= 0:
        raise RuntimeError("plugin endpoint vector does not induce positive pair probabilities")
    total = a + b + c
    return [a / total, b / total, c / total]


def multinomial3(rng, n, p):
    out = [0, 0, 0]
    cut0 = p[0]
    cut1 = p[0] + p[1]
    for _ in range(n):
        u = rng.random()
        if u < cut0:
            out[0] += 1
        elif u < cut1:
            out[1] += 1
        else:
            out[2] += 1
    return out


def quantile(xs, q):
    ys = sorted(xs)
    if not ys:
        raise RuntimeError("empty quantile input")
    pos = (len(ys) - 1) * q
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return ys[lo]
    w = pos - lo
    return ys[lo] * (1.0 - w) + ys[hi] * w


def ci95(xs):
    return [quantile(xs, 0.025), quantile(xs, 0.5), quantile(xs, 0.975)]


cum_raw = [list(map(int, r["raw"])) for r in rows]
cum_pair = [list(map(int, r["pair"])) for r in rows]
obs_rel = [relative_survival(raw, pair) for raw, pair in zip(cum_raw, cum_pair)]

shell_raw = [cum_raw[0]]
shell_pair = [cum_pair[0]]
for i in range(1, len(rows)):
    shell_raw.append(vec_sub(cum_raw[i], cum_raw[i - 1]))
    shell_pair.append(vec_sub(cum_pair[i], cum_pair[i - 1]))
shell_N2 = [sum(x) for x in shell_pair]
shell_probs = [pair_probs_from_raw(raw, plugin_survival) for raw in shell_raw]

expected_shell_pair = [[shell_N2[i] * shell_probs[i][j] for j in range(3)] for i in range(len(rows))]
expected_cum_pair = []
running = [0.0, 0.0, 0.0]
for v in expected_shell_pair:
    running = [running[j] + v[j] for j in range(3)]
    expected_cum_pair.append(list(running))
expected_rel = [relative_survival(cum_raw[i], expected_cum_pair[i]) for i in range(len(rows))]

rng = random.Random(SEED_PATH)
path_samples_ab = [[] for _ in rows]
path_samples_ac = [[] for _ in rows]
max_shape_l1_exceed = 0
range_ab_exceed = 0
range_ac_exceed = 0
obs_shape_dev = [l1(shape(obs_rel[i]), shape(expected_rel[i])) for i in range(len(rows))]
obs_max_shape_l1 = max(obs_shape_dev)
obs_range_ab = max(x[0] for x in obs_rel) - min(x[0] for x in obs_rel)
obs_range_ac = max(x[1] for x in obs_rel) - min(x[1] for x in obs_rel)

for _ in range(TRIALS):
    running_pair = [0, 0, 0]
    trial_rel = []
    trial_dev = []
    for i in range(len(rows)):
        d = multinomial3(rng, shell_N2[i], shell_probs[i])
        running_pair = [running_pair[j] + d[j] for j in range(3)]
        rel = relative_survival(cum_raw[i], running_pair)
        trial_rel.append(rel)
        path_samples_ab[i].append(rel[0])
        path_samples_ac[i].append(rel[1])
        trial_dev.append(l1(shape(rel), shape(expected_rel[i])))
    if max(trial_dev) >= obs_max_shape_l1:
        max_shape_l1_exceed += 1
    rab = [x[0] for x in trial_rel]
    rac = [x[1] for x in trial_rel]
    if max(rab) - min(rab) >= obs_range_ab:
        range_ab_exceed += 1
    if max(rac) - min(rac) >= obs_range_ac:
        range_ac_exceed += 1

pointwise_bands = []
for i, B in enumerate(checkpoints):
    pointwise_bands.append({
        "B": B,
        "observed_rel_bc": obs_rel[i],
        "expected_rel_bc": expected_rel[i],
        "ab_95_band": [quantile(path_samples_ab[i], 0.025), quantile(path_samples_ab[i], 0.975)],
        "ac_95_band": [quantile(path_samples_ac[i], 0.025), quantile(path_samples_ac[i], 0.975)],
    })

path_p = {
    "max_shape_L1": (max_shape_l1_exceed + 1) / (TRIALS + 1),
    "ab_range": (range_ab_exceed + 1) / (TRIALS + 1),
    "ac_range": (range_ac_exceed + 1) / (TRIALS + 1),
}

# B=1m endpoint uncertainty under the fitted cumulative pair-direction law.
rng2 = random.Random(SEED_ENDPOINT)
last_raw = cum_raw[-1]
last_pair = cum_pair[-1]
last_N2 = sum(last_pair)
last_p = [x / last_N2 for x in last_pair]
rel_ab = []
rel_ac = []
rr_ab_ac = []
rr_ab_bc = []
rr_ac_bc = []
for _ in range(TRIALS):
    d = multinomial3(rng2, last_N2, last_p)
    endpoint = pair_to_endpoint(d)
    rates = [endpoint[i] / last_raw[i] for i in range(3)]
    if min(rates) <= 0:
        continue
    rel = [rates[i] / rates[2] for i in range(3)]
    rel_ab.append(rel[0])
    rel_ac.append(rel[1])
    rr_ab_ac.append(rates[0] / rates[1])
    rr_ab_bc.append(rates[0] / rates[2])
    rr_ac_bc.append(rates[1] / rates[2])

endpoint_ci = {
    "rel_ab_to_bc": ci95(rel_ab),
    "rel_ac_to_bc": ci95(rel_ac),
    "rate_ratio_ab_ac": ci95(rr_ab_ac),
    "rate_ratio_ab_bc": ci95(rr_ab_bc),
    "rate_ratio_ac_bc": ci95(rr_ac_bc),
    "prob_ab_lt_ac": sum(x < 1 for x in rr_ab_ac) / len(rr_ab_ac),
    "prob_ab_lt_bc": sum(x < 1 for x in rr_ab_bc) / len(rr_ab_bc),
    "prob_ac_lt_bc": sum(x < 1 for x in rr_ac_bc) / len(rr_ac_bc),
}

last_band = pointwise_bands[-1]
hyp_target_inside_B1m_pointwise = (
    last_band["ab_95_band"][0] <= hyp_target[0] <= last_band["ab_95_band"][1]
    and last_band["ac_95_band"][0] <= hyp_target[1] <= last_band["ac_95_band"][1]
)

ab_separated_from_ac = endpoint_ci["rate_ratio_ab_ac"][2] < 1.0
ab_separated_from_bc = endpoint_ci["rate_ratio_ab_bc"][2] < 1.0
ac_bc_unresolved = endpoint_ci["rate_ratio_ac_bc"][0] <= 1.0 <= endpoint_ci["rate_ratio_ac_bc"][2]
no_detected_cumulative_drift = min(path_p.values()) > 0.05
park = ab_separated_from_ac and ab_separated_from_bc and ac_bc_unresolved and no_detected_cumulative_drift

out = {
    "stage": "14-num-alpha11-diag11",
    "classification": "CUMULATIVE_SECOND_FACE_SURVIVAL_UNCERTAINTY_AND_STOPPING_DECISION",
    "source": str(SRC.relative_to(ROOT)),
    "trials": TRIALS,
    "seeds": {"trajectory": SEED_PATH, "endpoint": SEED_ENDPOINT},
    "plugin_survival_rel_bc": plugin_survival,
    "hypothetical_bridge_target_rel_bc": hyp_target,
    "shell_N2": shell_N2,
    "shell_pair_probabilities_under_common_survival_plugin": shell_probs,
    "pointwise_cumulative_bands": pointwise_bands,
    "trajectory_diagnostics": {
        "observed_max_shape_L1": obs_max_shape_l1,
        "observed_ab_range": obs_range_ab,
        "observed_ac_range": obs_range_ac,
        "mc_p": path_p,
    },
    "B1m_fitted_endpoint_uncertainty": endpoint_ci,
    "decision": {
        "AB_RATE_LOWER_THAN_AC_AT_B1M_95_CALIBRATION": ab_separated_from_ac,
        "AB_RATE_LOWER_THAN_BC_AT_B1M_95_CALIBRATION": ab_separated_from_bc,
        "AC_VS_BC_RESOLVED_AT_B1M_95_CALIBRATION": not ac_bc_unresolved,
        "CUMULATIVE_DRIFT_EXCEEDS_COMMON_SURVIVAL_NOISE_AT_5PCT": not no_detected_cumulative_drift,
        "HYPOTHETICAL_STAGE13_LIMIT_PLUS_221_TARGET_INSIDE_B1M_POINTWISE_95_BANDS": hyp_target_inside_B1m_pointwise,
        "ASYMPTOTIC_SECOND_FACE_SURVIVAL_PROFILE_CLAIM": False,
        "ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM": False,
        "NUM_ALPHA_DIAGNOSTIC_BRANCH_PARK_RECOMMENDED": park,
        "REOPEN_TRIGGER": "substantially larger matched raw-face denominator census or a proof-side chamber/local-density prediction that can be tested without post-selection",
        "NEXT": "PAUSE_NUM_ALPHA_DIAG_BRANCH_AND_HAND_OFF_TO_STAGE14_BRIDGE_OR_PROOF_TRACKS" if park else "Stage14-num-alpha11-diag12 targeted follow-up",
    },
    "interpretation": "Multinomial/plug-in finite-sample calibration only; arithmetic objects are not asserted IID. Confidence bands are diagnostic, not asymptotic theorems.",
}
print(json.dumps(out, indent=2, sort_keys=True))
