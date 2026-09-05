#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,re,subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BLIND=ROOT/'stages/stage36/36-09I/blind-rediscovery-only.json'
CERT=ROOT/'stages/stage36/36-09I/post-w01-breadth-refresh.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='2f708b8f0b36483eb7ce19fbb4f7dcc6b9d9d0bc'
BLIND_COMMIT='aedd6245f27166fd77072af1dbc12e63dc796ddf'
BLIND_BLOB='decf74e9566a58e02dc160cac339fb96482c264e'
COMPARISON_COMMIT='c440b5ba219b9e2832b471a8b069be35a5bb2d48'
COMPARISON_CERT_BLOB='81d211b8f02c104b5d16074c2f6c37a01a64e298'
AUDIT_REPAIR_COMMIT='2b258166b82873e8cb04f932b9ddb1572418656f'
CERT_BLOB='f9bf252f3be47f606a3b270961df3b5943fa1909'
LOCKS={
 ROOT/'docs/arsenal/index.json':'aa45d19c2f1d8970c7f142bf744c5c17e75abe5a',
 ROOT/'docs/arsenal/cards/formal/S31-W01.md':'122a6c1c5c871c1c7b797017e854de8ec55e7c50',
 ROOT/'docs/arsenal/cards/formal/S34-W01.md':'01a8e90e34b4aa46edbfa825803d488e5230e9d0',
 ROOT/'docs/arsenal/cards/formal/S34-W03.md':'1d5275321f42768a6414d4610ac912c63be43f96',
 ROOT/'docs/research-os/policies/cycle-exploration-safety-protocol.md':'4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37',
}

def req(ok:bool,msg:str)->None:
    if not ok: raise SystemExit(msg)
def git(*args:str,check=True)->subprocess.CompletedProcess:
    return subprocess.run(['git',*args],cwd=ROOT,check=check,capture_output=True,text=True)
def out(*args:str)->str: return git(*args).stdout.strip()
def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def padd(a,b):
    c=dict(a)
    for m,v in b.items(): c[m]=c.get(m,0)+v
    return {m:v for m,v in c.items() if v}
def pneg(a): return {m:-v for m,v in a.items()}
def psub(a,b): return padd(a,pneg(b))
def pmul(a,b):
    c={}
    for ma,va in a.items():
        for mb,vb in b.items():
            m=tuple(x+y for x,y in zip(ma,mb)); c[m]=c.get(m,0)+va*vb
    return {m:v for m,v in c.items() if v}
def ppow(a,n):
    z=(0,)*len(next(iter(a))); r={z:1}
    for _ in range(n): r=pmul(r,a)
    return r
def pscale(a,k): return {m:k*v for m,v in a.items() if k*v}

