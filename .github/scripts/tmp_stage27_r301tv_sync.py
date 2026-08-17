from pathlib import Path
import json

root = Path('stages/stage27')
t = root/'27-20-r301t'; u = root/'27-20-r301u'; v = root/'27-20-r301v'; b = root/'27-20-r301t-v'
for p in (t,u,v,b):
    p.mkdir(parents=True, exist_ok=True)

t.joinpath('result.md').write_text(r'''# Stage27-20-r301t — occupied q1 support embeds into Stage14 active-face support by an exact Möbius adapter

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301s
SOURCE_STAGE=Stage20

## 1. Exact coordinate adapter

For a primitive oriented Stage14 face
\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]
use the frozen rational-circle coordinate
\[
q_0=u/v\in(0,1),\qquad
(S,X,H)=\delta^{-1}(v^2-u^2,2uv,v^2+u^2),\quad \delta\in\{1,2\}.
\]
The Stage20/27 torus coordinate attached to the same oriented face is
\[
q_1=\frac{H+X}{S}.
\]
Substitution gives
\[
\boxed{q_1=\frac{v+u}{v-u}=\frac{1+q_0}{1-q_0}},\qquad
\boxed{q_0=\frac{q_1-1}{q_1+1}}.
\]
Thus physical `q1>1` and Stage14 `q0 in (0,1)` determine each other uniquely. The primitive oriented face is reconstructed from reduced `u/v`; the parity factor `delta` is fixed by primitiveness.

## 2. Support injection

Let `Q(B)` be the occupied first-coordinate support from r301s. Every Stage27 survivor contributing an occupied `q1` contains the corresponding oriented primitive integral face, hence that face is an active Stage14 vertex at the same space-diagonal cutoff. Therefore
\[
\boxed{Q(B)\hookrightarrow V(B)}.
\]
Forgetting first-face orientation introduces at most an absolute face-swap multiplicity. No fixed power is lost.

This is deliberately only an injection. Stage14 `V(B)` also contains the other endpoint of each raw two-face edge and vertices from triple objects; equality with all active vertices is not asserted.

## 3. Packet transfer

The Stage14 complete packet decomposition can therefore be restricted to occupied `q1` support with at most its audited `B^o(1)` cell/decorative multiplicity. This reproduces the half-power ceiling but does not improve it by itself.

```text
STAGE27_20_R301T_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
Q1_TO_STAGE14_FACE_MOBIUS_ADAPTER_PROVED=true
Q1_TO_ACTIVE_FACE_SUPPORT_INJECTION_PROVED=true
Q1_EQUALS_ALL_STAGE14_ACTIVE_VERTICES_CLAIMED=false
FIXED_POWER_LOSS_IN_ADAPTER=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301u
```
''')

u.joinpath('result.md').write_text(r'''# Stage27-20-r301u — fixed-distance off-wall occupied support is strictly sub-half

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301t
SOURCE_STAGE=Stage20

Stage14 Proposition 3.6 gives the complete nonproportional host bounds
\[
E_k\le 3\theta-\frac14\quad(\theta\le1/4),\qquad
E_{\rm RRF}\le1-2\theta\quad(\theta\ge1/4),
\]
and the proportional branch is `<=7/16`.
By r301t, occupied first-coordinate support is a subset of this same active-face measure; no independent saving is multiplied into another ledger.

Fix a constant `eta>0`. If `theta<=1/4-eta`, then
\[
E_k\le\frac12-3\eta.
\]
If `theta>=1/4+eta`, then
\[
E_{\rm RRF}\le\frac12-2\eta.
\]
Hence, after the `B^o(1)` packet multiplicity,
\[
\boxed{|Q_{\rm off,eta}(B)|\ll B^{1/2-2\eta+o(1)}}.
\]
The same exponent bound holds for the corresponding occupied `j` support because r301m proves bounded physical multiplicity of the `q1 -> j` map.

This is not a global strict sub-square-root theorem: it excludes only cells a fixed distance from `theta=1/4`. A shrinking wall neighborhood remains.

```text
STAGE27_20_R301U_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
OFF_WALL_FIXED_DISTANCE_SUPPORT_SAVING_PROVED=true
OFF_WALL_Q1_BOUND=B^(1/2-2eta+o(1))
OFF_WALL_J_BOUND=B^(1/2-2eta+o(1))
CRITICAL_THETA=1/4
GLOBAL_Q1_SUPPORT_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301v
```
''')

