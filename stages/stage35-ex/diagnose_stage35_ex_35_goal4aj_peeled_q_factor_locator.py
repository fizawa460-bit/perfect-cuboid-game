#!/usr/bin/env python3
"""Goal4AJ diagnostic: recover the two literal Q-linear factors peeled from the denominator.

Re-run the exact Goal4AJ Q-hyperplane factor-peel reconstruction and read the two
singleton complete-hyperplane packets selected by the passing MILP: packet 0 with
multiplicity 1 and packet 3 with multiplicity 11.  The source linear forms were
already scalar-normalized in the verified Q(i,sqrt(2)) arithmetic.  For singleton
Galois orbits their normalized coefficients must therefore lie in Q; fail closed
otherwise.  This leaf only materializes the peeled degree-12 Q factor and grants
no residual/full-denominator/F_B/E1 credit.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import runpy

ROOT=Path(__file__).resolve().parents[2]
QPEEL=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_q_hyperplane_factor_peel.py'
QPEEL_SHA='c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba'
DIVISOR_PACKET_SHA='c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009'

ns=runpy.run_path(str(QPEEL))
out0=ns['out']
assert out0['canonical_sha256']==QPEEL_SHA
assert out0['source_locks']['degree31_divisor_packet_sha256']==DIVISOR_PACKET_SHA
sel=out0['denominator']['orbit_multiplicities']
assert sel==[
 {'orbit_hyperplane_indices_0based':[0],'orbit_size':1,'multiplicity':1},
 {'orbit_hyperplane_indices_0based':[3],'orbit_size':1,'multiplicity':11},
]
complete=ns['complete']
assert len(complete)==31

# A normalized source form is a 7-tuple of K=Q(i,sqrt(2)) coefficients, each
# encoded as four rational coordinates in basis 1,i,s,is.  Singleton Q-defined
# hyperplane lines must have only the rational coordinate after pivot normalization.
def q_coeff_vector(L):
    ans=[]
    for coeff4 in L:
        vals=[Fraction(int(n),int(d)) for n,d in coeff4]
        if any(vals[j] for j in (1,2,3)):
            raise SystemExit('selected singleton hyperplane form did not normalize over Q')
        ans.append(vals[0])
    return ans

def canon_fraction(q:Fraction):
    return [q.numerator,q.denominator]

L0=q_coeff_vector(complete[0][0])
L3=q_coeff_vector(complete[3][0])
assert any(L0) and any(L3)
vars_=['a1','a2','a3','b1','b2','b3','c']

def expr(v):
    terms=[]
    for q,x in zip(v,vars_):
        if not q: continue
        if q.denominator==1:
            c=q.numerator
            if c==1: terms.append(x)
            elif c==-1: terms.append('-'+x)
            else: terms.append(f'{c}*{x}')
        else:
            terms.append(f'({q.numerator}/{q.denominator})*{x}')
    s='+'.join(terms).replace('+-','-')
    return s or '0'

out={
 'schema':'STAGE35_EX_GOAL4AJ_PEELED_Q_LINEAR_FACTOR_LOCATOR_DIAGNOSTIC_V1',
 'source_locks':{
   'q_hyperplane_factor_peel_canonical_sha256':QPEEL_SHA,
   'degree31_divisor_packet_sha256':DIVISOR_PACKET_SHA,
 },
 'selected_complete_hyperplane_indices_0based':[0,3],
 'multiplicities':[1,11],
 'orbit_sizes':[1,1],
 'L0_coefficients_q':[canon_fraction(q) for q in L0],
 'L3_coefficients_q':[canon_fraction(q) for q in L3],
 'L0_expression':expr(L0),
 'L3_expression':expr(L3),
 'peeled_q_factor_expression':f'({expr(L0)})*({expr(L3)})^11',
 'peeled_q_factor_homogeneous_degree':12,
 'peeled_q_factor_materialized':True,
 'denominator_residual_degree19_materialized':False,
 'literal_degree31_denominator_materialized':False,
 'literal_numerator_coefficients_materialized':False,
 'literal_F_B_materialized':False,
 'E1_proved':False,
 'stage35_closed':False,
 'theorem_credit':False,
 'endpoint_credit':False,
}
out['canonical_sha256']=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('GOAL4AJ_PEELED_Q_FACTOR_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
print('GOAL4AJ_PEELED_Q_FACTOR=PASS')
