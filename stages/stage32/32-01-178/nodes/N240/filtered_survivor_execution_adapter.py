#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Iterable, Mapping

HERE = Path(__file__).resolve().parent
N230_DIR = HERE.parent / "N230"
sys.path.insert(0, str(N230_DIR))

from n220_filtered_terminal_indexer import N220FilteredTerminalIndexer

CONTRACT_REV = "STAGE32_32_01_178_N240_FILTERED_EXECUTION_ADAPTER_V1"
FULL178_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
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


class FilteredSurvivorExecutionAdapter:
    """Bridge N230 survivor execution back to N104/N106 old-rank completeness.

    The old CompressedTerminalIndexer rank remains the canonical completeness
    coordinate.  Filtered rank is only a secondary execution coordinate over
    N220 survivors.  A stratum is fully disposed relative to N104 only when:
      (1) the exact audited N220/N230 partition identity is locked, and
      (2) COMPLETE survivor work units cover [0, filtered_terminal_count)
          exactly once with zero unknown/resource-wall counts.

    This class does not run Picard leaves and does not grant numerical credit.
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
        self.filtered = N220FilteredTerminalIndexer(self.genus, self.degree, self.e)
        cert = self.filtered.certificate()
        self.row_id = f"g{self.genus}-d{self.degree:03d}"
        self.old_terminal_count = int(cert["old_terminal_count"])
        self.filtered_terminal_count = int(cert["filtered_terminal_count"])
        self.n220_rejected_terminal_count = int(cert["n220_rejected_terminal_count"])
        if self.n220_rejected_terminal_count + self.filtered_terminal_count != self.old_terminal_count:
            raise AssertionError("N220 partition identity regression")
        if not cert["old_rank_remains_completeness_authority"] or not cert["secondary_rank_only"]:
            raise AssertionError("N230 rank-authority contract regression")

    def partition_certificate(self) -> dict:
        body = {
            "schema": CONTRACT_REV,
            "row_id": self.row_id,
            "genus": self.genus,
            "degree": self.degree,
            "e": self.e,
            "full178_manifest_sha256": FULL178_MANIFEST_SHA256,
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
            "survivor_terminals_require_registered_exact_leaf_disposition": True,
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
        return {
            "contract_rev": CONTRACT_REV,
            "full178_manifest_sha256": FULL178_MANIFEST_SHA256,
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
            "planned_filtered_cover_exact": True,
            "planned_work_unit_count": len(units),
            "filtered_terminal_count": str(self.filtered_terminal_count),
            "n220_rejected_terminal_count": str(self.n220_rejected_terminal_count),
            "old_stratum_terminal_count": str(self.old_terminal_count),
            "old_partition_identity_exact": self.old_terminal_count == self.n220_rejected_terminal_count + self.filtered_terminal_count,
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
        records = list(records)
        units = []
        processed = 0
        for record in records:
            unit = record.get("work_unit")
            if not isinstance(unit, Mapping):
                raise ValueError("execution record missing work_unit")
            self.verify_work_unit(unit)
            if record.get("state") != "COMPLETE":
                raise ValueError("non-COMPLETE survivor work unit")
            if int(record.get("unknown_count", -1)) != 0:
                raise ValueError("survivor work unit has unknown_count")
            if int(record.get("resource_wall_count", -1)) != 0:
                raise ValueError("survivor work unit has resource_wall_count")
            lo, hi = int(unit["filtered_rank_lo"]), int(unit["filtered_rank_hi"])
            expected = hi - lo
            if int(record.get("registered_exact_leaf_disposition_count", -1)) != expected:
                raise ValueError("survivor leaf disposition count mismatch")
            digest = str(record.get("leaf_disposition_commitment_sha256", ""))
            if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
                raise ValueError("missing/invalid leaf disposition commitment")
            units.append(unit)
            processed += expected
        self.validate_planned_cover(units)
        if processed != self.filtered_terminal_count:
            raise ValueError("processed survivor count mismatch")
        body = {
            "row_id": self.row_id,
            "degree": self.degree,
            "e": self.e,
            "n220_rejected_terminal_count": str(self.n220_rejected_terminal_count),
            "processed_survivor_terminal_count": str(processed),
            "old_stratum_terminal_count": str(self.old_terminal_count),
            "old_domain_fully_disposed_relative_to_registered_leaf_contract": True,
            "full178_global_complete": False,
        }
        return {**body, "canonical_sha256": canonical_sha256(body)}
