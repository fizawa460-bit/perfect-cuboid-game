#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROMO = ROOT / "docs" / "stage32-arsenal-promotion.md"
INDEX = ROOT / "docs" / "arsenal" / "index.json"
REVAL = ROOT / "docs" / "arsenal" / "stage32-harvest4-registration-revalidation.json"
MARKER = "# Fourth Stage32 provisional harvest — Harvest 4 ready-wave registration"

WEAPONS = {
    "S32-PW07": ("SUPPORT_MASS_CAP_NECESSARY_PRUNER", "Combine exact exceptional mass/support information with remaining support capacity into a zero-loss necessary pruning inequality on the source-compatible finite population."),
    "S32-PW08": ("FINITE_STABILIZER_CAPACITY_PARITY_ELIMINATOR", "On a complete finite stabilizer family, apply exact capacity elimination and then an exhaustive residual parity discriminator; finite branch forcing only."),
    "S32-PW09": ("NORMALIZATION_CONDUCTOR_EVEN_CORRECTION_COUPLER", "Use Disc(pi)=Br+2A and exact degree accounting to couple normalization/conductor defect to branch degree as a necessary condition."),
    "S32-PW10": ("CELLULAR_SMITH_COKERNEL_ASSEMBLY_OBSTRUCTION", "Compute the actual cellular assembly class in a source-locked Smith cokernel and classify zero/nonzero and torsion order on a complete finite assembly population."),
    "S32-PW11": ("WEIGHTED_LOCAL_DEBT_AND_FACTORWISE_RAMIFICATION_SPLIT", "Track weighted local divisor debt and split nonnode ramification factorwise; retain exact accounting only and do not promote endpoint/effectivity credit."),
    "S32-PW12": ("SOURCE_BOUND_ORBIT_CHARACTER_WITH_ABSOLUTE_MARKING_FIREWALL", "Extract a source-bound abstract orbit-character/direction while certifying that the absolute retained marking torsor remains unresolved."),
}
WORKFLOWS = {
    "S32-WF01": ("SYMBOLIC_FREE_AXIS_EXACT_UNSAT_BLOCK_PARTITION", "Partition a finite outer rank into exact blocks while keeping an independent free axis symbolic through every exact leaf; transfer requires an exact source-model adapter."),
    "S32-WF02": ("CANONICAL_GEOMETRIC_IDENTITY_RECONSTRUCTION_STACK", "Reconstruct exact geometric objects and bind runtime indices to collision-free canonical projective identities; runtime order itself is never semantic identity."),
}


def section(item, kind, role, summary, source_lines, firewall):
    return f"""\n## {item} — {role.lower().replace('_',' ')}\n\n**Type:** `{role}`\n\n**Maturity:** `PROVISIONAL` ({kind})\n\nSource-lock / audit provenance:\n\n```text\n{source_lines}\n```\n\nReusable contract:\n\n{summary}\n\n```text\nHYPOTHESES=exact source/population match plus the source-bound adapters stated above\nAPPLICABILITY=only when object, field, cutoff, canonicalization, multiplicity, measure, quantifiers and adapter hypotheses match\nDO_NOT_USE_FOR={firewall}\nSEMANTIC_CREDIT_BOUNDARY=provisional Arsenal routing only; no Stage32 authority, receiver, theorem, endpoint or Perfect Cuboid credit\n```\n"""


