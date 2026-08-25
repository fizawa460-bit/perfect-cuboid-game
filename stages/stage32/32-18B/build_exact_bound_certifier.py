#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, pathlib

EXPECTED_SOURCE_SHA256 = "cb1b7b47c7a03c8bab243e867cb5fecac38643b3"
OLD_SCHEMA = "STAGE32_18A_D16_EXACT_B6_TRAVERSAL_CERT_V1"
NEW_SCHEMA = "STAGE32_18B_D16_EXACT_BOUNDED_TRAVERSAL_CERT_V1"
OLD_LOCK = '        if(bound!=6) throw std::runtime_error("Stage32-18A certifier is intentionally locked to b6");\n'

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",type=pathlib.Path,required=True)
    ap.add_argument("--output",type=pathlib.Path,required=True)
    args=ap.parse_args()
    raw=args.source.read_bytes()
    sha=hashlib.sha1(raw).hexdigest()
    # Git blob SHA is not a plain file hash; lock the repository blob identity separately in CI.
    text=raw.decode()
    if text.count(OLD_SCHEMA)!=1:
        raise RuntimeError("unexpected 18A schema occurrence count")
    if text.count(OLD_LOCK)!=1:
        raise RuntimeError("unexpected 18A b6 lock occurrence count")
    text=text.replace(OLD_SCHEMA,NEW_SCHEMA)
    text=text.replace(OLD_LOCK,"")
    text=text.replace(
        '"TRAVERSAL_COMPLETENESS_CERTIFICATE": true',
        '"TRAVERSAL_COMPLETENESS_CERTIFICATE": true'
    )
    args.output.write_text(text)
    print({"source_bytes":len(raw),"source_sha1":sha,"schema":NEW_SCHEMA,"b6_lock_removed":True})

if __name__=="__main__":
    main()
