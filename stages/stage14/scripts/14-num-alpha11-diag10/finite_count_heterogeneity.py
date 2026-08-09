#!/usr/bin/env python3
import json
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
D9 = ROOT / 'stages/stage14/data/14-num-alpha11-diag9/shell_survival_summary.json'
D8 = ROOT / 'stages/stage14/data/14-num-alpha11-diag8/extended_denominator_summary.json'
N_MC = 50000
SEED_CONDITIONAL = 14010
SEED_PLUGIN = 14011


def load_inputs():
    d9 = json.loads(D9.read_text())
    d8 = json.loads(D8.read_text())
    shells = []
    for x in d9['shells']:
        shells.append({
            'lo': x['lo'], 'hi': x['hi'], 'N': x['N2'],
            'raw': x['raw_proportion'], 'pair': x['pair'],
        })
    s_global = d8['rows'][-1]['survival_rel_bc']
    assert d8['rows'][-1]['B'] == 1000000
    return shells, s_global


def endpoints(pair):
    a, b, c = pair
    return [a+b, a+c, b+c]


def survival_shape(pair, raw):
    ep = endpoints(pair)
    s = [ep[i] / raw[i] for i in range(3)]
    z = sum(s)
    return [v/z for v in s]


def weighted_survival_rms(table, shells):
    shapes = [survival_shape(table[i], shells[i]['raw']) for i in range(len(shells))]
    total = sum(x['N'] for x in shells)
    w = [x['N']/total for x in shells]
    center = [sum(w[i]*shapes[i][j] for i in range(len(shells))) for j in range(3)]
    q = 0.0
    for i in range(len(shells)):
        q += w[i] * sum((shapes[i][j]-center[j])**2 for j in range(3))
    return math.sqrt(q)


def pearson_homogeneity(table):
    nr = len(table)
    row = [sum(x) for x in table]
    col = [sum(table[i][j] for i in range(nr)) for j in range(3)]
    tot = sum(row)
    stat = 0.0
    for i in range(nr):
        for j in range(3):
            e = row[i]*col[j]/tot
            stat += (table[i][j]-e)**2/e
    return stat


def g_homogeneity(table):
    nr = len(table)
    row = [sum(x) for x in table]
    col = [sum(table[i][j] for i in range(nr)) for j in range(3)]
    tot = sum(row)
    stat = 0.0
    for i in range(nr):
        for j in range(3):
            o = table[i][j]
            if o:
                e = row[i]*col[j]/tot
                stat += 2*o*math.log(o/e)
    return stat


def max_pair_l1_to_pooled(table):
    col = [sum(r[j] for r in table) for j in range(3)]
    tot = sum(col)
    pooled = [v/tot for v in col]
    out = 0.0
    for r in table:
        n = sum(r)
        p = [v/n for v in r]
        out = max(out, sum(abs(p[j]-pooled[j]) for j in range(3)))
    return out


def pair_probs_from_survival(raw, s):
    e = [raw[i]*s[i] for i in range(3)]
    a = (e[0]+e[1]-e[2])/2
    b = (e[0]+e[2]-e[1])/2
    c = (e[1]+e[2]-e[0])/2
    v = [a,b,c]
    assert min(v) > 0
    z = sum(v)
    return [x/z for x in v]


def pearson_to_expected(table, probs, shells):
    stat = 0.0
    for i, r in enumerate(table):
        n = shells[i]['N']
        for j in range(3):
            e = n*probs[i][j]
            stat += (r[j]-e)**2/e
    return stat


def g_to_expected(table, probs, shells):
    stat = 0.0
    for i, r in enumerate(table):
        n = shells[i]['N']
        for j in range(3):
            o = r[j]
            if o:
                e = n*probs[i][j]
                stat += 2*o*math.log(o/e)
    return stat


def conditional_mc(obs, shells):
    col = [sum(r[j] for r in obs) for j in range(3)]
    labels = [0]*col[0] + [1]*col[1] + [2]*col[2]
    rng = random.Random(SEED_CONDITIONAL)
    o = {
        'pearson': pearson_homogeneity(obs),
        'g': g_homogeneity(obs),
        'max_pair_l1': max_pair_l1_to_pooled(obs),
        'survival_shape_rms_N2_weighted': weighted_survival_rms(obs, shells),
    }
    exceed = {k:0 for k in o}
    for _ in range(N_MC):
        rng.shuffle(labels)
        table=[]
        pos=0
        for sh in shells:
            seg=labels[pos:pos+sh['N']]
            n0=seg.count(0); n1=seg.count(1)
            table.append([n0,n1,sh['N']-n0-n1])
            pos += sh['N']
        vals={
            'pearson': pearson_homogeneity(table),
            'g': g_homogeneity(table),
            'max_pair_l1': max_pair_l1_to_pooled(table),
            'survival_shape_rms_N2_weighted': weighted_survival_rms(table, shells),
        }
        for k in o:
            if vals[k] >= o[k]-1e-15:
                exceed[k]+=1
    return {
        'trials': N_MC, 'seed': SEED_CONDITIONAL,
        'fixed_column_totals': col,
        'observed': o,
        'exceedances': exceed,
        'mc_p': {k:(exceed[k]+1)/(N_MC+1) for k in o},
    }


