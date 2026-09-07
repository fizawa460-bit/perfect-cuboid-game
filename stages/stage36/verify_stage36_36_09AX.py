#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,math,subprocess
from pathlib import Path
import verify_stage36_36_09AW as aw
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09AX/bounded-fixed-p-tunnell-sieve-scan-preflight.json'
AW=ROOT/'stages/stage36/36-09AW/fixed-p-finite-squareclass-tunnell-branch-sieve-preflight.json'
AWV=ROOT/'stages/stage36/verify_stage36_36_09AW.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='d43db1874b0e657143fa07b1a16eb87fc27e0238'
AW_HEAD='40befe5dc8362444a127e066d6cfdbe4a6171943'
AW_CI='34086704923/101632013190'
CERT_BLOB='e72142f2ec8a2ab0dec4a6602874e1c2edc87c60'
AW_BLOB='c1970a020803275ba87b249229e319367fa8f811'
AWV_BLOB='a45d38d7db7428073e55e9cfeb929f335fd037e5'
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def main():
 assert blob(CERT)==CERT_BLOB and blob(AW)==AW_BLOB and blob(AWV)==AWV_BLOB
 subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
 subprocess.check_call(['git','merge-base','--is-ancestor',AW_HEAD,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text()); assert c['batch_parent']['36_09AW_exact_head']==AW_HEAD and c['batch_parent']['36_09AW_exact_head_ci']==AW_CI
 rows=[]; zero=[]; minv=10**9; mincases=[]; maxb=0; maxs=0; maxcases=[]
 tbr=tdn=tsv=tsn=0; count=0
 for a in range(1,11):
  for b in range(1,11):
   if a==b or math.gcd(a,b)!=1: continue
   s=aw.summary(a,b); count+=1
   br,di,su,sd=s['branches'],s['distinct'],s['surv'],s['surv_distinct']
   rows.append(f'{a},{b},{br},{di},{su},{sd}\n'); tbr+=br; tdn+=di; tsv+=su; tsn+=sd
   if su==0: zero.append((a,b))
   if su<minv: minv=su; mincases=[(a,b)]
   elif su==minv: mincases.append((a,b))
   if br>maxb: maxb=br
   if su>maxs: maxs=su; maxcases=[(a,b)]
   elif su==maxs: maxcases.append((a,b))
 digest=hashlib.sha256(''.join(rows).encode()).hexdigest()
 x=c['exact_scan_summary']
 assert count==c['scan_domain']['ordered_p_count']==62
 assert (tbr,tdn,tsv,tsn)==(5668,2214,3542,1436)
 assert (len(zero),minv,maxb,maxs)==(0,6,296,208)
 assert mincases==[(1,2),(1,3),(2,1),(3,1)]
 assert maxcases==[(7,10),(10,7)]
 assert digest==x['row_digest_sha256']=='1e1702dc17a70b69e54442e93a632fa86b313c662bcd6f849269524d18f05a5d'
 st=json.loads(STATE.read_text()); assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V86_36_09AX_CANDIDATE'; ax=st['authority_frontier']['36-09AX']; assert ax['BOUNDED_FIXED_P_SCAN_COMPLETE'] is True; assert ax['FIXED_P_ZERO_SURVIVOR_COUNT']==0; assert ax['TUNNELL_ALONE_PARAMETER_SHRINK_OBSERVED'] is False; assert ax['UNIFORM_NONEXCLUSION_THEOREM'] is False; assert ax['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and ax['RECEIVER_CLOSED'] is False; assert st['current']['unit']=='36-09AY' and st['current']['36_09AY_entry_allowed'] is True
 print('36-09AX verified: 62 primitive ordered p with 1<=a,b<=10; total AE branches 5668 -> Tunnell survivors 3542; zero fixed-p exclusions; minimum 6 survivors at 1/2,1/3,2,3. Bounded diagnostic only.')
if __name__=='__main__':main()
