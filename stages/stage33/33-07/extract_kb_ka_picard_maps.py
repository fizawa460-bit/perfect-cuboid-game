#!/usr/bin/env python3
"""Extract integral Picard Gram/pullback/Smith data for K_b or K_a.

Usage: python extract_kb_ka_picard_maps.py kb|ka
Each request starts from the pinned Testa--Stoll cuboid surface and constructs
only one coordinate K3 quotient, keeping the public Magma call below its hard
wall.  Galois actions are induced later from the already source-locked Pic(S)
action via the integral pullback matrix; no l-adic twist assumption is used.
"""
import ast, hashlib, json, pathlib, re, sys
from stoll_cuboid_source import load_pinned_source, run_magma

if len(sys.argv)!=2 or sys.argv[1] not in ('kb','ka'):
    raise SystemExit('usage: extract_kb_ka_picard_maps.py kb|ka')
mode=sys.argv[1]
HERE=pathlib.Path(__file__).resolve().parent
text,core,blob,source_attempt=load_pinned_source()

if mode=='kb':
    setup=r'''
Pr5X<X1,X2,X3,Y2,Y3,Z> := ProjectiveSpace(L,5);
eqnsX := [X2^2+Y2^2-Z^2,
           X3^2+Y3^2-Z^2,
           X1^2+X2^2+X3^2-Z^2];
KX := Scheme(Pr5X,eqnsX);
ptsX := Points(SingularSubscheme(KX));
projX := map<Pr6 -> Pr5X | [a1,a2,a3,b2,b3,c]>;
'''
    expected='[4,4]'
else:
    setup=r'''
Pr5X<X2,X3,Y1,Y2,Y3,Z> := ProjectiveSpace(L,5);
eqnsX := [X2^2+X3^2-Y1^2,
           Y3^2-X2^2+X3^2-Y2^2,
           Y3^2+X3^2-Z^2];
KX := Scheme(Pr5X,eqnsX);
ptsX := Points(SingularSubscheme(KX));
projX := map<Pr6 -> Pr5X | [a2,a3,b1,b2,b3,c]>;
'''
    expected='[4,8]'

