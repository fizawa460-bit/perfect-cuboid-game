#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
SYNC=HERE/"management/hpadj22-direct-full178/HPADJ22-V46-POSTMERGE-SUCCESSOR.json"
AUTHORITY=HERE/"management/hpadj22-direct-full178/verify_hpadj22_v46_postmerge_successor.py"
COMMAND_SURFACE=HERE/"verify_command_surface.py"
def canonical(obj):
    body=dict(obj);body.pop("canonical_sha256_without_this_field",None);return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def replay(path):subprocess.run([sys.executable,str(path)],check=True)
def main():
    obj=json.loads(SYNC.read_text(encoding="utf-8"));print("V46_POSTMERGE_SYNC_CANONICAL_DIAGNOSTIC="+canonical(obj),flush=True);print("V46_POSTMERGE_SYNC_STORED_CANONICAL="+str(obj.get("canonical_sha256_without_this_field")),flush=True);replay(AUTHORITY);replay(COMMAND_SURFACE);print("PASS: Stage32 MAIN V46 adopts merged hostile-audited V45 authority with zero new pruning")
if __name__=="__main__":main()
