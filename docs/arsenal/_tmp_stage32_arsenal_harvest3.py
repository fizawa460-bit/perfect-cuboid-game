#!/usr/bin/env python3
from pathlib import Path
import json

promo = Path('docs/stage32-arsenal-promotion.md')
marker = '## S32-PW06 — basis-independent symplectic transvection candidate pruning'
text = promo.read_text()
assert marker not in text, 'PW06 section already present'
addition = r'''

# Second Stage32 provisional harvest — post-#1478

```text
SECOND_HARVEST_KIND=POST1478_PROVISIONAL_PROMOTION
PREVIOUS_ARSENAL_INTEGRATION_PR=1478
PREVIOUS_ARSENAL_MERGE_COMMIT=b5b810be420eedc74cfa8074ae043d681598b412
DISCOVERY_LOWER_BOUND=b5b810be420eedc74cfa8074ae043d681598b412
HARVEST_UPPER_BOUND=714bd143f0c20082edcbb81c3905a86b1a56b4bf
RANGE_EXPANDED_AFTER_DISCOVERY=false
NEW_ACTIVE_PROVISIONAL_WEAPONS=S32-PW06
EXISTING_CARD_EXTENSIONS=NONE
NEW_WORKFLOW_IDS=NONE
PROMOTION_BLOCKED_CANDIDATES=ORBIT_SUM_STABILIZER_COMMUTATOR,SOURCE_BOUND_GEOMETRIC_ORBIT_CHARACTER
FORMAL_PROMOTION=false
STAGE32_MAIN_MATHEMATICAL_CREDIT_CHANGE=0
```

This second harvest preserves the first provisional harvest and the retired-ID rule `S32-PW02 -> S32-PW01`. It registers only the post-#1478 result whose hostile-audit provenance is recoverable from the frozen source itself. Later Stage32 main movement is not part of this harvest.

## S32-PW06 — basis-independent symplectic transvection candidate pruning

**Type:** `BASIS_INDEPENDENT_SYMPLECTIC_TRANSVECTION_PRUNER`

Authoritative source provenance:

```text
source_pr=1505
source_exact_audited_head=efb26374a5d46dd6118428306ae6dcee417a1041
hostile_reaudit_review=5102652713
certificate_path=stages/stage32/residual-32-01-production/post1505-o210-q602-weierstrass-parity-transvection-refinement.json
certificate_blob_sha=8e9a402706921c71217fc275be6b9885feea8bee
certificate_canonical_sha256=83fd16fdaac674a3f63b4b2dac498136f1bc584c9e06d89f1aa1a7bdc4c30386
certifier_path=stages/stage32/residual-32-01-production/certify_stage32_post1505_o210_q602_weierstrass_parity_transvection_refinement.py
certifier_blob_sha=825fb92370ef18f4f6f1c8b5028134f260cac66d
replay_workflow=.github/workflows/stage32-post1505-o210-q602-weierstrass-parity-transvection-refinement.yml
replay_workflow_blob_sha=acfc88fff6e18994e0e7a4db25d5eaefa9b391bd
```

Reusable contract:

```text
INPUT=
  exact finite symplectic F2-module V
  + exact finite candidate operators T on V
  + source-bound subspace W <= V
  + source-derived geometric branch transposition/parity action
  + exact symplectic/Weil pairing

CONSTRUCTION=
  reconstruct the geometric involution/transposition on V
  -> prove it is a nonidentity rank-one symplectic transvection
  -> use the intrinsic predicate
       rank(T-I)=1,
       T symplectic,
       0 != im(T-I) <= W
  -> filter the finite operator/marking candidate set

OUTPUT=
  the exact subset of candidates compatible with the source-derived
  transvection predicate, without choosing an absolute marked line in W
```

```text
HYPOTHESES=complete finite candidate population; exact symplectic pairing; exact source-derived transposition/parity action; exact source-bound W; exact arithmetic over F2
APPLICABILITY=finite symplectic candidate sets where geometric parity/transposition data determines an intrinsic transvection constraint before an absolute marking is available
DO_NOT_USE_FOR=identifying an individual nonzero W-line; treating a gauge representative as an absolute source marking; inferring semantic/geometric identity from abstract group type; extending finite pruning to theorem/receiver/endpoint credit
SEMANTIC_CREDIT_BOUNDARY=exact finite candidate pruning only; no absolute marking, arithmetic exclusion, carrier existence, receiver, route, theorem, endpoint, or perfect-cuboid credit
```

Stage32's `16 -> 3`, residues `73,97,235`, concrete Weierstrass labels, and individual retained W-lines are provenance only and are not reusable constants.

Nearest existing Arsenal interfaces:

- `S30-W01` identifies a concrete source-target finite action using a semantic anchor; PW06 instead consumes source-derived geometric transvection data to prune operator/marking candidates without completing an absolute adapter.
- `S32-PW05` consumes an already validated finite action and invariant seed relation to reconstruct a full relation table; PW06 outputs a filtered candidate set and does not reconstruct an invariant table.
- `S30-WF01` remains the audit firewall after pruning: finite survival or a gauge representative is not semantic identification.

## Second-harvest promotion blockers retained as provenance

### Orbit-sum stabilizer / blow-down commutator candidate — not registered

```text
classification=GENUINELY_NEW_INTERFACE_BUT_PROMOTION_BLOCKED
source_pr=1570
source_exact_head=80de2c23979a691a8255baa221e31ad4b6f93f49
certificate_path=stages/stage32/residual-32-01-production/post1566-orbit-sum-commutator-batch.json
certificate_blob_sha=b3daf670f62878c8b0830df6c63df6665fef50e7
certificate_canonical_sha256=d96ae71a5a863b66160d510ec26c913aeddec8b3f9aa8709305114aecfe2ee9b
certifier_path=stages/stage32/residual-32-01-production/certify_stage32_post1566_orbit_sum_commutator_batch.py
certifier_blob_sha=b5e8194982b74458c36b490adeaa343d0e50b20b
diagnostic_path=stages/stage32/residual-32-01-production/diagnose_stage32_post1566_orbit_sum_commutator.py
diagnostic_blob_sha=53e9f81813af13637ce62d4bd8770b81b4b23fb2
blocker=exact hostile-re-audit receipt for the V2 blow-down repair is not recoverable from the frozen repository/PR review surface inspected by this harvest
```

Do not revive the withdrawn V1 strict-transform bridge. The reusable V2 idea is quotient stabilizer -> noninvariance -> equivariant injective pullback -> correspondence commutator, but it remains unregistered until audit provenance is closed.

### Source-bound geometric orbit-character candidate — not registered

```text
classification=GENUINELY_NEW_INTERFACE_BUT_ACTIVE_AUTHORITY_NOT_ESTABLISHED_AT_FROZEN_BOUND
source_pr=1643
source_exact_head=8550ab88e12cbbfd42b2d1e07c8f42be124de1a6
certificate_path=stages/stage32/residual-32-01-production/post1623-hperp-v6-hdeck-character-preflight.json
certificate_blob_sha=f9bf3da925fc66505900db793f48c507725461d1
certificate_canonical_sha256=00843ec64f7ecd522614f750c9f84d3a746ce664064d1c4413784cab9d26791c
verifier_path=stages/stage32/residual-32-01-production/verify_stage32_post1623_hperp_v6_hdeck_character_preflight.py
verifier_blob_sha=80282c3bb31bee826aa7d751a5af8cb8c015f68a
diagnostic_path=stages/stage32/residual-32-01-production/diagnose_stage32_post1623_hperp_v6_hdeck_anchor.py
diagnostic_blob_sha=a1d857180921688c5cf22a428a102bb2cd26b6c7
blocker=frozen MAIN-STATE still names PR 1621 as latest hostile-audited Stage32 authority; the PR1643 preflight therefore cannot be promoted by this harvest alone
```

The source-bound character extraction `geometric orbit profile -> exact H-character -> abstract torsion direction` remains a future candidate. It grants no absolute retained-coordinate identification.

## Second-harvest workflow dedup

No new Stage32 workflow ID is created.

```text
minimal source-locked action adapter completion
  -> S30-W01 + S30-WF01 + existing SOURCE_LOCKED_ADAPTER_WALL

gauge orbit != absolute source marking
  -> S30-W01 / S30-WF01

ambient automorphism != action on a particular geometric member
abstract lift != retained marked Picard/lattice action
  -> existing SOURCE_LOCKED_ADAPTER_WALL + S30-WF03 credit firewall

bounded search miss != repository absence/nonexistence
  -> existing Research OS repository-asset-discovery policy
```

## Second-harvest nonpromotion / credit firewall

The following remain Stage32-specific or historical only: Q602 residue numbers, named Stoll words, concrete W-line labels, Hperp curve labels, exceptional labels/ranks, cusp/normalizer failures, the exceptional-supported direct mod-2 fiber identity, and the withdrawn strict-transform bridge.

```text
ARSENAL_REGISTRATION_IMPLIES_STAGE32_PROGRESS_INCREMENT=false
ARSENAL_REGISTRATION_IMPLIES_STAGE32_MAIN_AUTHORITY_CHANGE=false
ARSENAL_REGISTRATION_IMPLIES_STAGE32_CLOSURE=false
ARSENAL_REGISTRATION_IMPLIES_RECEIVER_CREDIT=false
ARSENAL_REGISTRATION_IMPLIES_ROUTE_CREDIT=false
ARSENAL_REGISTRATION_IMPLIES_THEOREM_CREDIT=false
ARSENAL_REGISTRATION_IMPLIES_ENDPOINT_CREDIT=false
ARSENAL_REGISTRATION_IMPLIES_PERFECT_CUBOID_CONCLUSION=false
```
'''
promo.write_text(text.rstrip() + addition + '\n')

