#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-genus2-rankle1-gaussian-elliptic-quotient-lock.json"
OUT=ROOT/"d2-stageA2-genus2-rankle1-gaussian-rank-index-chabauty-probe.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-gaussian-rank-index-chabauty-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"; REFERER="https://magma.maths.usyd.edu.au/calc/"; TIMEOUT=660

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode(); req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-gaussian-rank-index/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp: raw=resp.read().decode("utf-8",errors="replace"); status=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"): lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")

def val(prefix,out,required=True):
    for line in out.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    if required: raise RuntimeError(prefix+" missing")
    return None

def code_for(t):
    a,b=map(int,t["q"].split('/')); d=list(map(int,t["delta"])); n=int(t["n"]); c=int(t["c"]); A=int(t["A"]); a2=t["elliptic_a2"].replace("i","ii"); a4=t["elliptic_a4"].replace("i","ii")
    return f'''SetColumns(0); SetQuitOnError(true);\nQ:=Rationals(); Qz<z>:=PolynomialRing(Q); K<ii>:=NumberField(z^2+1);\nE<EX,EY,EZ>:=EllipticCurve([K|0,{a2},0,{a4},0]); assert Discriminant(E) ne 0;\nprint \"BEGIN branch={t['branch_id']} q={t['q']} model={t['model_id']}\";\nlo,hi:=RankBounds(E : Effort:=1); print \"RANK_BOUNDS:\",lo,hi;\nT,tm:=TorsionSubgroup(E); tinv:=Invariants(T); print \"TORSION_INVARIANTS:\",tinv;\nsuccess,G,pm:=PseudoMordellWeilGroup(E); pinv:=Invariants(G); print \"PMW_SUCCESS:\",success; print \"PMW_INVARIANTS:\",pinv;\nP1:=ProjectiveSpace(Q,1); pi:=map< E -> P1 | [EX,EZ] >; pie:=Extend(pi);\nVset:={{}}; RR:=1; complete_index:=false; mode:=\"NONE\";\nif lo eq 0 and hi eq 0 then\n  mode:=\"RANK0_TORSION_FULL\"; complete_index:=true;\n  Vset:={{ t : t in T }}; print \"ENUM_GROUP_COUNT:\",#Vset;\nelif lo eq 1 and hi eq 1 and #pinv gt 0 then\n  gensG:=[G.i : i in [1..Ngens(G)]]; freeG:=[g : g in gensG | Order(g) eq 0];\n  print \"PMW_FREE_GENERATOR_COUNT:\",#freeG;\n  if #freeG eq 1 then\n    P:=pm(freeG[1]); print \"FREE_POINT:\",P; assert Order(P) eq 0;\n    SP:=Saturation([P],2 : TorsionFree:=true); print \"SAT2_COUNT:\",#SP; assert #SP eq 1; QP:=SP[1]; print \"SAT2_POINT:\",QP;\n    H:=AbelianGroup([2,2,0]); tors_ok:=(tinv eq [2,2]); print \"TORSION_MATCH_22:\",tors_ok;\n    if tors_ok then\n      T1:=tm(T.1); T2:=tm(T.2); assert Order(T1) eq 2 and Order(T2) eq 2 and Order(QP) eq 0;\n      hm:=map< H -> E | h :-> (Integers()!Eltseq(h)[1])*T1 + (Integers()!Eltseq(h)[2])*T2 + (Integers()!Eltseq(h)[3])*QP >;\n      VV,RR:=Chabauty(hm,pi : IndexBound:=2); Vset:=VV; mode:=\"RANK1_SAT2_ELLCHAB\"; complete_index:=true;\n      print \"ELLCHAB_R:\",RR; print \"ELLCHAB_COUNT:\",#Vset;\n      assert IsOdd(RR) eq false or RR eq 1;\n    end if;\n  end if;\nend if;\nprint \"MODE:\",mode; print \"INDEX_COPRIME_2_PROVED:\",complete_index;\nquotient_rational_x:=0; reconstructed_C_x:=0; nondeg_parent:=0; image_lines:=0;\nif complete_index then\n  for g in Vset do\n    Pcur := mode eq \"RANK0_TORSION_FULL\" select tm(g) else hm(g); im:=pie(Pcur); print \"GROUP_IMAGE:\",g,\" -> \",im; image_lines +:= 1;\n    if im[2] ne 0 then\n      kval:=im[1]/im[2]; ok,qx:=IsCoercible(Q,kval);\n      if ok then\n        quotient_rational_x +:= 1; uu:=qx/({A}); ds:=uu^2+4; sq,sd:=IsSquare(ds); print \"QX:\",qx,\" U:\",uu,\" XDISCR_SQUARE:\",sq;\n        if sq then\n          for xx in [(uu+sd)/2,(uu-sd)/2] do\n            ff:=({c})*xx*(xx^2-1)*(xx+({n}))*(({n})*xx-1); cpt,yy:=IsSquare(ff);\n            U:=xx^2-1; Vform:=2*xx; AA:={a}*U+{b}*Vform; BB:={b}*U+{a}*Vform; deg:=U eq 0 or Vform eq 0 or AA eq 0 or BB eq 0;\n            sU:=IsSquare(U/({d[0]})); sV:=IsSquare(Vform/({d[1]})); sA:=IsSquare(AA/({d[2]})); sB:=IsSquare(BB/({d[3]})); parent:=cpt and sU and sV and sA and sB;\n            if cpt then reconstructed_C_x +:= 1; end if; if parent and not deg then nondeg_parent +:= 1; end if;\n            print \"PULLBACK_X:\",xx,\" C_POINT:\",cpt,\" DEG:\",deg,\" PARENT:\",parent,\" SQ_UVAB:\",sU,sV,sA,sB;\n          end for;\n        end if;\n      end if;\n    end if;\n  end for;\n  print \"QUOTIENT_RATIONAL_X_COUNT:\",quotient_rational_x; print \"RECONSTRUCTED_C_X_COUNT_WITH_MULTIPLICITY:\",reconstructed_C_x; print \"NONDEGENERATE_FULL_PARENT_LIFT_COUNT:\",nondeg_parent;\n  print \"CLOSURE_CANDIDATE:\",nondeg_parent eq 0;\nelse\n  print \"CLOSURE_CANDIDATE: false\";\nend if;\nprint \"END branch={t['branch_id']}\";\n'''

