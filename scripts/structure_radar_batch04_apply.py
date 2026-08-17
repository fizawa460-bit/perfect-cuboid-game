#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RADAR = ROOT / "docs" / "structure-radar"
PROGRESS = RADAR / "progress.json"
REGISTRY = RADAR / "structure-registry.json"
QUEUE = RADAR / "exploration-queue.json"
PARTS = RADAR / "source-manifest"

BATCH_ID = "SR-BATCH-STAGE16_25_CURRENT-04-R01"
TASK_ID = "SR-CENSUS-STAGE16_25_CURRENT-01"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


progress = load(PROGRESS)
registry = load(REGISTRY)
queue = load(QUEUE)

ready = next((t for t in queue["tasks"] if t.get("status") == "READY"), None)
if not ready or ready.get("task_id") != TASK_ID or ready.get("group") != "STAGE16_25_CURRENT":
    raise SystemExit(f"unexpected ready task: {ready}")
source_ids = ready["source_ids"]
if len(source_ids) != 60:
    raise SystemExit(f"expected 60 sources, got {len(source_ids)}")

source_map = {}
path_map = {}
for part in sorted(PARTS.glob("part-*.json")):
    for src in load(part)["sources"]:
        source_map[src["source_id"]] = src
        path_map[src["path"]] = src

missing = [sid for sid in source_ids if sid not in source_map]
if missing:
    raise SystemExit(f"missing source metadata: {missing}")

cards = {c["structure_id"]: c for c in registry["structures"]}
for sid in ["SR-STR-006", "SR-STR-008", "SR-STR-016", "SR-STR-018", "SR-STR-055", "SR-STR-145"]:
    if sid not in cards:
        raise SystemExit(f"missing existing card {sid}")


def prov(path: str, locator: str):
    src = path_map[path]
    return {
        "source_id": src["source_id"],
        "path": path,
        "locator": locator,
        "fingerprint": src["fingerprint"],
    }


def upsert_prov(card_id: str, path: str, locator: str):
    card = cards[card_id]
    p = prov(path, locator)
    replaced = False
    out = []
    for old in card.get("repo_provenance", []):
        if old.get("source_id") == p["source_id"] or old.get("path") == path:
            if not replaced:
                out.append(p)
                replaced = True
        else:
            out.append(old)
    if not replaced:
        out.append(p)
    card["repo_provenance"] = out


# Existing-card provenance upgrades on the newly reviewed current slice.
upsert_prov("SR-STR-006", "stages/stage23/23-70/result.md", "Stage23 closeout pair-overlap zero-density transition")
upsert_prov("SR-STR-055", "stages/stage24/24-10/result.md", "literal Stage18-to-Stage19 subset contract and squareclass predicate")
upsert_prov("SR-STR-008", "stages/stage24/24-30/result.md", "space-square geometrically integral degree-two thin-cover proof")
upsert_prov("SR-STR-008", "stages/stage24/24-70/result.md", "thin-but-infinite Stage24 closeout interface")
upsert_prov("SR-STR-016", "stages/stage24/24-50/result.md", "mixed-parity C17 positive-rank exactly-two construction")
upsert_prov("SR-STR-016", "stages/stage24/final.md", "self-contained C17 construction and sqrt(log B) lower interface")
upsert_prov("SR-STR-018", "stages/stage24/24-60/result.md", "Stage24 interaction cross-ratio bounds and unresolved sign")
upsert_prov("SR-STR-018", "stages/stage25/25-10/result.md", "two exact path factorizations for the combined M1-to-N2 transition")
upsert_prov("SR-STR-145", "stages/stage24/24-30/result.md", "fixed-prime paired-squareclass local-sieve zero-density route")