idx = Path('docs/arsenal/index.json')
data = json.loads(idx.read_text())
stage32 = next(h for h in data['provisional_harvests'] if h['source_stage'] == 'Stage32')
assert stage32['active_cards'] == ['S32-PW01','S32-PW03','S32-PW04','S32-PW05']
assert stage32['retired_merged_ids'] == {'S32-PW02':'S32-PW01'}
stage32['active_cards'].append('S32-PW06')
stage32['card_roles']['S32-PW06'] = 'BASIS_INDEPENDENT_SYMPLECTIC_TRANSVECTION_PRUNER'
stage32.setdefault('card_summaries', {})['S32-PW06'] = 'use source-derived geometric transposition/parity data to impose an intrinsic rank-one symplectic-transvection predicate and prune a complete finite operator/marking candidate set without choosing an absolute marked line'
stage32['provisional_card_count'] = 5
stage32['provisional_active_entry_count'] = 5
stage32['post1478_harvest'] = {
    'previous_arsenal_integration_pr': 1478,
    'previous_arsenal_merge_commit': 'b5b810be420eedc74cfa8074ae043d681598b412',
    'discovery_lower_bound': 'b5b810be420eedc74cfa8074ae043d681598b412',
    'harvest_upper_bound': '714bd143f0c20082edcbb81c3905a86b1a56b4bf',
    'range_expanded_after_harvest1': False,
    'new_weapon_ids': ['S32-PW06'],
    'extended_ids': [],
    'new_workflow_ids': [],
    'promotion_blocked_candidates': [
        {'role':'ORBIT_SUM_STABILIZER_TO_QUOTIENT_NONINVARIANCE_AND_COMMUTATOR','source_pr':1570,'source_exact_head':'80de2c23979a691a8255baa221e31ad4b6f93f49','certificate':'stages/stage32/residual-32-01-production/post1566-orbit-sum-commutator-batch.json','certificate_blob_sha':'b3daf670f62878c8b0830df6c63df6665fef50e7','canonical_sha256':'d96ae71a5a863b66160d510ec26c913aeddec8b3f9aa8709305114aecfe2ee9b','blocker':'V2 hostile-re-audit receipt not recoverable from frozen repository/PR review surface'},
        {'role':'SOURCE_BOUND_GEOMETRIC_ORBIT_CHARACTER_EXTRACTION','source_pr':1643,'source_exact_head':'8550ab88e12cbbfd42b2d1e07c8f42be124de1a6','certificate':'stages/stage32/residual-32-01-production/post1623-hperp-v6-hdeck-character-preflight.json','certificate_blob_sha':'f9bf3da925fc66505900db793f48c507725461d1','canonical_sha256':'00843ec64f7ecd522614f750c9f84d3a746ce664064d1c4413784cab9d26791c','blocker':'frozen MAIN-STATE does not establish PR1643 as hostile-audited active Stage32 authority'}
    ],
    'workflow_dedup': {
        'new_workflow_ids': [],
        'source_locked_action_completion': ['S30-W01','S30-WF01','SOURCE_LOCKED_ADAPTER_WALL'],
        'gauge_orbit_not_absolute_marking': ['S30-W01','S30-WF01'],
        'typed_action_adapter_wall': ['SOURCE_LOCKED_ADAPTER_WALL','S30-WF03'],
        'bounded_search_miss': 'RESEARCH_OS_POLICY_ALREADY_COVERS'
    },
    'historical_or_stage32_specific_promoted': False,
    'promotion_status': 'PROVISIONAL_POST1478_HARVEST_PENDING_HOSTILE_AUDIT',
    'arsenal_registration_adds_stage32_mathematical_credit': False
}

