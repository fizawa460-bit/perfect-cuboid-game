#!/usr/bin/env python3
from __future__ import annotations
import concurrent.futures, json, pathlib, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parent
CORE=json.loads((ROOT/'picard-core.json').read_text())
MAGMA_URL='https://magma.maths.usyd.edu.au/xml/calculator.xml'; REFERER='https://magma.maths.usyd.edu.au/calc/'

def mm(M): return f"Matrix(Integers(),{len(M)},{len(M[0])},["+','.join(str(int(x)) for r in M for x in r)+'])'
def vv(v): return '['+','.join(str(int(x)) for x in v)+']'
G=CORE['basis_gram']; H=CORE['hyperplane']; I=CORE['raw_cross_pairings_with_basis']
hf=[sum(H[i]*G[i][j] for i in range(64)) for j in range(64)]
ef=[sum(I[k][j] for k in range(92,140)) for j in range(64)]
# Split the 92 nonexceptional known curves into two deterministic halves.
gf=[sum(I[k][j] for k in range(46)) for j in range(64)]

def one(d,g,e,a):
    lower=-d-2+2*g
    imgs=', '.join(f'Z3![{hf[j]},{ef[j]},{gf[j]}]' for j in range(64))
    code=f'''
SetColumns(0);
G:={mm(G)}; Pic:=RSpace(Integers(),64,G); H:=Pic!{vv(H)}; I:={mm(I)};
Z64:=RSpace(Integers(),64); Z3:=RSpace(Integers(),3);
phi:=hom<Z64 -> Z3 | [{imgs}]>;
tar:=Z3![{d},{e},{a}];
if tar notin Image(phi) then
  printf "STAGE32_CURVEGROUP d={d} g={g} e={e} a={a} feasible=0 raw=0 kept=0\\n";
else
  c0z:=tar @@ phi; C0:=Pic!Eltseq(c0z); K:=Kernel(phi);
  B:=BasisMatrix(K); Q:=-B*G*Transpose(B); assert IsPositiveDefinite(Q);
  KM:=RSpace(Integers(),Dimension(K)); inc:=hom<KM -> Pic | [Pic!Eltseq(b): b in Basis(K)]>;
  b:=Vector(Rationals(),[(C0,inc(KM.j)): j in [1..Dimension(K)]]);
  QQ:=ChangeRing(Q,Rationals()); center:=Solution(QQ,b);
  radius:=-{lower}+(C0,C0)+(center*QQ,center);
  raw:=0; kept:=0;
  if radius ge 0 then
    L:=LatticeWithGram(Q); clv:=CloseVectors(L,center,radius); raw:=#clv;
    for cv in clv do
      z:=KM!Eltseq(cv[1]); C:=C0+inc(z);
      exmass:=&+[&+[I[k,j]*C[j] : j in [1..64]] : k in [93..140]];
      amass:=&+[&+[I[k,j]*C[j] : j in [1..64]] : k in [1..46]];
      if (C,H) eq {d} and exmass eq {e} and amass eq {a}
         and (C,C) ge {lower}
         and forall{{k : k in [1..140] | &+[I[k,j]*C[j] : j in [1..64]] ge 0}} then kept +:= 1; end if;
    end for;
  end if;
  printf "STAGE32_CURVEGROUP d={d} g={g} e={e} a={a} feasible=1 raw=%o kept=%o\\n",raw,kept;
end if;
printf "STAGE32_CURVEGROUP_END\\n";
'''
    data=urllib.parse.urlencode({'input':code}).encode(); req=urllib.request.Request(MAGMA_URL,data=data,headers={'Content-Type':'application/x-www-form-urlencoded','Referer':REFERER,'User-Agent':'perfect-cuboid-stage32/1.8'},method='POST')
    t0=time.time()
    try:
      with urllib.request.urlopen(req,timeout=72) as resp: rawxml=resp.read().decode('utf-8','replace')
      root=ET.fromstring(rawxml); lines=[''.join(line.itertext()) for result in root.findall('.//results') for line in result.findall('.//line')]
      out='\n'.join(lines); ok='STAGE32_CURVEGROUP_END' in out and not any(x in out for x in ('Runtime error','User error','Internal error'))
      return {'a':a,'ok':ok,'seconds':round(time.time()-t0,3),'stdout':out}
    except Exception as exc: return {'a':a,'ok':False,'seconds':round(time.time()-t0,3),'error':repr(exc)}

def run(d,g,e):
    total_curve=19*d-5*e
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
      futs=[ex.submit(one,d,g,e,a) for a in range(total_curve+1)]
      for f in concurrent.futures.as_completed(futs):
        r=f.result(); results.append(r); print(json.dumps(r,sort_keys=True),flush=True)
    results.sort(key=lambda r:r['a'])
    p={'schema':'STAGE32_NUMERIC_MAGMA_CURVEGROUP_REFINE_V1','degree':d,'genus':g,'exceptional_mass':e,'curve_mass_total':total_curve,'subshard_count':total_curve+1,'all_completed':all(r['ok'] for r in results),'results':results}
    (ROOT/f'numeric-magma-curvegroup-d{d}-g{g}-e{e}.json').write_text(json.dumps(p,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'degree':d,'genus':g,'e':e,'completed':sum(r['ok'] for r in results),'subshards':total_curve+1,'all_completed':p['all_completed']},sort_keys=True))
    if not p['all_completed']: raise SystemExit('one or more curve-group shards did not complete')
if __name__=='__main__': run(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