def main():
    reval = json.loads(REVAL.read_text())
    assert reval["status"] == "READY_WAVE_REVALIDATED_REGISTRY_MATERIALIZATION_PENDING"
    assert reval["registration_shape_after_materialization"]["pw13_active"] is False

    text = PROMO.read_text()
    if "AUTHORITY_PRESERVING_FILTERED_RANDOM_ACCESS_ADAPTER" not in text:
        anchor = "## S32-PW03 —"
        insertion = """\n### Harvest 4 extension — authority-preserving filtered random access\n\n`S32-PW01` is extended by audited N230: an exact filtered survivor rank/unrank coordinate may be used for execution while the original canonical rank remains completeness authority. The adapter must retain a reversible bridge to canonical rank and may not replace canonical ordering or grant FULL178/theorem credit. Source: PR #1753 N230, hostile PASS review `5160389467`, exact head `1206475517ed8caf59e92d0d6daa57eb14ab4a41`.\n\n"""
        if anchor not in text:
            raise SystemExit("S32-PW03 anchor missing")
        text = text.replace(anchor, insertion + anchor, 1)

    if MARKER not in text:
        block = "\n" + MARKER + "\n\n```text\nHARVEST=4\nIMPLEMENTATION_PR=1763\nFROZEN_MERGED_SOURCE_UPPER_BOUND=bf2890ec0b8168f70db803de876024aa6b6d1f6d\nRANGE_EXPANDED=false\nREGISTRATION_MATHEMATICAL_CREDIT_CHANGE=0\nS32_PW02_RETIRED_TO_S32_PW01=true\nS32_PW13_ACTIVE=false\n```\n"
        source_by_id = {
            "S32-PW07": "source=PR#1753 N220\nhostile_review=5159411821\naudited_exact_head=940fe99a20c1eaa215126acd92e7c390295bb441",
            "S32-PW08": "source=PR#1688 EX1-05C/05D\nhostile_review=5135375926\naudited_exact_head=93c455e1e69ed65fbfb553462fdcfbc8e2becbae",
            "S32-PW09": "source=PR#1700 EX1-05H\nhostile_review=5136931113\naudited_exact_head=b17e5a32e08adf3c668c07a71f5b2621b3485c87",
            "S32-PW10": "source=PR#1728 cellular Smith terminal bridge\nhostile_review=5147627146\naudited_exact_head=e3c4a04d5010e6dca9428722e334890e2614297a",
            "S32-PW11": "source1=PR#1697@205cf415424a84dbf716c75a61e945165b36912d (nonfreshness re-audit PASS)\nsource2=PR#1715@5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7 (retained provisional, no hostile audit)",
            "S32-PW12": "source=PR#1643\nhostile_review=5123545511\naudited_exact_head=8550ab88e12cbbfd42b2d1e07c8f42be124de1a6",
            "S32-WF01": "source=PR#1742 retained exact UNSAT prefix\nhostile_review=5161068590\naudited_exact_head=a5e59bab3f7fe5a31e356c5a78edcbd741b093a6",
            "S32-WF02": "source1=PR#1742 BC2-01B@4a85517bbe12cc435313fcd9a14be3017c982914 (hostile PASS)\nsource2=PR#1743@2593d86733b3c3a4c276bbbc180c6c52e4a97130 (retained component)",
        }
        for item, (role, summary) in WEAPONS.items():
            firewall = {
                "S32-PW07": "turning necessary finite pruning into feasibility/completeness/theorem credit",
                "S32-PW08": "global geometric existence or Stage closure from finite stabilizer forcing",
                "S32-PW09": "existence from necessary discriminant/conductor degree coupling",
                "S32-PW10": "using abstract Smith group structure without the actual source-bound assembly-to-cokernel map",
                "S32-PW11": "effectivity, global descended tensor, endpoint exclusion or recharging dependent identities",
                "S32-PW12": "selecting an absolute W-line or arithmetic residue from an abstract source-bound character",
            }[item]
            block += section(item, "weapon", role, summary, source_by_id[item], firewall)
        for item, (role, summary) in WORKFLOWS.items():
            firewall = "mathematical exclusion or authority promotion from workflow/infrastructure success alone"
            block += section(item, "workflow", role, summary, source_by_id[item], firewall)
        block += """\n## Harvest 4 held / blocked boundary\n\nThe following are deliberately **not active** in this registration: `S32-PW13`; `ABS-S32-H4-06 -> S32-PW03`; `ABS-S32-H4-12 -> S30-W01/S30-WF01`; `ABS-S32-H4-CF20`. Their existing hold/audit gates remain load-bearing.\n"""
        text += block
    PROMO.write_text(text)

    idx = json.loads(INDEX.read_text())
    s32 = next(x for x in idx["provisional_harvests"] if x.get("source_stage") == "Stage32")
    expected_cards = ["S32-PW01","S32-PW03","S32-PW04","S32-PW05","S32-PW06","S32-PW07","S32-PW08","S32-PW09","S32-PW10","S32-PW11","S32-PW12"]
    s32["active_cards"] = expected_cards
    s32.setdefault("card_roles", {}).update({k:v[0] for k,v in WEAPONS.items()})
    s32.setdefault("card_summaries", {}).update({k:v[1] for k,v in WEAPONS.items()})
    s32["active_workflows"] = ["S32-WF01","S32-WF02"]
    s32["workflow_roles"] = {k:v[0] for k,v in WORKFLOWS.items()}
    s32["workflow_summaries"] = {k:v[1] for k,v in WORKFLOWS.items()}
    s32["provisional_card_count"] = len(expected_cards)
    s32["provisional_workflow_count"] = 2
    s32["provisional_active_entry_count"] = 13
    assert s32.get("retired_merged_ids", {}).get("S32-PW02") == "S32-PW01"
    s32["harvest4_registration"] = {
        "planning_pr": 1755,
        "implementation_pr": 1763,
        "frozen_merged_source_upper_bound": "bf2890ec0b8168f70db803de876024aa6b6d1f6d",
        "range_expanded": False,
        "new_weapon_ids": list(WEAPONS),
        "extended_ids": ["S32-PW01"],
        "new_workflow_ids": list(WORKFLOWS),
        "held_ids_or_extensions": ["S32-PW13","ABS-S32-H4-06 -> S32-PW03","ABS-S32-H4-12 -> S30-W01/S30-WF01","ABS-S32-H4-CF20"],
        "source_revalidation": "docs/arsenal/stage32-harvest4-registration-revalidation.json",
        "arsenal_registration_adds_stage32_mathematical_credit": False,
    }
    INDEX.write_text(json.dumps(idx, indent=2, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    main()
