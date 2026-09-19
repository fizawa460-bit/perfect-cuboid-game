# MB104 — shallow fresh-weapon portfolio R4 — 2026-09-20

Status: **PRE-AUDIT SHALLOW PORTFOLIO / ALL THREE ROUTES FAIL SHALLOW / NO CREDIT**

## Scope

Current active leaf:

```text
MB104-SHALLOW-FRESH-WEAPON-PORTFOLIO-R4
```

Dangerous balanced support:

```text
000707000f0f.
```

Compare at equal shallow depth:

A. the six fixed cuboid fibrations as one decomposable global web;
B. fixed-surface Hilbert/Chow boundedness for integral curves of geometric genus one;
C. good-prime arithmetic specialization / finite-field obstruction.

This pass does not reopen individual six-map ramification/jet scans, the parked log-tangent route,
32-01 fibration classification, or the size48 local analytic chain.

## A. Six-fibration global web

The six already-fixed rank-3 fibrations on 000707 have

```text
P.G_j = (40,40,56,44,44,56),
sum_j P.G_j = 280.
```

For a hypothetical carrier C in |lP| with elliptic normalization nu:E->C,

```text
deg R_j = 2l(P.G_j),
sum_j deg R_j = 560l.
```

The source-valid local Piene adapter retained in the previous shallow scan gives, for each relative
polar direction,

```text
polar_j|E = Delta + R_j,
deg Delta = 336l^2+112l.
```

The six-fibration web is decomposable: it is the product of those six foliation directions.
Accordingly its total contact/polar section is the product of the six factor contact sections, so
on E its divisor is the sum

```text
6 Delta + sum_j R_j.
```

Its degree is therefore exactly

```text
6(336l^2+112l)+560l
=
2016l^2+1232l.
```

This is not a new quadratic inequality.  It repeats the same conductor factor six times.

After removing the common conductor factor, the entire remaining web-contact budget is only

```text
560l.
```

The discriminant/curvature objects of the fixed web depend only on the six fixed surface
fibrations, not on l.  Their intersection with C therefore has degree O(l).  They can modify a
linear residual term but cannot create a new negative quadratic coefficient.

The structural obstruction is also local.  A singularity can acquire large delta through
collision of branches away from the fixed web discriminant.  The common conductor factor records
that collision in every relative polar, but ordinary web discriminant/tangency data do not turn
that repeated common factor into a strict upper bound.

Thus:

```text
WEB CONTACT = six copies of the retained conductor/polar identity
             + O(l) residual web data.
```

No theorem found in the shallow web literature supplies an additional collision term with a
coefficient capable of beating the retained conductor mass.

Disposition:

```text
A = NO FINITE-l RETURN.
Do not deepen web curvature/discriminant calculations.
```

## B. Fixed-surface Hilbert/Chow boundedness by geometric genus

For C=lP,

```text
H.C = 112l,
p_a(C)
 = 1 + (C^2+K.C)/2
 = 168l^2+56l+1.
```

Hence the Hilbert polynomial with respect to H is

```text
P_C(n)
=
112l*n + 1-p_a(C)
=
112l*n -168l^2-56l.
```

So changing l changes both degree and Hilbert polynomial.  Ordinary Hilbert-scheme boundedness is
only a boundedness statement after fixing that polynomial; it gives no bounded union over all l.

The same issue remains on the Chow side: the cycle degree is

```text
112l
```

and is unbounded.

This is not merely a missing standard citation.  A general canonical-degree bound for integral
curves on a fixed smooth surface in terms of geometric genus is itself conjectural in this level of
generality.  Ciliberto--Fontanari prove such a bound under extra hypotheses including

```text
h0(S,2K_S+C)=0.
```

That hypothesis fails immediately in the hostile problem: if C exists, then C is effective and
2K_S=2H is effective, so the product of their defining sections gives

```text
h0(S,2K_S+C) >= 1.
```

The positive-Segre/canonical-degree theorems already inspected in R3 also do not apply because

```text
K_S^2-c2(S) = -64.
```

Therefore neither Hilbert/Chow finite type nor the located fixed-surface canonical-degree
theorems bound l.

Disposition:

```text
B = NO SOURCE-VALID FIXED-SURFACE DEGREE BOUND.
```

## C. Good-prime specialization / finite-field receiver

