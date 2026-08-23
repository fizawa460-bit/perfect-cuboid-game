#!/usr/bin/env python3
from __future__ import annotations
import json, math, pathlib, urllib.parse, urllib.request, xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
CORE=json.loads((ROOT/'picard-core.json').read_text())
MAGMA_URL='https://magma.maths.usyd.edu.au/xml/calculator.xml'
REFERER='https://magma.maths.usyd.edu.au/calc/'

def egcd_coeffs(vals):
    coeff=[0]*len(vals)
    g=0
    for i,a in enumerate(vals):
        oldg=g
        if oldg==0:
            g=abs(a); coeff[i]=1 if a>=0 else -1
            continue
        # x*oldg + y*a = newg
        def eg(a,b):
            if b==0:return (abs(a),1 if a>=0 else -1,0)
            q=a//b
            gg,x1,y1=eg(b,a-q*b)
            return gg,y1,x1-q*y1
        ng,x,y=eg(oldg,a)
        coeff=[x*c for c in coeff]
        coeff[i]+=y
        g=ng
    return g,coeff

def magma_matrix(M):
    flat=','.join(str(int(x)) for r in M for x in r)
    return f'Matrix(Integers(),{len(M)},{len(M[0])},[{flat}])'

def magma_vec(v):
    return '['+','.join(str(int(x)) for x in v)+']'

def run(d,g):
    G=CORE['basis_gram']; H=CORE['hyperplane']; I=CORE['raw_cross_pairings_with_basis']
    hform=[sum(H[i]*G[i][j] for i in range(64)) for j in range(64)]
    gg,bez=egcd_coeffs(hform)
    if d%gg: raise SystemExit(f'degree {d} not represented; gcd={gg}')
    c0=[(d//gg)*x for x in bez]
    r=math.gcd(d,16); m=16//r; n=d//r
    lower=-d-2+2*g
    bound=m*m*(d*d-16*lower)//16
    code=f'''
SetColumns(0);
G := {magma_matrix(G)};
Pic := RSpace(Integers(),64,G);
H := Pic!{magma_vec(H)};
C0 := Pic!{magma_vec(c0)};
assert (C0,H) eq {d};
Hperp := Kernel(Transpose(Matrix([Eltseq(H)])*G));
posG := -BasisMatrix(Hperp)*G*Transpose(BasisMatrix(Hperp));
L := LatticeWithGram(posG);
HM := RSpace(Integers(),63);
inc := hom<HM -> Pic | Basis(Hperp)>;
y0 := {m}*C0 - {n}*H;
base := L!Eltseq(y0 @@ inc);
clv := CloseVectors({m}*L, base, {bound});
I := {magma_matrix(I)};
kept := 0;
for cv in clv do
    zz := HM!Eltseq(L!(1/{m}*cv[1]));
    C := C0 - inc(zz);
    if (C,H) eq {d} and (C,C) ge {lower} and forall{{k : k in [1..140] | &+[I[k,j]*C[j] : j in [1..64]] ge 0}} then
        kept +:= 1;
    end if;
end for;
printf "STAGE32_NUMERIC_SLICE d={d} g={g} raw=%o kept=%o\\n", #clv, kept;
printf "STAGE32_NUMERIC_SLICE_END\\n";
'''
    data=urllib.parse.urlencode({'input':code}).encode()
    req=urllib.request.Request(MAGMA_URL,data=data,headers={'Content-Type':'application/x-www-form-urlencoded','Referer':REFERER,'User-Agent':'perfect-cuboid-stage32/1.4'},method='POST')
    with urllib.request.urlopen(req,timeout=75) as resp: raw=resp.read().decode('utf-8','replace')
    root=ET.fromstring(raw); lines=[]
    for result in root.findall('.//results'):
        for line in result.findall('.//line'): lines.append(''.join(line.itertext()))
    out='\n'.join(lines)
    print(out)
    (ROOT/f'numeric-magma-slice-d{d}-g{g}.txt').write_text(out+'\n')
    if 'STAGE32_NUMERIC_SLICE_END' not in out or any(x in out for x in ('Runtime error','User error','Internal error')):
        raise SystemExit('numeric Magma slice failed')

if __name__=='__main__':
    run(2,0)
