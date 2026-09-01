#!/usr/bin/env python3
import hashlib
import json
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER = "https://magma.maths.usyd.edu.au/calc/"
CASES = [(20,21,29),(80,39,89),(24,7,25),(84,13,85),(48,55,73),(20,99,101),(60,11,61)]


def code_for(a,b,c,d):
    if d == 1:
        quartic = "(1+q^2)*t^4 + 8*q*t^3 + 2*(1+q^2)*t^2 - 8*q*t + (1+q^2)"
        point = "C![1, 2*r, 1]"
        pminus = "C![1, -2*r, 1]"
        testpoint = "C![0, r, 1]"
    else:
        quartic = "4*(q+1)^2*t^4 - 8*(q+1)^2*t^3 + 8*(1+q^2)*t^2 - 4*(q-1)^2*t + (q-1)^2"
        point = "C![0, q-1, 1]"
        pminus = "C![0, 1-q, 1]"
        testpoint = "C![1, q-1, 1]"
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ := Rationals();\nQt<t> := PolynomialRing(Q);\nq := Q!{a}/Q!{b};\nr := Q!{c}/Q!{b};\nassert r^2 eq 1+q^2;\nf := {quartic};\nC := HyperellipticCurve(f);\nP := {point};\nPm := {pminus};\nT := {testpoint};\nassert Genus(C) eq 1;\nassert P in C and Pm in C and T in C;\nE, phi := EllipticCurve(C, P);\nII := 16*(q^4+14*q^2+1);\nJJ := 128*(q^2+1)*(q^4-34*q^2+1);\nJq := EllipticCurve([Q|0,0,0,-II/48,-JJ/1728]);\nok, iso := IsIsomorphic(E,Jq); assert ok;\nokinv, psi := IsInvertible(phi); assert okinv;\nphiext := Extend(phi);\npsiext := Extend(psi);\nassert IsRegular(phiext);\nassert IsRegular(psiext);\nassert phiext(P) eq E!0;\nassert psiext(E!0) eq P;\nQtst := phiext(T); assert psiext(Qtst) eq T;\nQminus := phiext(Pm); assert psiext(Qminus) eq Pm;\nfw := DefiningPolynomials(phi);\ninv := InverseDefiningPolynomials(phi);\nbaseeq := DefiningPolynomials(BaseScheme(phi));\nibaseeq := DefiningPolynomials(BaseScheme(psi));\nextbase := DefiningPolynomials(BaseScheme(phiext));\niextbase := DefiningPolynomials(BaseScheme(psiext));\nprint \"STAGE34_D2_MAP_BEGIN q={a}/{b} d={d}\";\nprint \"E_AINVARIANTS:\", aInvariants(E);\nprintf \"FORWARD_COUNT: %o\\n\", #fw; for i in [1..#fw] do printf \"FORWARD_POLY_%o: %o\\n\",i,fw[i]; end for;\nprintf \"INVERSE_COUNT: %o\\n\", #inv; for i in [1..#inv] do printf \"INVERSE_POLY_%o: %o\\n\",i,inv[i]; end for;\nprint \"ISO_DATA_TO_JQ:\", IsomorphismData(iso);\nprintf \"BASE_EQ_COUNT: %o\\n\",#baseeq; for i in [1..#baseeq] do printf \"BASE_EQ_%o: %o\\n\",i,baseeq[i]; end for;\nprintf \"INVERSE_BASE_EQ_COUNT: %o\\n\",#ibaseeq; for i in [1..#ibaseeq] do printf \"INVERSE_BASE_EQ_%o: %o\\n\",i,ibaseeq[i]; end for;\nprintf \"EXTENDED_BASE_EQ_COUNT: %o\\n\",#extbase; for i in [1..#extbase] do printf \"EXTENDED_BASE_EQ_%o: %o\\n\",i,extbase[i]; end for;\nprintf \"EXTENDED_INVERSE_BASE_EQ_COUNT: %o\\n\",#iextbase; for i in [1..#iextbase] do printf \"EXTENDED_INVERSE_BASE_EQ_%o: %o\\n\",i,iextbase[i]; end for;\nprint \"SELECTED_BASE_POINT:\",P;\nprint \"CONJUGATE_POINT:\",Pm;\nprint \"CONJUGATE_IMAGE_E:\",Qminus;\nprint \"TEST_POINT:\",T;\nprint \"TEST_IMAGE_E:\",Qtst;\nprint \"ORIGIN_INVERSE_EXTENSION:\",psiext(E!0);\nprint \"FORWARD_EXTENDED_REGULAR: true\";\nprint \"INVERSE_EXTENDED_REGULAR: true\";\nprint \"ROUNDTRIP_SELECTED_BASE_PASS: true\";\nprint \"ROUNDTRIP_CONJUGATE_PASS: true\";\nprint \"ROUNDTRIP_TEST_PASS: true\";\nprint \"STAGE34_D2_MAP_END q={a}/{b} d={d}\";\n'''