v.joinpath('result.md').write_text(r'''# Stage27-20-r301v — exact critical-support wall and remaining receiver

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301u
SOURCE_STAGE=Stage20

On the Stage14 feasible domain set `theta=1/4`. Then
\[
\frac18\le\phi\le\frac14,\qquad
\chi=2\theta+2\phi-\frac34=2\phi-\frac14\in[0,1/4].
\]
For nonproportional cells, both complete-host exponents saturate:
\[
\boxed{E_k=3\theta-1/4=1/2},\qquad
\boxed{E_{\rm RRF}=1-2\theta=1/2}.
\]
The proportional branch stays below the wall (`<=7/16`). Thus the surviving fixed-power obstruction is precisely the nonproportional segment
\[
\boxed{\theta=1/4,\quad 1/8\le\phi\le1/4,\quad \chi=2\phi-1/4}.
\]

R301s gives `N2(B) <= |Q(B)| B^o(1)` and r301u gives fixed-power savings at every fixed distance from the wall. A sufficient new receiver is therefore a target-specific critical support theorem
\[
\boxed{|Q_{\rm crit}(B)|\ll B^{1/2-\delta+o(1)}}
\]
for some fixed `delta>0`, with a compatible wall-neighborhood statement. The existing fixed-x elliptic `B^o(1)`, fixed-x squareclass `B^o(1)`, height-only support, and off-wall Stage14 hosts do not supply this deficit.

Legal next weapons are critical-wall-specific: weighted local obstruction, occupied-slope collision/energy deficit, or a thin-projection theorem on the exact critical receiver.

```text
STAGE27_20_R301V_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CRITICAL_SUPPORT_SEGMENT_IDENTIFIED=true
CRITICAL_THETA=1/4
CRITICAL_PHI_RANGE=[1/8,1/4]
CRITICAL_CHI_FORMULA=2phi-1/4
CRITICAL_E_K=1/2
CRITICAL_E_RRF=1/2
FIXED_X_FIBER_EXPONENT_ALREADY_ZERO=true
CRITICAL_Q1_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301w
```
''')

reg = {
  'batch_id':'Stage27-20-r301t-v','checkpoint':40,'route_kind':'UPPER_REENTRY_PREFLIGHT','source_stage':'Stage20',
  'parent_route':'Stage27-20-r301s','routes':['Stage27-20-r301t','Stage27-20-r301u','Stage27-20-r301v'],
  'status':'BATCH_SUBMITTED_PENDING_FRESH_AUDIT','audit_status':'PENDING','merge_allowed':False,'advance_allowed':False,
  'fresh_reaudit_required':True,
  'claims':{
    'q1_to_stage14_face_mobius_adapter_proved':True,
    'q1_to_active_face_support_injection_proved':True,
    'off_wall_fixed_distance_support_saving_proved':True,
    'critical_support_segment_identified':True,
    'critical_q1_support_fixed_power_deficit_proved':False,
    'strict_sub_sqrt_upper_proved':False,'new_mu_lt_half_proved':False,'true_N2_exponent_identified':False},
  'next_derived_route':'27-20-r301w',
  'numbering_contract':{'after_r301z':'Stage27-20-r302-main-batch','r301aa_forbidden':True},
  'stop_reason':'CRITICAL_WALL_OCCUPIED_Q1_SUPPORT_DEFICIT_THEOREM_REQUIRED'}
b.joinpath('batch-registry.json').write_text(json.dumps(reg, indent=2)+'\n')

b.joinpath('verify_27_20_r301t_v.py').write_text(r'''from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
S=ROOT/'stages'/'stage27'
t=(S/'27-20-r301t'/'result.md').read_text(); u=(S/'27-20-r301u'/'result.md').read_text(); v=(S/'27-20-r301v'/'result.md').read_text()
reg=json.loads((S/'27-20-r301t-v'/'batch-registry.json').read_text()); qs=json.loads((S/'27-20-r301q-s'/'batch-registry.json').read_text()); ctl=json.loads((S/'27-controller.json').read_text())
assert 'Q1_TO_STAGE14_FACE_MOBIUS_ADAPTER_PROVED=true' in t
assert 'Q1_TO_ACTIVE_FACE_SUPPORT_INJECTION_PROVED=true' in t
assert 'Q1_EQUALS_ALL_STAGE14_ACTIVE_VERTICES_CLAIMED=false' in t
assert 'OFF_WALL_FIXED_DISTANCE_SUPPORT_SAVING_PROVED=true' in u
assert 'OFF_WALL_Q1_BOUND=B^(1/2-2eta+o(1))' in u
assert 'CRITICAL_THETA=1/4' in u
assert 'CRITICAL_PHI_RANGE=[1/8,1/4]' in v
assert 'CRITICAL_CHI_FORMULA=2phi-1/4' in v
assert 'CRITICAL_E_K=1/2' in v and 'CRITICAL_E_RRF=1/2' in v
assert 'CRITICAL_Q1_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false' in v
assert 'NEXT_DERIVED_ROUTE=27-20-r301w' in v
assert qs['status']=='AUDITED_PASS_MERGED' and qs['audit_status']=='PASS' and qs['advance_allowed'] is True
assert reg['status']=='BATCH_SUBMITTED_PENDING_FRESH_AUDIT' and reg['audit_status']=='PENDING'
assert reg['merge_allowed'] is False and reg['advance_allowed'] is False and reg['fresh_reaudit_required'] is True
for name in ('Stage27-20-r301t','Stage27-20-r301u','Stage27-20-r301v'):
    e=ctl['derived_routes'][name]
    assert e['status']=='BATCH_SUBMITTED_PENDING_FRESH_AUDIT' and e['audit_status']=='PENDING'
    assert e['merge_allowed'] is False and e['advance_allowed'] is False
assert ctl['derived_routes']['Stage27-20-r301v']['next_derived_route']=='27-20-r301w'
assert ctl['checkpoint_status']['50']=='BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE'
assert ctl['state']['CURRENT_CHECKPOINT']==40 and ctl['state']['NEXT_CHECKPOINT']==40
assert ctl['state']['MAIN_STATUS']=='UPPER_REENTRY_STAGE27_19_R402C_F_BATCH_SUBMITTED_PENDING_FRESH_AUDIT'
assert ctl['stage20_r301_numbering_contract']['after_r301z']=='Stage27-20-r302-main-batch'
assert ctl['stage20_r301_numbering_contract']['r301aa_forbidden'] is True
print('Stage27-20-r301t-v verifier: PASS')
''')

