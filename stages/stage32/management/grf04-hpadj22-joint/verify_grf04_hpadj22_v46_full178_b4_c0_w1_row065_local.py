#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
WORKER = HERE / "run_grf04_hpadj22_full178_parent.py"
CERTIFICATE = HERE / "GRF04-HPADJ22-V46-FULL178-B4-C0-W1-ROW065.json"
PROFILE = HERE / "GRF04-HPADJ22-V46-FULL178-B4-C0-W1-ROW065-LOCAL-PROFILE.json"
WORKER_BLOB = "c9fbf71242581f096718ebf0dbc9ac88878c91f1"
CERTIFICATE_CANONICAL = "df73e851b80cc6a8b44cf6228433ad85b3c5a23bd8fa0e2c4eb26d221759f172"


def require(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def canonical(value: dict) -> str:
    payload = dict(value)
    payload.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_worker():
    require(blob(WORKER) == WORKER_BLOB, "production worker blob drift")
    spec = importlib.util.spec_from_file_location("v46_row65_retained_worker", WORKER)
    require(spec is not None and spec.loader is not None, "cannot load production worker")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    worker = load_worker()
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    require(canonical(certificate) == CERTIFICATE_CANONICAL, "certificate canonical drift")
    accepted = worker.validate_carry(
        CERTIFICATE,
        worker_blob=WORKER_BLOB,
        band=4,
        chunk=0,
        b0=48,
        b1=50,
        row_index=65,
        row_id="g0-d164",
        g=0,
        d=164,
    )
    require(accepted is not None, "production validate_carry rejected row65")
    result = certificate["result"]
    require(int(result["hpadj22_exact_survivors"]) == 167203747351172777, "baseline drift")
    require(int(result["joint_exact_survivors"]) == 154702893862142934, "joint result drift")
    require(int(result["exact_improvement"]) == 12500853489029843, "improvement drift")

    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    require(profile["canonical_sha256_without_this_field"] == canonical(profile), "profile canonical drift")
    require(profile["certificate"]["canonical_sha256_without_this_field"] == CERTIFICATE_CANONICAL, "profile/certificate link drift")
    require(profile["certificate"]["production_validate_carry_accepted"] is True, "profile carry status drift")
    firewalls = profile["firewalls"]
    require(all(firewalls[key] is False for key in (
        "main_pruning_credit", "full178_complete", "theorem_credit", "effectivity_credit",
        "receiver_credit", "route_credit", "endpoint_credit", "merge_authorized"
    )), "credit firewall drift")
    require(firewalls["hostile_audit_required_before_promotion"] is True, "hostile audit firewall drift")
    print("PASS: exact local row65 certificate canonical and production validate_carry")
    print("PASS: profile source-lock, integer results, and zero-credit firewalls")


if __name__ == "__main__":
    main()