common=r'''
CsX := [];
for C in Cs do
  im := projX(C);
  if Dimension(im) eq 1 and Position(CsX,im) eq 0 then Append(~CsX,im); end if;
end for;
GsX := [ArithmeticGenus(C) : C in CsX];
CptsX := [{pt : pt in ptsX | pt in C} : C in CsX];
function intersectionX(C,j)
  if j le #CsX then
    m:=0; CC:=C meet CsX[j];
    if Dimension(CC) eq 1 then
      while IsSubscheme(CsX[j],C) do m+:=1; C:=Difference(C,CsX[j]); end while;
      CC:=C meet CsX[j]; assert Dimension(CC) lt 1;
      return m*2*(GsX[j]-1)+Degree(CC)-&+[Integers()|Multiplicity(C,pt):pt in CptsX[j]|pt in C];
    else
      return Degree(CC)-&+[Integers()|Multiplicity(C,pt):pt in CptsX[j]|pt in C];
    end if;
  else
    pt:=ptsX[j-#CsX]; return pt in C select Multiplicity(C,pt) else 0;
  end if;
end function;
bdimX:=#CsX+#ptsX;
pairX:=ZeroMatrix(Integers(),bdimX,bdimX);
MatCCX:=SymmetricMatrix(Integers(),[k eq j select 2*(GsX[j]-1) else intersectionX(CsX[j],k):k in [1..j],j in [1..#CsX]]);
MatCPX:=Matrix(Integers(),[[ptsX[k] in pc select 1 else 0:k in [1..#ptsX]] where pc:=CptsX[j]:j in [1..#CsX]]);
InsertBlock(~pairX,MatCCX,1,1); InsertBlock(~pairX,MatCPX,1,#CsX+1);
InsertBlock(~pairX,Transpose(MatCPX),#CsX+1,1);
InsertBlock(~pairX,DiagonalMatrix(Integers(),[-2:j in [1..#ptsX]]),#CsX+1,#CsX+1);
assert Rank(pairX) eq 20;
BigX:=RSpace(Integers(),bdimX); PicX,qPicX:=quo<BigX|Kernel(pairX)>;
PicbasX:=[b @@ qPicX:b in Basis(PicX)];
pmX:=Matrix(Integers(),[[(r1*pairX,r2):r2 in PicbasX]:r1 in PicbasX]); assert Rank(pmX) eq 20;
imagesX := [<Position(CsX,C),ExactQuotient(Degree(Cs[j]),Degree(C))> where C:=projX(Cs[j]):j in [1..#Cs]]
 cat [projX(pt) in ptsX select <Position(ptsX,projX(pt))+#CsX,1> else <0,0>:pt in pts];
preX:=[];
for j:=1 to bdimX do
  ss:=[<k,imagesX[k,2]>:k in [1..#imagesX]|imagesX[k,1] eq j];
  if #ss eq 0 then Append(~preX,[]);
  elif &+[Integers()|x[2]:x in ss] eq 2 then Append(~preX,[<x[1],1>:x in ss]);
  else Append(~preX,[<ss[1,1],2>]); end if;
end for;
for j:=1 to #CsX do
  preX[j] cat:= [<#Cs+k,Multiplicity(CsX[j],projX(pts[k]))>:k in [1..#pts]|not(projX(pts[k]) in ptsX) and projX(pts[k]) in CsX[j]];
end for;
prePicS := [qPic(Big![pos gt 0 select pr[pos,2] else 0 where pos:=Position([x[1]:x in pr],j):j in [1..bdim]]):pr in preX];
MatXtoS:=Matrix(Integers(),[Eltseq(&+[s[j]*prePicS[j]:j in [1..#s]]) where s:=Eltseq(b):b in PicbasX]);
assert Nrows(MatXtoS) eq 20 and Ncols(MatXtoS) eq 64;
assert Rank(Matrix(GF(2),MatXtoS)) eq 20;
D,U,V:=SmithForm(pmX);
diag:=[Abs(Integers()!D[j,j]):j in [1..20]];
printf "STAGE33_07_KX_MAPS_BEGIN\n";
printf "NODES=%o\n",#ptsX; printf "CURVES=%o\n",#CsX;
printf "DET=%o\n",Determinant(pmX); printf "DIAG=%o\n",diag;
for r in [1..20] do printf "P_ROW_%o=%o\n",r,[pmX[r,c]:c in [1..20]]; end for;
for r in [1..20] do printf "KS_ROW_%o=%o\n",r,[MatXtoS[r,c]:c in [1..64]]; end for;
for r in [1..20] do printf "V_ROW_%o=%o\n",r,[V[r,c]:c in [1..20]]; end for;
printf "STAGE33_07_KX_MAPS_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+setup+'\n'+common
stdout,attempt=run_magma(code,300,f'Stage33-07 {mode.upper()} Picard maps Magma')
(HERE/f'{mode}-picard-maps-magma-stdout.txt').write_text(stdout,encoding='utf-8')
if 'STAGE33_07_KX_MAPS_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
    print(stdout); raise SystemExit(f'{mode} Picard maps extraction failed')
def grab(name):
    m=re.search(rf'^{name}=(.+)$',stdout,re.M)
    if not m: raise SystemExit(f'missing {name}')
    return ast.literal_eval(m.group(1))
def rows(prefix,n,m):
    out=[]
    for r in range(1,n+1):
        x=[int(v) for v in grab(f'{prefix}_ROW_{r}')]
        if len(x)!=m: raise SystemExit(f'{prefix} row length regression')
        out.append(x)
    return out
diag=[int(x) for x in grab('DIAG')]
det=int(re.search(r'^DET=(-?\d+)$',stdout,re.M).group(1))
nodes=int(re.search(r'^NODES=(\d+)$',stdout,re.M).group(1))
curves=int(re.search(r'^CURVES=(\d+)$',stdout,re.M).group(1))
exp=[4,4] if mode=='kb' else [4,8]
expdet=16 if mode=='kb' else 32
if diag[-2:]!=exp or abs(det)!=expdet:
    raise SystemExit(f'{mode} Smith regression det={det} tail={diag[-2:]}')
out={'schema':f'STAGE33_07_{mode.upper()}_PICARD_MAPS_V1','coordinate_k3':mode,
 'upstream_git_blob_sha1':blob,'source_fetch_attempt':source_attempt,
 'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),'magma_request_attempt':attempt,
 'singular_node_count':nodes,'projected_known_curve_count':curves,
 'picard_determinant':det,'picard_smith_diagonal':diag,
 'picard_gram_20x20':rows('P',20,20),'MatKtoS_20x64':rows('KS',20,64),
 'smith_right_transform_V_20x20':rows('V',20,20),
 'pullback_mod2_rank':20,'full_picard_lattice_certified':True}
can=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_sha256']=hashlib.sha256(can).hexdigest()
(HERE/f'{mode}-picard-maps.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'coordinate_k3':mode,'nodes':nodes,'determinant':det,
 'nontrivial_smith':diag[-2:],'certificate_sha256':out['canonical_sha256']},indent=2,sort_keys=True))
