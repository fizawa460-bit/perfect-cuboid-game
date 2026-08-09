#!/usr/bin/env python3
"""Stage14-4am: separate Selmer, MW-rank, and first-small-point thinning.

For primitive oriented Pythagorean bases F=(S,X,H), define at cutoff B:

  A(B)      = all bases with H<=B
  Sigma(B)  = bases with full-2-torsion Selmer dimension > 2
  R(B)      = bases with positive Mordell-Weil rank (not fully computable here)
  V(B)      = bases with first physical Stage14 height mu(F)<=B

Merged Stage14 gives V subset R subset Sigma subset A. Hence exactly

  V/A = (Sigma/A) * (R/Sigma) * (V/R).

PARI ellrank(E,0) gives unconditional MW rank bounds and the exact full-2-torsion
Selmer dimension used by merged s1. We audit every primitive oriented base through
H<=20,000, not a case-control sample. Active but PARI-unresolved fibers are added
to the rigorous lower bound for R because merged Stage14 proves active => rank>0.
"""

from collections import Counter
from math import gcd, log
from pathlib import Path
import json, runpy, shutil, subprocess

ROOT = Path(__file__).resolve().parents[4]
GRAPH = ROOT / 'stages/stage14/scripts/14-4/rank_jump_graph_audit.py'
OUT = ROOT / 'stages/stage14/data/14-4/rank_smallpoint_factor_audit.json'
MAX_H = 20_000
CUTS = (2_000, 5_000, 10_000, 20_000)
EXPECTED_V = {2_000: 7, 5_000: 25, 10_000: 39, 20_000: 54}


def primitive_faces(max_h):
    out = []
    m = 2
    while m*m + 1 <= max_h:
        for n in range(1, m):
            if ((m-n) & 1) == 0 or gcd(m,n) != 1:
                continue
            u = m*m - n*n
            v = 2*m*n
            h = m*m + n*n
            if h > max_h:
                continue
            out.append((u,v,h))
            out.append((v,u,h))
        m += 1
    return sorted(out, key=lambda f:(f[2],f[0],f[1]))


def active_first_hits(max_b):
    mod = runpy.run_path(str(GRAPH))
    keep,_ = mod['enumerate_multi'](max_b)
    object_edges = mod['object_edges']
    first = {}
    for (a,b,c,d),(mask,ds) in keep.items():
        if d > max_b or mask.bit_count() < 2:
            continue
        for f1,f2 in object_edges(a,b,c,mask,ds):
            first[f1] = min(first.get(f1,d), d)
            first[f2] = min(first.get(f2,d), d)
    for f,mu in first.items():
        assert f[2] < mu
    return first


def curve_coeff(face):
    S,X,H = face
    assert gcd(S,X)==1 and S*S+X*X==H*H
    return X*X-S*S, -(S*S)*(X*X)


def gp_rank_selmer(faces):
    gp = shutil.which('gp')
    if gp is None:
        raise SystemExit("PARI/GP executable 'gp' required")
    lines = ['default(parisizemax,8G);']
    for i,f in enumerate(faces):
        a2,a4 = curve_coeff(f)
        lines.append(
            f'E=ellinit([0,{a2},0,{a4},0]);R=ellrank(E,0);'
            f'print("{i}|",R[1],"|",R[2],"|",R[3]);'
        )
    lines.append('quit;')
    p = subprocess.run([gp,'-q'], input='\n'.join(lines)+'\n', text=True,
                       capture_output=True, check=True)
    got = {}
    for line in p.stdout.splitlines():
        if '|' not in line:
            continue
        z = line.strip().split('|')
        if len(z) != 4:
            continue
        i = int(z[0]); lo=int(z[1]); hi=int(z[2]); s=int(z[3])
        got[i] = {'rank_lower':lo,'rank_upper':hi,'sha_2_mod_4_rank_s':s,
                  'selmer_2_rank':hi+2+s}
    assert len(got)==len(faces), (len(got),len(faces),p.stderr[-2000:])
    return got


def neglog_density(x, B):
    assert 0 < x <= 1
    return -log(x)/log(B)


