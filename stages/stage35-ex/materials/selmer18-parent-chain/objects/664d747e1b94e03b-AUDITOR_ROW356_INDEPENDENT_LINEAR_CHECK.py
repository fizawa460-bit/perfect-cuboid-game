#!/usr/bin/env python3
"""Independent standalone GF(2) and witness-admissibility checks for row356.
Only Python stdlib; does not import the author's GF(2) rank or local arithmetic.
Run from any directory: python3 AUDITOR_ROW356_INDEPENDENT_LINEAR_CHECK.py
The p-adic characters are externally recomputed by the mathematical source replay;
this companion checks their logical use, witness admissibility, and exact rank.
"""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
C=json.loads((P/'math/global_local_restriction_certificate.json').read_text())
D=json.loads((P/'math/dyadic_full_kummer_certificate.json').read_text())

def rank(v):
    basis={}
    for q in v:
        a=int(q)
        while a:
            k=a.bit_length()-1
            if k in basis:a^=basis[k]
            else:basis[k]=a;break
    return len(basis)

def parity(x):return x.bit_count()&1

units=C['unit_records']
names=[u['name'] for u in units]
assert len(units)==12 and len(set(names))==12
h=[int(s,16) for s in D['local_constraint_interface']['unit_fake_image_constraints_hex']]
sc=int(D['scalar_minus1_character_hex'],16)
L=[int(r['character_hex'],16) for r in D['selected_fake_basis']]
assert rank(h)==19 and rank(L+[sc])==19 and len(L)==18
assert all(not parity(c & z) for c in h for z in L+[sc])

unit_c=[int(u['dyadic_character_hex'],16) for u in units]
recomputed_defect=[sum(parity(c & q)<<i for i,c in enumerate(h)) for q in unit_c]
assert recomputed_defect==[int(u['dyadic_defect_hex'],16) for u in units]
qrows=[sum(((d>>i)&1)<<j for j,d in enumerate(recomputed_defect)) for i in range(19)]
normrow=sum((int(u['norm']==-1)<<j) for j,u in enumerate(units))
realrow=sum(((u['real_sign_bits'][0]^u['real_sign_bits'][1])<<j) for j,u in enumerate(units))
assert rank(qrows)==6 and rank([normrow,realrow])==2
assert rank(qrows+[normrow,realrow])==6

words=[['epsilon','gamma8','gamma6'],['gamma8','gamma12'],['tau3'],['epsilon','upsilon3']]
mapu={u['name']:u for u in units}
def get_word(w):
    norm=1;sign=[0]*4;char=0
    for name in w:
        u=mapu[name]
        norm*=u['norm']
        sign=[a^b for a,b in zip(sign,u['real_sign_bits'])]
        char^=int(u['dyadic_character_hex'],16)
    assert norm==1 and (sign[0]^sign[1])==0
    assert (sign[2]^sign[3])==0 # norm 1 enforces even total sign parity
    defect=sum(parity(row&char)<<j for j,row in enumerate(h))
    return {'name':'*'.join(w),'norm':norm,'real_sign_bits':sign,'dyadic_char':hex(char),'defect':hex(defect)}
W=[get_word(w) for w in words]
wv=[int(w['defect'],16) for w in W]
assert rank(wv)==4
for mask in range(1,16):
    xor=0
    for i,v in enumerate(wv):
        if mask>>i&1:xor^=v
    assert xor!=0 # direct exhaustive independence, no same rank implementation
minor_indices=[0,2,4,5]
minor=[[int((col>>row)&1) for col in wv]for row in minor_indices]
assert minor==[[1,1,0,0],[1,1,1,1],[0,1,1,0],[0,0,1,0]]
assert rank([sum(x<<i for i,x in enumerate(row)) for row in minor])==4
assert W[0]['defect']=='0x2ce07' and W[1]['defect']=='0x39017' and W[2]['defect']=='0x383f4' and W[3]['defect']=='0x2d584'
old6=[int(s,16) for s in C['old_six_kernel_unit_masks_hex']]
assert rank(old6)==6 and all(not parity(x&r) for x in old6 for r in qrows)
assert 12-rank(qrows)==6
out={
  'status':'PASS_INDEPENDENT_LINEAR_AND_WITNESS_CHECK',
  'unit_total':len(units), 'local_unit_constraint_rank':rank(h),
  'old_norm_real_rank':2,'known_unit_dyadic_rank':6,
  'additional_rank_on_norm_real_candidate':rank(qrows+[normrow,realrow])-rank([normrow,realrow]),
  'witnesses':W,'witness_minor_indices':minor_indices,'witness_minor_matrix':minor,
  'full_nonzero_witness_combinations_tested':15,
  'known_unit_kernel_dim':12-rank(qrows),
  'fake_bound':'27+c_S','true_bound':'28+c_S',
  'global_c_S_uncomputed':True, 'source_exclusions':0}
assert out['additional_rank_on_norm_real_candidate']==4
print(json.dumps(out,ensure_ascii=False,indent=2))
