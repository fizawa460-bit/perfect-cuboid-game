# MB104 Z31+ cleanup audit — second pass — 2026-09-19

Status: **SECOND-PASS HOSTILE CLEANUP / DEPENDENCY AND SOURCE-SCOPE AUDIT / NO CREDIT**

## Scope

This is a second independent audit of the retained Z31+ chain.

The first cleanup audit classified nodes by utility.  This pass deliberately challenges those
classifications and asks two stricter questions:

1. does each claimed KEEP node actually carry a load-bearing fact not already supplied elsewhere?
2. are the theorem/source hypotheses strong enough for the exact claim used by the next node?

No Z31+ research route is restarted here.  No MAIN/theorem/endpoint credit changes are made.

At the start of this second pass the current late leaf had already advanced to a bounded
maximal-ideal-generator reconstruction after the Z55 T0/T1 receiver.

## Executive correction to the first audit

The first audit's broad portfolio split remains mostly correct:

- Z32/Z34 are Z12 material;
- Z35/Z45 are Z2 material;
- Z36 and the conductor application of Z48 belong to Z4';
- Z37/Z38/Z40B belong to Z3;
- Z33G, Z40B, Z41B and the conductor-scheme Z48 are genuinely useful.

However one part must be weakened:

```text
Z48 explicit neighborhood
 -> Z49B
 -> Z50
 -> Z51
 -> Z52
 -> Z53
 -> Z54
 -> Z55
```

should **not** yet be described as a fully exact independent chain.

It is better described as

```text
promising PRE-AUDIT late analytic chain
with exact numerical/algebraic substeps
and two source-scope gates that still need hostile confirmation.
```

The two gates are detailed below.

## 1. Z48 explicit negative-elliptic neighborhood — DOWNGRADE

### Exact retained part

The following remains strong and reusable:

```text
j(Q)=1728,
N_(Q/S)=O_Q(-H)=O_Q(-4p),
exact marked attachment/intersection points.
```

These are genuine cuboid data.

### Source-scope problem

The note then states that because

```text
deg N_(Q/S)=-4<0,
```

the analytic germ of the surface along Q is linearizable to the zero section of the normal
bundle.

This does not follow merely from the usual Grauert formal principle.

The negative-neighborhood literature distinguishes:

```text
normal bundle data,
finite/formal neighborhood data,
analytic neighborhood.
```

Grauert-type formal principles say that sufficiently much formal-neighborhood information
determines the analytic germ; they do not in general say that the normal bundle alone determines
all higher formal neighborhoods.

Thus the safe retained statement is:

```text
exact component curve + exact normal bundle + exact marked points are known;
the component neighborhood is strongly constrained;
full analytic linearization from normal-bundle data alone is not source-locked here.
```

Disposition:

```text
Z48_EXPLICIT_NEIGHBORHOOD:
KEEP DATA,
HOLD LINEARIZATION CLAIM pending an exact theorem with verified hypotheses.
```

This does not affect the independent Z48 conductor-scheme adapter.

## 2. Z49B holomorphic-cover uniqueness — KEEP, but narrow the claim

The following argument is sound once the **actual punctured analytic germ U** and its topological
cover are fixed:

```text
finite topological cover of the complex manifold U
 -> unique complex structure making it holomorphic etale;

finite meromorphic field extension
 -> unique normal finite extension by normalization.
```

So:

```text
fixed actual U + fixed topological character
=> unique holomorphic cover of U
=> unique normal extension over the point.
```

What this does **not** prove is:

```text
resolution graph + component normal bundles
=> unique analytic base plumbing.
```

Nor does it independently kill moduli in the base contraction germ.

Therefore the phrase

```text
"no residual holomorphic plumbing parameter survives"
```

is too broad unless it is explicitly restricted to

```text
the lift of a fixed actual base germ.
```

Disposition:

```text
Z49B = KEEP,
but only as uniqueness of the canonical cover over the fixed cuboid contraction germ.
Do not use it as a uniqueness theorem for the base plumbing analytic type.
```

## 3. Z50 canonical-cover resolution graph — KEEP CONDITIONAL

Given the local cyclic-cover model

```text
xy=t^3
```

at each Q--B attachment, the A2 resolution computation and projection-formula self-intersection
calculation are internally consistent:

```text
seven-component chain,
all self-intersections -2,
elliptic endpoints,
Z^2=-2,
p_a(Z)=2,
Z_K=2Z.
```

This result depends only on the local cover model and not on a global analytic normal form.

So Z50 remains useful even after narrowing Z48/Z49B.

Disposition:

```text
KEEP CONDITIONAL on the exact local meridian character / xy=t^3 model.
```

Z49C variants remain duplicate/superseded by Z50.

## 4. Z51 Konno type-(ii.a) classification — KEEP PROVISIONAL, not "exact authority"

The cited Konno paper does source-level support the general program:

```text
fundamental-genus-two equality cases,
Gorenstein multiplicity,
embedding dimension,
rough resolution-graph classification.
```

But the retained Z51 note uses several exact proposition/lemma specializations:

```text
exact type (ii.a),
p_g=3,
maximal ideal cycle F=Z+A5,
mult=4,
embdim=4.
```

Those are load-bearing for every later tangent-cone claim.

The second audit did not find an internal mathematical contradiction, but the current repository
asset is still PRE-AUDIT and the exact source hypotheses are not independently reproduced inside
the certificate.

Therefore:

```text
Z51 = KEEP PROVISIONAL / HOSTILE SOURCE CHECK REQUIRED.
```

In particular, Z51 should not yet be treated like an audited theorem authority.

## 5. Z52 — internally strong if Z51 holds

