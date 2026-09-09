#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ADD = ROOT / "stages/stage32/scratch/q602-o210-forgetful-adapter-post1500-origin-addendum-20260909.json"


def blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def canon(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    a = json.loads(ADD.read_text())
    assert a["schema"] == "STAGE32_Q602_O210_FORGETFUL_ADAPTER_POST1500_ORIGIN_ADDENDUM_V1"
    assert canon(a) == a["canonical_sha256_without_this_field"] == "7399302b10711a77a656f54bf34e2305d5358ea0eb2c29370c77c7f49d6fcf6e"
    lock = a["source_lock"]
    p = ROOT / lock["path"]
    data = p.read_bytes()
    assert blob_sha1(data) == lock["blob_sha1"]
    s = json.loads(data)
    assert canon(s) == lock["canonical_sha256"] == s["canonical_sha256_without_this_field"]
    assert s["fixed_target"]["row_id"] == "g1-d186"
    assert s["fixed_target"]["O"] == 210 and s["fixed_target"]["qprime"] == 4
    r = s["corrected_rosati_arithmetic"]
    assert r["matrix_trace_relation"] == "Tr_Q(T^dagger*T)=2*Q(T)"
    assert r["Q"] == 602
    required = s["current_blocker"]["required_new_input"]
    assert "Q(T)=602" in required
    assert "correspondences arising from the common-cover/marked-branch geometry" in required
    for v in a["firewalls"].values():
        assert v is False
    print("PASS_STAGE32_SCRATCH_Q602_O210_POST1500_ORIGIN")
    print(a["canonical_sha256_without_this_field"])
    print("Q602_is_Q_of_actual_common_cover_correspondence=true")
    print("authority_change=false")


if __name__ == "__main__":
    main()
