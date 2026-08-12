# Stage15-6-cycle — 6ar through 6au

Base: merged Stage15-6an--6aq (`PR #844`, merge commit `10b87c5f`).

This cycle makes the audit stages visible. It starts from the `j=1728 twist-height or norm-core correlation` gate and stops when one theorem species has a sufficiently exact match that the next task is a concrete adapter rather than another theorem search.

## Visible stage / audit ledger

```text
6ar  exact binary-quartic Jacobian and twist parameter
     AUDIT=PASS
     d=sf(2*k*kappa)
     E_d: y^2=x^3-d^2*x
     k*kappa recovered from d

6as  Nara explicit canonical-height theorem applicability
     AUDIT=BLOCK
     base y^2=x^3-x has Delta=64=2^6
     Nara Theorem 1.1 sixth-power-free hypothesis fails directly
     covering-map/non-torsion bridge also missing

6at  remembered 6ac low-core size condition
     AUDIT=BLOCK
     retain k^2<4*R0*S0 legally
     but size inequalities alone allow polynomial k range
     old AR-009 modulus not recharged

6au  small-height twist-family theorem audit
     AUDIT=NEW_GATE
     Petit theorem species counts almost-minimal twists at X^(1/2)*log X
     exact Stage15 twist family matches structurally
     four concrete adapters remain
```

## Main exact advance

For the small-coordinate-core quartic

\[
\kappa T^2=f_K(a,b)g_K(a,b),
\qquad N(K)=k,
\]

6ar proves

\[
I=12(k\kappa)^2,\qquad J=0,
\]

so its Jacobian is

\[
y^2=x^3-324(k\kappa)^2x.
\]

After rational scaling this is

\[
\boxed{E_d:y^2=x^3-d^2x,\qquad d=sf(2k\kappa).}
\]

Because `(k,kappa)=1` and both are squarefree, `d` determines `k*kappa` uniquely by the 2-primary rule, while all splits/orientations/cells cost only `B^o(1)`.

## Literature boundary

The direct explicit Nara theorem is not imported because its stated sixth-power-free discriminant assumption does not match the base curve `y^2=x^3-x`.

The more promising theorem species is Petit's count of quadratic twists carrying a non-torsion point of almost minimal canonical height. For `alpha<1/120`, the relevant twist set has size

\[
X^{1/2+o(1)}
\]

(more precisely an asymptotic of `c(alpha) X^(1/2) log X` in the cited setup).

This is the first external theorem species in the post-6aq search whose family-count exponent is exactly on the desired half-power scale.

## Why it is not applied yet

Four adapters are mandatory:

```text
A  explicit binary-quartic 2-covering map C_{K,kappa} -> E_d
B  prove/count non-torsion image branch
C  Stage15 physical/projective height -> canonical-height upper bound
   strong enough for eta_d <= d^(1/8+alpha), alpha<1/120
D  control Stage15 point-pair multiplicity per twist d
```

No theorem is promoted across these missing links.

## Cycle verdict

```text
STAGE15_6_CYCLE_START=6ar
STAGE15_6_CYCLE_END=6au
STAGE15_6_CYCLE_AUDIT_LEDGER=PASS,BLOCK,BLOCK,NEW_GATE
STAGE15_6_CYCLE_EXACT_TWIST_PARAMETER=true
STAGE15_6_CYCLE_TWIST_PARAMETER=d=sf(2*k*kappa)
STAGE15_6_CYCLE_NARA_DIRECT_ROUTE_BLOCKED=true
STAGE15_6_CYCLE_LOW_CORE_SIZE_ONLY_ROUTE_BLOCKED=true
STAGE15_6_CYCLE_PETIT_HALF_POWER_THEOREM_SPECIES_MATCH=true
STAGE15_6_CYCLE_PETIT_STAGE15_ADAPTER_PROVED=false
STAGE15_6_CYCLE_GLOBAL_NORM_CORE_AGGREGATION_PROVED=false
STAGE15_6_CYCLE_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6_CYCLE_EXIT=EXPLICIT_2COVERING_CANONICAL_HEIGHT_ADAPTER_READY
```

Next stage: `Stage15-6av`. Do not perform another broad theorem search first.