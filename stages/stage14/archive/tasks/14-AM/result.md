# Stage14-AM — Azevedo--Moreira physical-selector transfer audit

## Status

```text
STAGE14_AM=COMPLETE
FINAL_CLASSIFICATION=BLOCKED
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_EXPONENT=1/2
```

This audit uses merged main `b63ac232` through `Stage14-Work-bfX18`, including merged `q11`, `X15`, `Work-beX17`, `4dl`, `4dm`, `s7-55`, `s7-56`, and `t96`.  Unmerged descendants are advisory only and are not theorem sources.

The sources checked at theorem/proof-contract level are:

1. G. Azevedo and J. Moreira, *Pythagorean triples in level sets of completely multiplicative functions*, arXiv:2607.04903, especially Theorems 1.2, 1.10, 1.12 and the averaging scheme in Sections 1.3--1.5;
2. N. Frantzikinakis and B. Host, *Higher order Fourier analysis of multiplicative functions and applications*, arXiv:1403.0945;
3. N. Frantzikinakis and A. Mountakis, *Recurrence for pretentious systems along generalized Pythagorean triples*, arXiv:2508.09778.

No result below treats a literature resemblance as a power saving.

## 1. Exact dictionary

On the primitive Euclid chart used by the Stage14 global packet, write

```text
AM variables                 Stage14 variables
m,n                          Euclid/Pythagorean chart coordinates
P_x=m^2-n^2                  first signed projection
P_y=2mn                      even projection / cofactor projection
P_z=m^2+n^2                  Gaussian norm projection
k P_x,k P_y,k P_z            common radial dilation of the triple
k averaged in a mult. Folner set   absent: primitive physical packet fixes k=1
f_j:N->S^1                   candidate completely multiplicative phase
psi(f_j(P_*))                candidate smooth phase-level selector
triangle m>n                 only one coarse angular support condition
W_+,W_-,W_k                  physical signed/norm selectors after all masks
pair covariance              Delta_pair + Err_pair (s7-55/4dm notation)
connected triple term        kappa_3(W_+,W_-,W_k)
```

The polynomial identity is exact.  The probability spaces are not: AM averages over the whole positive triangle and then over a common multiplier `k` along a multiplicative Folner sequence; Stage14 conditions on a full-conductor, near-maximal, interior-dense, primitive, root-oriented, charged-once packet and fixes the primitive radial scale.

## 2. Hypothesis ledger

| AM contract | Status | Stage14 audit |
|---|---|---|
| Pythagorean parametrisation by `m^2-n^2,2mn,m^2+n^2` | VERIFIED | Exact on the selected Euclid chart, up to the already-accounted finite fibres/signs. |
| Fixed finite family `f_1,...,f_d` | FAILED | Full conductor grows with `B`; the rational root projector alone needs `phi(q)=B^{chi+o(1)}` characters when `q=B^{chi+o(1)}`. |
| Every `f_j` unimodular and completely multiplicative on `N` | FAILED | Full physical selectors contain inequalities, primitivity/gcd, root orientation and charged-once bookkeeping; no such factorisation is proved. |
| Whole triangular `(m,n)` average | FAILED | Stage14 uses a conditioned near-maximal interior-dense packet. |
| Common multiplier `k` averaged through a multiplicative Folner sequence | FAILED | Stage14 fixes primitive `k=1`; averaging it back destroys the primitive receiver. |
| Fixed test function `psi` and qualitative positive limsup | VERIFIED for AM, insufficient for Stage14 | It proves recurrence/existence, not a uniform upper bound or rate. |
| Aperiodic branch gives vanishing polynomial averages | VERIFIED for fixed AM phases | No uniform fixed-power rate in growing conductor/complexity is supplied. |
| Pretentious branch concentrates | VERIFIED for AM | This preserves recurrence and can support saturation; it is not a deficit theorem. |
| Physical masks retained under transfer | UNVERIFIED | This is precisely the missing adapter. |

Thus AM is not `DIRECT`, and the adapter needed for `NEAR_WITH_PROVED_ADAPTER` is not proved.

## 3. What does decompose

Let `q=prod_{p in P} p` be squarefree with all `p=1 mod 4`, choose a Gaussian prime `pi_p` above every `p`, and let `epsilon_p(z)` record which of `pi_p,bar(pi_p)` divides the relevant primitive Gaussian factor.  For a prescribed orientation vector `epsilon^0`, the local ideal-orientation projector has the exact Walsh expansion

```text
1_{epsilon(z)=epsilon^0}
 = 2^(-r) sum_{S subset P} prod_{p in S} epsilon_p(z) epsilon_p^0,
r=|P|.
```