rels = data.setdefault('cross_stage_relationships', [])
additions = [
    {'source':'S30-W01','target':'S32-PW06','relation':'COMPLEMENTARY_NOT_DUPLICATE','note':'S30-W01 semantically identifies concrete finite actions; S32-PW06 uses already source-derived geometric transvection data to prune candidate operators/markings without completing an absolute adapter.'},
    {'source':'S32-PW05','target':'S32-PW06','relation':'DISTINCT_FINITE_OUTPUT_CONTRACTS','note':'PW05 reconstructs an invariant relation table from a validated action and orbit-covering seeds; PW06 filters a finite candidate operator/marking population by an intrinsic symplectic-transvection predicate.'},
    {'source':'S30-WF01','target':'S32-PW06','relation':'POST_PRUNING_SEMANTIC_IDENTIFICATION_FIREWALL','note':'survival under the PW06 intrinsic predicate, or choosing a gauge representative, does not by itself identify the absolute source marking.'}
]
existing={(r.get('source'),r.get('target'),r.get('relation')) for r in rels}
for r in additions:
    k=(r['source'],r['target'],r['relation'])
    if k not in existing:
        rels.append(r); existing.add(k)

fw = data.setdefault('firewalls', {})
fw['arsenal_registration_implies_stage32_progress_increment'] = False
fw['arsenal_registration_implies_stage32_main_authority_change'] = False
fw['arsenal_registration_implies_stage32_closure'] = False
idx.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