new_cards = [
    {
        "structure_id": "SR-STR-152",
        "canonical_math_name": "Already-space pair-overlap thinning for the second-face transition",
        "exact_equations_or_object": "On the Stage17 source host, x^2+y^2=p^2 and p^2+z^2=d^2 are already imposed. Entering Stage19 requires x^2+z^2=q^2 or y^2+z^2=q^2. The same-host pair-overlap theorem gives N2(B)<=P(B)=o(B(log B)^3), hence N2(B)/N1(B)->0 without charging the space condition again.",
        "search_terms_primary": [
            "pair overlap thinning inside integral space Pythagorean chain",
            "second face cross leg compatibility zero density"
        ],
        "search_terms_aliases": [
            "Stage23 source-host causal zero density",
            "already-space pair-overlap mechanism"
        ],
        "theorem_species": [
            "pair-overlap zero density",
            "causal decomposition",
            "no-double-charge firewall"
        ],
        "repo_provenance": [
            prov("stages/stage23/23-70/result.md", "accepted checkpoint60 pair-overlap causal synthesis"),
            prov("stages/stage23/23-70/self-contained-bundle.md", "self-contained Stage23 pair-overlap transition interface"),
        ],
        "target_populations": [
            "matched Stage17 exactly-one-face-plus-space and Stage19 exactly-two-face-plus-space populations"
        ],
        "potential_weapon_types": [
            "ZERO_DENSITY",
            "CAUSAL_DECOMPOSITION",
            "NO_DOUBLE_CHARGE_FIREWALL"
        ],
        "applicability_gaps": [
            "This proves qualitative lower-order pair-overlap thinning only; it does not derive the inherited half-power N2 upper rate."
        ],
        "existing_radar_overlap": [
            "SR-STR-006",
            "SR-STR-145"
        ],
        "search_status": "NOT_SEARCHED",
        "arsenal_decision": "PENDING",
        "card_status": "SUBMITTED_FOR_AUDIT"
    },
    {
        "structure_id": "SR-STR-153",
        "canonical_math_name": "Odd-odd Stage15-2 family mod-16 space-lift annihilation",
        "exact_equations_or_object": "For the historical Stage15-2 explicit exactly-two ambient family with coprime odd p,q, the space condition is R^2=17(p^4+q^4). Since p^4=q^4=1 mod 16, the right side is 2 mod 16, impossible for an integer square; the entire odd-odd specialization has zero Stage19 survivors.",
        "search_terms_primary": [
            "Stage15-2 odd odd family mod 16 obstruction",
            "17 p4 q4 space diagonal square obstruction"
        ],
        "search_terms_aliases": [
            "ambient linear family space-lift death certificate",
            "odd-odd two-face family annihilation"
        ],
        "theorem_species": [
            "congruence obstruction",
            "family exclusion",
            "lower-family filter"
        ],
        "repo_provenance": [
            prov("stages/stage23/23-70/result.md", "global mod-16 exclusion of the historical odd-odd specialization"),
            prov("stages/stage24/24-60/result.md", "odd-odd dead versus mixed-parity infinite stratum comparison"),
            prov("stages/stage24/24-70/result.md", "closeout arithmetic-stratum heterogeneity ledger"),
        ],
        "target_populations": [
            "odd-odd specialization of the Stage15-2 primitive exactly-two ambient construction tested for integral space diagonal"
        ],
        "potential_weapon_types": [
            "LOCAL_OBSTRUCTION",
            "SLICE_EXCLUSION",
            "LOWER_FAMILY_FILTER"
        ],
        "applicability_gaps": [
            "The obstruction is parity-specific: the broader mixed-parity formula contains the infinite C17 family, so this is not a global Stage19 upper theorem."
        ],
        "existing_radar_overlap": [
            "SR-STR-016",
            "SR-STR-150"
        ],
        "search_status": "NOT_SEARCHED",
        "arsenal_decision": "PENDING",
        "card_status": "SUBMITTED_FOR_AUDIT"
    },
    {
        "structure_id": "SR-STR-154",
        "canonical_math_name": "Exact matched M2-to-N2 finite census through one million",
        "exact_equations_or_object": "Under the identical primitive canonical R<=B Stage24 contract, exact matched counts are tabulated through B=1,000,000; at the endpoint M2=13,817,725 and N2=255, with directional target counts (98,101,56). The later-window effective slopes are diagnostic only and are explicitly not promoted to an asymptotic exponent.",
        "search_terms_primary": [
            "matched M2 N2 exact finite census one million",
            "two-face space survivor finite oracle"
        ],
        "search_terms_aliases": [
            "Stage24 checkpoint20 matched panel",
            "M2 to N2 regression oracle"
        ],
        "theorem_species": [
            "certified computation",
            "matched finite census",
            "regression oracle"
        ],
        "repo_provenance": [
            prov("stages/stage24/24-20/result.md", "exact matched census and source-level revalidation through B=1,000,000"),
            prov("stages/stage24/24-70/result.md", "closeout finite-census summary and non-extrapolation boundary"),
        ],
        "target_populations": [
            "matched primitive canonical Stage18 M2 and Stage19 N2 populations under R<=B"
        ],
        "potential_weapon_types": [
            "NUMERICAL_ORACLE",
            "REGRESSION_ORACLE"
        ],
        "applicability_gaps": [
            "Finite effective slopes and directional ordering prove no asymptotic exponent or limiting direction law; unmatched larger-N2 thresholds must not be inserted into this ratio panel."
        ],
        "existing_radar_overlap": [
            "SR-STR-014",
            "SR-STR-076"
        ],
        "search_status": "DEFERRED_WITH_REASON",
        "arsenal_decision": "PENDING",
        "card_status": "SUBMITTED_FOR_AUDIT"
    },
    {
        "structure_id": "SR-STR-155",
        "canonical_math_name": "Fixed rational-curve sub-square-root ceiling and moving-family gate",
        "exact_equations_or_object": "With exact physical Kummer height H_M=d=R, the M.C=4 physical rational-bisection mechanism is empty. Hence every fixed physical rational curve has M.C>=5 and contributes O(B^(2/5+o(1))); every fixed finite union is strict sub-square-root. No uniform implied constant or o(1) is proved across a B-dependent moving family, leaving the moving Jacobi/Kummer first-small-point gate unresolved.",
        "search_terms_primary": [
            "Kummer fixed rational curve degree four void B two fifths",
            "moving genus one family uniform summation gate"
        ],
        "search_terms_aliases": [
            "Stage24 fixed-curve localization",
            "moving-family half-power barrier"
        ],
        "theorem_species": [
            "height geometry",
            "fixed-curve upper bound",
            "quantifier firewall"
        ],
        "repo_provenance": [
            prov("stages/stage24/24-40/result.md", "repaired fixed-curve degree-four void and 2/5 ceiling"),
            prov("stages/stage24/24-70/result.md", "closeout fixed-curve versus moving-family boundary"),
            prov("stages/stage24/final.md", "self-contained fixed-curve and moving-family upper-attack boundary"),
        ],
        "target_populations": [
            "Stage19 physical Kummer/Jacobi space-diagonal survivors under R<=B"
        ],
        "potential_weapon_types": [
            "UPPER_BOUND",
            "GEOMETRY_ADAPTER",
            "EXTERNAL_GATE",
            "NO_DOUBLE_CHARGE_FIREWALL"
        ],
        "applicability_gaps": [
            "The per-fixed-curve B^(2/5+o(1)) estimate cannot be summed over a growing family without a new uniform theorem; no whole-family strict sub-square-root bound follows."
        ],
        "existing_radar_overlap": [
            "SR-STR-068",
            "SR-STR-151"
        ],
        "search_status": "NOT_SEARCHED",
        "arsenal_decision": "PENDING",
        "card_status": "SUBMITTED_FOR_AUDIT"
    },
]

