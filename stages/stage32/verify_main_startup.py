#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
SYNC=HERE/"management/hpadj22-direct-full178/HPADJ22-V46-POSTMERGE-SUCCESSOR.json"
AUTHORITY=HERE/"management/hpadj22-direct-full178/verify_hpadj22_v46_postmerge_successor.py"
CONSUMER=HERE/"management/br204-current-authority/verify_br204_v46_current_authority_consumer_preflight.py"
GRF04_H22=HERE/"management/grf04-hpadj22-joint/verify_grf04_hpadj22_v46_e_independence_preflight.py"
COMMAND_SURFACE=HERE/"verify_command_surface.py"
def canonical(obj):
    body=dict(obj);body.pop("canonical_sha256_without_this_field",None);return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def replay(path):subprocess.run([sys.executable,str(path)],check=True)
def main():
    obj=json.loads(SYNC.read_text(encoding="utf-8"));print("V46_POSTMERGE_SYNC_CANONICAL_DIAGNOSTIC="+canonical(obj),flush=True);print("V46_POSTMERGE_SYNC_STORED_CANONICAL="+str(obj.get("canonical_sha256_without_this_field")),flush=True);replay(AUTHORITY);replay(CONSUMER);replay(GRF04_H22);replay(COMMAND_SURFACE);print("PASS: Stage32 MAIN V46 adopts merged V45 authority and retains BR204 plus GRF04xHPADJ22 preflights")
if __name__=="__main__":main()
