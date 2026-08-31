#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path

EXPECTED_MANIFEST = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PREFLIGHT = "1654ef385558c606623f81bfbaf7c68063141a5be39d9b692d58567f011a6c65"


def csha(v):
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected: str):
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    got = csha(raw)
    if claimed != expected or got != expected:
        raise SystemExit(f"canonical regression {path}: claimed={claimed} got={got}")
    return raw


def parse(row_id: str):
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--preflight", type=Path, required=True)
    ap.add_argument("--driver", type=Path, required=True)
    ap.add_argument("--bridge", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    a = ap.parse_args()

    manifest = load_canonical(a.manifest, EXPECTED_MANIFEST)
    preflight = load_canonical(a.preflight, EXPECTED_PREFLIGHT)
    driver = a.driver.read_text()
    bridge = a.bridge.read_text()
    if 'for e in range(emin, emax + 1)' not in driver:
        raise SystemExit("21ad e-loop semantic regression")
    if 'slice_coordinates": ["degree", "exceptional_total", "first_normal_half_total"]' not in bridge:
        raise SystemExit("bridge slice-coordinate semantic regression")
    if 'EXCEPTIONAL_COUNT = 48' not in bridge:
        raise SystemExit("exceptional count semantic regression")

    rows=[]
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv:int(kv[0])):
        rows.extend(ids)
    if len(rows)!=178 or len(set(rows))!=178:
        raise SystemExit("FULL178 row population regression")

    total=after=affected=0
    by_g={0:{"rows":0,"original":0,"after_cut":0,"eliminated":0,"affected_rows":0},
          1:{"rows":0,"original":0,"after_cut":0,"eliminated":0,"affected_rows":0}}
    for row in rows:
        g,d=parse(row)
        old_min=8 if g==0 else 4
        max_e=(19*d)//5
        required=math.ceil((d-16*g+16)/4)
        new_min=max(old_min, required)
        old=max_e-old_min+1
        new=max_e-new_min+1
        p=old-new
        total+=old; after+=new
        by_g[g]["rows"]+=1; by_g[g]["original"]+=old; by_g[g]["after_cut"]+=new; by_g[g]["eliminated"]+=p
        if p:
            affected+=1; by_g[g]["affected_rows"]+=1
    eliminated=total-after
    expected=(64111,60491,3620,168)
    if (total,after,eliminated,affected)!=expected:
        raise SystemExit(f"coarse census regression {(total,after,eliminated,affected)}")
    if by_g[0] != {"rows":85,"original":29087,"after_cut":27447,"eliminated":1640,"affected_rows":80}:
        raise SystemExit(f"g0 regression {by_g[0]}")
    if by_g[1] != {"rows":93,"original":35024,"after_cut":33044,"eliminated":1980,"affected_rows":88}:
        raise SystemExit(f"g1 regression {by_g[1]}")

    c=preflight["full178_coarse_strata"]
    if (c["original_coarse_e_strata"], c["after_cheap_node_mass_cut"], c["eliminated_coarse_e_strata"], c["affected_rows"]) != expected:
        raise SystemExit("preflight count mismatch")

    out={
      "schema":"STAGE32_POST21BL_FULL178_NODE_SUPPORT_PREFLIGHT_FRESH_AUDIT_V1",
      "status":"PASS_STAGE32_POST21BL_FULL178_NODE_SUPPORT_PREFLIGHT_FRESH_AUDIT",
      "source_locks":{"manifest_canonical_sha256":EXPECTED_MANIFEST,"preflight_canonical_sha256":EXPECTED_PREFLIGHT},
      "recomputed":{"rows":178,"original_coarse_e_strata":total,"after_cut":after,"eliminated":eliminated,"affected_rows":affected,"genus0":by_g[0],"genus1":by_g[1]},
      "semantic_checks":{"legacy_21ad_uses_e_as_slice_coordinate":True,"exceptional_count":48,"cheap_cut":"e >= ceil((d-16g+16)/4)","strong_support_not_reconstructed":True},
      "firewalls":{"heavy_run_performed":False,"full178_closed":False,"multibranch_closed":False,"receiver_credit":False,"perfect_cuboid_nonexistence_claim":False}
    }
    out["canonical_sha256_without_this_field"]=csha(out)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":out["status"],"eliminated":eliminated,"affected_rows":affected,"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__": main()
