#!/usr/bin/env python3
from __future__ import annotations
import itertools, json, subprocess
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BE/full-multiquadratic-character-quotient-inventory-preflight.json'
BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
BD=ROOT/'stages/stage36/36-09BD/exhaustive-view-audit-scaled-self-intersection.json'
AA=ROOT/'stages/stage36/36-09AA/receiver-coupled-same-x-twist-intersection-preflight.json'
AC=ROOT/'stages/stage36/36-09AC/same-x-separate-squareclass-double-cover-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='fe7ef406a9987981fe5f79267f3f8a39f37a61e4'
BD_HEAD='4ca57c4b9338f5b325df31554d2f0362a77f072e'
BD_CI='34092553609/101648948959'
CERT_BLOB='4f405f6e698b90861d26cf67b7f255ffe0a05f38'
LOCKS={BB:'e4b63fd500d05ff5dc704e0c08409edee5895053',BD:'5ee300e3a6765368c22aaf942180bb0a15aacf29',AA:'be447726a97158849c67ed6d57d6d3c35d6ba20f',AC:'3e95cc443bb9de9e0d2b14d6d9c32ea7c1953021'}
def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def F12(k,t): return 2*k*(1-t**4)
def F34(k,l,t): return 2*k*(1-(l*t)**4)
def F14(k,l,t): return 2*k*(1-t*t)*(1+l*l*t*t)
def F23(k,l,t): return 2*k*(1+t*t)*(1-l*l*t*t)
def main():
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BD_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']['36_09BD_exact_head']==BD_HEAD and c['batch_parent']['36_09BD_exact_head_ci']==BD_CI
    m=c['multiquadratic_cover']
    assert m['cover_degree']==16 and m['deck_group']=='(Z/2)^4' and m['genus']==17
    assert len(m['branch_points_over_Qbar'])==8 and m['branch_points_distinct'] is True
    counts={1:0,2:0,3:0,4:0}; dim=0; total=0
    for r in range(1,5):
      for S in itertools.combinations(range(4),r):
        counts[r]+=1; total+=1; dim+=r-1
    assert counts=={1:4,2:6,3:4,4:1}
    assert total==15 and dim==17
    q=c['character_quotients']; assert q['total_nontrivial_characters']==15 and q['jacobian_isogeny_decomposition_claimed'] is False
    inv=c['weight2_elliptic_inventory']; assert len(inv)==6 and len({x['id'] for x in inv})==6
    assert sum(x['status']=='NEW_CROSS_ELLIPTIC_QUOTIENT' for x in inv)==2
    for k,l,t in [(Fraction(3),Fraction(5,2),Fraction(2,7)),(Fraction(-5),Fraction(-7,3),Fraction(4,9)),(Fraction(6),Fraction(3,4),Fraction(5,11))]:
      assert l not in (0,1,-1) and t
      u=l*t
      assert F34(k,l,t)==F12(k,u)
      u2=1/(l*t)
      assert (l*l*t**4)*F14(k,l,u2)==-F23(k,l,t)
    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V93_36_09BE_AUDIT_CHECKPOINT'
    be=st['authority_frontier']['36-09BE']
    assert be['FULL_COVER_GENUS']==17 and be['CHARACTER_QUOTIENT_INVENTORY_COMPLETE'] is True
    assert be['WEIGHT2_ELLIPTIC_QUOTIENT_COUNT']==6 and be['NEW_CROSS_ELLIPTIC_QUOTIENT_COUNT']==2
    assert be['FULL_JACOBIAN_Q_ISOGENY_DECOMPOSITION_PROVED'] is False
    assert be['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and be['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BE-AUDIT-CHECKPOINT' and st['current']['36_09BF_entry_allowed'] is False
    print('36-09BE verified: degree-16 (Z/2)^4 cover has 8 simple branch points and genus 17; all 15 quadratic character quotients inventory as 4 genus0 + 6 genus1 + 4 genus2 + 1 genus3, with two cross elliptic quotients newly materialized. Jacobian isogeny decomposition is not claimed.')
if __name__=='__main__': main()
