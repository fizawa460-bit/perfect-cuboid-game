# Stage32 MB104 — `000707000f0f` e=2 irregularity/torsion refinement

Status: **RETAINED AMBIENT IRREGULARITY REDUCTION / NUMERICAL REMAINDER UPGRADES TO FIXED FINITE TORSION / CONDUCTOR SIGN STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Assume conditionally that the retained dangerous packet is realized in the `e=2` case. Keep the retained smooth residual double cover

```text
pi:Y -> S
```

defined by the absent half-branch class, and the anti-invariant numerical remainder

```text
w = (C_1-C_2) + sum_(j in Sigma) (d_j/2)(E_j^+-E_j^-),
w == 0 numerically.                            (W-NUM)
```

The previous anti-invariant leaf deliberately stopped at numerical equivalence. This refinement computes the irregularity of the ambient smooth model and identifies exactly what can remain beyond `(W-NUM)`.

## 1. The residual Kummer surface has the function field of `X_H`

Put

```text
P=C8 x C8,
H=<T',TT'R> ~= (Z/2)^2,
X_H=P/H_diag,
B=P/G_diag.
```

The retained support-specific intermediate quotient gives a residual degree-two extension

```text
k(X_H)=k(B)(r),
r^2=2*f_t                                      (XH)
```

in the one-factor Kummer coordinate, equivalently the simultaneous sign extension in `(r_z,r_w)`.

The retained ambient half-branch/Kummer chain gives

```text
k(Y)=k(S)(sqrt(f_t))                           (Y)
```

up to inversion and a nonzero square scalar. Since `S` resolves `B`,

```text
k(S)=k(B).
```

Over `C`, `2` is a square, and inversion does not change a quadratic square-class extension. Hence `(XH)` and `(Y)` define the same function field:

```text
k(Y)=k(X_H).                                   (FIELD)
```

Therefore `Y` is birational to any smooth projective resolution `Xtilde_H` of `X_H`.

This is only a birational/function-field identification. No isomorphism between the displayed models is claimed.

## 2. `q(Xtilde_H)=0`

The retained Hurwitz quotient computation gives

```text
R=C8/H ~= P1.
```

For the finite quotient `C8 -> R`, characteristic-zero averaging gives

```text
H^1(C8,O_C8)^H
 = H^1(R,O_R)
 = 0.                                          (C-H1)
```

Kunneth gives

```text
H^1(P,O_P)
 = H^1(C8,O_C8) direct_sum H^1(C8,O_C8).
```

The diagonal `H` action is the same `H` action on each summand, so `(C-H1)` implies

```text
H^1(P,O_P)^H = 0.                              (P-H1)
```

For the finite quotient `P -> X_H`, Reynolds averaging and finiteness give

```text
H^1(X_H,O_X_H)=H^1(P,O_P)^H=0.                (XH-H1)
```

The singularities of `X_H` are finite quotient surface singularities over `C`, hence rational. Thus a resolution does not change `H^1(O)`:

```text
H^1(Xtilde_H,O_Xtilde_H)=0.
```

Consequently

```text
q(Xtilde_H)=0.                                 (QXH)
```

The standard characteristic-zero quotient and rational-singularity facts used here are isolated in `FINITE-QUOTIENT-IRREGULARITY-TORSION-SOURCE-NOTE.md`.

## 3. `q(Y)=0` and `Pic^0(Y)=0`

By `(FIELD)`, the smooth projective surfaces `Y` and `Xtilde_H` are birational. Irregularity is a birational invariant for smooth projective surfaces, so `(QXH)` gives

```text
q(Y)=0.
```

Therefore the Picard variety has dimension zero and

```text
Pic^0(Y)=0.                                    (PIC0)
```

This is the load-bearing new ambient fact.

## 4. The previous numerical remainder is finite torsion

For a smooth projective variety, numerically trivial line bundles form `Pic^tau`; the quotient

```text
Pic^tau/Pic^0
```

is finite. By `(PIC0)`, `Pic^tau(Y)` itself is finite.

Since `(W-NUM)` says `O_Y(w)` is numerically trivial,

```text
[O_Y(w)] in Pic^tau(Y),
```

and hence there exists an integer

```text
N_Y >= 1
```

such that

```text
N_Y * w ~ 0.                                   (TORS)
```

The surface `Y` is fixed by the active absent node type and does not depend on the ray parameter `l` or on an individual hypothetical carrier. Therefore one may choose `N_Y` as the exponent of the finite group `Pic^tau(Y)`, uniformly for every `l` in this active `000707`, `e=2` route.

Substituting the definition of `w` gives the fixed-exponent linear-equivalence refinement

```text
N_Y*(C_1-C_2)
 ~ -N_Y*sum_(j in Sigma)(d_j/2)(E_j^+-E_j^-).  (ANTI-PIC-TOR)
```

This is strictly stronger than the retained numerical identity, but weaker than ordinary linear equivalence with exponent one.

## 5. What this does not determine

No value of `N_Y` is computed. In particular this note does **not** prove

```text
N_Y=1,
N_Y=2,
or w~0.
```

It also does not decide the branch allocations `d_j`, the conductor transition `M_(u,v)`, or the simultaneous residual sign of `(r_z,r_w)` at a conductor pair.

Thus the active leaf remains the conductor-preimage/residual-sheet map. The useful new alternative is narrower than before: an integral Picard attack no longer has to control a positive-dimensional `Pic^0(Y)` ambiguity. It only has to compute or kill the fixed finite group `Pic^tau(Y)` (or the particular class `[w]`) before promoting `(ANTI-PIC-TOR)` to exponent-one linear equivalence.

## Route consequence

The previous list of possible post-numerical obstructions

```text
continuous Pic^0 ambiguity,
finite torsion ambiguity,
actual conductor transition
```

reduces to

```text
finite torsion ambiguity,
actual conductor transition.
```

A successful next refinement may therefore use either:

1. a computation proving the relevant anti-invariant part of `Pic^tau(Y)` is trivial, or at least determining its exponent/class; or
2. the still-primary source-locked conductor-preimage map into `R=C8/H` / the equivalent residual square-root transport.

## Firewalls

- `Y` and `Xtilde_H` are asserted only birational, not isomorphic.
- `q(Y)=0` does not imply `pi_1(Y)=0`.
- `Pic^0(Y)=0` does not imply `Pic(Y)` is torsion-free.
- `(ANTI-PIC-TOR)` does not imply exponent-one linear equivalence.
- No torsion exponent is guessed.
- No individual conductor pair receives a residual sign.
- No weighted-cut upper bound is claimed.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge authorization.
