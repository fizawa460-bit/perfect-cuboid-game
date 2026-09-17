# MB104 uniform-closure route update — 2026-09-17

Status: **POST-SPLIT RESEARCH ROUTING / ZERO NEW MATHEMATICAL CREDIT**

This compact update supersedes the candidate-status portion of `MB104-UNIFORM-CLOSURE-RESTART-20260917.md` where later post-split preflights have resolved a route. The archive/repetition firewall in the restart ledger remains in force.

## New retained facts

### Ordinary effectivity is not the obstruction

For the displayed ray

```text
D_l = 7lH - 4l sum_(p in Sigma)E_p,
|Sigma|=14,
l>=1,
```

Riemann--Roch plus `H=K_S` nef gives

```text
h^0(S,O(D_l)) > 0
```

for every `l>=1`. Thus the old restart-ledger wording saying effectivity was unproved is obsolete. What remains unproved is existence of an **irreducible normalization-genus-one carrier with the exact balanced fourteen-node/product-cover packet**.

### Routes resolved after the split

```text
U1 simple equigeneric/Severi codimension:
  BLOCKED by exact conductor superabundance h1=112l.

U2 ordinary effective-cone / non-effectivity:
  BLOCKED as an exclusion route; |D_l| is nonempty for every l>=1.

U5 conductor-ideal vanishing:
  BLOCKED at the same h1=112l superabundance wall.

U6 standard log/orbifold inequalities:
  BLOCKED standalone; retained inequalities remain numerically slack.
  Re-entry requires genuinely global packet geometry, e.g. a theorem forcing many branches into controlled collisions/high contact.

U7 receiver-preserving degeneration:
  BLOCKED_PENDING_TARGET_DEGENERATION_ADAPTER.
  No source-locked MB104 relative/log degeneration currently preserves all of
  normalization genus, 000707 support, 8l balanced contacts, product-cover passport,
  and no-untracked-splitting semantics.

U8 standard cotangent/orbifold positivity:
  BLOCKED at the exact coefficient wall; current positivity criteria do not beat the balanced packet.

U9 branch-value Hurwitz redistribution:
  DOMINATED by the parked counting-only route. The two absent branch values consume 56l of the 112l total ramification and leave 56l; the retained zero-quartic saturated fibers add no forced ramification charge.

U10 non-arithmetic commensurator degree bound:
  BLOCKED. C8=X(8) lies in the arithmetic (2,3,8) triangle commensurability class, so discrete finite-index commensurator arguments cannot uniformly bound the etale correspondence degree n=14el.
```

## Product-correspondence boundary

The archive already reaches, conditionally in the e=2 product-correspondence chain,

```text
n=28l,
Zbar^2=1568l^2,
delta(Zbar)=784l^2+112l=n^2+4n,
Phi_Z=0.
```

Therefore a generic Jacobian/Rosati or correspondence-degree argument is not a fresh route. The remaining self-intersection multiplicity is carried by isolated collisions of the two etale projections and falls back onto the conductor/pair-incidence geometry unless a new packet-sensitive global theorem is supplied.

## Current live search

The clean high-level routes remaining are:

```text
U3-PACKET = a global incidence/singularity theorem acting simultaneously on
            normalization genus 1 + exact fourteen-node balanced packet
            + product-cover passport;

U4 = a genuine large-l theorem yielding an explicit L and a finite backend
     for 1<=l<=L.
```

A new route is admissible only if it does not reduce to the parked conductor-sign, counting-only, fixed-jet, ordinary-effectivity, or generic-correspondence arguments.

One still-unresolved arithmetic variant is the **packet-sensitive arithmetic correspondence index/passport problem**: not merely whether arithmetic etale correspondences of large degree exist, but whether one can realize degree `14el` together with the exact fixed quotient/node-stabilizer passport. This is `UNTESTED`, not a claimed obstruction.

## Firewalls

```text
MB104_complete=false
finite_degree_window_proved=false
receiver_credit=false
effectivity_credit=false
final_milestone_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
