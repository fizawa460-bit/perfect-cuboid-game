#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, pathlib


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--reports",type=pathlib.Path,required=True)
    ap.add_argument("--output",type=pathlib.Path,required=True)
    args=ap.parse_args()
    by={}
    for p in args.reports.glob("report-*.json"):
        d=json.loads(p.read_text()); by[d["mode"]]=d
    if set(by)!={"cap","sym","both"}: raise RuntimeError(f"missing reports {set(by)}")
    miss={k:by[k]["variant_missing_audited_b8_count"] for k in by}
    if miss["both"]==0:
        if miss["cap"]==0 and miss["sym"]>0:
            verdict="CAP_ACCUMULATOR_ROUNDTRIP_DRIFT_IS_SUFFICIENT_CAUSE_FOR_AUDITED_B8_LOSS"
        elif miss["sym"]==0 and miss["cap"]>0:
            verdict="SYMMETRY_ACCUMULATOR_ROUNDTRIP_DRIFT_IS_SUFFICIENT_CAUSE_FOR_AUDITED_B8_LOSS"
        elif miss["cap"]==0 and miss["sym"]==0:
            verdict="EITHER_ACCUMULATOR_SNAPSHOT_RESTORE_INDEPENDENTLY_REPAIRS_AUDITED_B8_LOSS"
        else:
            verdict="COMBINED_CAP_AND_SYMMETRY_SNAPSHOT_RESTORE_REQUIRED_TO_REPAIR_AUDITED_B8_LOSS"
    else:
        verdict="SNAPSHOT_RESTORE_HYPOTHESIS_INSUFFICIENT__OTHER_FLOATING_FAILURE_REMAINS"
    out={
      "schema":"STAGE32_SCOUT2_FAST_STATE_DRIFT_SUMMARY_V1",
      "SCOUT_ONLY":True,
      "verdict":verdict,
      "baseline_b10_known_missing_audited_b8":22,
      "missing_after_cap_snapshot":miss["cap"],
      "missing_after_symmetry_snapshot":miss["sym"],
      "missing_after_both_snapshot":miss["both"],
      "recovered_of_22":{k:by[k]["recovered_of_baseline_22_count"] for k in by},
      "variant_canonical_counts":{k:by[k]["variant_b10_count"] for k in by},
      "variant_histograms":{k:by[k]["variant_b10_histogram"] for k in by},
      "variant_elapsed_seconds":{k:by[k]["variant_elapsed_seconds"] for k in by},
      "next_required_test":"COMPARE_BOTH_SNAPSHOT_B10_AGAINST_COMPLETE_EXACT_B10_WHEN_STAGE32_18C_SHARDS_FINISH",
      "FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED":False,
      "CERTIFIED_FAST_ENGINE_ESTABLISHED":False,
      "THEOREM_CREDIT":False,
      "RECEIVER_CREDIT":False,
      "FULL_D16_G0_ROW_COMPLETE":False
    }
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,sort_keys=True))

if __name__=="__main__": main()
