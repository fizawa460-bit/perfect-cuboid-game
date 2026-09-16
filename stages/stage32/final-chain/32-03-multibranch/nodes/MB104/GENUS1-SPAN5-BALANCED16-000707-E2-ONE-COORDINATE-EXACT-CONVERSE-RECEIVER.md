# Stage32 MB104 — `000707000f0f` e=2 one-coordinate exact-converse conductor receiver

Status: **RETAINED EXACT ONE-COORDINATE RECEIVER / `S35-PW02` EXACT-CONVERSE PATTERN CONSUMED / POINTWISE CONDUCTOR SIGN STILL MISSING / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

This note consumes the retained support-specific intermediate quotient

```text
X_H=P/H_diag -> B=P/G_diag
```

and the retained order-two conductor-pair receiver.  It does not assign a sign to any actual Stage32 conductor pair.  Its purpose is to replace the two-coordinate residual lift comparison by one intrinsic order-two scalar with an exact converse.

The construction follows the reusable shape recorded by Arsenal `S35-PW02`: make the finite quotient explicit and retain both the forward map and the converse reconstruction.  `S35-PW02` is routing/proof-pattern provenance only; no Stage35 mathematical credit is imported.

## 1. Retained two-factor quotient data

On the source-locked chart from the intermediate `H`-quotient model, write

```text
A_z = 2*(C+W3)/(W1-i*W2),
A_w = 2*(C+W3)/(W1+i*W2),
m   = 2*Z3/(C-W3).
```

The residual lift coordinates satisfy

```text
r_z^2 = A_z,
r_w^2 = A_w,
r_z*r_w = m.                                      (BASE)
```

All three right-hand sides are rational functions on the box quotient `B`.  The residual deck involution is

```text
tau:(r_z,r_w)->(-r_z,-r_w).                     (TAU)
```

For the active `000707` carrier the absent divisor is the residual branch divisor, so the conductor comparison is made on the etale locus.  On any displayed overlap where `r_z` is a valid nonzero generator, the formulas below apply; generator-independence shows that the result patches across Kummer-coordinate changes.

## 2. One-coordinate relative receiver

Let `x_i,x_j` be two normalization preimages in one conductor identification, mapping to the same point of `B`.  Define

```text
delta_ij := r_z(x_j)/r_z(x_i).                  (DELTA)
```

Because `A_z` has the same value at the two preimages,

```text
delta_ij^2
 = r_z(x_j)^2/r_z(x_i)^2
 = A_z/A_z
 = 1.                                           (ORDER2)
```

Thus

```text
delta_ij in mu_2={+1,-1}.
```

This is not a new choice of sheet label: it is a relative coordinate and is unchanged by simultaneously replacing the Kummer generator by its negative.

## 3. Exact converse reconstructs the full two-factor lift

The retained base function `m=r_z*r_w` has the same value at `x_i,x_j`.  Hence

```text
r_w(x_j)
 = m/r_z(x_j)
 = delta_ij^(-1) * m/r_z(x_i)
 = delta_ij * r_w(x_i),                         (RW)
```

where the last equality uses `delta_ij^2=1`.

Therefore one scalar recovers the complete residual pair relation:

```text
delta_ij=+1
 <=> (r_z,r_w)(x_j)=( r_z,r_w)(x_i),

delta_ij=-1
 <=> (r_z,r_w)(x_j)=(-r_z,-r_w)(x_i).           (CONVERSE)
```

So the two-coordinate pair receiver has an exact one-coordinate converse.  No independent `r_w` sign needs to be materialized.

## 4. Equality with the retained conductor character

The previous conductor-pair quotient uses, for a Kummer generator `r` with `r^2=h`,

```text
chi_ij = r_i*r_j/h.
```

Taking `r=r_z` and `h=A_z` gives

```text
chi_ij
 = r_z(x_i)*r_z(x_j)/A_z
 = r_z(x_j)/r_z(x_i)
 = delta_ij.                                    (CHI=DELTA)
```

Thus the new scalar is not a second character.  It is exactly the existing residual conductor character in a one-coordinate exact-converse presentation.

Consequently the retained weighted cut may be written without change as

```text
y/2
 = sum_p sum_(i<j) I_p(beta_i,beta_j)
   * (1-delta_(p;i,j))/2,                       (CUT)
```

and the Hodge requirement remains

```text
y/2 >= 84*l^2.
```

## 5. Intrinsic overlap and symmetry checks

If a Kummer-chart change replaces the generator by

```text
r_z' = a(B)*r_z,
```

with nonzero base function `a`, then the two conductor preimages have the same base value and

```text
r_z'(x_j)/r_z'(x_i)=delta_ij.
```

Hence `delta_ij` is independent of such generator rescaling.  Also

```text
delta_ji=delta_ij^(-1)=delta_ij,
```

so the receiver is symmetric under exchange of the conductor pair.  For three branch preimages at one singular point,

```text
delta_ij*delta_jk=delta_ik,
```

recovering the already-retained local relative-sign cocycle.

## 6. Arsenal `S35-PW02` specialization

The exact-converse pattern is now instantiated inside MB104 as

```text
conductor pair
  -> delta_ij in mu_2
  -> {identity component, tau-twisted component},
```

with

```text
delta_ij=+1 iff identity component,
delta_ij=-1 iff tau-twisted component.
```

The induced character on the order-two quotient is primitive, so there is no remaining ambiguity once `delta_ij` is evaluated.  The missing datum is upstream of this gate: the repository still lacks the branch-specific specialization of `r_z` (equivalently the modular transition class) at the actual conductor normalization preimages.

## Route consequence

The active e=2 target can now be narrowed from

```text
materialize both H-orbit lift coordinates at both conductor preimages
```

to

```text
materialize one residual semi-invariant r_z at paired normalization preimages
 -> compute delta_ij=r_z(j)/r_z(i)
 -> exact converse recovers the full residual lift relation.
```

Equivalent acceptable input remains a source-locked modular transition `M_(i,j)`, because the retained evaluator gives

```text
delta_ij=(-1)^chi_res(M_(i,j)).
```

The next load-bearing task is therefore to compute or constrain this single transition on the high-intersection conductor pairs strongly enough to put the weighted cut below `84*l^2`, or to derive a contradiction by another exact route.

## Firewalls

- No actual conductor pair is assigned `delta=+1` or `delta=-1`.
- No claim is made that all conductor pairs use one affine chart; only the overlap-invariant relative coordinate is retained.
- No new upper bound for the weighted cut is claimed.
- No `e=2`, `e=4`, or `000707000f0f` closure is claimed.
- The active MB104 leaf remains unchanged.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- `S35-PW02` contributes proof-pattern provenance only.
- No heavy compute is armed.
- No merge authorization.
