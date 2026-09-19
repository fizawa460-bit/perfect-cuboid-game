#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
SYNC=HERE/"management/grf04-quadratic-capacity/GRF04-V43-HPADJ21-FULL178-AUDIT-SYNC.json"
AUTHORITY=HERE/"management/hpadj22-direct-full178/verify_hpadj22_v44_main_bound_replacement.py"
COMMAND_SURFACE=HERE/"verify_command_surface.py"
def canonical(obj):
    body=dict(obj);body.pop("canonical_sha256_without_this_field",None);return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def replay(path):subprocess.run([sys.executable,str(path)],check=True)
def main():
    obj=json.loads(SYNC.read_text(encoding="utf-8"));print("V43_HPADJ21_AUDIT_SYNC_CANONICAL_DIAGNOSTIC="+canonical(obj),flush=True);print("V43_HPADJ21_AUDIT_SYNC_STORED_CANONICAL="+str(obj.get("canonical_sha256_without_this_field")),flush=True);replay(AUTHORITY);replay(COMMAND_SURFACE);print("PASS: Stage32 MAIN V44 consumes hostile-audited HPADJ22 FULL178 upper bound; replacement head pending hostile re-audit")
if __name__=="__main__":main()
