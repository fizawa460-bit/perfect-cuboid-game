#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/'stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization.json'
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SNAP=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V62-67c4f6dafa63.json'

def blob(path:str)->str:
    b=(ROOT/path).read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

a=json.loads(ART.read_text()); s=json.loads(STATE.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4Z_ONE_EXPLICIT_BIQUATERNION_SECOND_QI_PRINCIPALIZATION_V1'
assert a['base_main_sha']=='8a04691d03f8ec17cf2236aab3d0f0d2dbde3fc3'
assert a['parent']['source_head_sha']=='67c4f6dafa63896f68b97a217d71443388b6d1ee'
assert blob(a['parent']['snapshot_path'])==a['parent']['snapshot_blob_sha']
for k,v in a['source_locks'].items():
    if 'path' in v and 'blob_sha' in v:
        assert blob(v['path'])==v['blob_sha'],k
assert a['source_locks']['upstream_stoll']['commit']=='51233ed5ef2bf228fac9416c66db9adc0ebcaadd'
assert a['source_locks']['upstream_stoll']['git_blob_sha1']=='0422b69847f2afb97cb7b3ed02ebef91279f61b1'

# Exact boundary parity algebra for the explicit class-A symbol.
p=a['boundary_parity_by_type']
xor=lambda *vs:[sum(z)%2 for z in zip(*vs)]
assert xor(p['u1'],p['u2'],p['u3'])==p['u1u2u3']==[1,0,0,0]
assert xor(p['u2'],p['u3'],p['r'])==p['u2u3r']==[1,1,0,0]
assert a['functions']['unit_identities']==['(p+x)(p-x)=1','(q+y)(q-y)=1','(w+z)(w-z)=1']
assert a['class_A']['r_zero_divisor']=='four Q(sqrt(2))-defined C3 components x=+/-1,p=+/-sqrt(2),z=-q'
assert a['class_A']['r_avoids_affine_A1_nodes'] is True
assert a['class_A']['unramified_on_U'] is True

# Recompute Goal4Y against its persisted V61 parent to lock the two residue targets.
orig=Path.read_text; sr=STATE.resolve(); snap61=ROOT/'stages/stage35-ex/snapshots/MAIN-STATE-V61-0a8af929e004.json'; snaptext=snap61.read_text()
def patched(self:Path,*args,**kwargs):
    if self.resolve()==sr:return snaptext
    return orig(self,*args,**kwargs)
Path.read_text=patched
try:
    core=runpy.run_path(str(ROOT/'stages/stage35-ex/stage35_ex_35_goal4y_core.py'))
finally:
    Path.read_text=orig
out=core['out']; assert out['success'] is True
assert out['h1_two_generator_positions_0based']==[12,13]
A,B=out['classes']
assert A['smith_h1_position_0based']==12 and B['smith_h1_position_0based']==13
# A: strict bits cc=ct=1, eps cc=0/ct=1, delta/eta zero.
Ao=A['boundary_orbit_residue_data']
for j in range(8): assert Ao[j]['character_bits']['cc']==1 and Ao[j]['character_bits']['ct']==1
for j in range(8,16): assert Ao[j]['character_bits']['cc']==0 and Ao[j]['character_bits']['ct']==1
for j in range(16,len(Ao)): assert not any(Ao[j]['character_bits'].values())
assert a['class_A']['boundary_residue_matches_goal4y_A'] is True
assert a['class_A']['explicit_rational_symbol_materialized'] is True

# B is literally zero on ct, hence the remaining cyclic direction is Q(i)/Q.
assert all(v==0 for v in B['h1_cocycle_ct'])
assert a['class_B']['h1_cocycle_ct_zero'] is True
assert a['class_B']['cyclic_extension']=='Q(i)/Q'
assert a['class_B']['explicit_F_B_materialized'] is False

# Recompute the exact Pic(Sbar) lift of B(cc) in the pinned upstream INDLIST basis.
indlist=[1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,33,34,35,37,38,41,45,49,53,69,93,94,95,96,97,98,99,101,102,103,104,105,106,107,109,110,111,113,117,118,119,120,121,125,126,127,129,133,135]
known=[[int(x) for x in r] for r in core['ns']['known']]
M=sp.Matrix([known[i-1] for i in indlist]); Minv=M.inv()
f,_=core['h1_generator'](13); lift=core['liftP'](f[1]); coeff=lift*Minv
assert all(x.q==1 for x in coeff)
sparse={str(indlist[j]):int(coeff[0,j]) for j in range(64) if coeff[0,j]}
assert sparse==a['class_B']['picard_lift_cc_indlist_coefficients']

# Exact B boundary target from Goal4Y.
Bo=B['boundary_orbit_residue_data']
for j in range(8): assert Bo[j]['character_bits']['cc']==1 and Bo[j]['character_bits']['ct']==0
selected={94,96,98,100,101,103,105,107}
# Goal4Y components 9..24 correspond known 93..108.
for j,known_idx in enumerate(range(93,109),start=8):
    assert Bo[j]['character_bits']['cc']==(1 if known_idx in selected else 0)
    assert Bo[j]['character_bits']['ct']==0
for j in range(24,len(Bo)): assert not any(Bo[j]['character_bits'].values())
assert a['class_B']['boundary_target']['exceptional_known_indices_1based']==sorted(selected)

# V63 credit firewall.
assert s['schema']=='STAGE35_EX_PESCH_E1_STATE_V63_GOAL4Z_ONE_EXPLICIT_BIQUATERNION_SECOND_QI_PRINCIPALIZATION_PENDING_AUDIT'
assert s['current']['unit']==a['unit']
assert s['claims']['goal4z_executed'] is True
assert s['claims']['open_receiver_explicit_rational_symbol_representative_count']==1
assert s['claims']['open_receiver_both_goal4y_explicit_symbols_materialized'] is False
assert s['claims']['open_receiver_local_evaluations_computed'] is False
assert s['claims']['brauer_manin_obstruction_obtained'] is False
assert s['claims']['E1_proved'] is False
assert s['claims']['stage35_closed'] is False
print('PASS Stage35-EX Goal4Z: class A explicit biquaternion; class B reduced to exact Q(i) cyclic principalization')
