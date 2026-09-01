#!/usr/bin/env python3
import hashlib, json, pathlib, urllib.parse, urllib.request, xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parent
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"
CASES=[(20,21,29),(80,39,89),(24,7,25),(84,13,85),(48,55,73),(20,99,101),(60,11,61)]

def code_for(a,b,c,d):
    if d==1:
        quartic="(1+q^2)*t^4+8*q*t^3+2*(1+q^2)*t^2-8*q*t+(1+q^2)"
        P=f"C![1,2*(Q!{c}/Q!{b}),1]"
        Pm=f"C![1,-2*(Q!{c}/Q!{b}),1]"
    else:
        quartic="4*(q+1)^2*t^4-8*(q+1)^2*t^3+8*(1+q^2)*t^2-4*(q-1)^2*t+(q-1)^2"
        P="C![0,q-1,1]"
        Pm="C![0,1-q,1]"
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ:=Rationals(); Qt<t>:=PolynomialRing(Q); q:=Q!{a}/Q!{b};\nf:={quartic}; C:=HyperellipticCurve(f); P:={P}; Pm:={Pm};\nassert P in C and Pm in C;\nE,phi:=EllipticCurve(C,P);\nassert EvaluateByPowerSeries(phi,P) eq E!0;\nQm:=EvaluateByPowerSeries(phi,Pm);\nprint \"BEGIN q={a}/{b} d={d}\";\nprint \"E_AINV:\",aInvariants(E);\nprint \"CONJUGATE_IMAGE:\",Qm;\nprint \"CONJUGATE_IMAGE_ORDER2:\",2*Qm eq E!0;\nprint \"END q={a}/{b} d={d}\";\n'''

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-d2-conjugate/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=150) as resp: raw=resp.read().decode("utf-8",errors="replace"); status=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"): lines.append("".join(line.itertext()))
    out="\n".join(lines)+("\n" if lines else "")
    return status,raw,out

def val(prefix,out):
    for line in out.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    raise RuntimeError(prefix)

records=[]; rawparts=[]
for a,b,c in CASES:
    for d in (1,2):
        status,raw,out=submit(code_for(a,b,c,d))
        if status!=200 or f"END q={a}/{b} d={d}" not in out or any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error")):
            raise SystemExit(f"failed q={a}/{b} d={d}\n{out}")
        image=val("CONJUGATE_IMAGE:",out); ord2=val("CONJUGATE_IMAGE_ORDER2:",out)
        if ord2!="true": raise SystemExit(f"conjugate image not 2-torsion q={a}/{b} d={d}: {image}")
        records.append({"q":f"{a}/{b}","d":d,"magma_E_a_invariants":val("E_AINV:",out),"conjugate_image":image,"order2":True,"stdout_sha256":hashlib.sha256(out.encode()).hexdigest()})
        rawparts.append(f"===== q={a}/{b} d={d} =====\n{out}")
raw="\n".join(rawparts)
payload={"schema":"STAGE34_02_D2_CONJUGATE_EXCEPTION_CERTIFICATE_V1","status":"PASS_14_OF_14_FORWARD_POWER_SERIES_CONJUGATE_IMAGES","protocol":"official-magma-xml-calculator","cases":records,"raw_stdout_sha256":hashlib.sha256(raw.encode()).hexdigest(),"firewalls":{"conjugate_image_certificate_is_matching_x_closure":False,"receiver_closed":False}}
(ROOT/"d2-conjugate-exception-certificate.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
(ROOT/"d2-conjugate-exception-stdout.txt").write_text(raw)
print(json.dumps({"status":payload["status"],"cases":14},sort_keys=True))
