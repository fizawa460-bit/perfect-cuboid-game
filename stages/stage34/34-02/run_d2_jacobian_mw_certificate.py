#!/usr/bin/env python3
import hashlib
import json
import pathlib
import re
import subprocess
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parent
OUT_JSON = ROOT / "d2-jacobian-mw-certificate.json"
OUT_TXT = ROOT / "d2-jacobian-mw-stdout.txt"

FIBERS = [
    (20,21),(80,39),(24,7),(84,13),(48,55),(20,99),(60,11)
]
SUCCESS = "The rank and full Mordell-Weil basis have been determined unconditionally."


def package_version():
    p = subprocess.run(["dpkg-query","-W","-f=${Version}","eclib-tools"], text=True, capture_output=True, check=True)
    return p.stdout.strip()


def jacobian_coefficients(a,b):
    q = Fraction(a,b)
    I = 16*(q**4 + 14*q*q + 1)
    J = 128*(q*q+1)*(q**4 - 34*q*q + 1)
    a4 = -I/Fraction(48)
    a6 = -J/Fraction(1728)
    return q,I,J,a4,a6


def parse_rank(text):
    vals = [int(x) for x in re.findall(r"\bRank\s*=\s*(\d+)", text)]
    if not vals:
        raise RuntimeError("could not parse mwrank rank")
    if len(set(vals)) != 1:
        raise RuntimeError(f"inconsistent rank lines: {vals}")
    return vals[0]


def last_o_line(text):
    c = [ln.strip().replace(" ","") for ln in text.splitlines() if ln.strip().startswith("[[")]
    return c[-1] if c else None

records=[]
raw=[]
for a,b in FIBERS:
    q,I,J,a4,a6 = jacobian_coefficients(a,b)
    model = f"[0,0,0,{a4},{a6}]\n"
    proc = subprocess.run(["mwrank","-q","-v","1","-o"], input=model, text=True, capture_output=True, timeout=240)
    text = proc.stdout + ("\nSTDERR:\n"+proc.stderr if proc.stderr else "")
    raw.append(f"===== q={a}/{b} =====\nMODEL={model.strip()}\n{text}")
    if proc.returncode != 0:
        raise SystemExit(f"mwrank failed q={a}/{b} rc={proc.returncode}")
    if SUCCESS not in text:
        raise SystemExit(f"unconditional full-basis success sentence missing q={a}/{b}")
    bad = [s for s in ["unable to saturate","saturation failed","conditional rank","not saturated"] if s in text.lower()]
    if bad:
        raise SystemExit(f"mwrank warning q={a}/{b}: {bad}")
    rank = parse_rank(text)
    records.append({
        "q": f"{a}/{b}",
        "binary_quartic_I": str(I),
        "binary_quartic_J": str(J),
        "jacobian_a4": str(a4),
        "jacobian_a6": str(a6),
        "rank": rank,
        "mwrank_o_line": last_o_line(text),
        "raw_section_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "unconditional_full_basis": True
    })

raw_text="\n".join(raw)
OUT_TXT.write_text(raw_text,encoding="utf-8")
payload={
    "schema":"STAGE34_02_D2_COMMON_JACOBIAN_MW_CERTIFICATE_V1",
    "status":"PASS_ECLIB_UNCONDITIONAL_COMMON_JACOBIAN_RANKS",
    "source":"stages/stage34/34-02/d2-split-genus1-quotient-lock.json",
    "software":{"package":"eclib-tools","package_version":package_version(),"command":"mwrank -q -v 1 -o"},
    "jacobian_convention":"y^2=x^3-(I/48)x-(J/1728)",
    "fibers":records,
    "raw_stdout_sha256":hashlib.sha256(raw_text.encode()).hexdigest(),
    "firewalls":{
        "rank_certificate_is_quartic_point_completeness":False,
        "common_jacobian_rank_is_genus5_cover_completion":False,
        "receiver_closed":False
    }
}
OUT_JSON.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"status":payload["status"],"ranks":{r["q"]:r["rank"] for r in records}},sort_keys=True))
