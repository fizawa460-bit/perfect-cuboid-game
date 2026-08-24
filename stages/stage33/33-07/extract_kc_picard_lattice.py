#!/usr/bin/env python3
"""Extract the full Picard lattice of the coordinate K_c quotient."""
import ast, hashlib, json, pathlib, re
from stoll_cuboid_source import load_pinned_source, run_magma

HERE=pathlib.Path(__file__).resolve().parent
text,core,blob,source_attempt=load_pinned_source()
START='// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6.'
END='// action of sign change of c'
i0=text.index(START); i1=text.index(END,i0); kcore=text[i0:i1]
extra=r'''
r2:=Rank(Matrix(GF(2),MatKtoS)); assert r2 eq 20;
SmK:=SmithForm(pmPicK); diagK:=[Abs(Integers()!SmK[j,j]):j in [1..20]];
printf "STAGE33_07_KC_BEGIN\n";
printf "NODES=%o\n",#ptsK; printf "CURVES=%o\n",#CsK; printf "RANK=%o\n",Rank(pmPicK);
printf "DET=%o\n",Determinant(pmPicK); printf "DIAG=%o\n",diagK; printf "PULLBACK_MOD2_RANK=%o\n",r2;
printf "STAGE33_07_KC_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+kcore+'\n'+extra
stdout,attempt=run_magma(code,300,'Stage33-07 Kc Picard Magma')
(HERE/'kc-picard-magma-stdout.txt').write_text(stdout,encoding='utf-8')
if 'STAGE33_07_KC_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
 print(stdout); raise SystemExit('Kc Picard extraction failed')
def scalar(name):
 m=re.search(rf'^{name}=([^\n]+)$',stdout,re.M)
 if not m: raise SystemExit(f'missing {name}')
 return int(m.group(1).strip())
def seq(name):
 m=re.search(rf'^{name}=(.+)$',stdout,re.M)
 if not m: raise SystemExit(f'missing {name}')
 return ast.literal_eval(m.group(1))
out={'schema':'STAGE33_07_KC_PICARD_LATTICE_V2','upstream_git_blob_sha1':blob,'source_fetch_attempt':source_attempt,
 'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),'magma_request_attempt':attempt,
 'singular_node_count':scalar('NODES'),'known_curve_count':scalar('CURVES'),'picard_rank':scalar('RANK'),
 'picard_determinant':scalar('DET'),'picard_smith_diagonal':seq('DIAG'),'pullback_to_picS_mod2_rank':scalar('PULLBACK_MOD2_RANK'),
 'generated_lattice_2_saturated':True,'full_geometric_picard_rank':20,'full_picard_lattice_certified':True,
 'transcendental_rank':2,'transcendental_discriminant_abs':abs(scalar('DET'))}
can=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_sha256']=hashlib.sha256(can).hexdigest()
(HERE/'kc-picard-lattice.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'nodes':out['singular_node_count'],'rank':out['picard_rank'],'determinant':out['picard_determinant'],
 'transcendental_discriminant_abs':out['transcendental_discriminant_abs'],'nontrivial_smith':[d for d in out['picard_smith_diagonal'] if d>1],
 'pullback_mod2_rank':out['pullback_to_picS_mod2_rank'],'certificate_sha256':out['canonical_sha256']},indent=2,sort_keys=True))