Conditional on the Z51 package:

```text
dim=2,
codim=2 CI,
mult=4,
embdim=4,
p_g=3,
Z_K^2=-8,
e(E_red)=4,
```

the Z52 deductions are coherent:

```text
ord(f)=ord(g)=2,
quadratic initial forms form a regular sequence,
projectivized tangent cone is a (2,2) CI quartic scheme,
mu=31.
```

The main dependency is not the arithmetic but the Z51 source specialization and the exact
Laufer--Steenbrink formula convention.

Disposition:

```text
Z52 = KEEP PROVISIONAL DOWNSTREAM OF Z51.
```

Do not use mu=31 equivariantly without a deck-character decomposition.

## 6. Z53--Z55 — useful bounded reduction, still PRE-AUDIT

### Z53

Useful exact idea:

```text
maximal ideal cycle F=(1,2,2,2,2,2,1)
gives positive O(-F)-degree only on the two arm components.
```

This is a meaningful reduction of tangent support.

### Z54

The algebraic classification

```text
T0=(x^2,yz),
T1=(x^2,yz+xw)
```

is a strong finite normal-form reduction **if** the prior assertion that the reduced tangent
support is exactly two distinct intersecting lines is valid.

The main load-bearing source step is not the coordinate elimination; it is the claim that Konno's
maximal-ideal system separates the relevant endpoint images strongly enough to force two distinct
lines.

Disposition:

```text
Z54 = KEEP PROVISIONAL;
hostile audit the endpoint-separation/source step before promotion.
```

### Z55

The three discriminators are internally exact for T0/T1:

```text
rank-four quadric,
local embedding dimension at the line intersection,
pencil determinant.
```

Z55 therefore is a good receiver even though the actual cuboid bit is still unknown.

Disposition:

```text
Z55 = KEEP RECEIVER,
not a new geometric theorem.
```

Current bounded reconstruction after Z55 is appropriately narrow.  It should not expand into a
full ICIS normal-form search until the binary determinant bit is materialized.

## 7. Recheck of the older Z31+ classifications

The second pass finds no reason to revive the following:

```text
Z33B
Z33D
Z33F
Z33H
Z42
Z44
Z46
Z47
Z48B
Z39/Z40 numerical enumeration.
```

Their wall/supersession classifications remain correct.

Likewise the following reverse-imports remain correct:

```text
Z32R/Z32S/Z34 -> Z12
Z35/Z45       -> Z2
Z36            -> Z4'
Z37/Z38/Z40B -> Z3
Z48 conductor  -> Z4'
```

## 8. Revised confidence tiers

### Tier A — retain strongly

```text
Z33 base equality
Z33G non-torsion holonomy / one 768-orbit elimination
Z40B complete balanced null locus
Z41B exact 3K descent/index-three structure
Z48 conductor-scheme adjoint adapter
```

These materially change the managed Z1--Z30 picture or supply a new exact contraction structure.

### Tier B — retain, but with explicit dependency/source caveats

```text
Z48 explicit elliptic data:
  keep j=1728, N=O(-4p), marked points;
  hold blanket analytic-linearization claim.

Z49 discriminant character
Z49B fixed-base canonical-cover uniqueness
Z50 cover resolution graph
Z51 Konno type-(ii.a)
Z52 quadratic ICIS / mu=31
Z53 tangent-support reduction
Z54 T0/T1 normal-form reduction
Z55 binary discriminators
```

These form a promising late analytic route, but not an audited theorem chain yet.

### Tier C — supporting only

```text
Z33A
Z33E
Z37
Z38
Z41
Z49
```

### Tier D — park/supersede

```text
Z33B Z33D Z33F Z33H
Z39 Z40
Z42 Z44 Z46 Z47 Z48B
Z49 finite-root <=81 exploration
Z49C duplicates
```

## 9. Main-lane overlap, second check

No ownership conflict is exposed by this reclassification.

Current MAIN is still the FULL178/compressed-BTVA-Picard numerical program, whereas the
post-Z41B work is a local contraction/canonical-cover analysis of the MB balanced hard core.

Therefore:

```text
no MAIN credit,
no theorem credit,
no endpoint credit,
no merge.
```

The main practical change is not lane ownership but **confidence labeling**:
late analytic Z results should remain PRE-AUDIT until the Z48 linearization scope and Z51/Z54
source specializations are hostile-checked.

## Final second-pass verdict

The first cleanup audit was directionally right, but too generous in calling the whole late
canonical-cover chain "exact."

The best managed representation after this pass is:

```text
A. managed original routes:
   Z1--Z30
   + reverse-imported Z33/Z34/Z35/Z36/Z37/Z38/Z40B/Z48-conductor results.

B. strong new structural bridge:
   Z41B exact contraction / index-three structure.

C. provisional late analytic chain:
   exact cuboid elliptic data
   -> canonical-cover character
   -> fixed-base holomorphic cover
   -> cover graph
   -> Konno classification
   -> quadratic ICIS
   -> two-line tangent reduction
   -> T0/T1 binary receiver.

D. hostile-audit gates before promotion:
   1. exact negative-neighborhood linearization theorem/hypotheses;
   2. exact Konno specialization and endpoint-separation statements.
```

No reason exists to rerun all Z31+ sequentially.

## Firewalls

```text
second_pass_cleanup_only=true
late_chain_fully_audited=false
z48_blanket_linearization_promoted=false
z51_source_specialization_hostile_audited=false
z54_endpoint_separation_hostile_audited=false
main_credit_changed=false
theorem_credit_changed=false
endpoint_credit_changed=false
merge_authorized=false
```
