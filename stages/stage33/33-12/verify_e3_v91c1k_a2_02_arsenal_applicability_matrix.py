#!/usr/bin/env python3
"""Verify V91C1K Arsenal applicability matrix for the A2_02 marked proper14 gap.

The V91C1K certificate is an immutable historical snapshot.  Later Arsenal
harvests may regenerate a provisional card without changing the bounded
applicability conclusion.  In that case we accept only an explicitly locked
successor blob and verify the successor preserves the relevant failure
contract; we do not rewrite the historical certificate or infer new credit.
"""
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent; S33=HERE.parent; ROOT=S33.parent.parent
CERT=HERE/'e3-v91c1k-a2-02-arsenal-applicability-matrix.json'
LOCKS={
 HERE/'e3-v91c1d-a2-02-purity-cech-cartier-assembly.json':'fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14',
 HERE/'e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json':'5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f',
 HERE/'e3-v91c1i-a2-02-audited-localization-zero-fingerprint.json':'241112a8dceaae61027b803438f3dd5b34f3f85387b95c02b6d490666011213c',
 HERE/'e3-v91c1j-a2-02-global-hs-d2-scope-firewall.json':'8b415428c34464515d6c77c36f01575b93a414734d6b887697afda404ffc38e0',
 HERE/'e3-proper14-dual-to-discriminant-quotient-bridge-v89.json':'26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639',
 HERE/'e3-retained-at-marked-picard-dual-source-v91.json':'729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9'}
HISTORICAL_CARD_BLOBS={
 'S33-PW04':'1702de010168d91d587bb6fb0966358c76e6e505',
 'S33-PW07':'7f1337858bc6f9006e101d810dd72e67aef534fd',
 'S33-PW08':'c9e13a917811581578f833ea93619d85f717be6d'}
CURRENT_CARD_BLOBS={
 'docs/arsenal/cards/provisional/S33-PW04.md':'ba4ee397738aa0f3afef7c77bb7d5e2c19134076',
 'docs/arsenal/cards/provisional/S33-PW07.md':'7f1337858bc6f9006e101d810dd72e67aef534fd',
 'docs/arsenal/cards/provisional/S33-PW08.md':'c9e13a917811581578f833ea93619d85f717be6d'}
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,e):
 o=json.loads(p.read_text()); b=dict(o); h=b.pop('canonical_sha256'); assert h==e and csha(b)==e; return o
for p,e in LOCKS.items(): load(p,e)
c=load(CERT,'16ccf10acd65fd7101acd6a776771896cd3e3e91aa3a2bd49dba43e0d6cd11b3')
# The immutable V91C1K certificate must still record its original three-card snapshot.
for name,old in HISTORICAL_CARD_BLOBS.items():
 assert c['source_locks'][name]['git_blob_sha1']==old
# Current checkout may contain the audited post-#1478 PW04 harvest successor only.
for p,e in CURRENT_CARD_BLOBS.items():
 got=subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip(); assert got==e,(p,got,e)
pw04=(ROOT/'docs/arsenal/cards/provisional/S33-PW04.md').read_text(encoding='utf-8')
assert 'Role | `EXACT_MARKED_SOURCE_ADAPTER`' in pw04
assert 'Post-#1478 extension source lock:' in pw04
assert 'When that source-bound quotient witness is missing' in pw04
assert 'This extension adds a failure contract to PW04' in pw04
assert 'does not make the V91C1F Stage33 source itself a successful marked image' in pw04
m=c['applicability_matrix']; assert set(m)=={'S33-PW04','S33-PW07','S33-PW08'}
assert all(x['closes_current_interface'] is False for x in m.values())
assert m['S33-PW08']['exact_a2_02_absolute_localization_value']=='ZERO'
assert m['S33-PW08']['zero_value_is_discriminating_among_source_directions'] is False
assert c['exact_consequence']['a2_02_marked_brauer_image_computed'] is False
assert c['exact_consequence']['arsenal_miss_proves_repository_absence'] is False
assert c['entry_chain']['combined_hostile_audit_pending'] is True
assert c['credit_firewall']['stage33_progress']=='6/11' and c['credit_firewall']['merge_allowed'] is False
print(json.dumps({'success':True,'certificate_sha256':c['canonical_sha256'],'historical_cards_checked':3,'current_pw04_successor_blob':'ba4ee397738aa0f3afef7c77bb7d5e2c19134076','current_interface_closed':False,'stage33_progress':'6/11'},sort_keys=True))
