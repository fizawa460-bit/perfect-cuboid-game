#!/usr/bin/env python3
"""Retain the minimal exact Stage32 marking needed for Stage33 swap recovery."""
import argparse
import base64
import hashlib
import json
import pathlib
import zlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "stage32_picard_marking_retained.py"
ARTIFACT_ID = 9588229672
ARTIFACT_ZIP_SHA256 = "6e4e6e5350717296f0e76e5c972e945b72a61d32e039718a535e245826b5b159"
CORE_SHA256 = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
AUT_SHA256 = "50515608f546b85b19bf828103f9cfbfdf4ef4df490ed7fab19f2cdcb43d602d"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("content", type=pathlib.Path)
args = ap.parse_args()
hperp = (args.content / "d16-hperp.txt").read_text(encoding="utf-8")
aut_text = (args.content / "d16-aut-action.json").read_text(encoding="utf-8")
aut = json.loads(aut_text)
if hperp.splitlines()[:2] != ["S32_D16_AUT_CANON_HPERP_V1", CORE_SHA256]:
    raise SystemExit("Stage32 Hperp/core lock moved")
if aut.get("canonical_sha256_without_this_field") != AUT_SHA256:
    raise SystemExit("Stage32 Aut lock moved")
unsigned = dict(aut)
claimed = unsigned.pop("canonical_sha256_without_this_field")
if csha(unsigned) != claimed:
    raise SystemExit("Stage32 Aut canonical hash mismatch")

payload = {
    "schema": "STAGE33_07_RETAINED_STAGE32_PICARD_MARKING_V1",
    "source_artifact": {
        "artifact_id": ARTIFACT_ID,
        "artifact_zip_sha256": ARTIFACT_ZIP_SHA256,
        "workflow_run": 32915934318,
        "source_head_sha": "96a17a8f42480f58652a023c31ea4705c5d5c973",
    },
    "stage32_picard_core_sha256": CORE_SHA256,
    "stage32_aut_action_sha256": AUT_SHA256,
    "hperp_text_sha256": hashlib.sha256(hperp.encode()).hexdigest(),
    "aut_text_sha256": hashlib.sha256(aut_text.encode()).hexdigest(),
    "hperp_text": hperp,
    "aut_action": aut,
}
payload["canonical_sha256"] = csha(payload)
encoded = base64.b85encode(zlib.compress(
    json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(), 9
)).decode()
lines = [encoded[i:i + 100] for i in range(0, len(encoded), 100)]
source = '''#!/usr/bin/env python3
"""Nonexpiring retained Stage32 Picard marking for Stage33-07."""
import base64,hashlib,json,zlib
PAYLOAD=b"""%s"""
LOCK=%r
def load():
 x=json.loads(zlib.decompress(base64.b85decode(b"".join(PAYLOAD.split()))))
 y=dict(x);claimed=y.pop("canonical_sha256")
 got=hashlib.sha256(json.dumps(y,sort_keys=True,separators=(",", ":")).encode()).hexdigest()
 if claimed!=LOCK or got!=LOCK:raise RuntimeError("retained Stage32 Picard marking lock mismatch")
 return x
if __name__=="__main__":
 x=load();print(json.dumps({"success":True,"canonical_sha256":x["canonical_sha256"],"core_sha256":x["stage32_picard_core_sha256"],"aut_sha256":x["stage32_aut_action_sha256"]},indent=2,sort_keys=True))
''' % ("\n".join(lines), payload["canonical_sha256"])
OUT.write_text(source, encoding="utf-8")
print(json.dumps({
    "success": True,
    "retained_bundle_sha256": payload["canonical_sha256"],
    "hperp_bytes": len(hperp.encode()),
    "aut_bytes": len(aut_text.encode()),
    "encoded_bytes": len(encoded),
}, indent=2, sort_keys=True))
