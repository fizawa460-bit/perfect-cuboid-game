#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[2]
CERT = HERE / "post1697-o266-endpoint-contract.json"


def git_output(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout.strip()


data = json.loads(CERT.read_text())

assert data["schema"] == "STAGE32_EX6_O266_ENDPOINT_CONTRACT_V1"
assert data["status"] == "EXPLORATORY_EXACT_BOUNDED_RESULT"

t = data["fixed_target"]
e = t["exceptional_mass_e"]
O = t["O"]
assert (t["row_id"], t["d"], e, O) == ("g1-d186", 186, 266, 266)

end = data["endpoint_derivation"]
assert end["upper_bound"] == "O <= B <= e = 266"
assert O == e
assert end["B"] == e
assert end["S1"] == e
assert end["all_exceptional_contacts_m1"] is True
assert end["additional_positive_even_contacts"] == 0
assert end["positive_surface_nodes"] == 47
assert end["multibranch_surface_nodes_in_AN_witness"] == 38
assert end["all_FSM_branches_forced_minimal"] is False

local = data["local_feasibility"]
assert local["AN_explicit_endpoint_witness"] is True
assert local["normalization_node_preimages"] == e
assert local["forced_exceptional_locus_delta"] == 0
assert local["remaining_strict_transform_delta"] == 472
assert local["local_scalar_contradiction"] is False

slack = data["two_factor_endpoint_slack"]
assert slack["t"] == 0
r81 = slack["degree81"]["explicit_nonnegative_residual"]
r105 = slack["degree105"]["explicit_nonnegative_residual"]
assert r81["q81_node"] + r81["eta81"] + r81["rho81"] == 52
assert r105["q105_node"] + r105["eta105"] + r105["rho105"] == 28
assert min(r81.values()) >= 0 and min(r105.values()) >= 0
assert slack["minimum_FSM_minimal_branches"] == 186
assert slack["scalar_Hurwitz_contradiction"] is False

ros = data["rosati_endpoint_check"]
assert ros["Gamma_self_intersection"] == 15806
assert ros["sigma_Gamma"] == 1204
assert ros["Q_T"] == 602
assert ros["p_a_Gamma"] == 8090
assert ros["g_Y_at_O266"] == 1 + O // 2 == 134
assert ros["delta_Gamma_at_O266"] == ros["p_a_Gamma"] - ros["g_Y_at_O266"] == 7956
q_replay = 8691 - O // 2 - ros["delta_Gamma_at_O266"]
assert q_replay == ros["identity_replay_at_O266"] == ros["Q_T"] == 602
assert ros["delta_Gamma_at_O266"] >= ros["weierstrass_lower_bound"] == 1924
assert ros["weierstrass_excludes_O266"] is False
assert ros["D4xD4_excludes_Q602"] is False

dec = data["decision"]
assert dec["code"] == "O266_ENDPOINT_NOT_CLOSED"
assert dec["O266_ENDPOINT_EXCLUDED"] is False
assert dec["O266_ENDPOINT_NOT_CLOSED"] is True
assert len(dec["reentry_requires"]) == 4

# Historical evidence must resolve from the locked commit and path to the
# locked Git blob. This intentionally checks actual repository history rather
# than merely comparing strings stored inside the contract.
locks = data["source_locks"]
expected_sources = {
    "odd_branch_note": {
        "head": "131d7869c145563d3c9ee1116a9def9e671a6a63",
        "path": "stages/stage32/residual-32-01-production/post1473-specific-class-multibranch-beauville-odd-branch-wall.md",
        "blob_sha1": "cb20a9b287430c2e238f79d3151500c262905468",
    },
    "modular_factor_note": {
        "head": "0a888aa5195c558e2104c30a4351067ed1828287",
        "path": "stages/stage32/residual-32-01-production/post1484-v6-modular-factor-bidegree-source-note.md",
        "blob_sha1": "deeecac5599f3b542b445cd87c2070dae488bc85",
    },
    "AN_note": {
        "head": "82b551d92ad2ef1a86f8303758c7aa17c0a6d960",
        "path": "stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md",
        "blob_sha1": "512fcc70afb1acf16956fd4b7a2b9b935a052150",
    },
    "AR_note": {
        "head": "82b551d92ad2ef1a86f8303758c7aa17c0a6d960",
        "path": "stages/stage32/residual-32-01-production/post1648ar-two-factor-slack-minimal-branches-source-note.md",
        "blob_sha1": "da9b6ba755b8bd43d5b342d5540053caeb218f57",
    },
    "post1500_rosati_note": {
        "head": "a004dbc8e02fa57fb4c1d374710849aa571dae8e",
        "path": "stages/stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair-source-note.md",
        "blob_sha1": "b0ea281eae453929c292059a919bc1f68b3080b3",
    },
    "AT_note": {
        "head": "82b551d92ad2ef1a86f8303758c7aa17c0a6d960",
        "path": "stages/stage32/residual-32-01-production/post1648at-intermediate-quotient-blowup-conductor-source-note.md",
        "blob_sha1": "59849336b9e49610c00709b58989d17b9df1c6a7",
    },
}
assert set(locks) == set(expected_sources)
for key, expected in expected_sources.items():
    lock = locks[key]
    assert lock == expected
    assert git_output("cat-file", "-t", expected["head"]) == "commit"
    actual_blob = git_output("rev-parse", f'{expected["head"]}:{expected["path"]}')
    assert git_output("cat-file", "-t", actual_blob) == "blob"
    assert actual_blob == expected["blob_sha1"]

fw = data["firewalls"]
assert all(fw[k] is False for k in [
    "stage32_main_modified",
    "Q602_survivors_modified",
    "O212_plus_main_advance",
    "stage32_closure_credit",
    "perfect_cuboid_credit",
    "merge_authorized",
])

print("Stage32EX6 O266 endpoint contract: PASS")
print("endpoint: B=S1=O=e=266; all exceptional contacts have m=1")
print("historical source locks: head:path -> blob replay PASS (6/6)")
print("local endpoint witness: survives")
print("two-factor slack: survives with residuals 52 and 28")
print("Rosati replay: gY=134 deltaGamma=7956 Q=602")
print("decision: O266_ENDPOINT_NOT_CLOSED")