def summarize_cut(B, faces, audit, active):
    ids = [i for i,f in enumerate(faces) if f[2] <= B]
    A = len(ids)
    Sigma = sum(audit[i]['selmer_2_rank'] > 2 for i in ids)
    cert_pos = sum(audit[i]['rank_lower'] > 0 for i in ids)
    cert_zero = sum(audit[i]['rank_upper'] == 0 for i in ids)
    possible_pos = A - cert_zero
    active_faces = {f for f,mu in active.items() if mu <= B}
    V = len(active_faces)
    assert V == EXPECTED_V[B], (B,V)
    face_to_id = {f:i for i,f in enumerate(faces)}
    assert all(f in face_to_id and f[2] <= B for f in active_faces)
    assert all(audit[face_to_id[f]]['rank_upper'] > 0 for f in active_faces)
    assert all(audit[face_to_id[f]]['selmer_2_rank'] > 2 for f in active_faces)

    active_unresolved = sum(audit[face_to_id[f]]['rank_lower'] == 0 for f in active_faces)
    # Certified-positive fibers plus active unresolved fibers are disjoint known rank-positive sets.
    R_lo = cert_pos + active_unresolved
    R_hi = possible_pos
    assert V <= R_lo <= R_hi <= Sigma <= A

    rank_hist = Counter()
    sel_hist = Counter()
    for i in ids:
        a=audit[i]
        key = str(a['rank_lower']) if a['rank_lower']==a['rank_upper'] else f"{a['rank_lower']}..{a['rank_upper']}"
        rank_hist[key]+=1
        sel_hist[str(a['selmer_2_rank'])]+=1

    # Exact activation thinning exponent; decomposition intervals are rigorous but correlated.
    gamma = neglog_density(V/A, B)
    alpha_sel = neglog_density(Sigma/A, B)
    alpha_mw_lo = neglog_density(R_hi/Sigma, B)
    alpha_mw_hi = neglog_density(R_lo/Sigma, B)
    alpha_hit_lo = neglog_density(V/R_lo, B)
    alpha_hit_hi = neglog_density(V/R_hi, B)

    return {
        'B':B,
        'eligible_A':A,
        'selmer_candidate_Sigma':Sigma,
        'mw_rank_positive_lower':R_lo,
        'mw_rank_positive_upper':R_hi,
        'active_V':V,
        'certified_positive_rank':cert_pos,
        'certified_rank_zero':cert_zero,
        'active_pari_unresolved_but_geometrically_positive':active_unresolved,
        'rank_bound_histogram':dict(sorted(rank_hist.items())),
        'selmer_2_rank_histogram':dict(sorted(sel_hist.items(), key=lambda kv:int(kv[0]))),
        'densities':{
            'Sigma_over_A':Sigma/A,
            'R_over_A_interval':[R_lo/A,R_hi/A],
            'V_over_R_interval':[V/R_hi,V/R_lo],
            'V_over_A':V/A,
        },
        'thinning_exponents_base_B':{
            'total_gamma_exact':gamma,
            'selmer_alpha_exact':alpha_sel,
            'mw_given_selmer_alpha_interval':[alpha_mw_lo,alpha_mw_hi],
            'smallpoint_given_mw_beta_interval':[alpha_hit_lo,alpha_hit_hi],
            'identity':'gamma = alpha_sel + alpha_MW|Selmer + beta_hit|MW for the true R(B)',
        },
    }


def main():
    faces = primitive_faces(MAX_H)
    active = active_first_hits(MAX_H)
    audit = gp_rank_selmer(faces)
    profile = [summarize_cut(B,faces,audit,active) for B in CUTS]
    last=profile[-1]
    report={
        'metadata':{
            'stage':'14-4am',
            'max_full_rank_census_H':MAX_H,
            'eligible_oriented_bases_at_max':len(faces),
            'cuts':list(CUTS),
            'pari_effort':0,
            'census_type':'complete primitive oriented Pythagorean base census through H<=20000; not a matched sample',
        },
        'exact_factorization':{
            'sets':'V(B) subset R(B) subset Sigma(B) subset A(B)',
            'A':'primitive oriented Pythagorean bases F with H<=B',
            'Sigma':'bases with dim Sel_2(E_F)>dim E_F[2](Q)=2',
            'R':'bases with rank E_F(Q)>0',
            'V':'bases with first physical height mu(F)<=B',
            'density_identity':'V/A = (Sigma/A)*(R/Sigma)*(V/R)',
            'sqrt_budget':'If V=B^(1/2+o(1)) and A=B^(1+o(1)), the three thinning exponents sum to 1/2.',
        },
        'euclid_descent_handoff':{
            'S':'m^2-n^2','X':'2mn','H':'m^2+n^2',
            'moving_support':['m','n','m-n','m+n','m^2+n^2'],
            'meaning':('s5a local-character/large-sieve work targets the A->Sigma and possibly Sigma->R gates; '
                       'a separate height-sensitive argument is still required for the R->V first-small-point gate unless it is built into the same family theorem.'),
        },
        'profile':profile,
        'finite_max_cut_summary':{
            'B':MAX_H,
            'A':last['eligible_A'],'Sigma':last['selmer_candidate_Sigma'],
            'R_interval':[last['mw_rank_positive_lower'],last['mw_rank_positive_upper']],
            'V':last['active_V'],
            'Sigma_over_A':last['densities']['Sigma_over_A'],
            'R_over_A_interval':last['densities']['R_over_A_interval'],
            'V_over_R_interval':last['densities']['V_over_R_interval'],
            'V_over_A':last['densities']['V_over_A'],
        },
        'decision':{
            'STAGE14_4AM':'COMPLETE_EXACT_SELMER_RANK_SMALLPOINT_FACTOR_AND_FINITE_FULL_BASE_CENSUS',
            'ACTIVATION_DENSITY_THREE_GATE_FACTORIZATION_LOCKED':True,
            'FULL_BASE_RANK_SELMER_CENSUS_MAX_H':MAX_H,
            'MATCHED_CASE_CONTROL_ONLY':False,
            'POSITIVE_RANK_DENSITY_PROVED':False,
            'UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED':False,
            'FAMILY_LARGE_SIEVE_THEOREM_PROVED':False,
            'ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED':False,
            'NEXT':'Stage14-4an derive the explicit Euclid-factor local character/reciprocity matrix and identify which thinning gate it can rigorously bound',
        },
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report['finite_max_cut_summary'],indent=2))
    print(json.dumps(report['profile'],indent=2))
    print(json.dumps(report['decision'],indent=2))

if __name__=='__main__':
    main()
