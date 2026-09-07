#!/usr/bin/env python3
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "stages/stage35-ex"
ART = HERE / "35ex-35/goal4ae-c5k-name-collision-direct-s-imageinpic-route.json"
LOCK = HERE / "35ex-35/goal4ae-c5k-name-collision-direct-s-imageinpic-route-source-lock.md"
PIC = ROOT / "stages/stage33/33-07/certify_two_coordinate_swap_picard_rows.py"

EXPECTED_ART_BLOB = "1bdd1daeffbab6c4a6d3aade87280c913f1b9ca2"
EXPECTED_LOCK_BLOB = "e6c8a34b26ddb6fefd4b9f501e3e6b19fddfecb2"
EXPECTED_UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_CANON = "48aed34257798b049ffb2cd783c1b25964189b0eec2c84cfec476cb460679475"


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


art_raw = ART.read_bytes()
lock_raw = LOCK.read_bytes()
assert git_blob(art_raw) == EXPECTED_ART_BLOB
assert git_blob(lock_raw) == EXPECTED_LOCK_BLOB
art = json.loads(art_raw)
canon = art.pop("canonical_sha256")
assert canon == EXPECTED_CANON == csha(art)

assert art["schema"] == "STAGE35_EX_GOAL4AE_C5K_NAME_COLLISION_DIRECT_S_IMAGEINPIC_ROUTE_V1"
assert art["upstream_source"]["git_blob_sha1"] == EXPECTED_UPSTREAM_BLOB
sem = art["source_semantics"]
assert sem["surface_C5_count"] == 16
assert sem["surface_C5_family"] == "genus 3 nonhyperelliptic curves of degree 8"
assert sem["K_C5K_context"] == "representative of size-8 orbit among C^2=-2 smooth rational normal curves of degree 4"
assert sem["K_C5K_is_source_proven_image_of_surface_C5"] is False
assert sem["goal4ad_PicK_route_source_bridge_present"] is False
assert sem["direct_surface_imageinPic_function_present"] is True

res = art["resolution"]
assert res["PicK_C5K_name_based_route_rejected"] is True
assert res["selected_route"] == "SURFACE_C5S_TO_IMAGEINPIC_TO_HISTORICAL_PICS_TO_PRIMITIVE_INDLIST64"
assert res["numeric_C5_pair_classes_computed"] is False
assert res["target_span_computed"] is False
assert res["general_F_B_open"] is True

fw = art["credit_firewall"]
assert all(fw[k] is False for k in (
    "hostile_audit_pass", "theorem_credit", "endpoint_credit", "E1_proved",
    "stage35_closed", "perfect_cuboid_claim",
))

lock = lock_raw.decode()
for needle in (
    "Genus 3 nonhyperelliptic curves of degree 8",
    "smooth rational normal curves of degree 4",
    "C5K := Curve(IrreducibleComponents(Scheme(K, B1+B2+B3))[1]);",
    "function imageinPic(C)",
    "iseq := [intersection(C, j) : j in indlist];",
    "SURFACE" if False else "explicit S-side C5s",
):
    assert needle in lock, needle

# Check only the compact Stage33 source text: do not import retained payloads.
tree = ast.parse(PIC.read_text())
indlist = None
for node in tree.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "INDLIST":
                indlist = ast.literal_eval(node.value)
assert isinstance(indlist, list) and len(indlist) == 64
assert len(set(indlist)) == 64

print(json.dumps({
    "success": True,
    "goal4ae_route_repair": "PASS",
    "surface_C5_count": 16,
    "stage33_primitive_indlist_rank": 64,
    "numeric_C5_pair_classes_computed": False,
    "target_span_computed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}, sort_keys=True))