There is a legitimate arithmetic idea here, but the naive receiver is too weak.

For fixed l, the carrier Hilbert problem is algebraic over a number field containing the cuboid
marking.  A characteristic-zero point can be spread out, and proper compactifications can be
specialized to good primes.

However the exact property needed by MB is not simply a closed Hilbert condition:

```text
integral image
+
normalization genus one
+
the MB branch/contact packet.
```

Delta is upper-semicontinuous in flat families of curve singularities.  Thus specialisation can
increase delta and lower geometric genus.  An integral genus-one generic carrier can acquire a
lower-genus or reducible/nonreduced boundary object at a bad or boundary special fibre.

Therefore:

```text
"no integral genus-one curve over Fbar_p"
```

is not by itself a specialization obstruction to the characteristic-zero Hilbert point.

A proper receiver can be made using stable maps: the normalization gives a genus-one stable map,
and stable-map compactification is proper.  But its special fibre contains substantially more than
the desired carrier population:

```text
reducible stable maps,
contracted elliptic components,
boundary maps with the same total class lP.
```

Consequently a finite-field proof would have to exclude the entire relevant stable/log-map
boundary, not just integral genus-one image curves.

That boundary does not currently collapse to bounded discrete data.  The numerical inputs still
scale with l:

```text
H.(lP)=112l,
supported contact population=112l in the Z33 equality packet,
conductor degree=336l^2+112l.
```

Moreover checking only F_p-rational objects is insufficient; the geometric special fibre over
Fbar_p must be empty.

Thus a good-prime computation for one or several small l could be useful experimentally, but no
l-independent residue-state receiver or uniform contradiction is presently justified.

Disposition:

```text
C = SPECIALIZATION PRINCIPLE VALID IN A PROPER COMPACTIFICATION,
    BUT NO FINITE-STATE / l-UNIFORM RECEIVER.
Do not launch a finite-field computation campaign.
```

## R4 verdict

No route earns depth:

```text
A global six-web:
  common conductor repeats six times; only O(l) new web data.

B Hilbert/Chow:
  l changes the Hilbert polynomial and degree;
  general geometric-genus degree boundedness is unavailable here.

C good-prime:
  proper stable-map specialization is conceptually valid,
  but boundary populations remain l-growing and no finite-state receiver exists.
```

Therefore R4 has no visible finite-l coefficient or bounded receiver.

## Suggested next rotation

Three materially different shallow theorem species are worth comparing next:

1. **adjoint/conductor ideal powers**
   - use that the Z48 conductor is the adjoint/conductor object of the Gorenstein curve,
   - go beyond the already-tested first adjoint/regularity statement,
   - test powers or multiplier/adjoint filtrations against exact Riemann--Roch on lP.

2. **stable-map obstruction/cosection from p_g(S)=7**
   - use the seven holomorphic two-forms / canonical sections on the resolved surface,
   - determine whether the isolated genus-one stable map from P6F is actually excluded or only has
     zero virtual contribution.

3. **gonality-extension after embedded resolution**
   - E is elliptic and carries a degree-two pencil,
   - test Serrano/Reider-type extension theorems after resolving the singular carrier,
   - reject immediately if the required positive self-intersection is destroyed by the
     singularity-resolution multiplicities.

These are proposals only; current R4 grants no route promotion.

## External source boundary

- Ciliberto--Fontanari, *A remark on the canonical degree of curves on smooth projective surface*,
  arXiv:2305.17923: the general canonical-degree bound is posed as a conjectural shape and their
  theorem requires h0(2K_X+C)=0.
- Greuel--Pfister, *The Delta Invariant and Simultaneous Normalization for Families of Isolated
  Non-Normal Singularities*, arXiv:2107.07012: delta-type invariants are upper-semicontinuous in
  the relevant flat-family setting.
- Holomorphic-web literature on decomposable webs/discriminants was used only as a shallow
  theorem-species check; the load-bearing six-factor divisor calculation above follows directly
  from the already-retained Piene polar adapter.

## Firewalls

```text
web_finite_l=false
fixed_surface_genus_boundedness_applicable=false
good_prime_finite_state_receiver=false
finite_field_campaign_authorized=false
R4_deep_winner=false
finite_degree_window_proved=false
dangerous_000707_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
