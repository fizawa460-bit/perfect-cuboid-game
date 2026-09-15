# Stage32 MB104 — `000707000f0f` e=2 even norm-form conductor scheme

Status: **RETAINED CONDITIONAL LOCAL-ALGEBRA REFINEMENT / RESIDUAL EIGENSECTION BASE LOCUS IDENTIFIED WITH CROSS-SHEET CONDUCTOR INTERSECTION SCHEME / e=2 OPEN / NO CREDIT**

## Scope

Continue the even case `l=2m` of the active leaf and inherit the candidate ambient-H1 / half-hyperplane input from the preceding norm-form baselocus refinement.

On the etale locus of the residual double cover, the downstairs carrier norm is locally

```text
F=u^2-f_t v^2,
```

and after choosing a local square root

```text
r^2=f_t,
```

it factors as

```text
F=a*b,
a=u+r v,
b=u-r v.                                      (FACT)
```

The purpose here is to identify the local conductor intersection represented by the common zero scheme.

## 1. Away from the eigensection base locus there is only one residual sheet branch

Let `R` be the completed or strict-henselian regular local ring of the smooth surface `S` at a carrier point away from the absent branch divisor. Then `r` is a unit in the chosen etale local splitting.

If `(u,v)` is not the maximal-ideal pair `(0,0)` at the point and `F=0`, exactly one of `a,b` vanishes while the other is a unit. Locally the carrier is therefore represented by only one of the two sheet factors.

Equivalently the ambient square root

```text
g=u/v
```

(or `v/u` in the complementary chart) extends across the ambient point and has the same limit on every normalization branch belonging to that local factor.

Thus same-point branches can acquire opposite residual sheet labels only at a common zero of `u` and `v`.

## 2. At a common zero the two sheet factors meet with ideal `(u,v)`

At a common zero, both factors in `(FACT)` vanish. Since `2r` is a unit, the linear change of generators

```text
(a,b)=(u+rv,u-rv)
```

is invertible. Hence exactly

```text
(a,b)=(u,v)                                     (IDEAL)
```

as ideals in the local ring.

Therefore the local intersection multiplicity of the two residual sheet factors is

```text
I_p(a,b)
 = length_R R/(a,b)
 = length_R R/(u,v).                            (LOCAL-I)
```

The etale double cover has two local lifts of the downstairs point. At the second lift the roles of `a,b` are exchanged, so the same length occurs again. Consequently a residual downstairs common-zero length `I` contributes

```text
2I
```

to `C1.C2=y`, or equivalently exactly `I` to the retained weighted cut `y/2`.

Thus, after removing the fixed exceptional contributions discussed below, the residual base-locus zero-cycle is not merely a support bound: its scheme length is the cross-sheet conductor intersection weight.

## 3. Supported exceptional correction is exact local excess intersection

At a supported exceptional `E`, remove the common eigensection vanishing order

```text
mu=4m-|b|.
```

The retained adaptive cancellation order is

```text
q=2|b|.
```

After formally trivializing `L_abs` near `E`, one of the two residual conjugate combinations has order zero and the other order `q`. In a local equation `e=0` write

```text
b=k,
a=e^q h,
```

where `k` does not contain `E` as a component. By the same invertible linear change as `(IDEAL)`, the residual eigensection base ideal is

```text
(u',v')=(k,e^q h).
```

Its intersection with the `q`-fold exceptional factor splits as

```text
I(k,e^q h)
 = q*(k.E) + I(k,h).                            (SPLIT)
```

The retained line-bundle calculation gives

```text
k.E=2mu.
```

Hence the first term in `(SPLIT)` is exactly

```text
2mu*q.                                         (FIXED)
```

This is the forced exceptional cancellation contribution. The remaining term `I(k,h)` is precisely the residual meeting of the two sheet factors after the exceptional factor has been removed, hence contributes to the cross-sheet conductor scheme.

## 4. Global scheme-length identity

Summing the residual eigensection intersection over the surface gives

```text
A_mu.B_mu
 =336m^2+16mR1-2Q.
```

Summing the forced local terms `(FIXED)` gives

```text
sum_j 2mu_j q_j
 =16mR1-4Q.
```

Therefore the residual common-zero scheme has total length

```text
length Z_res(u,v)
 =336m^2+2Q.                                    (ZLEN)
```

By `(LOCAL-I)` and the two-lift accounting,

```text
length Z_res(u,v)=y/2.                          (SCHEME-CUT)
```

This recovers the retained A1 square-energy formula at scheme level, not just as a numerical coincidence.

## Route consequence

For even `l`, within the retained candidate eigensection framework, the active residual-sheet problem admits the exact translation

```text
branchwise cross-sheet conductor intersection
<=>
residual common-zero scheme of the downstairs eigensections (u,v),
```

with the supported-exceptional excess `sum 2mu_j q_j` removed explicitly.

This removes the need to model the aggregate weighted cut as fourteen independent local sign choices. The next genuinely new computation is the global geometry/rank of the modified two-section base locus under the adaptive normal-jet conditions. A closure would require a bound or incompatibility beyond the already-known total length `(SCHEME-CUT)`.

## Firewalls

- The result inherits the candidate status of the ambient-H1/half-hyperplane linearization.
- It identifies the aggregate cross-sheet intersection scheme after the exact exceptional correction; it does not label every individual normalization branch in the original conductor presentation.
- No new upper or lower bound beyond the retained exact length is claimed.
- No existence of a nondegenerate eigensection pair is proved.
- `e=2`, `e=4`, `000707000f0f`, MB104, span5, finite-window, receiver, effectivity, theorem and endpoint credit remain open/zero.
- No heavy compute is armed.
- No merge or rebase authorization.