d=json.loads(LOCK.read_text()); records=[]; rawparts=[]
for t in d["targets"]:
    out=""; err=None; status="UNRESOLVED_RESOURCE_OR_EXTERNAL_WALL"
    try:
        http,out=submit(code_for(t)); bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
        if http==200 and f"END branch={t['branch_id']}" in out and not bad: status="PASS_RETURN"
        else: err=f"http={http} malformed_or_magma_error"
    except Exception as ex: err=f"{type(ex).__name__}: {ex}"
    rec={"branch_id":t["branch_id"],"q":t["q"],"model_id":t["model_id"],"sign_partner":t["sign_partner"],"status":status,"error":err,"stdout_sha256":hashlib.sha256(out.encode()).hexdigest()}
    rec["rank_bounds"]=val("RANK_BOUNDS:",out,False); rec["torsion_invariants"]=val("TORSION_INVARIANTS:",out,False); rec["pmw_success"]=val("PMW_SUCCESS:",out,False); rec["pmw_invariants"]=val("PMW_INVARIANTS:",out,False); rec["mode"]=val("MODE:",out,False)
    for pfx,key,typ in [("PMW_FREE_GENERATOR_COUNT:","pmw_free_generator_count",int),("INDEX_COPRIME_2_PROVED:","index_coprime_2_proved",lambda s:s=="true"),("ELLCHAB_R:","ellchab_R",int),("ELLCHAB_COUNT:","ellchab_count",int),("QUOTIENT_RATIONAL_X_COUNT:","quotient_rational_x_count",int),("RECONSTRUCTED_C_X_COUNT_WITH_MULTIPLICITY:","reconstructed_C_x_count_with_multiplicity",int),("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:","nondegenerate_full_parent_lift_count",int),("CLOSURE_CANDIDATE:","closure_candidate",lambda s:s=="true")]:
        z=val(pfx,out,False)
        if z is not None:
            try: rec[key]=typ(z)
            except Exception: rec[key+"_raw"]=z
    rec["evidence_lines"]=[x for x in out.splitlines() if x.startswith(("FREE_POINT:","SAT2_","TORSION_MATCH_22:","GROUP_IMAGE:","QX:","PULLBACK_X:"))]
    if status!="PASS_RETURN": rec["raw_tail"]=out[-3000:]
    records.append(rec); rawparts.append(f"===== branch={t['branch_id']} =====\n{out}\nERROR={err or ''}\n")
    print(json.dumps({"branch":t["branch_id"],"status":status,"rank":rec.get("rank_bounds"),"mode":rec.get("mode"),"candidate":rec.get("closure_candidate")},sort_keys=True))
raw="\n".join(rawparts); RAW.write_text(raw); cands=[r for r in records if r.get("closure_candidate") and r.get("index_coprime_2_proved")]
payload={"schema":"STAGE34_02B_D2_STAGEA2_GENUS2_RANKLE1_GAUSSIAN_RANK_INDEX_CHABAUTY_PROBE_V1","status":"DIAGNOSTIC_NO_CREDIT","input_representatives":2,"resolved_returns":sum(r["status"]=="PASS_RETURN" for r in records),"index_proved":sum(bool(r.get("index_coprime_2_proved")) for r in records),"closure_candidate_count":len(cands),"closure_candidate_branch_ids":[r["branch_id"] for r in cands],"records":records,"raw_stdout_sha256":hashlib.sha256(raw.encode()).hexdigest(),"credit":"Diagnostic only; exact rank, saturation/index, quotient completeness, and parent pullback require separate deterministic replay and hostile-audit promotion.","firewalls":{"diagnostic_candidate_is_parent_closure":False,"sign_partner_transfer_authoritative_before_audit":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n"); print("GAUSSIAN_RANK_INDEX="+json.dumps({k:payload[k] for k in ["resolved_returns","index_proved","closure_candidate_count","closure_candidate_branch_ids"]},sort_keys=True))