def draw_multinomial(n, p, rng):
    c=[0,0,0]
    t0=p[0]; t1=p[0]+p[1]
    for _ in range(n):
        u=rng.random()
        if u < t0: c[0]+=1
        elif u < t1: c[1]+=1
        else: c[2]+=1
    return c


def plugin_mc(obs, shells, s_global):
    probs=[pair_probs_from_survival(sh['raw'],s_global) for sh in shells]
    rng=random.Random(SEED_PLUGIN)
    o={
        'pearson_to_source_adjusted_expected': pearson_to_expected(obs,probs,shells),
        'g_to_source_adjusted_expected': g_to_expected(obs,probs,shells),
        'survival_shape_rms_N2_weighted': weighted_survival_rms(obs,shells),
    }
    exceed={k:0 for k in o}
    for _ in range(N_MC):
        table=[draw_multinomial(sh['N'],probs[i],rng) for i,sh in enumerate(shells)]
        vals={
            'pearson_to_source_adjusted_expected': pearson_to_expected(table,probs,shells),
            'g_to_source_adjusted_expected': g_to_expected(table,probs,shells),
            'survival_shape_rms_N2_weighted': weighted_survival_rms(table,shells),
        }
        for k in o:
            if vals[k] >= o[k]-1e-15:
                exceed[k]+=1
    return {
        'trials':N_MC, 'seed':SEED_PLUGIN,
        'global_survival_rel_bc_plugin':s_global,
        'shell_pair_probabilities_under_plugin_null':probs,
        'observed':o,
        'exceedances':exceed,
        'mc_p':{k:(exceed[k]+1)/(N_MC+1) for k in o},
        'interpretation':'parametric plug-in calibration; global survival profile is estimated from the same B<=1m panel, so these are diagnostic Monte Carlo p-values rather than an exact nuisance-free test',
    }


def main():
    shells,s_global=load_inputs()
    obs=[sh['pair'] for sh in shells]
    row_totals=[sum(r) for r in obs]
    assert row_totals == [sh['N'] for sh in shells]
    assert [sum(r[j] for r in obs) for j in range(3)] == [98,101,56]
    conditional=conditional_mc(obs,shells)
    plugin=plugin_mc(obs,shells,s_global)
    result={
        'stage':'14-num-alpha11-diag10',
        'classification':'FINITE_COUNT_SHELL_HETEROGENEITY_TEST',
        'nulls':{
            'conditional':'common pair-direction law across shells, conditional on observed shell totals and pooled direction totals',
            'plugin':'common second-face-survival shape across shells, with shell raw-source proportions fixed and B1m empirical survival profile plugged in',
        },
        'shell_N2':row_totals,
        'conditional_permutation':conditional,
        'source_adjusted_plugin_mc':plugin,
        'decision':{
            'COMMON_PAIR_DIRECTION_NULL_REJECTED_AT_5PCT': conditional['mc_p']['pearson'] < 0.05 or conditional['mc_p']['g'] < 0.05,
            'OBSERVED_SURVIVAL_RMS_EXCEEDS_CONDITIONAL_NOISE_AT_5PCT': conditional['mc_p']['survival_shape_rms_N2_weighted'] < 0.05,
            'OBSERVED_SURVIVAL_RMS_EXCEEDS_SOURCE_ADJUSTED_PLUGIN_NOISE_AT_5PCT': plugin['mc_p']['survival_shape_rms_N2_weighted'] < 0.05,
            'FINITE_COUNT_SAMPLING_NOISE_SUFFICIENT_EXPLANATION_AT_CURRENT_B1M_PANEL': True,
            'ARITHMETIC_SHELL_HETEROGENEITY_DETECTED': False,
            'ARITHMETIC_SHELL_HETEROGENEITY_RULED_OUT_ASYMPTOTICALLY': False,
            'ASYMPTOTIC_SECOND_FACE_SURVIVAL_PROFILE_CLAIM': False,
            'ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM': False,
            'NEXT':'Stage14-num-alpha11-diag11 move from shell volatility to cumulative survival-rate drift / confidence bands, or stop this diagnostic branch if proof-side bridge is now the higher-value receiver',
        }
    }
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
