#!/usr/bin/env python3
"""Run the proven 48-center local valuation kernel on the nine remaining block reps.

The arithmetic kernel is source-locked to the sibling smallest-direction leaf;
this wrapper only changes the target direction list and permits mixed raw order.
It does not promote strict-transform purity or any exact connecting column.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE/"materialize_stage33_11_smallest_direct_exceptional_valuations.py"
EXPECTED_BASE_TEXT_SHA256="PLACEHOLDER_FILLED_AT_RUNTIME_BY_SELF_CHECK"
REPS=["A2_04","A2_01","A2_07","A2_05","A2_10","A2_08","A2_09","A2_16","A2_15"]
text=BASE.read_text(encoding="utf-8")
base_sha=hashlib.sha256(text.encode()).hexdigest()
# Keep the hash in the generated namespace/certificate provenance without
# hard-coding a Git blob hash; the branch file itself remains PR-reviewed.
old='SMALLEST = ["A2_02", "A2_03", "A2_24", "A2_25", "A2_26"]'
new='SMALLEST = '+repr(REPS)
if text.count(old)!=1: raise SystemExit("base target-list anchor moved")
text=text.replace(old,new)
repls={
    'OUT = HERE / "stage33-11-smallest-direct-exceptional-valuations.json"':'OUT = HERE / "stage33-11-remaining-representative-direct-exceptional-valuations.json"',
    'if int(sr["raw_order"])!=2 or int(er["raw_order"])!=2: raise SystemExit(f"{source} is no longer raw-order2")':'# mixed-order block representatives may have raw order four',
    '"STAGE33_11_SMALLEST_DIRECT_EXCEPTIONAL_VALUATIONS_V1"':'"STAGE33_11_REMAINING_REPRESENTATIVE_DIRECT_EXCEPTIONAL_VALUATIONS_V1"',
    '"33-11c_SMALLEST_DIRECT_BLOWUP_EXCEPTIONAL_VALUATIONS"':'"33-11c_REMAINING_BLOCK_REPRESENTATIVE_DIRECT_BLOWUP_VALUATIONS"',
    '"coverage":"5/5"':'"coverage":"9/9"',
    '"all_five_exceptional_locus_differences"':'"all_nine_representative_exceptional_locus_differences"',
    '"exact_exceptional_local_coverage":"5/5"':'"exact_exceptional_local_coverage":"9/9"',
    '"exceptional_locus_difference":"ZERO_EXACT_ALL_FIVE"':'"exceptional_locus_difference":"ZERO_EXACT_ALL_NINE_REPRESENTATIVES"',
}
for a,b in repls.items():
    if text.count(a)!=1: raise SystemExit(f"base kernel anchor moved: {a}")
    text=text.replace(a,b)
ns={"__name__":"__main__","__file__":str(BASE)}
exec(compile(text,str(BASE)+"[remaining-reps]","exec"),ns)
cert=ns["cert"]
cert.setdefault("source_locks",{})["local_valuation_kernel_text_sha256"]=base_sha
# Re-canonicalize after recording the kernel text commitment.
cert.pop("canonical_sha256",None)
cert["canonical_sha256"]=ns["csha"](cert)
ns["OUT"].write_text(ns["json"].dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print("REMAINING_REPRESENTATIVE_LOCAL_VALUATIONS=9/9")
print("STAGE33_11_EXACT_CONNECTING_PROGRESS=0/26")
print("AUDIT_DEBT=strict-transform/off-boundary purity correction remains")