def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-d2/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=150) as resp: rawb=resp.read(); status=resp.status
    raw=rawb.decode("utf-8",errors="replace"); root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"): lines.append("".join(line.itertext()))
    stdout="\n".join(lines)+("\n" if lines else "")
    return status,raw,stdout


def value_after(prefix,stdout):
    for line in stdout.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    raise RuntimeError("missing "+prefix)


def numbered(prefix,count_prefix,stdout):
    n=int(value_after(count_prefix,stdout)); return [value_after(f"{prefix}_{i}:",stdout) for i in range(1,n+1)]

records=[]; raws=[]
for a,b,c in CASES:
  for d in (1,2):
    status,raw,stdout=submit(code_for(a,b,c,d)); begin=f"STAGE34_D2_MAP_BEGIN q={a}/{b} d={d}"; end=f"STAGE34_D2_MAP_END q={a}/{b} d={d}"
    if status!=200 or begin not in stdout or end not in stdout or any(x in stdout for x in ("Runtime error","Internal error","User error","Assertion failed")):
        raise SystemExit(f"Magma map case failed q={a}/{b} d={d} status={status}\n{stdout}")
    for marker in ("FORWARD_EXTENDED_REGULAR: true","INVERSE_EXTENDED_REGULAR: true","ROUNDTRIP_SELECTED_BASE_PASS: true","ROUNDTRIP_CONJUGATE_PASS: true","ROUNDTRIP_TEST_PASS: true"):
        if marker not in stdout: raise SystemExit(f"marker missing q={a}/{b} d={d}: {marker}")
    raws.append(f"===== q={a}/{b} d={d} =====\n{stdout}")
    records.append({"q":f"{a}/{b}","d":d,"magma_elliptic_a_invariants":value_after("E_AINVARIANTS:",stdout),"forward_polynomials":numbered("FORWARD_POLY","FORWARD_COUNT:",stdout),"inverse_polynomials":numbered("INVERSE_POLY","INVERSE_COUNT:",stdout),"isomorphism_data_to_common_Jq":value_after("ISO_DATA_TO_JQ:",stdout),"naive_forward_base_scheme_equations":numbered("BASE_EQ","BASE_EQ_COUNT:",stdout),"naive_inverse_base_scheme_equations":numbered("INVERSE_BASE_EQ","INVERSE_BASE_EQ_COUNT:",stdout),"extended_forward_base_scheme_equations":numbered("EXTENDED_BASE_EQ","EXTENDED_BASE_EQ_COUNT:",stdout),"extended_inverse_base_scheme_equations":numbered("EXTENDED_INVERSE_BASE_EQ","EXTENDED_INVERSE_BASE_EQ_COUNT:",stdout),"selected_base_point":value_after("SELECTED_BASE_POINT:",stdout),"conjugate_point":value_after("CONJUGATE_POINT:",stdout),"conjugate_image_E":value_after("CONJUGATE_IMAGE_E:",stdout),"test_point":value_after("TEST_POINT:",stdout),"test_image_E":value_after("TEST_IMAGE_E:",stdout),"origin_inverse_extension":value_after("ORIGIN_INVERSE_EXTENSION:",stdout),"forward_extended_regular":True,"inverse_extended_regular":True,"roundtrip_selected_base":True,"roundtrip_conjugate":True,"roundtrip_test":True,"raw_stdout_sha256":hashlib.sha256(stdout.encode()).hexdigest(),"raw_xml_sha256":hashlib.sha256(raw.encode()).hexdigest()})
rawtext="\n".join(raws); (ROOT/"d2-quartic-map-stdout.txt").write_text(rawtext)
payload={"schema":"STAGE34_02_D2_EXPLICIT_QUARTIC_JACOBIAN_MAP_CERTIFICATE_V4","status":"PASS_14_OF_14_REGULAR_EXTENSIONS_AND_ROUNDTRIP","source":"stages/stage34/34-02/d2-split-genus1-quotient-lock.json","protocol":"official-magma-xml-calculator","magma_intrinsics":["EllipticCurve(C,P)","IsInvertible","Extend","IsRegular","BaseScheme","IsIsomorphic","IsomorphismData"],"cases":records,"case_count":len(records),"raw_stdout_sha256":hashlib.sha256(rawtext.encode()).hexdigest(),"firewalls":{"regular_birational_isomorphisms_are_quartic_point_completeness":False,"full_jacobian_MW_basis_plus_isomorphisms_is_cover_point_completeness":False,"receiver_closed":False}}
(ROOT/"d2-quartic-map-certificate.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"case_count":len(records)},sort_keys=True))