def rank_f2(rows):
    a=[list(r) for r in rows]; rank=0
    for col in range(len(a[0])):
        piv=next((i for i in range(rank,len(a)) if a[i][col]),None)
        if piv is None: continue
        a[rank],a[piv]=a[piv],a[rank]
        for i in range(len(a)):
            if i!=rank and a[i][col]: a[i]=[x^y for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank

def is_rational_square(q:Fraction)->bool:
    if q<0: return False
    import math
    return math.isqrt(q.numerator)**2==q.numerator and math.isqrt(q.denominator)**2==q.denominator

def main()->None:
    # Fail-close blind chronology from immutable git history. The comparison
    # certificate is historical evidence; the working certificate may have
    # later audit-only ledger repairs and is locked separately below.
    req(out('show','-s','--format=%P',BLIND_COMMIT)==BASE,'blind commit must have exact base as sole parent')
    req(out('show','-s','--format=%P',COMPARISON_COMMIT)==BLIND_COMMIT,'comparison commit must be direct child of blind commit')
    req(git('merge-base','--is-ancestor',COMPARISON_COMMIT,'HEAD',check=False).returncode==0,'comparison commit not ancestor of HEAD')
    req(git('merge-base','--is-ancestor',AUDIT_REPAIR_COMMIT,'HEAD',check=False).returncode==0,'ledger audit repair not ancestor of HEAD')
    req(out('rev-parse',f'{BLIND_COMMIT}:stages/stage36/36-09I/blind-rediscovery-only.json')==BLIND_BLOB,'blind snapshot blob moved')
    req(out('rev-parse',f'{COMPARISON_COMMIT}:stages/stage36/36-09I/post-w01-breadth-refresh.json')==COMPARISON_CERT_BLOB,'historical comparison certificate blob moved')
    absent=git('cat-file','-e',f'{BLIND_COMMIT}:stages/stage36/36-09I/post-w01-breadth-refresh.json',check=False)
    req(absent.returncode!=0,'comparison certificate already existed at blind commit')
    req(blob(BLIND)==BLIND_BLOB and blob(CERT)==CERT_BLOB,'working 36-09I evidence drift')
    blind_text=BLIND.read_text()
    forbidden=['mapped_ledger','selected_route','arsenal','S31-W','S34-W']
    req(all(t.lower() not in blind_text.lower() for t in forbidden),'blind snapshot contains forbidden history/Arsenal marker')
    req(re.search(r'\"B(?:[1-9]|10|11)_[A-Z0-9_]+\"',blind_text) is None,'blind snapshot contains historical B-route identifier')

    for p,sha in LOCKS.items(): req(blob(p)==sha,f'locked comparison source drift: {p}')
    c=json.loads(CERT.read_text())
    req(c['schema']=='STAGE36_36_09I_POST_W01_BREADTH_REFRESH_V1','36-09I schema moved')
    req(c['base_main_sha']==BASE,'36-09I base moved')
    bp=c['blind_provenance']
    req(bp['blind_snapshot_commit']==BLIND_COMMIT and bp['blind_snapshot_blob_sha']==BLIND_BLOB,'blind provenance identity moved')

    # Exact polynomial verification of reciprocal identities, after clearing Laurent denominators.
    one={(0,0):1}; x={(1,0):1}; z={(0,1):1}
    x2=ppow(x,2); z2=ppow(z,2)
    F1=padd(x,z)
    F2=padd(pmul(x,z),one)
    lhs12=pmul(F1,F2)
    rhs12=padd(pmul(z,padd(x2,one)),pmul(x,padd(z2,one)))
    req(lhs12==rhs12,'reciprocal F1F2 identity failed')
    lhs34=padd(pmul(ppow(padd(x,one),2),ppow(psub(z,one),2)),pscale(pmul(x,z),16))
    rhs34=padd(pmul(ppow(psub(z,one),2),padd(x2,one)),pscale(pmul(x,padd(padd(z2,one),pscale(z,6))),2))
    req(lhs34==rhs34,'reciprocal F3F4 identity failed')

    for q in map(Fraction,[Fraction(2,3),Fraction(3,2),Fraction(5,4),Fraction(7,3)]):
        X=q*q+1/(q*q)
        req(X-2==(q-1/q)**2 and X+2==(q+1/q)**2,'X reconstruction forward identity failed')
    for U,V in [(Fraction(3,2),Fraction(5,2)),(Fraction(4,3),Fraction(10,3))]:
        if V*V-U*U==4:
            q=(V+U)/2; qi=(V-U)/2
            req(q*qi==1,'X reconstruction converse failed')

    for Z,k in [(Fraction(5,2),Fraction(1,3)),(Fraction(10,3),Fraction(2,5)),(Fraction(17,4),Fraction(1,5))]:
        D=1-k*k*(Z-2)
        req(D!=0,'test ratio denominator unexpectedly zero')
        X=(2*k*k*(Z+6)-Z)/D
        G1=X+Z; G2=(Z-2)*X+2*(Z+6)
        req(G1==k*k*G2,'ratio X formula failed')
        req(X-2==(Z+2)*(4*k*k-1)/D,'X-2 ratio formula failed')
        req(X+2==(16*k*k-(Z-2))/D,'X+2 ratio formula failed')
    req(not is_rational_square(Fraction(8,1)),'exceptional Z=6 unexpectedly physical')
    ex=c['ratio_parameterization']['exceptional_denominator_audit']
    req(ex['compatibility_forces']==['Z=6','k^2=1/4'] and ex['physical_exceptional_points']==0,'exceptional denominator certificate moved')

    common=[[1,1,1],[1,1,0]]
    req(rank_f2(common)==2,'common character rank moved')
    in_span=[]; outside=[]
    for mask in range(8):
        row=[(mask>>i)&1 for i in range(3)]
        r=rank_f2(common+[row])
        if r==2: in_span.append(row)
        elif r==3: outside.append(row)
        else: req(False,f'unexpected character rank {r}')
    req(len(in_span)==4 and len(outside)==4,'character quotient-space size moved')
    req(c['character_linear_refinement_exhaustion']['quotient_dimension']==1,'character quotient dimension moved')
    req(c['character_linear_refinement_exhaustion']['strictly_intermediate_character_linear_refinement_exists'] is False,'intermediate character receiver falsely claimed')

    # Comparison/route/firewall checks, including audit repair: C2 is NOT B7.
    mapping={m['blind_id']:(m['mapped_ledger'],m['classification']) for m in c['blind_candidate_mapping']}
    req(mapping['C1_RECIPROCAL_INVOLUTION_TWO_LINEAR_QUOTIENT']==('B3_FINITE_CURVE_OR_COVER_DECOMPOSITION','LIVE'),'C1 mapping moved')
    req(mapping['C2_GAUSSIAN_NORM_COMPRESSION']==(None,'UNTESTED_DISTINCT_UNMAPPED'),'Gaussian candidate incorrectly mapped onto a historical route')
    req(mapping['C4_VARIABLE_PRIME_RECIPROCITY'][1]=='UNTESTED','reciprocity candidate discarded')
    sep=c['candidate_separation_repair']
    req(sep['hostile_audit_fail_review']==5121228524,'ledger repair review provenance moved')
    req(sep['exact_equivalence_B7_C2_proved'] is False,'unsupported B7/C2 equivalence granted')
    req(sep['exact_implication_B7_to_C2_proved'] is False and sep['exact_implication_C2_to_B7_proved'] is False,'unsupported B7/C2 implication granted')
    req(sep['cycle_safety_distinct_untested_preserved'] is True,'distinct candidate preservation lost')
    led=c['cycle_ledger_after_comparison']
    req(led['B7_STANDARD_CAMPEDELLI_MODEL_ARITHMETIC_TRANSFER']=='UNTESTED_STANDARD_CAMPEDELLI_MODEL_ARITHMETIC_TRANSFER','preexisting B7 overwritten')
    req(led['C2_GAUSSIAN_NORM_COMPRESSION']=='UNTESTED_DISTINCT_FROM_B7_NO_EXACT_EQUIVALENCE','Gaussian candidate not independently retained')
    req(led['counts']=={'live':1,'untested':3,'blocked':6,'dominated':2},'36-09I repaired cycle counts moved')
    req(led['B3_FINITE_CURVE_OR_COVER_DECOMPOSITION']=='LIVE_RECIPROCAL_INVOLUTION_COVER_PREFLIGHT','B3 active route moved')
    req(led['B10_receiver_remains_exact_infrastructure'] is True,'B10 infrastructure lost')
    req(led['distinct_unmapped_candidates']==['C2_GAUSSIAN_NORM_COMPRESSION'],'distinct unmapped candidate ledger moved')
    route=c['route_decision']
    req(route['CYCLE_ROUTE_STATUS']=='PASS_NEW_GATE_FROM_STRONGER_VIEW','cycle verdict moved')
    req(route['CYCLE_LIVE_CANDIDATES']==1 and route['CYCLE_UNTESTED_CANDIDATES']==3,'route candidate counts moved')
    req(route['CYCLE_EXHAUSTIVE_VIEW_AUDIT'] is True and route['CYCLE_BLIND_REDISCOVERY'] is True,'fresh breadth evidence lost')
    req(route['CYCLE_SPLIT_TRIGGERED'] is False,'unexpected route split')
    req(route['selected_route']=='B3_FINITE_CURVE_OR_COVER_DECOMPOSITION','selected route moved')
    req(route['next_leaf_after_hostile_audit']=='36-09J_RECIPROCAL_INVOLUTION_TWO_LINEAR_COVER_PREFLIGHT','36-09J routing moved')
    ars=c['arsenal_comparison_after_blind_pass']
    req(ars['S31_W01']['triggered'] is False and ars['S34_W01']['triggered'] is False and ars['S34_W03']['triggered'] is False,'Arsenal credit prematurely triggered')
    req(all(v is False for v in c['scope_firewalls'].values()),'36-09I higher credit leaked')

    s=json.loads(STATE.read_text())
    req(s['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V30_36_09I_PENDING_HOSTILE_AUDIT','V30 schema moved')
    req(s['status']=='ACTIVE_PENDING_HOSTILE_AUDIT' and s['base_main_sha']==BASE,'V30 base/status moved')
    a=s['authority_frontier']['36-09I']
    req(a['blind_snapshot_commit']==BLIND_COMMIT and a['comparison_commit']==COMPARISON_COMMIT,'V30 chronology moved')
    req(a['blind_snapshot_blob_sha']==BLIND_BLOB and a['comparison_certificate_blob_sha']==COMPARISON_CERT_BLOB and a['certificate_blob_sha']==CERT_BLOB,'V30 evidence blobs moved')
    req(a['BLIND_PROVENANCE_FAIL_CLOSED'] is True,'V30 blind provenance not fail-closed')
    req(a['RECIPROCAL_TWO_LINEAR_REDUCTION_EXACT'] is True,'V30 reciprocal reduction lost')
    req(a['CHARACTER_LINEAR_INTERMEDIATE_REFINEMENT_EXISTS'] is False,'V30 character firewall moved')
    req(a['B3_STATUS']=='LIVE_RECIPROCAL_INVOLUTION_COVER_PREFLIGHT','V30 B3 route moved')
    req(a['B7_STATUS']=='UNTESTED_STANDARD_CAMPEDELLI_MODEL_ARITHMETIC_TRANSFER','V30 preexisting B7 overwritten')
    req(a['C2_GAUSSIAN_NORM_COMPRESSION_STATUS']=='UNTESTED_DISTINCT_FROM_B7_NO_EXACT_EQUIVALENCE','V30 Gaussian candidate not independently retained')
    req(a['B7_C2_EXACT_EQUIVALENCE_PROVED'] is False,'V30 unsupported B7/C2 equivalence')
    req(s['cycle_ledger']['counts']=={'live':1,'untested':3,'blocked':6,'dominated':2},'V30 repaired ledger counts moved')
    req(s['current']['36_09J_entry_allowed'] is False,'36-09J prematurely unlocked')
    req(s['promotion_gates']['receiver_emptiness_proved'] is False and s['promotion_gates']['R29_CAMP2_closed'] is False,'V30 theorem credit leaked')
    req(all(v is False for v in s['claims'].values()),'V30 high credit leaked')

    print('PASS STAGE36_36_09I_POST_W01_BREADTH_REFRESH_REPAIRED')
    print(f'blind={BLIND_COMMIT} -> comparison={COMPARISON_COMMIT} direct-child chronology verified')
    print('four factors -> reciprocal two-linear quotient; character-linear middle layer exhausted')
    print('B3 reciprocal cover LIVE; B7 standard transfer + C2 Gaussian + B11 reciprocity separately UNTESTED')
    print('36-09J locked pending hostile re-audit')

if __name__=='__main__': main()
