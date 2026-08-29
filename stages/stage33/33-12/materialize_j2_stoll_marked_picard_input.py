#!/usr/bin/env python3
"""Fresh pinned-Stoll extraction of the named J2 carrier/exceptional PicK input."""
import ast,hashlib,json,re,sys
from pathlib import Path
H=Path(__file__).resolve().parent; sys.path.insert(0,str(H.parent/'33-07'))
from stoll_cuboid_source import load_pinned_source,run_magma
OUT=H/'j2-stoll-marked-picard-input.json'; SUP=H/'j2-ruled-to-stoll-marked-kc-support.json'
SUPSHA='881d2637c83bcae5d7bdfe9cf534baea7ad15b983719f7a482d3b7240fe8c510'; BLOB='0422b69847f2afb97cb7b3ed02ebef91279f61b1'
def sh(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def grab(s,n):
 m=re.search(rf'^{re.escape(n)}=(.+)$',s,re.M)
 if not m: raise SystemExit('missing '+n)
 return ast.literal_eval(m.group(1))
s=json.loads(SUP.read_text()); b=dict(s); got=b.pop('canonical_sha256')
assert got==SUPSHA and sh(b)==SUPSHA and s['branch_component']['stoll_CsK_index_1based']==22
text,_,blob,fa=load_pinned_source(); assert blob==BLOB
ks=text.index('Pr5<A1,A2,A3,B1,B2,B3> := ProjectiveSpace(L, 5);')
ke=text.index('printf "\\nConstructing canonical maps Pic(S) --> Pic(K) and Pic(K) --> Pic(S)...',ks)
extra=r'''
t := Pr5![1,0,0,0,-1,-1]; k := Position(ptsK,t); assert k ne 0 and #CsK eq 62 and t in CsK[22];
e := #CsK+k; M := Matrix(Integers(),[Eltseq(qPicK(BigK.indlistK[r])):r in [1..20]]); d:=Determinant(M); assert Abs(d) eq 1;
MQ:=ChangeRing(M,Rationals()); cq:=Vector(Rationals(),Eltseq(qPicK(BigK.22))); eqv:=Vector(Rationals(),Eltseq(qPicK(BigK.e)));
cm:=cq*MQ^-1; em:=eqv*MQ^-1; assert forall{x:x in Eltseq(cm)|Denominator(x) eq 1} and forall{x:x in Eltseq(em)|Denominator(x) eq 1};
printf "BEGINJ2\nPT=%o\nEX=%o\nMUL=%o\nDET=%o\nCQ=%o\nEQ=%o\nCM=%o\nEM=%o\nCI=%o\nEI=%o\nENDJ2\n",k,e,Multiplicity(CsK[22],t),d,[Integers()!x:x in Eltseq(cq)],[Integers()!x:x in Eltseq(eqv)],[Integers()!x:x in Eltseq(cm)],[Integers()!x:x in Eltseq(em)],[pairingmatK[22,indlistK[r]]:r in [1..20]],[pairingmatK[e,indlistK[r]]:r in [1..20]];
'''
code='SetColumns(0);\nquick:=true;\nL<i,s>:=ext<Rationals()|Polynomial([1,0,1]),Polynomial([-2,0,1])>;\n'+text[ks:ke]+extra
out,ma=run_magma(code,180,'Stage33-12 J2 marked Kc Picard input',user_agent='perfect-cuboid-stage33/3.3-j2-marked-kc-picard-input')
if 'ENDJ2' not in out or any(x in out for x in ('Runtime error','Internal error','User error','Assertion failed')): print(out); raise SystemExit('Magma extraction failed')
pt=int(grab(out,'PT')); ex=int(grab(out,'EX')); mul=int(grab(out,'MUL')); det=int(grab(out,'DET'))
cq=[int(x) for x in grab(out,'CQ')]; eqv=[int(x) for x in grab(out,'EQ')]; cm=[int(x) for x in grab(out,'CM')]; em=[int(x) for x in grab(out,'EM')]; ci=[int(x) for x in grab(out,'CI')]; ei=[int(x) for x in grab(out,'EI')]
assert ex==62+pt and abs(det)==1 and mul>0 and all(len(x)==20 for x in (cq,eqv,cm,em,ci,ei))
cert={'schema':'STAGE33_12_J2_STOLL_MARKED_PICARD_INPUT_V1','source_locks':{'stoll_repository':'MichaelStollBayreuth/Verification','stoll_commit':'51233ed5ef2bf228fac9416c66db9adc0ebcaadd','stoll_path':'Cuboids/cuboids.magma','stoll_git_blob_sha1':blob,'j2_ruled_to_stoll_support_sha256':SUPSHA,'submitted_magma_code_sha256':hashlib.sha256(code.encode()).hexdigest()},'execution':{'source_fetch_attempt':fa,'magma_request_attempt':ma,'remote_cas_role':'pinned Kc Picard quotient and named J2 carrier/exceptional marking only','smith_form_computed':False,'full_surface_picard_recomputed':False,'automorphism_computed':False,'gersten_data_computed':False},'stoll_kc_marked_basis':{'basis':'indlistK','indlistK_1based':[2,4,5,7,9,10,20,21,26,35,39,42,44,47,49,52,54,64,67,72],'rank':20,'determinant':det,'unimodular':True},'named_J2_carrier':{'CsK_index_1based':22,'equations':['B1=0','i*A2-A3=0'],'contains_infinity_singularity':True,'multiplicity_at_infinity_singularity':mul,'magma_qPicK_coordinates':cq,'marked_indlistK_coordinates':cm,'intersection_signature_against_indlistK':ci},'named_J2_infinity_exceptional':{'singular_point':['1','0','0','0','-1','-1'],'ptsK_index_1based':pt,'BigK_exceptional_index_1based':ex,'exceptional_tangent_attachment_direction':['1','i','0'],'magma_qPicK_coordinates':eqv,'marked_indlistK_coordinates':em,'intersection_signature_against_indlistK':ei},'exact_scope':{'J2_carrier_marked_PicK_class_materialized':True,'infinity_exceptional_marked_PicK_class_materialized':True,'finite_support_points_are_not_promoted_to_PicK_divisor_classes':True,'branch_jacobian_2torsion_to_picard_discriminant_kummer_glue_materialized':False,'J2_kc_discriminant_coordinate_materialized':False,'J2_q1_kc_adapter_unique':False,'GL2_F2_adapter_survivors':6,'finite_v4_kummer_defect_columns_materialized':0},'next_exact_leaf':'APPLY_NAMED_BRANCH_JACOBIAN_2TORSION_TO_KC_PICARD_TRANSCENDENTAL_KUMMER_GLUE_USING_MARKED_CARRIER_AND_EXCEPTIONAL_INPUT_THEN_FIX_J2_KERNEL_LINE','promotion_firewall':{'arithmetic_hs_d2_computed':False,'global_q_residue_lifts_complete':False,'stage33_12_closed':False,'stage33_07_closed':False,'stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,'receiver_credit':False,'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False}}
cert['canonical_sha256']=sh(cert); OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print('STAGE33_12_J2_STOLL_MARKED_PICARD_INPUT=PASS_EXACT'); print('PTSK_INDEX_1BASED='+str(pt)); print('EXCEPTIONAL_BIGK_INDEX_1BASED='+str(ex)); print('J2_CARRIER_MARKED='+json.dumps(cm,separators=(',',':'))); print('J2_INFINITY_EXCEPTIONAL_MARKED='+json.dumps(em,separators=(',',':'))); print('CERTIFICATE_SHA256='+cert['canonical_sha256'])
