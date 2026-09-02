#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-genus2-rankle1-gaussian-6b-shainfo-lock.json"
OUT=ROOT/"d2-stageA2-genus2-rankle1-gaussian-6b-shainfo-probe.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-gaussian-6b-shainfo-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"; REFERER="https://magma.maths.usyd.edu.au/calc/"; TIMEOUT=900

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-gaussian-6b-shainfo/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:
        raw=resp.read().decode("utf-8",errors="replace"); status=resp.status
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
    return f'''SetColumns(0); SetQuitOnError(true);\nQ:=Rationals(); Qz<z>:=PolynomialRing(Q); K<ii>:=NumberField(z^2+1);\nE<EX,EY,EZ>:=EllipticCurve([K|0,{a2},0,{a4},0]); assert Discriminant(E) ne 0;\nprint \"BEGIN branch={t['branch_id']}\";\nrb,gens,sha:=MordellWeilShaInformation(E : ShaInfo:=true, Effort:=3, Silent:=true);\nprint \"MWSHA_RANK_BOUNDS:\",rb; print \"MWSHA_GENERATOR_COUNT:\",#gens; print \"MWSHA_SHA_INFO:\",sha;\nT,tm:=TorsionSubgroup(E); tinv:=Invariants(T); print \"TORSION_INVARIANTS:\",tinv;\nmode:=\"UNRESOLVED\"; complete_index:=false; Vset:={{}}; RR:=1;\nP1:=ProjectiveSpace(Q,1); pi:=map< E -> P1 | [EX,EZ] >; pie:=Extend(pi);\nif #rb eq 2 and rb[1] eq 0 and rb[2] eq 0 then\n  mode:=\"RANK0_TORSION_FULL\"; complete_index:=true; Vset:={{t : t in T}}; print \"ENUM_GROUP_COUNT:\",#Vset;\nelif #rb eq 2 and rb[1] eq 1 and rb[2] eq 1 and #gens ge 1 then\n  free:=[P : P in gens | Order(P) eq 0]; print \"MWSHA_FREE_GENERATOR_COUNT:\",#free;\n  if #free ge 1 then\n    SP:=Saturation([free[1]],2 : TorsionFree:=true); print \"SAT2_COUNT:\",#SP; assert #SP eq 1; QP:=SP[1]; print \"SAT2_POINT:\",QP;\n    if tinv eq [2,2] then\n      H:=AbelianGroup([2,2,0]); T1:=tm(T.1); T2:=tm(T.2);\n      hm:=map< H -> E | h :-> (Integers()!Eltseq(h)[1])*T1 + (Integers()!Eltseq(h)[2])*T2 + (Integers()!Eltseq(h)[3])*QP >;\n      VV,RR:=Chabauty(hm,pi : IndexBound:=2); Vset:=VV; complete_index:=true; mode:=\"RANK1_SAT2_ELLCHAB\"; print \"ELLCHAB_R:\",RR; print \"ELLCHAB_COUNT:\",#Vset;\n    end if;\n  end if;\nend if;\nprint \"MODE:\",mode; print \"INDEX_COPRIME_2_PROVED:\",complete_index;\nquotient_rational_x:=0; reconstructed_C_x:=0; nondeg_parent:=0;\nif mode eq \"RANK0_TORSION_FULL\" then\n  for g in Vset do\n    Pcur:=tm(g); im:=pie(Pcur); print \"GROUP_IMAGE:\",g,\" -> \",im;\n    if im[2] ne 0 then\n      kval:=im[1]/im[2]; ok,qx:=IsCoercible(Q,kval);\n      if ok then\n        quotient_rational_x +:= 1; uu:=qx/({A}); ds:=uu^2+4; sq,sd:=IsSquare(ds); print \"QX:\",qx,\" U:\",uu,\" XDISCR_SQUARE:\",sq;\n        if sq then\n          for xx in [(uu+sd)/2,(uu-sd)/2] do\n            ff:=({c})*xx*(xx^2-1)*(xx+({n}))*(({n})*xx-1); cpt,yy:=IsSquare(ff);\n            U:=xx^2-1; Vform:=2*xx; AA:={a}*U+{b}*Vform; BB:={b}*U+{a}*Vform; deg:=U eq 0 or Vform eq 0 or AA eq 0 or BB eq 0;\n            sU:=IsSquare(U/({d[0]})); sV:=IsSquare(Vform/({d[1]})); sA:=IsSquare(AA/({d[2]})); sB:=IsSquare(BB/({d[3]})); parent:=cpt and sU and sV and sA and sB;\n            if cpt then reconstructed_C_x +:= 1; end if; if parent and not deg then nondeg_parent +:= 1; end if;\n            print \"PULLBACK_X:\",xx,\" C_POINT:\",cpt,\" DEG:\",deg,\" PARENT:\",parent,\" SQ_UVAB:\",sU,sV,sA,sB;\n          end for;\n        end if;\n      end if;\n    end if;\n  end for;\nelif mode eq \"RANK1_SAT2_ELLCHAB\" then\n  for g in Vset do\n    Pcur:=hm(g); im:=pie(Pcur); print \"GROUP_IMAGE:\",g,\" -> \",im;\n    if im[2] ne 0 then\n      kval:=im[1]/im[2]; ok,qx:=IsCoercible(Q,kval);\n      if ok then\n        quotient_rational_x +:= 1; uu:=qx/({A}); ds:=uu^2+4; sq,sd:=IsSquare(ds); print \"QX:\",qx,\" U:\",uu,\" XDISCR_SQUARE:\",sq;\n        if sq then\n          for xx in [(uu+sd)/2,(uu-sd)/2] do\n            ff:=({c})*xx*(xx^2-1)*(xx+({n}))*(({n})*xx-1); cpt,yy:=IsSquare(ff);\n            U:=xx^2-1; Vform:=2*xx; AA:={a}*U+{b}*Vform; BB:={b}*U+{a}*Vform; deg:=U eq 0 or Vform eq 0 or AA eq 0 or BB eq 0;\n            sU:=IsSquare(U/({d[0]})); sV:=IsSquare(Vform/({d[1]})); sA:=IsSquare(AA/({d[2]})); sB:=IsSquare(BB/({d[3]})); parent:=cpt and sU and sV and sA and sB;\n            if cpt then reconstructed_C_x +:= 1; end if; if parent and not deg then nondeg_parent +:= 1; end if;\n            print \"PULLBACK_X:\",xx,\" C_POINT:\",cpt,\" DEG:\",deg,\" PARENT:\",parent,\" SQ_UVAB:\",sU,sV,sA,sB;\n          end for;\n        end if;\n      end if;\n    end if;\n  end for;\nend if;\nif complete_index then\n  print \"QUOTIENT_RATIONAL_X_COUNT:\",quotient_rational_x; print \"RECONSTRUCTED_C_X_COUNT_WITH_MULTIPLICITY:\",reconstructed_C_x; print \"NONDEGENERATE_FULL_PARENT_LIFT_COUNT:\",nondeg_parent; print \"CLOSURE_CANDIDATE:\",nondeg_parent eq 0;\nelse\n  print \"CLOSURE_CANDIDATE: false\";\nend if;\nprint \"END branch={t['branch_id']}\";\n'''

