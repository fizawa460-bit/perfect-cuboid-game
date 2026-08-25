#!/usr/bin/env python3
from __future__ import annotations
import argparse, pathlib
EXPECTED_FAST_BLOB="f9479ee73c9a5960cb8a3a8bc11a0c1c0fe8f4ba"
def rep(t,o,n,label):
    if t.count(o)!=1: raise RuntimeError(f"{label}: {t.count(o)} occurrences")
    return t.replace(o,n,1)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source',type=pathlib.Path,required=True); ap.add_argument('--output',type=pathlib.Path,required=True); a=ap.parse_args(); t=a.source.read_text()
    loop="        for (long long zi=lo;zi<=hi;zi++) {\n"
    snap=("        std::array<long double,140> parent_assigned{};\n"
          "        for (int r=0;r<m_;r++) parent_assigned[r]=assigned_[r];\n"
          "        std::vector<long double> parent_sassigned(s_.k);\n"
          "        for (int r=0;r<s_.k;r++) parent_sassigned[r]=sassigned_[r];\n"+loop)
    t=rep(t,loop,snap,'loop')
    old=("            z_[i]=zi;\n"
         "            for (int r=0;r<m_;r++) assigned_[r]+=a_[r][i]*ti;\n"
         "            for (int r=0;r<s_.k;r++) sassigned_[r]+=sa_[r][i]*ti;\n")
    new=("            z_[i]=zi;\n"
         "            for (int r=0;r<m_;r++) assigned_[r]=parent_assigned[r]+a_[r][i]*ti;\n"
         "            for (int r=0;r<s_.k;r++) sassigned_[r]=parent_sassigned[r]+sa_[r][i]*ti;\n")
    t=rep(t,old,new,'update')
    restore=("            for (int r=0;r<s_.k;r++) sassigned_[r]-=sa_[r][i]*ti;\n"
             "            for (int r=0;r<m_;r++) assigned_[r]-=a_[r][i]*ti;\n")
    t=rep(t,restore,"",'restore')
    marker="struct TierResult {\n"; t=rep(t,marker,"// STAGE32_SCOUT3_VARIABLE_BREAKER_SNAPSHOT=1\n"+marker,'marker')
    a.output.write_text(t); print({'expected_source_blob':EXPECTED_FAST_BLOB,'snapshot_parent_restore':'both','variable_breaker_count':True,'scout_only':True})
if __name__=='__main__': main()
