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
CASES = [
    (20,21,29),(80,39,89),(24,7,25),(84,13,85),(48,55,73),(20,99,101),(60,11,61)
]


def code_for(a,b,c,d):
    if d == 1:
        quartic = "(1+q^2)*t^4 + 8*q*t^3 + 2*(1+q^2)*t^2 - 8*q*t + (1+q^2)"
        point = f"C![1, 2*(Q!{c}/Q!{b}), 1]"
    else:
        quartic = "4*(q+1)^2*t^4 - 8*(q+1)^2*t^3 + 8*(1+q^2)*t^2 - 4*(q-1)^2*t + (q-1)^2"
        point = "C![0, q-1, 1]"
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ := Rationals();\nQt<t> := PolynomialRing(Q);\nq := Q!{a}/Q!{b};\nf := {quartic};\nC := HyperellipticCurve(f);\nP := {point};\nassert Genus(C) eq 1;\nE, phi := EllipticCurve(C, P);\nII := 16*(q^4+14*q^2+1);\nJJ := 128*(q^2+1)*(q^4-34*q^2+1);\nJq := EllipticCurve([Q|0,0,0,-II/48,-JJ/1728]);\nok, iso := IsIsomorphic(E,Jq);\nassert ok;\nassert phi(P) eq E!0;\nfw := DefiningPolynomials(phi);\ninv := InverseDefiningPolynomials(phi);\nbaseeq := DefiningPolynomials(BaseScheme(phi));\nassert #fw gt 0 and #inv gt 0;\nprint \"STAGE34_D2_MAP_BEGIN q={a}/{b} d={d}\";\nprint \"E_AINVARIANTS:\", aInvariants(E);\nprintf \"FORWARD_COUNT: %o\\n\", #fw;\nfor i in [1..#fw] do printf \"FORWARD_POLY_%o: %o\\n\", i, fw[i]; end for;\nprintf \"INVERSE_COUNT: %o\\n\", #inv;\nfor i in [1..#inv] do printf \"INVERSE_POLY_%o: %o\\n\", i, inv[i]; end for;\nprint \"ISO_DATA_TO_JQ:\", IsomorphismData(iso);\nprintf \"BASE_EQ_COUNT: %o\\n\", #baseeq;\nfor i in [1..#baseeq] do printf \"BASE_EQ_%o: %o\\n\", i, baseeq[i]; end for;\nprint \"STAGE34_D2_MAP_END q={a}/{b} d={d}\";\n'''


def submit(code):
    data = urllib.parse.urlencode({"input": code}).encode("utf-8")
    req = urllib.request.Request(
        URL,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html, application/xml, application/xhtml+xml",
            "Referer": REFERER,
            "User-Agent": "perfect-cuboid-stage34-d2/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=150) as resp:
        raw_bytes = resp.read()
        status = resp.status
    raw = raw_bytes.decode("utf-8", errors="replace")
    root = ET.fromstring(raw)
    lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):
            lines.append("".join(line.itertext()))
    stdout="\n".join(lines)
    if stdout and not stdout.endswith("\n"):
        stdout += "\n"
    return status, raw, stdout


def value_after(prefix, stdout):
    for line in stdout.splitlines():
        if line.startswith(prefix):
            return line[len(prefix):].strip()
    raise RuntimeError(f"missing {prefix}")


def numbered(prefix, count_prefix, stdout):
    n=int(value_after(count_prefix,stdout))
    return [value_after(f"{prefix}_{i}:",stdout) for i in range(1,n+1)]

records=[]
raw_sections=[]
for a,b,c in CASES:
    for d in (1,2):
        code=code_for(a,b,c,d)
        status, raw_xml, stdout = submit(code)
        begin=f"STAGE34_D2_MAP_BEGIN q={a}/{b} d={d}"
        end=f"STAGE34_D2_MAP_END q={a}/{b} d={d}"
        if status != 200 or begin not in stdout or end not in stdout:
            raise SystemExit(f"Magma map case failed q={a}/{b} d={d} status={status}\n{stdout}")
        if any(x in stdout for x in ("Runtime error","Internal error","User error","Assertion failed")):
            raise SystemExit(f"Magma runtime error q={a}/{b} d={d}\n{stdout}")
        raw_sections.append(f"===== q={a}/{b} d={d} =====\n{stdout}")
        fw=numbered("FORWARD_POLY","FORWARD_COUNT:",stdout)
        inv=numbered("INVERSE_POLY","INVERSE_COUNT:",stdout)
        base=numbered("BASE_EQ","BASE_EQ_COUNT:",stdout)
        if any(x == "[" for x in fw+inv+base):
            raise SystemExit(f"truncated polynomial parse q={a}/{b} d={d}")
        records.append({
            "q":f"{a}/{b}",
            "d":d,
            "magma_elliptic_a_invariants":value_after("E_AINVARIANTS:",stdout),
            "forward_polynomials":fw,
            "inverse_polynomials":inv,
            "isomorphism_data_to_common_Jq":value_after("ISO_DATA_TO_JQ:",stdout),
            "forward_base_scheme_equations":base,
            "base_point_sent_to_origin":True,
            "raw_stdout_sha256":hashlib.sha256(stdout.encode()).hexdigest(),
            "raw_xml_sha256":hashlib.sha256(raw_xml.encode()).hexdigest()
        })

raw_text="\n".join(raw_sections)
(ROOT/"d2-quartic-map-stdout.txt").write_text(raw_text,encoding="utf-8")
payload={
    "schema":"STAGE34_02_D2_EXPLICIT_QUARTIC_JACOBIAN_MAP_CERTIFICATE_V2",
    "status":"PASS_MAGMA_EXPLICIT_BIRATIONAL_MAPS_TO_COMMON_JACOBIANS_SELF_CONTAINED",
    "source":"stages/stage34/34-02/d2-split-genus1-quotient-lock.json",
    "protocol":"official-magma-xml-calculator",
    "magma_intrinsics":["EllipticCurve(C,P)","DefiningPolynomials","InverseDefiningPolynomials","IsIsomorphic","IsomorphismData","BaseScheme"],
    "cases":records,
    "case_count":len(records),
    "raw_stdout_sha256":hashlib.sha256(raw_text.encode()).hexdigest(),
    "firewalls":{
        "explicit_birational_maps_are_quartic_point_completeness":False,
        "common_jacobian_full_MW_basis_plus_maps_is_cover_point_completeness":False,
        "receiver_closed":False
    }
}
(ROOT/"d2-quartic-map-certificate.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"status":payload["status"],"case_count":len(records)},sort_keys=True))