Each product is an ideal-/Hecke-multiplicative phase on the coprime Gaussian domain.  The number of terms is `2^r`; the coefficient `l1` cost is exactly `1` and the coefficient `l2` cost is `2^(-r/2)`.  In the Stage14 squarefree-support regime `r=omega(q)=O(log B/log log B)`, hence

```text
2^r = B^o(1).
```

This is a genuine local adapter for orientation only.  It is not an AM adapter: these phases live on Gaussian ideals/elements, their definition is restricted by coprimality and the selected factorisation, and AM's theorem is for fixed completely multiplicative functions on positive integers.

By contrast, if the same prescribed root is encoded as a single residue class `a mod q` and expanded inside ordinary Dirichlet/ray characters, orthogonality gives

```text
1_{n=a (mod q)} = 1/phi(q) sum_{chi mod q} conjugate(chi(a)) chi(n)
```

on units.  All `phi(q)` Fourier coefficients are nonzero.  Character orthogonality therefore makes `phi(q)` the exact support size in that character basis.  For full conductor `q=B^{chi+o(1)}` this is `B^{chi+o(1)}`, not `B^o(1)`.  The coefficient `l1` cost is still `1`, so the obstruction is dimension/term count rather than coefficient mass.

## 4. What does not decompose

Even after using the `2^r` Gaussian orientation expansion, no exact `B^o(1)`-term formula is established for

```text
W_+, W_-, W_k,
Delta_pair,
Err_pair,
kappa_3(W_+,W_-,W_k)
```

with all of the following simultaneously retained:

```text
full physical range/angular masks;
primitive and gcd conditions;
near-maximal/full-conductor conditioning;
root orientation;
charged-once identification of the three pair charts.
```

The smallest concrete obstruction to importing AM is already the radial quantifier mismatch:

```text
AM: average over common k in a multiplicative Folner sequence;
Stage14: impose gcd(P_x,P_y,P_z)=1 and fix k=1.
```

The AM proof may choose highly divisible common multipliers (indeed its Folner sets eventually contain every fixed divisor).  Projecting this average to the single primitive fibre has no positive-density or quantitative consequence.  This obstruction persists even if the orientation projector is supplied for free.

## 5. Uniform and structured branches

The Frantzikinakis--Host/Azevedo--Moreira aperiodic branch gives qualitative vanishing for a fixed bounded multiplicative phase system.  Stage14 would need a bound uniform in a `B`-dependent family and strong enough to give `B^{-delta}` after the `B^o(1)` expansion.  No cited theorem supplies such a fixed `delta`; therefore

```text
APERIODIC_BRANCH_FIXED_POWER_SAVING=false.
```

The pretentious branch is more decisive: AM and the pretentious recurrence theorem show that structured phases can sustain positive Pythagorean recurrence.  None of the primitive, gcd, orientation, or charged-once conditions is currently proved to force either a fixed-power density deficit or a signed anticorrelation inside this branch.  Therefore sqrt saturation remains compatible with all imported results:

```text
PRETENTIOUS_SQRT_SATURATION_EXCLUDED=false.
```

## 6. Exponent ledger and verdict

```text
input whole-family exponent                    1/2
Gaussian orientation expansion cost           B^o(1)
rational full-root character term count        B^(chi+o(1))  [unacceptable]
aperiodic quantitative gain                    0 proved
pretentious density/anticorrelation gain       0 proved
output whole-family exponent                   1/2
```

Final classification:

```text
DIRECT=false
NEAR_WITH_PROVED_ADAPTER=false
NEAR_ADAPTER_INCOMPLETE=false
BLOCKED=true
```

`NEAR_ADAPTER_INCOMPLETE` is not used as the final label because two independent theorem-contract failures remain after the useful local orientation adapter: primitive `k=1` versus multiplicative-Folner dilation, and qualitative fixed-family recurrence versus a quantitative growing-family upper bound.

## 7. Single next lemma

The next target is deliberately one lemma, not another literature search:

```text
Primitive Physical Hecke Adapter Lemma.

On every full-conductor, near-maximal, interior-dense charged-once cell,
after exact Mobius projection to k=1, express each centered W_*, and hence
Delta_pair, Err_pair and kappa_3, as at most B^o(1) Gaussian Hecke phases
with total coefficient l1 cost B^o(1), uniformly in the conductor, while
preserving the physical angular/range masks.
```

A proof would move the classification to `NEAR_ADAPTER_INCOMPLETE` and expose the separate quantitative uniform/pretentious tasks.  A lower bound showing that one retained physical mask requires `B^c` phases would close the AM route completely.

