#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def build_joint_bc_t_shard(H: int, b_start: int, b_stop: int):
    H=int(H); b_start=int(b_start); b_stop=int(b_stop)
    req(0 <= b_start <= b_stop <= H, "invalid b shard")

    B=[[[defaultdict(lambda: defaultdict(int)) for _ in range(2)] for __ in range(3)] for ___ in range(H+1)]
    C=[[[defaultdict(lambda: defaultdict(int)) for _ in range(2)] for __ in range(4)] for ___ in range(H+1)]
    for m in range(H+1):
        for x9 in range(m+1):
            x5=m-x9
            B[m][int(x5>0)+int(x9>0)][x9&1][x5*x5+x9*x9][x9]+=1
        for x8 in range(m+1):
            for x10 in range(m-x8+1):
                x6=m-x8-x10
                C[m][int(x6>0)+int(x8>0)+int(x10>0)][(x8+x10)&1][x6*x6+x8*x8+x10*x10][x6]+=1

    out=defaultdict(lambda: defaultdict(int))

    # Unequal x0<x1 branch.  b=x1+x5+x9 lets us restrict x1 and b before
    # combining the preserved x9/x6 coordinates needed for exact t.
    for x0 in range(H+1):
        extra=int(x0>0)+1
        x0par=x0&1
        for x1 in range(x0+1,min(H,b_stop)+1):
            x1par=x1&1
            q01=x0*x0+x1*x1
            for b in range(max(b_start,x1),b_stop+1):
                g2=b-x1
                for g3 in range(H-x0+1):
                    c=x0+g3
                    for sb in range(3):
                        for x9par in (0,1):
                            left=B[g2][sb][x9par]
                            if not left:
                                continue
                            required_cpar=x9par^x1par
                            r=x0par^x1par^x9par
                            for sc in range(4):
                                right=C[g3][sc][required_cpar]
                                if not right:
                                    continue
                                support=sb+sc+extra
                                for ql,x9_counts in left.items():
                                    for qr,x6_counts in right.items():
                                        dst=out[(b,c,support,r,q01+ql+qr)]
                                        for x9,vl in x9_counts.items():
                                            for x6,vr in x6_counts.items():
                                                dst[x0+x1+x6+x9]+=vl*vr

    # Equal x0=x1=u, lex-strict x5<x8.
    for u in range(H+1):
        terminal_parity=u&1
        cap=H-u
        for x5 in range(cap+1):
            for x9 in range(cap-x5+1):
                b=u+x5+x9
                if not (b_start <= b <= b_stop):
                    continue
                for x8 in range(x5+1,cap+1):
                    for x6 in range(cap-x8+1):
                        for x10 in range(cap-x8-x6+1):
                            c=u+x8+x6+x10
                            if ((x8+x9+x10)&1) != terminal_parity:
                                continue
                            vals=(u,u,x5,x6,x8,x9,x10)
                            support=sum(v>0 for v in vals)
                            qbc=sum(v*v for v in vals)
                            r=(u+x8+x10)&1
                            out[(b,c,support,r,qbc)][2*u+x6+x9]+=1

        # Equal x5=x8, enforce x6<=x9.
        for x5 in range(cap+1):
            x8=x5
            for x9 in range(cap-x5+1):
                b=u+x5+x9
                if not (b_start <= b <= b_stop):
                    continue
                for x6 in range(min(x9,cap-x8)+1):
                    for x10 in range(cap-x8-x6+1):
                        c=u+x8+x6+x10
                        if ((x8+x9+x10)&1) != terminal_parity:
                            continue
                        vals=(u,u,x5,x6,x8,x9,x10)
                        support=sum(v>0 for v in vals)
                        qbc=sum(v*v for v in vals)
                        r=(u+x8+x10)&1
                        out[(b,c,support,r,qbc)][2*u+x6+x9]+=1
    return out

def record_bytes(key, counts) -> bytes:
    b,c,s,r,qbc=key
    pairs=[[int(t),int(v)] for t,v in sorted(counts.items())]
    return (json.dumps([b,c,s,r,qbc,pairs],separators=(",",":"))+"\n").encode()

def stream_metrics(hist, output: Path | None=None) -> dict:
    sha=hashlib.sha256()
    lines=entries=multiplicity=nbytes=0
    fh=output.open("wb") if output is not None else None
    try:
        for key in sorted(hist):
            raw=record_bytes(key,hist[key])
            sha.update(raw)
            if fh is not None:
                fh.write(raw)
            lines+=1
            entries+=len(hist[key])
            multiplicity+=sum(int(v) for v in hist[key].values())
            nbytes+=len(raw)
    finally:
        if fh is not None:
            fh.close()
    return {
        "stream_sha256":sha.hexdigest(),
        "line_count":lines,
        "exact_t_support_entries":entries,
        "canonical_tuple_multiplicity":multiplicity,
        "utf8_bytes":nbytes,
    }

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--H",type=int,required=True)
    ap.add_argument("--b-start",type=int,required=True)
    ap.add_argument("--b-stop",type=int,required=True)
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    hist=build_joint_bc_t_shard(args.H,args.b_start,args.b_stop)
    if args.output is not None:
        args.output.parent.mkdir(parents=True,exist_ok=True)
    m=stream_metrics(hist,args.output)
    print(json.dumps({
        "status":"EXACT_T_SHARD_COMPLETE_ZERO_CREDIT",
        "H":args.H,
        "b_start":args.b_start,
        "b_stop":args.b_stop,
        **m,
    },sort_keys=True))

if __name__=="__main__":
    main()
