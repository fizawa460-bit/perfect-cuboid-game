#!/usr/bin/env python3
from __future__ import annotations
import json, pathlib, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parent
CORE=json.loads((ROOT/'picard-core.json').read_text())
MAGMA_URL='https://magma.maths.usyd.edu.au/xml/calculator.xml'; REFERER='https://magma.maths.usyd.edu.au/calc/'

def mm(M): return f"Matrix(Integers(),{len(M)},{len(M[0])},["+','.join(str(int(x)) for r in M for x in r)+'])'
def vv(v): return '['+','.join(str(int(x)) for x in v)+']'
G=CORE['basis_gram']; H=CORE['hyperplane']; I=CORE['raw_cross_pairings_with_basis']
hf=[sum(H[i]*G[i][j] for i in range(64)) for j in range(64)]
ef=[sum(I[k][j] for k in range(92,140)) for j in range(64)]
gf=[sum(I[k][j] for k in range(46)) for j in range(64)]

def run(d,g,e):
    lower=-d-2+2*g; total=19*d-5*e
    imgs=', '.join(f'Z3![{hf[j]},{ef[j]},{gf[j]}]' for j in range(64))
    code=f'''
SetColumns(0);
G:={mm(G)}; Pic:=RSpace(Integers(),64,G); H:=Pic!{vv(H)}; I:={mm(I)};
Z64:=RSpace(Integers(),64); Z3:=RSpace(Integers(),3);
phi:=hom<Z64 -> Z3 | [{imgs}]>;
K:=Kernel(phi); B:=BasisMatrix(K); Q:=-B*G*Transpose(B); assert IsPositiveDefinite(Q);
KM:=RSpace(Integers(),Dimension(K)); inc:=hom<KM -> Pic | [Pic!Eltseq(b): b in Basis(K)]>;
QQ:=ChangeRing(Q,Rationals()); L:=LatticeWithGram(Q);
for aa in [0..{total}] do
  tar:=Z3![{d},{e},aa]; raw:=0; kept:=0; feas:=0;
  if tar in Image(phi) then
    feas:=1; c0z:=tar @@ phi; C0:=Pic!Eltseq(c0z);
    b:=Vector(Rationals(),[(C0,inc(KM.j)): j in [1..Dimension(K)]]);
    center:=Solution(QQ,b); radius:=-{lower}+(C0,C0)+(center*QQ,center);
    if radius ge 0 then
      clv:=CloseVectors(L,center,radius); raw:=#clv;
      for cv in clv do
        z:=KM!Eltseq(cv[1]); C:=C0+inc(z);
        exmass:=&+[&+[I[k,j]*C[j] : j in [1..64]] : k in [93..140]];
        amass:=&+[&+[I[k,j]*C[j] : j in [1..64]] : k in [1..46]];
        if (C,H) eq {d} and exmass eq {e} and amass eq aa and (C,C) ge {lower}
           and forall{{k : k in [1..140] | &+[I[k,j]*C[j] : j in [1..64]] ge 0}} then kept +:= 1; end if;
      end for;
    end if;
  end if;
  printf "STAGE32_CURVEGROUP_BATCH a=%o feasible=%o raw=%o kept=%o\\n",aa,feas,raw,kept;
end for;
printf "STAGE32_CURVEGROUP_BATCH_END\\n";
'''
    data=urllib.parse.urlencode({'input':code}).encode(); req=urllib.request.Request(MAGMA_URL,data=data,headers={'Content-Type':'application/x-www-form-urlencoded','Referer':REFERER,'User-Agent':'perfect-cuboid-stage32/1.9'},method='POST')
    t0=time.time()
    try:
      with urllib.request.urlopen(req,timeout=75) as resp: rawxml=resp.read().decode('utf-8','replace')
    except Exception as exc:
      payload={'schema':'STAGE32_CURVEGROUP_BATCH_V1','degree':d,'genus':g,'exceptional_mass':e,'ok':False,'seconds':round(time.time()-t0,3),'error':repr(exc)}
      (ROOT/f'numeric-magma-curvegroup-batch-d{d}-g{g}-e{e}.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n'); print(json.dumps(payload,sort_keys=True)); raise
    root=ET.fromstring(rawxml); lines=[''.join(line.itertext()) for result in root.findall('.//results') for line in result.findall('.//line')]
    out='\n'.join(lines); rows=[]
    for line in lines:
      if line.startswith('STAGE32_CURVEGROUP_BATCH a='):
        vals={q.split('=')[0]:int(q.split('=')[1]) for q in line.split()[1:]}
        rows.append(vals)
    ok='STAGE32_CURVEGROUP_BATCH_END' in out and len(rows)==total+1 and not any(x in out for x in ('Runtime error','User error','Internal error'))
    payload={'schema':'STAGE32_CURVEGROUP_BATCH_V1','degree':d,'genus':g,'exceptional_mass':e,'curve_mass_total':total,'subshard_count':total+1,'ok':ok,'seconds':round(time.time()-t0,3),'rows':rows,'stdout':out}
    (ROOT/f'numeric-magma-curvegroup-batch-d{d}-g{g}-e{e}.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'degree':d,'genus':g,'e':e,'ok':ok,'seconds':payload['seconds'],'rows':len(rows),'raw_total':sum(r['raw'] for r in rows),'kept_total':sum(r['kept'] for r in rows)},sort_keys=True))
    if not ok: raise SystemExit('batched curve-group enumeration did not complete')
if __name__=='__main__': run(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
