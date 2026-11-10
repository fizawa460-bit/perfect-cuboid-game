"""Card217 symbolic row(B) cubefull receiver; synthetic, not endpoints."""
import math,json
from pathlib import Path
states=[]
for alpha in range(1,13):
    for beta in range(13):
        rows=['A','C'] if beta==0 else ['A','B','C']
        for row in rows:
            HQ=alpha if row in ['A','B'] else 0;HS=alpha-HQ
            TQ=beta if row=='A' else 0;TS=beta-TQ
            TB=beta if row=='B' else 0;TC=beta if row=='C' else 0;TF=0
            JB=alpha if TB else 0;PB=2*JB+TB
            ce=TS+2*HQ+3*TQ
            assert TB+TC+TF==TS and (not PB or PB>=3)
            assert (not PB or PB==ce)
            states.append((row,alpha,beta,ce,PB))
for beta in range(1,13):
    for side in ['Q','S']:
        TS=beta if side=='S' else 0;TF=TS;ce=beta if side=='S' else 3*beta
        assert TF==TS
        states.append(('fresh'+side,0,beta,ce,0))
cube=[]
for n in range(1,200001):
    rem=n;p=2;ok=True
    while p*p<=rem:
        e=0
        while rem%p==0:rem//=p;e+=1
        if e and e<3:ok=False;break
        p+=1
    if rem>1:ok=False
    if ok:cube.append(n)
checks=[]
for U in [10,100,1000,10000,200000]:
    count=sum(n<=U for n in cube);assert count<=10*U**(1/3)
    checks.append({'U':U,'cubefull_count':count})
tails=[]
for T in [1,2,10,100,1000,10000]:
    val=sum(1/n for n in cube if n>=T);assert val<=40*T**(-2/3)
    tails.append({'T':T,'truncated_reciprocal_sum':val,'proved_infinite_bound':40*T**(-2/3)})
# Show why row(C)/fresh-S do not imply the same cubefull divisor.
negative={'row_C_alpha1_beta1_c_depth':1,'fresh_S_beta1_c_depth':1}
out={'card':'M3-T11-217','local_exponent_states':len(states),'cubefull_census_checks':checks,'reciprocal_tail_checks':tails,'unsupported_extension_examples':negative,'scope':'symbolic retained-table replay and finite integer-label checks only;no physical population/cancellation','independent_audit':'NOT RUN'}
Path('M3-T11-217-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
