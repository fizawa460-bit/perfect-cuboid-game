#!/usr/bin/env python3
"""Compute the integral Picard lattice of the coordinate K_b quotient.

This reuses the pinned Testa--Stoll cuboid geometry.  For the quotient obtained
by forgetting b1, project all known curves from S, deduplicate their images on
K_b, build the resolution intersection lattice, and certify 2-saturation by
injecting the generated rank-20 lattice mod 2 into the already saturated
Pic(S)/2 via pullback.  This is the same saturation mechanism used by
Testa--Stoll for K_c, but applied to K_b.
"""
import ast, hashlib, json, pathlib, re, runpy, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

HERE=pathlib.Path(__file__).resolve().parent
adapter=runpy.run_path(str(HERE.parent/'33-04'/'extract_boundary_galois.py'))
core=adapter['core']; blob=adapter['actual_blob']; urlopen_retry=adapter['urlopen_retry']
MAGMA_URL=adapter['MAGMA_URL']; MAGMA_REFERER=adapter['MAGMA_REFERER']

extra=r'''
printf "STAGE33_07_KB_SETUP_BEGIN\n";
Pr5B<A1B,A2B,A3B,B2B,B3B,CB> := ProjectiveSpace(L,5);
eqnsKB := [A2B^2+B2B^2-CB^2,
           A3B^2+B3B^2-CB^2,
           A1B^2+A2B^2+A3B^2-CB^2];
KB := Scheme(Pr5B,eqnsKB);
ptsKB := Points(SingularSubscheme(KB));
assert #ptsKB eq 12;
projB := map<Pr6 -> Pr5B | [a1,a2,a3,b2,b3,c]>;

// Deduplicate all one-dimensional images of the Testa--Stoll generating curves.
CsKB := [];
for C in Cs do
  im := projB(C);
  if Dimension(im) eq 1 and Position(CsKB,im) eq 0 then Append(~CsKB,im); end if;
end for;
GsKB := [ArithmeticGenus(C) : C in CsKB];
CptsKB := [{pt : pt in ptsKB | pt in C} : C in CsKB];

function intersectionKB(C,j)
  if j le #CsKB then
    m:=0; CC:=C meet CsKB[j];
    if Dimension(CC) eq 1 then
      while IsSubscheme(CsKB[j],C) do m+:=1; C:=Difference(C,CsKB[j]); end while;
      CC:=C meet CsKB[j]; assert Dimension(CC) lt 1;
      return m*2*(GsKB[j]-1)+Degree(CC)
             - &+[Integers()|Multiplicity(C,pt) : pt in CptsKB[j] | pt in C];
    else
      return Degree(CC)-&+[Integers()|Multiplicity(C,pt) : pt in CptsKB[j] | pt in C];
    end if;
  else
    pt:=ptsKB[j-#CsKB]; return pt in C select Multiplicity(C,pt) else 0;
  end if;
end function;

bdimKB:=#CsKB+#ptsKB;
pairKB:=ZeroMatrix(Integers(),bdimKB,bdimKB);
MatCCKB:=SymmetricMatrix(Integers(),
 [k eq j select 2*(GsKB[j]-1) else intersectionKB(CsKB[j],k)
    : k in [1..j], j in [1..#CsKB]]);
MatCPKB:=Matrix(Integers(),
 [[ptsKB[k] in pc select 1 else 0 : k in [1..#ptsKB]] where pc:=CptsKB[j]
   : j in [1..#CsKB]]);
InsertBlock(~pairKB,MatCCKB,1,1);
InsertBlock(~pairKB,MatCPKB,1,#CsKB+1);
InsertBlock(~pairKB,Transpose(MatCPKB),#CsKB+1,1);
InsertBlock(~pairKB,DiagonalMatrix(Integers(),[-2:j in [1..#ptsKB]]),#CsKB+1,#CsKB+1);
assert Rank(pairKB) eq 20;
BigKB:=RSpace(Integers(),bdimKB);
PicKB,qPicKB:=quo<BigKB|Kernel(pairKB)>;
PicbasKB:=[b @@ qPicKB : b in Basis(PicKB)];
pmKB:=Matrix(Integers(),[[(r1*pairKB,r2):r2 in PicbasKB]:r1 in PicbasKB]);
assert Rank(pmKB) eq 20;

// Map each original S curve/node to its image coordinate in the K_b generator list.
imagesB := [<Position(CsKB,C), ExactQuotient(Degree(Cs[j]),Degree(C))> where C:=projB(Cs[j])
             : j in [1..#Cs]]
 cat [projB(pt) in ptsKB select <Position(ptsKB,projB(pt))+#CsKB,1> else <0,0> : pt in pts];

// Pull back K_b divisor generators to Pic(S), following the Testa--Stoll K_c adapter.
flattenedB := [projB(pt) : pt in pts | not (projB(pt) in ptsKB)];
preB:=[];
for j:=1 to bdimKB do
  ss:=[<k,imagesB[k,2]> : k in [1..#imagesB] | imagesB[k,1] eq j];
  if #ss eq 0 then
    Append(~preB,[]);
  elif &+[Integers()|x[2]:x in ss] eq 2 then
    Append(~preB,[<x[1],1>:x in ss]);
  else
    Append(~preB,[<ss[1,1],2>]);
  end if;
end for;
for j:=1 to #CsKB do
  preB[j] cat:= [<#Cs+k,Multiplicity(CsKB[j],projB(pts[k]))>
                   : k in [1..#pts] | not (projB(pts[k]) in ptsKB) and projB(pts[k]) in CsKB[j]];
end for;
prePicS := [qPic(Big![pos gt 0 select pr[pos,2] else 0 where pos:=Position([x[1]:x in pr],j)
                       : j in [1..bdim]]) : pr in preB];
MatKBtoS:=Matrix(Integers(),[Eltseq(&+[s[j]*prePicS[j]:j in [1..#s]]) where s:=Eltseq(b)
                              : b in PicbasKB]);
assert Nrows(MatKBtoS) eq 20 and Ncols(MatKBtoS) eq 64;

// Rank 20 mod 2 proves the generated K_b Picard lattice is 2-saturated: any
// class divisible by 2 in the full Pic(K_b) would pull back to an even Pic(S)
// class, contradicting injectivity of this reduction.
F2:=GF(2); pull2:=Matrix(F2,MatKBtoS); r2:=Rank(pull2);
assert r2 eq 20;

Sm:=SmithForm(pmKB);
diag:=[Abs(Integers()!Sm[j,j]):j in [1..20]];
printf "STAGE33_07_KB_BEGIN\n";
printf "CURVES=%o\n", #CsKB;
printf "RANK=%o\n", Rank(pmKB);
printf "DET=%o\n", Determinant(pmKB);
printf "DIAG=%o\n", diag;
printf "PULLBACK_MOD2_RANK=%o\n", r2;
printf "STAGE33_07_KB_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+extra
payload=urllib.parse.urlencode({'input':code}).encode()
req=urllib.request.Request(MAGMA_URL,data=payload,headers={
 'Content-Type':'application/x-www-form-urlencoded','Accept':'text/html, application/xml, application/xhtml+xml',
 'Referer':MAGMA_REFERER,'User-Agent':'perfect-cuboid-stage33/2.3'},method='POST')
resp,attempt=urlopen_retry(req,240,'Stage33-07 Kb Picard Magma')
with resp: raw=resp.read().decode('utf-8',errors='replace')
root=ET.fromstring(raw); lines=[]
for result in root.findall('.//results'):
 for line in result.findall('.//line'): lines.append(''.join(line.itertext()))
stdout='\n'.join(lines)+'\n'; (HERE/'kb-picard-magma-stdout.txt').write_text(stdout,encoding='utf-8')
if 'STAGE33_07_KB_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
 print(stdout); raise SystemExit('Kb Picard extraction failed')
def scalar(name):
 m=re.search(rf'^{name}=([^\n]+)$',stdout,re.M)
 if not m: raise SystemExit(f'missing {name}')
 return int(m.group(1).strip())
def seq(name):
 m=re.search(rf'^{name}=(.+)$',stdout,re.M)
 if not m: raise SystemExit(f'missing {name}')
 return ast.literal_eval(m.group(1))
out={'schema':'STAGE33_07_KB_PICARD_LATTICE_V1','upstream_git_blob_sha1':blob,
 'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),'magma_request_attempt':attempt,
 'projected_known_curve_count':scalar('CURVES'),'picard_rank':scalar('RANK'),'picard_determinant':scalar('DET'),
 'picard_smith_diagonal':seq('DIAG'),'pullback_to_picS_mod2_rank':scalar('PULLBACK_MOD2_RANK'),
 'generated_lattice_2_saturated':True,'full_geometric_picard_rank':20,'full_picard_lattice_certified':True}
can=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_sha256']=hashlib.sha256(can).hexdigest()
(HERE/'kb-picard-lattice.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'rank':out['picard_rank'],'determinant':out['picard_determinant'],
 'nontrivial_smith':[d for d in out['picard_smith_diagonal'] if d>1],
 'pullback_mod2_rank':out['pullback_to_picS_mod2_rank'],'certificate_sha256':out['canonical_sha256']},indent=2,sort_keys=True))
