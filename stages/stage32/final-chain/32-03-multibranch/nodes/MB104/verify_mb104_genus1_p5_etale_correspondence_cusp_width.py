#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-P5-ETALE-CORRESPONDENCE-CUSP-WIDTH-CERTIFICATE.json"
NOTE = HERE / "GENUS1-P5-ETALE-CORRESPONDENCE-CUSP-WIDTH-OBSTRUCTION.md"

LOCKS = {
    "EQUALITY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY-CERTIFICATE.json",
        "62a2d01447016731001d35cc5915880daa2bfada",
    ),
    "PRODUCT_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-PRODUCT-COVER-SOURCE-NOTE.md",
        "974c6cfecb6e4141615583841a0c90146ad2b4a6",
    ),
}

def req(cond, message):
    if not cond:
        raise SystemExit("FAIL: " + message)

def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")

def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def main():
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_GENUS1_P5_ETALE_CORRESPONDENCE_CUSP_WIDTH_REJECTED_V2", "schema")
    req(cert["status"] == "REJECTED_HOSTILE_AUDIT_FAIL", "rejected status")
    req(cert["candidate_exact_head"] == "d83914576150bf0c5c6e3be0fcadf3baf7104ece", "candidate head")
    req(cert["hostile_audit_review_id"] == 5194067386, "audit receipt")
    req(cert["hostile_audit_result"] == "FAIL", "audit result")
    req(cert["consumable"] is False and cert["proof_credit"] is False, "non-consumable firewall")

    defect = cert["blocking_defect"]
    req(defect["missing_common_puncture_statement"] == "f1^{-1}(Cusps)=f2^{-1}(Cusps)", "missing statement")
    req(defect["proved"] is False, "missing statement must remain unproved")
    req(defect["compact_universal_cover_repairs_route"] is False, "compact-cover non-repair")

    preserved = cert["preserved_retained_authority"]
    req(preserved["equality_rigidity_unchanged"] is True, "equality authority preservation")
    req(preserved["MB104_state_unchanged"] is True, "STATE preservation")
    req(preserved["000707_e2_open"] is True and preserved["000707_e4_open"] is True, "000707 remains open")

    fw = cert["credit_firewall"]
    req(all(v is False for v in fw.values()), "all closure/credit/promotion/merge flags false")

    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    rr = root()
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"source lock exists: {key}")
        req(blob_sha1(p) == expected, f"source lock hash: {key}")

    note = NOTE.read_text()
    for token in (
        "REJECTED BY HOSTILE AUDIT",
        "NON-CONSUMABLE",
        "5194067386",
        "f1^{-1}(Cusps) = f2^{-1}(Cusps)",
        "uniform F1-P5 equality face closed here: **false**",
        "STATE promotion: **none**",
    ):
        req(token in note, f"rejection note token: {token}")

    print("PASS STAGE32_MB104_GENUS1_P5_ETALE_CORRESPONDENCE_CUSP_WIDTH_REJECTED_V2")
    print("route is fail-closed and non-consumable; prior MB104 retained authority is unchanged")

if __name__ == "__main__":
    main()