existing_ids = {c["structure_id"] for c in registry["structures"]}
for card in new_cards:
    if card["structure_id"] in existing_ids:
        raise SystemExit(f"new card id already exists: {card['structure_id']}")
    registry["structures"].append(card)
    cards[card["structure_id"]] = card

registry["status"] = "BATCH_SUBMITTED_FOR_AUDIT"

# Build source->structure carrier map from provenance touched in this batch.
carrier = {}
for card_id in ["SR-STR-006", "SR-STR-008", "SR-STR-016", "SR-STR-018", "SR-STR-055", "SR-STR-145", "SR-STR-152", "SR-STR-153", "SR-STR-154", "SR-STR-155"]:
    card = cards[card_id]
    for p in card["repo_provenance"]:
        sid = p["source_id"]
        if sid in source_ids:
            carrier.setdefault(sid, set()).add(card_id)

for sid in source_ids:
    src = source_map[sid]
    ids = sorted(carrier.get(sid, set()))
    review = {
        "fingerprint": src["fingerprint"],
        "status": "STRUCTURES_RECORDED" if ids else "DUPLICATE_SOURCE",
        "batch_id": BATCH_ID,
    }
    if ids:
        review["structure_ids"] = ids
    progress["source_reviews"][sid] = review

# Replace any pre-existing batch entry only if an interrupted retry exists.
audit_batches = [b for b in progress.get("audit_batches", []) if b.get("batch_id") != BATCH_ID]
carrier_count = sum(1 for sid in source_ids if carrier.get(sid))
audit_batches.append({
    "batch_id": BATCH_ID,
    "task_id": TASK_ID,
    "status": "SUBMITTED_FOR_AUDIT",
    "source_ids": source_ids,
    "sources_reviewed": len(source_ids),
    "structures_added": len(new_cards),
    "structures_updated": 6,
    "structures_deduped": len(source_ids) - carrier_count,
    "structure_carrier_sources": carrier_count,
    "searches_completed": 0,
    "arsenal_decisions": 0,
    "audit_required": True,
})
progress["audit_batches"] = audit_batches

dump(REGISTRY, registry)
dump(PROGRESS, progress)
print(f"applied {BATCH_ID}: sources={len(source_ids)} carriers={carrier_count} added={len(new_cards)}")
