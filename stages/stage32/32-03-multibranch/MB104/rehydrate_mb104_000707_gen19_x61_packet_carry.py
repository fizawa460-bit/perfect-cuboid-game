#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import verify_mb104_000707_gen19_x61_packet_carry as carry
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--manifest",type=Path,required=True); ap.add_argument("--bundle",type=Path,required=True); ap.add_argument("--out-dir",type=Path,required=True); a=ap.parse_args(); m,p,c=carry.decode_bundle(a.manifest,a.bundle,a.out_dir); print(json.dumps({"success":True,"materialized_packets":len(c),"complete_children":m["complete_child_count"],"incomplete_children":m["incomplete_child_count"],"out_dir":str(a.out_dir)},sort_keys=True))
if __name__=="__main__": main()
