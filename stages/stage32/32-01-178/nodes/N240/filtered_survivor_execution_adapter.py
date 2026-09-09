#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Iterable, Mapping

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N230_DIR = HERE.parent / "N230"
RESIDUAL_DIR = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(N230_DIR))

from n220_filtered_terminal_indexer import N220FilteredTerminalIndexer

CONTRACT_REV = "STAGE32_32_01_178_N240_FILTERED_EXECUTION_ADAPTER_V2"
FULL178_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
FULL178_MANIFEST_BLOB_SHA1 = "0a46b34e278688240656b4977e9cb7f589e90e06"
FULL178_MANIFEST_SCHEMA = "STAGE32_RESIDUAL32_01_FULL178_MANIFEST_V1"
FULL178_MANIFEST_PATH = RESIDUAL_DIR / "full178-manifest.json"
N220_AUDIT_REVIEW_ID = 5159411821
N220_AUDIT_EXACT_HEAD = "940fe99a20c1eaa215126acd92e7c390295bb441"
N230_AUDIT_REVIEW_ID = 5160389467
N230_AUDIT_EXACT_HEAD = "1206475517ed8caf59e92d0d6daa57eb14ab4a41"
N230_IMPLEMENTATION_BLOB_SHA1 = "2c04cceb374971dbf83cb684bd8a17a2ee4b50ed"
N230_IMPLEMENTATION_PATH = N230_DIR / "n220_filtered_terminal_indexer.py"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def load_locked_full178_manifest() -> tuple[dict, dict[str, dict[str, int]]]:
    if git_blob_sha1(FULL178_MANIFEST_PATH) != FULL178_MANIFEST_BLOB_SHA1:
        raise ValueError("FULL178 manifest blob source-lock regression")
    manifest = json.loads(FULL178_MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest.get("schema") != FULL178_MANIFEST_SCHEMA:
        raise ValueError("FULL178 manifest schema regression")

    embedded_hash = manifest.get("canonical_sha256_without_this_field")
    body = dict(manifest)
    body.pop("canonical_sha256_without_this_field", None)
    computed_hash = canonical_sha256(body)
    if embedded_hash != FULL178_MANIFEST_SHA256 or computed_hash != FULL178_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest canonical SHA-256 regression")

    rows: list[str] = []
    for key, class_rows in manifest.get("m_class_rows", {}).items():
        if not isinstance(class_rows, list):
            raise ValueError(f"FULL178 manifest m-class {key} is not a row list")
        rows.extend(str(row_id) for row_id in class_rows)
    if len(rows) != int(manifest.get("residual_row_count", -1)):
        raise ValueError("FULL178 manifest residual row count regression")
    if len(rows) != len(set(rows)):
        raise ValueError("FULL178 manifest duplicate row_id")

    params = manifest.get("row_parameter_derivation", {})
    emin_g0 = int(params.get("exceptional_mass_min_g0", -1))
    emin_g1 = int(params.get("exceptional_mass_min_g1", -1))
    table: dict[str, dict[str, int]] = {}
    stratum_count = 0
    for row_id in rows:
        if not row_id.startswith("g") or "-d" not in row_id:
            raise ValueError(f"invalid FULL178 row_id: {row_id}")
        g_text, d_text = row_id[1:].split("-d", 1)
        genus = int(g_text)
        degree = int(d_text)
        if row_id != f"g{genus}-d{degree:03d}":
            raise ValueError(f"noncanonical FULL178 row_id: {row_id}")
        if genus not in (0, 1):
            raise ValueError(f"unsupported FULL178 genus: {row_id}")
        e_min = emin_g0 if genus == 0 else emin_g1
        e_max = (19 * degree) // 5
        if e_max < e_min:
            raise ValueError(f"empty FULL178 e-range: {row_id}")
        table[row_id] = {
            "genus": genus,
            "degree": degree,
            "e_min": e_min,
            "e_max": e_max,
        }
        stratum_count += e_max - e_min + 1

    if stratum_count != int(manifest.get("coarse_strata_count", -1)):
        raise ValueError("FULL178 manifest reconstructed coarse-strata count regression")
    if stratum_count != 64111:
        raise ValueError("FULL178 manifest expected 64111 strata")
    return manifest, table


class FilteredSurvivorExecutionAdapter:
    """Bridge N230 survivor execution back to the old canonical rank domain.

    V2 deliberately separates structural filtered-interval mechanics from any
    numerical leaf-completeness claim.  Until a source-locked production leaf
    verifier is registered in this adapter, production COMPLETE validation
    fails closed unconditionally.
    """

    def __init__(self, genus: int, degree: int, e: int, *, leaf_contract_rev: str) -> None:
        self.genus = int(genus)
        self.degree = int(degree)
        self.e = int(e)
        self.leaf_contract_rev = str(leaf_contract_rev)
        if not self.leaf_contract_rev:
            raise ValueError("leaf_contract_rev must be non-empty")
        if git_blob_sha1(N230_IMPLEMENTATION_PATH) != N230_IMPLEMENTATION_BLOB_SHA1:
            raise ValueError("N230 implementation source-lock regression")

        _, manifest_table = load_locked_full178_manifest()
        self.row_id = f"g{self.genus}-d{self.degree:03d}"
        entry = manifest_table.get(self.row_id)
        if entry is None:
            raise ValueError("stratum row_id is not present in locked FULL178 manifest")
        if entry["genus"] != self.genus or entry["degree"] != self.degree:
            raise ValueError("FULL178 manifest row identity mismatch")
        if not entry["e_min"] <= self.e <= entry["e_max"]:
            raise ValueError("e is not an authorized FULL178 stratum for this row")
        self.manifest_e_min = entry["e_min"]
        self.manifest_e_max = entry["e_max"]

        self.filtered = N220FilteredTerminalIndexer(self.genus, self.degree, self.e)
        cert = self.filtered.certificate()
        self.old_terminal_count = int(cert["old_terminal_count"])
        self.filtered_terminal_count = int(cert["filtered_terminal_count"])
        self.n220_rejected_terminal_count = int(cert["n220_rejected_terminal_count"])
        if self.old_terminal_count <= 0:
            raise AssertionError("authorized FULL178 stratum has nonpositive old terminal count")
        if self.n220_rejected_terminal_count + self.filtered_terminal_count != self.old_terminal_count:
            raise AssertionError("N220 partition identity regression")
        if not cert["old_rank_remains_completeness_authority"] or not cert["secondary_rank_only"]:
            raise AssertionError("N230 rank-authority contract regression")

    def manifest_membership_certificate(self) -> dict:
        body = {
            "schema": "STAGE32_32_01_178_N240_MANIFEST_MEMBERSHIP_V1",
            "full178_manifest_blob_sha1": FULL178_MANIFEST_BLOB_SHA1,
            "full178_manifest_sha256": FULL178_MANIFEST_SHA256,
            "row_id": self.row_id,
            "genus": self.genus,
            "degree": self.degree,
            "e": self.e,
            "authorized_e_min": self.manifest_e_min,
            "authorized_e_max": self.manifest_e_max,
            "old_stratum_terminal_count": str(self.old_terminal_count),
            "exact_manifest_membership_verified": True,
        }
        return {**body, "canonical_sha256": canonical_sha256(body)}

    def partition_certificate(self) -> dict:
        membership = self.manifest_membership_certificate()
        body = {
            "schema": CONTRACT_REV,
            "row_id": self.row_id,
            "genus": self.genus,
            "degree": self.degree,
            "e": self.e,
            "full178_manifest_blob_sha1": FULL178_MANIFEST_BLOB_SHA1,
            "full178_manifest_sha256": FULL178_MANIFEST_SHA256,
            "manifest_membership_sha256": membership["canonical_sha256"],
            "n220_audit_review_id": N220_AUDIT_REVIEW_ID,
            "n220_audit_exact_head": N220_AUDIT_EXACT_HEAD,
            "n230_audit_review_id": N230_AUDIT_REVIEW_ID,
            "n230_audit_exact_head": N230_AUDIT_EXACT_HEAD,
            "n230_implementation_blob_sha1": N230_IMPLEMENTATION_BLOB_SHA1,
            "leaf_contract_rev": self.leaf_contract_rev,
            "old_stratum_terminal_count": str(self.old_terminal_count),
            "n220_rejected_terminal_count": str(self.n220_rejected_terminal_count),
            "filtered_terminal_count": str(self.filtered_terminal_count),
            "partition_identity_exact": self.old_terminal_count == self.n220_rejected_terminal_count + self.filtered_terminal_count,
            "old_canonical_rank_remains_completeness_authority": True,
            "filtered_rank_is_secondary_execution_coordinate_only": True,
            "rejected_terminals_require_picard_leaf_execution": False,
            "survivor_terminals_require_source_locked_exact_leaf_verification": True,
            "production_complete_validator_registered": False,
            "n104_old_domain_release_available": False,
            "full178_complete": False,
            "heavy_compute_authorized": False,
        }
        return {**body, "canonical_sha256": canonical_sha256(body)}

    def planned_work_unit_count(self, chunk_size: int) -> int:
        chunk_size = int(chunk_size)
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if self.filtered_terminal_count == 0:
            return 0
        return math.ceil(self.filtered_terminal_count / chunk_size)

    def _work_unit_body(self, filtered_rank_lo: int, filtered_rank_hi: int) -> dict:
        lo, hi = int(filtered_rank_lo), int(filtered_rank_hi)
        if not 0 <= lo < hi <= self.filtered_terminal_count:
            raise ValueError("invalid filtered rank interval")
        membership = self.manifest_membership_certificate()
        return {
            "contract_rev": CONTRACT_REV,
            "full178_manifest_blob_sha1": FULL178_MANIFEST_BLOB_SHA1,
            "full178_manifest_sha256": FULL178_MANIFEST_SHA256,
            "manifest_membership_sha256": membership["canonical_sha256"],
            "row_id": self.row_id,
            "d": self.degree,
            "e": self.e,
            "old_stratum_terminal_count": str(self.old_terminal_count),
            "n220_rejected_terminal_count": str(self.n220_rejected_terminal_count),
            "filtered_terminal_count": str(self.filtered_terminal_count),
            "n220_audit_review_id": N220_AUDIT_REVIEW_ID,
            "n230_audit_review_id": N230_AUDIT_REVIEW_ID,
            "n230_implementation_blob_sha1": N230_IMPLEMENTATION_BLOB_SHA1,
            "leaf_contract_rev": self.leaf_contract_rev,
            "filtered_rank_lo": lo,
            "filtered_rank_hi": hi,
        }

    def planned_work_unit(self, index: int, chunk_size: int) -> dict:
        index, chunk_size = int(index), int(chunk_size)
        count = self.planned_work_unit_count(chunk_size)
        if not 0 <= index < count:
            raise ValueError("work-unit index outside plan")
        lo = index * chunk_size
        hi = min(self.filtered_terminal_count, lo + chunk_size)
        body = self._work_unit_body(lo, hi)
        return {**body, "work_unit_id": canonical_sha256(body)}

    def verify_work_unit(self, unit: Mapping[str, object]) -> None:
        lo = int(unit["filtered_rank_lo"])
        hi = int(unit["filtered_rank_hi"])
        expected = self._work_unit_body(lo, hi)
        for key, value in expected.items():
            if unit.get(key) != value:
                raise ValueError(f"work-unit contract mismatch: {key}")
        if unit.get("work_unit_id") != canonical_sha256(expected):
            raise ValueError("work_unit_id mismatch")

    def validate_planned_cover(self, units: Iterable[Mapping[str, object]]) -> dict:
        units = list(units)
        if self.filtered_terminal_count == 0:
            if units:
                raise ValueError("empty survivor stratum must have no work units")
        else:
            if not units:
                raise ValueError("nonempty survivor stratum has no work units")
            for unit in units:
                self.verify_work_unit(unit)
            units.sort(key=lambda u: int(u["filtered_rank_lo"]))
            if int(units[0]["filtered_rank_lo"]) != 0:
                raise ValueError("filtered cover does not start at zero")
            cursor = 0
            for unit in units:
                lo, hi = int(unit["filtered_rank_lo"]), int(unit["filtered_rank_hi"])
                if lo != cursor:
                    raise ValueError("filtered cover has gap or overlap")
                cursor = hi
            if cursor != self.filtered_terminal_count:
                raise ValueError("filtered cover does not end at survivor count")
        body = {
            "row_id": self.row_id,
            "degree": self.degree,
            "e": self.e,
            "manifest_membership_sha256": self.manifest_membership_certificate()["canonical_sha256"],
            "planned_filtered_cover_exact": True,
            "planned_work_unit_count": len(units),
            "filtered_terminal_count": str(self.filtered_terminal_count),
            "n220_rejected_terminal_count": str(self.n220_rejected_terminal_count),
            "old_stratum_terminal_count": str(self.old_terminal_count),
            "old_partition_identity_exact": self.old_terminal_count == self.n220_rejected_terminal_count + self.filtered_terminal_count,
            "structural_interval_mechanics_only": True,
            "production_leaf_evidence_verified": False,
            "old_domain_fully_disposed_for_n104": False,
            "numerical_leaf_completion_claimed": False,
        }
        return {**body, "canonical_sha256": canonical_sha256(body)}

    def replay_filtered_rank(self, filtered_rank: int) -> dict:
        filtered_rank = int(filtered_rank)
        values = self.filtered.unrank(filtered_rank)
        old_rank = self.filtered.old_rank_of_filtered(filtered_rank)
        disposition = self.filtered.disposition_of_old(old_rank)
        if disposition.get("disposition") != "N220_SURVIVOR":
            raise AssertionError("filtered rank replayed to rejected old rank")
        if int(disposition["filtered_rank"]) != filtered_rank:
            raise AssertionError("filtered/old inverse replay regression")
        return {
            "filtered_rank": filtered_rank,
            "old_rank": old_rank,
            "terminal": list(values),
            "disposition": "N220_SURVIVOR",
        }

    def disposition_of_old_rank(self, old_rank: int) -> dict:
        old_rank = int(old_rank)
        if not 0 <= old_rank < self.old_terminal_count:
            raise ValueError("old canonical rank outside stratum")
        return self.filtered.disposition_of_old(old_rank)

    def validate_complete_execution_cover(self, records: Iterable[Mapping[str, object]]) -> dict:
        # Hostile-audit repair: V1 trusted count + 64-hex commitment shape.
        # V2 has no source-locked production leaf verifier/certificate format,
        # so production completeness credit is unavailable and must fail closed.
        list(records)
        raise ValueError(
            "NO_SOURCE_LOCKED_PRODUCTION_LEAF_VERIFIER_REGISTERED: "
            "N240 V2 cannot mark survivor leaves COMPLETE or release N104 old-domain disposal"
        )
