#!/usr/bin/env python3
import json
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
CODE = (ROOT / "magma_quartic_certificate.m").read_text(encoding="utf-8")
URL = "https://calc.magma-maths.org/execute"

req = urllib.request.Request(
    URL,
    data=json.dumps({"code": CODE}).encode("utf-8"),
    headers={"Content-Type": "application/json", "User-Agent": "perfect-cuboid-stage31/1.0"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=150) as resp:
    raw = resp.read().decode("utf-8")

payload = json.loads(raw)
(ROOT / "magma-response.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
(ROOT / "magma-stdout.txt").write_text(payload.get("stdout", ""), encoding="utf-8")

print(json.dumps({
    "success": payload.get("success"),
    "magma": payload.get("magma"),
    "warnings": payload.get("warnings"),
}, sort_keys=True))
print(payload.get("stdout", ""))

if not payload.get("success", False):
    raise SystemExit(1)
if "STAGE31_MAGMA_QUARTIC_CERTIFICATE_END" not in payload.get("stdout", ""):
    raise SystemExit("missing completion marker")
