#!/usr/bin/env python3
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
# Representative compact child uses the smallest retained exact partition identity.
# This is a format/retention measurement only; it performs no heavy enumeration and earns no credit.
payload={
 "schema":"STAGE32_BR204_G4_COMPACT_CHILD_CERT_V1",
 "target":{"b":0,"d":102},"partition":{"kind":"BC16","child_index":0},
 "status":"REPRESENTATIVE_FORMAT_MEASUREMENT_ONLY",
 "commitments":{"state_count":"0","mass":"0","canonical_payload_sha256":"0"*64},
 "source":{"plan_blob":"3e6239b7e2aeae24ed3f1184e767fc1c7811b5f8","runkey_blob":"3f1d20aadd66d8b2294223b46993232e1db15de2"},
 "credit":False
}
raw=(json.dumps(payload,sort_keys=True,separators=(",",":"))+"\n").encode()
out=ROOT/"BR204-G4-REPRESENTATIVE-COMPACT-CHILD.json"
out.write_bytes(raw)
receipt={"schema":"STAGE32_BR204_G4_REPRESENTATIVE_STORAGE_MEASUREMENT_V1","payload_path":out.name,"payload_bytes":len(raw),"payload_sha256":hashlib.sha256(raw).hexdigest(),"hard_cap_bytes":65536,"within_hard_cap":len(raw)<=65536,"measurement_scope":"FORMAT_AND_RETENTION_ONLY__NO_MATHEMATICAL_CREDIT"}
(ROOT/"BR204-G4-REPRESENTATIVE-STORAGE-MEASUREMENT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,sort_keys=True))
