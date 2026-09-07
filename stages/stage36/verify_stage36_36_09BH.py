#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BH/bad-place-full-cover-valuation-preflight.json'
BG=ROOT/'stages/stage36/36-09BG/full-character-ay-pullback-collapse-preflight.json'
BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
BC=ROOT/'stages/stage36/36-09BC/boundary-neighborhood-open-local-no-loop-preflight.json'
AD=ROOT/'stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
BA=ROOT/'stages/stage36/36-09BA/ay-auxiliary-genusone-open-points-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='e758e05953df2cf8cd4ab26ac1e9d72374e99760'
AUDIT_HEAD='731265665feb2bed991cf912b89431bb35ce65ad'
CERT_BLOB='76487371ed363868af18a9fa0f6f7e1367d28f27'
LOCKS={
    BG:'a47f1354f74f2ed5412fe5d58daeb657d47fef66',
    BB:'e4b63fd500d05ff5dc704e0c08409edee5895053',
    BC:'317638c4d1a76f683c7af9bdb4e8285af35f4d05',
    AD:'9d0388845955efee71d1a761ae4ee943d8b565d5',
    AE:'ddae37dd35cd0e732cebadf9c17f3f3fa57930df',
    BA:'2f31c89b2760f2270fa0ea21106ef97a3ec0840b',
}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))

def norm(p): return {m:c for m,c in p.items() if c}
def add(x,y):
    z=dict(x)
    for m,c in y.items(): z[m]=z.get(m,0)+c
    return norm(z)
def neg(x): return {m:-c for m,c in x.items()}
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    z={}
    for m,c in x.items():
        for n,d in y.items():
            k=tuple(i+j for i,j in zip(m,n)); z[k]=z.get(k,0)+c*d
    return norm(z)
def scale(c,x): return norm({m:c*v for m,v in x.items()})
def pw(x,n):
    z={(0,0,0,0):1}
    for _ in range(n): z=mul(z,x)
    return z

def V(i):
    e=[0,0,0,0]; e[i]=1
    return {tuple(e):1}

a,b,u,v=V(0),V(1),V(2),V(3)

def main():
    assert blob(CERT)==CERT_BLOB,(blob(CERT),CERT_BLOB)
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text())
    bg=json.loads(BG.read_text()); bb=json.loads(BB.read_text()); bc=json.loads(BC.read_text())
    ad=json.loads(AD.read_text()); ae=json.loads(AE.read_text()); ba=json.loads(BA.read_text())
    assert c['base_main_sha']==BASE
    ap=c['audited_parent']
    assert ap=={'pr':1689,'hostile_audit_review':5129489415,'audited_exact_head':AUDIT_HEAD,'exact_head_ci':'34098010028/101665838247','merged_main_sha':BASE}
    assert bg['cycle_result']['selected_next']=='36-09BH_BAD_PLACE_FULL_COVER_VALUATION_PREFLIGHT'
    assert bb['notation']['P']=='a^2+2ab-b^2' and bb['notation']['M']=='a^2-2ab-b^2'
    assert bc['good_prime_local_analysis']['remaining_local_places']=='finite parameter-dependent bad places dividing 2*R0*S0*kappa*lambda'
    assert ad['odd_reservoir_disjointness']['alpha']==['P','M']
    assert ad['odd_reservoir_disjointness']['beta']==['a','b','a-b','a+b']
    assert ad['two_adic_parity_reduction']['complete_2adic_congruence_branch_enumeration'] is False
    assert ae['interpretation']['fixed_finite_S_recovered'] is False
    assert 'A=B=D=1' in ba['AY_branch']['squareclasses']

    P=add(sub(pw(a,2),pw(b,2)),scale(2,mul(a,b)))
    M=sub(sub(pw(a,2),pw(b,2)),scale(2,mul(a,b)))
    D0=mul(mul(a,b),mul(sub(a,b),add(a,b)))
    Q=add(pw(a,2),pw(b,2))
    assert sub(pw(P,2),pw(M,2))==scale(8,D0)
    assert add(pw(P,2),pw(M,2))==scale(2,pw(Q,2))
    assert sub(pw(M,4),pw(P,4))==scale(-16,mul(D0,pw(Q,2)))
    assert sub(P,Q)==scale(2,mul(b,sub(a,b)))
    assert sub(Q,M)==scale(2,mul(b,add(a,b)))

    A=sub(pw(u,2),pw(v,2)); B=add(pw(u,2),pw(v,2))
    C=sub(mul(pw(M,2),pw(u,2)),mul(pw(P,2),pw(v,2)))
    D=add(mul(pw(M,2),pw(u,2)),mul(pw(P,2),pw(v,2)))
    assert C==sub(mul(pw(Q,2),A),scale(4,mul(D0,B)))
    assert D==add(scale(-4,mul(D0,A)),mul(pw(Q,2),B))

    bs=c['branch_discriminant_support']
    assert bs['potential_odd_bad_support']=='rad_odd(P*M*D0*Q)'
    assert bs['seven_pairwise_odd_disjoint_reservoirs']==['P','M','a','b','a-b','a+b','Q']
    assert bs['new_odd_reservoir_from_full_cover']=='Q=a^2+b^2'
    qd=c['Q_reservoir_disjointness']
    assert qd['Q_mod_a']=='b^2' and qd['Q_mod_b']=='a^2'
    assert qd['Q_mod_a_minus_b']=='2*a^2' and qd['Q_mod_a_plus_b']=='2*a^2'
    qr=c['Q_reservoir_local_reduction']
    assert qr['r_s_not_both_q_divisible'] is True
    assert qr['full_cover_first_residue_necessary_condition']=='(-1/q)=+1'
    assert qr['new_Q_reservoir_quadratic_residue_filter'] is False
    assert qr['new_Q_reservoir_parameter_shrink'] is False
    rr=c['route_result']
    assert rr['odd_bad_support_classified_to_seven_reservoirs'] is True
    assert rr['new_Q_reservoir_first_residue_row_automatic'] is True
    assert rr['candidate_parameter_set_shrunk'] is False and rr['receiver_closed'] is False
    assert rr['next_leaf']=='36-09BI_PRIME2_FULL_COVER_CONGRUENCE_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V96_36_09BH_BAD_PLACE_FULL_COVER_VALUATION'
    hist=st['audited_history']['36-09BF-BG']
    assert hist['pr']==1689 and hist['hostile_audit_review']==5129489415 and hist['audited_exact_head']==AUDIT_HEAD and hist['merged_main_sha']==BASE
    bh=st['authority_frontier']['36-09BH']
    assert bh['certificate_blob_sha']==CERT_BLOB
    assert bh['ODD_BAD_SUPPORT_SEVEN_RESERVOIRS'] is True
    assert bh['NEW_Q_RESERVOIR_FIRST_RESIDUE_FILTER'] is False
    assert bh['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bh['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BH'
    assert st['current']['next_exact_leaf']=='36-09BI_PRIME2_FULL_COVER_CONGRUENCE_PREFLIGHT'
    assert st['current']['36_09BI_entry_allowed'] is True
    for key in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][key] is False
    print('36-09BH verified: odd full-cover bad support is seven pairwise-odd-disjoint reservoirs; Q=a^2+b^2 is the only new odd reservoir and its first residue condition (-1/q)=+1 is automatic. No parameter shrink; prime 2 selected next.')

if __name__=='__main__': main()