ctlp = root/'27-controller.json'
ctl = json.loads(ctlp.read_text()); dr = ctl['derived_routes']
dr['Stage27-20-r301t'] = {'trigger_checkpoint':40,'route_kind':'UPPER_REENTRY_PREFLIGHT','source_stage':'Stage20','parent_route':'Stage27-20-r301s','batch_audit_group':'Stage27-20-r301t-v','status':'BATCH_SUBMITTED_PENDING_FRESH_AUDIT','audit_status':'PENDING','merge_allowed':False,'advance_allowed':False,'result_path':'stages/stage27/27-20-r301t/result.md','q1_to_stage14_face_mobius_adapter_proved':True,'q1_to_active_face_support_injection_proved':True,'q1_equals_all_stage14_active_vertices_claimed':False,'strict_sub_sqrt_upper_proved':False,'next_derived_route':'27-20-r301u'}
dr['Stage27-20-r301u'] = {'trigger_checkpoint':40,'route_kind':'UPPER_REENTRY_PREFLIGHT','source_stage':'Stage20','parent_route':'Stage27-20-r301t','batch_audit_group':'Stage27-20-r301t-v','status':'BATCH_SUBMITTED_PENDING_FRESH_AUDIT','audit_status':'PENDING','merge_allowed':False,'advance_allowed':False,'result_path':'stages/stage27/27-20-r301u/result.md','off_wall_fixed_distance_support_saving_proved':True,'critical_theta':'1/4','global_q1_support_deficit_proved':False,'strict_sub_sqrt_upper_proved':False,'next_derived_route':'27-20-r301v'}
dr['Stage27-20-r301v'] = {'trigger_checkpoint':40,'route_kind':'UPPER_REENTRY_PREFLIGHT','source_stage':'Stage20','parent_route':'Stage27-20-r301u','batch_audit_group':'Stage27-20-r301t-v','status':'BATCH_SUBMITTED_PENDING_FRESH_AUDIT','audit_status':'PENDING','merge_allowed':False,'advance_allowed':False,'result_path':'stages/stage27/27-20-r301v/result.md','critical_support_segment_identified':True,'critical_theta':'1/4','critical_phi_range':'[1/8,1/4]','critical_chi_formula':'2phi-1/4','critical_q1_support_fixed_power_deficit_proved':False,'strict_sub_sqrt_upper_proved':False,'new_mu_lt_half_proved':False,'true_N2_exponent_identified':False,'next_derived_route':'27-20-r301w'}
ctlp.write_text(json.dumps(ctl, indent=2)+'\n')

Path('.github/workflows/stage27-20-r301t-v-critical-support.yml').write_text("""name: Stage27-20-r301t-v critical support batch

on:
  push:
    branches:
      - agent/stage27-20-r301t-v-critical-support
  pull_request:
    paths:
      - 'stages/stage27/27-20-r301t/**'
      - 'stages/stage27/27-20-r301u/**'
      - 'stages/stage27/27-20-r301v/**'
      - 'stages/stage27/27-20-r301t-v/**'
      - 'stages/stage27/27-controller.json'
      - '.github/workflows/stage27-20-r301t-v-critical-support.yml'

jobs:
  verify-stage27-20-r301t-v:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Verify Stage27-20-r301t-v
        run: python stages/stage27/27-20-r301t-v/verify_27_20_r301t_v.py
      - name: Validate controller and registry JSON
        run: |
          python -m json.tool stages/stage27/27-controller.json >/dev/null
          python -m json.tool stages/stage27/27-20-r301t-v/batch-registry.json >/dev/null
      - name: Diff hygiene
        run: |
          git fetch origin main
          git diff --check origin/main...HEAD
""")
