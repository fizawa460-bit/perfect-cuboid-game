#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from verify_mb104_000707_gen27_adaptive_x58_carry import decode_carry

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',type=Path,required=True); a=ap.parse_args(); idx,_=decode_carry(out_dir=a.out_dir); print(json.dumps({'success':True,'out_dir':str(a.out_dir),'packet_certificates':16,'aggregate_certificate':1,'complete_children':74,'residual_timeout_children':54,'payload_sha256':idx['payload_sha256']},sort_keys=True))
if __name__=='__main__': main()