d=json.loads(LOCK.read_text()); t=d["target"]
out=""; err=None; status="UNRESOLVED_RESOURCE_OR_EXTERNAL_WALL"
try:
    http,out=submit(code_for(t)); bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
    if http==200 and f"END branch={t['branch_id']}" in out and not bad: status="PASS_RETURN"
    else: err=f"http={http} malformed_or_magma_error"
except Exception as ex: err=f"{type(ex).__name__}: {ex}"
RAW.write_text(out)
rec={"branch_id":t["branch_id"],"status":status,"error":err,"stdout_sha256":hashlib.sha256(out.encode()).hexdigest(),"rank_bounds":val("MWSHA_RANK_BOUNDS:",out,False),"generator_count":val("MWSHA_GENERATOR_COUNT:",out,False),"sha_info":val("MWSHA_SHA_INFO:",out,False),"torsion_invariants":val("TORSION_INVARIANTS:",out,False),"mode":val("MODE:",out,False)}
for pfx,key,typ in [("INDEX_COPRIME_2_PROVED:","index_coprime_2_proved",lambda s:s=="true"),("ELLCHAB_R:","ellchab_R",int),("ELLCHAB_COUNT:","ellchab_count",int),("QUOTIENT_RATIONAL_X_COUNT:","quotient_rational_x_count",int),("RECONSTRUCTED_C_X_COUNT_WITH_MULTIPLICITY:","reconstructed_C_x_count_with_multiplicity",int),("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:","nondegenerate_full_parent_lift_count",int),("CLOSURE_CANDIDATE:","closure_candidate",lambda s:s=="true")]:
    z=val(pfx,out,False)
    if z is not None:
        try: rec[key]=typ(z)
        except Exception: rec[key+"_raw"]=z
rec["evidence_lines"]=[x for x in out.splitlines() if x.startswith(("SAT2_","GROUP_IMAGE:","QX:","PULLBACK_X:"))]
if status!="PASS_RETURN": rec["raw_tail"]=out[-4000:]
payload={"schema":"STAGE34_02B_D2_STAGEA2_GENUS2_RANKLE1_GAUSSIAN_6B_SHAINFO_PROBE_V1","status":"DIAGNOSTIC_NO_CREDIT","record":rec,"raw_stdout_sha256":hashlib.sha256(out.encode()).hexdigest(),"credit":"Diagnostic only; exact rank and finite pullback require separate deterministic proof replay and hostile-audit promotion.","firewalls":{"rank_bounds_0_1_implies_rank_zero":False,"diagnostic_candidate_is_parent_closure":False,"sign_partner_transfer_authoritative_before_audit":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("GAUSSIAN_6B_SHAINFO="+json.dumps({"status":status,"rank_bounds":rec.get("rank_bounds"),"mode":rec.get("mode"),"candidate":rec.get("closure_candidate")},sort_keys=True))
