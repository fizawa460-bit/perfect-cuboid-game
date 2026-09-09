#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import pathlib
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parents[3]
CODE = (ROOT / "export_stoll_runtime_points.m").read_text(encoding="utf-8")
URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER = "https://magma.maths.usyd.edu.au/calc/"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


data = urllib.parse.urlencode({"input": CODE}).encode("utf-8")
req = urllib.request.Request(
    URL,
    data=data,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": REFERER,
        "User-Agent": "perfect-cuboid-stage32ex5-b/1.1",
    },
    method="POST",
)
with urllib.request.urlopen(req, timeout=240) as resp:
    raw = resp.read().decode("utf-8", errors="replace")
    http_status = resp.status

root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()).strip())
stdout = "\n".join(lines)
records = []
for line in lines:
    if not line.startswith("NODE|"):
        continue
    tag, idx, payload, fingerprint = line.split("|", 3)
    records.append((int(idx), payload, fingerprint))

indices = [idx for idx, _, _ in records]
payloads = [payload for _, payload, _ in records]
runtime_fps = [fp for _, _, fp in records]
completion = "STAGE32EX5_B_RUNTIME_POINTS_END" in stdout
runtime_error = any(marker in stdout for marker in (
    "Runtime error", "Internal error", "User error", "Assertion failed"
))
index_ok = indices == list(range(48))
unique_points_ok = len(set(payloads)) == 48
coordinate_arity_ok = all(len(payload.split(",")) == 7 for payload in payloads)
fingerprint_arity_ok = all(len(fp) == 92 and set(fp) <= {"0", "1"} for fp in runtime_fps)
unique_runtime_fps_ok = len(set(runtime_fps)) == 48

# Recover the retained all-140 intersection matrix using the exact Stage32
# Hperp adapter, but keep the denylisted retained payload runner-local.
residual = REPO / "stages" / "stage32" / "residual-32-01-production"
sys.path.insert(0, str(residual))
marking_path = REPO / "stages" / "stage33" / "33-07" / "stage32_picard_marking_retained.py"
marking_mod = load_module(marking_path, "s32ex5_b_retained_marking")
marking = marking_mod.load()
import hperp_integral_adapter as hperp  # noqa: E402
q, degree, linear, _, _ = hperp._parse_hperp(marking["hperp_text"])
full = hperp._recover_full_intersection(q, degree, linear)

retained_fps = []
for k in range(48):
    bits = []
    for j in range(92):
        value = int(full[j, 92 + k])
        if value not in (0, 1):
            raise ValueError(f"retained incidence is not binary at normal={j}, exceptional={k}: {value}")
        bits.append(str(value))
    retained_fps.append("".join(bits))
unique_retained_fps_ok = len(set(retained_fps)) == 48

retained_by_fp = {fp: k for k, fp in enumerate(retained_fps)}
mapping = []
for idx, payload, fp in records:
    if fp not in retained_by_fp:
        raise ValueError(f"runtime fingerprint absent from retained all140 matrix at runtime index {idx}")
    mapping.append((idx, retained_by_fp[fp], payload, fp))

mapped_retained = [k for _, k, _, _ in mapping]
bijection_ok = sorted(mapped_retained) == list(range(48))
identity_permutation = mapped_retained == list(range(48))

success = (
    http_status == 200
    and completion
    and not runtime_error
    and len(records) == 48
    and index_ok
    and unique_points_ok
    and coordinate_arity_ok
    and fingerprint_arity_ok
    and unique_runtime_fps_ok
    and unique_retained_fps_ok
    and bijection_ok
    and "COUNT|48" in stdout
    and "CURVES|92" in stdout
)

point_table = [
    {
        "runtime_index_0based": idx,
        "retained_exceptional_index_0based": ridx,
        "normalized_projective_coordinates": payload.split(","),
        "incidence_fingerprint_92": fp,
    }
    for idx, ridx, payload, fp in mapping
]
print(json.dumps({
    "http_status": http_status,
    "node_records": len(records),
    "indices_0_through_47": index_ok,
    "unique_normalized_points": unique_points_ok,
    "coordinate_arity_7": coordinate_arity_ok,
    "fingerprint_arity_92": fingerprint_arity_ok,
    "unique_runtime_fingerprints": unique_runtime_fps_ok,
    "unique_retained_fingerprints": unique_retained_fps_ok,
    "runtime_to_retained_bijection": bijection_ok,
    "runtime_to_retained_identity_permutation": identity_permutation,
    "point_table_sha256": csha(point_table),
    "runtime_error_seen": runtime_error,
    "completion_marker_seen": completion,
    "success": success,
}, sort_keys=True))
for row in point_table:
    print(
        "MAP|{runtime}|{retained}|{coords}|{fp}".format(
            runtime=row["runtime_index_0based"],
            retained=row["retained_exceptional_index_0based"],
            coords=",".join(row["normalized_projective_coordinates"]),
            fp=row["incidence_fingerprint_92"],
        )
    )
print("COUNT|48")
print("UNIQUE_POINTS|48" if unique_points_ok else f"UNIQUE_POINTS|{len(set(payloads))}")
print("UNIQUE_RUNTIME_FP|48" if unique_runtime_fps_ok else f"UNIQUE_RUNTIME_FP|{len(set(runtime_fps))}")
print("UNIQUE_RETAINED_FP|48" if unique_retained_fps_ok else f"UNIQUE_RETAINED_FP|{len(set(retained_fps))}")
print("BIJECTION|48" if bijection_ok else f"BIJECTION|{len(set(mapped_retained))}")
print("STAGE32EX5_B_RUNTIME_POINTS_END")
if not success:
    raise SystemExit("Stage32EX5-B runtime/retained incidence bridge did not finish cleanly")
