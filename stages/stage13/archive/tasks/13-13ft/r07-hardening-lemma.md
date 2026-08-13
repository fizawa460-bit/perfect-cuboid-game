# Stage13-13ft — R07 exact arithmetic and quantifier hardening

> STATUS: `STAGE13_13FT_R07_HARDENING`
>
> PURPOSE: complete the non-theorem-changing hardening obligations left after R07 Gates A–C. This note removes the remaining avoidable ambiguity in the explicit Wiener constants, retained-harmonic logarithmic moments, overlap squeeze quantifiers, and the frozen Stage12 factor-two interface.
>
> INPUTS: `13-13fb`, `13-13fe`, `13-13fq`, `13-13fr`, `13-13fs`.

No theorem constant changes in this stage.

---

## 1. Exact rational inequalities for the Wiener constants

The large split-prime coefficient estimate obtained in `13-13fb` is

\[
\frac{3465625}{6561}.
\]

The comparison with `529` is exact, with no floating-point input:

\[
529\cdot6561=3470769,
\]

and

\[
\boxed{3465625<3470769}.
\]

Therefore

\[
\boxed{\frac{3465625}{6561}<529}.
\]

Likewise the exceptional split prime `p=5` gives exactly

\[
\frac{10799919009}{25000000}.
\]

Since

\[
432\cdot25000000=10800000000
\]

and

\[
\boxed{10799919009<10800000000},
\]

we have the exact rational inequality

\[
\boxed{\frac{10799919009}{25000000}<432}.
\]

The decimals used historically are checks only and have no proof role.

```text
WIENER_529_PROVED_BY_INTEGER_INEQUALITY=true
WIENER_P5_432_PROVED_BY_INTEGER_INEQUALITY=true
FLOATING_POINT_USED_AS_PROOF=false
```

---

## 2. Retained-harmonic logarithmic moments are uniform in ell

Let the global mixed correction for retained harmonic `ell` have coefficients

\[
C_\ell(\mathbf s)=\sum_{u,v,w\ge1}
\frac{c_\ell(u,v,w)}{u^{s_h}v^{s_r}w^{s_s}}.
\]

The phase-uniform local Wiener estimate from `13-13fb` implies a global constant `K`, independent of every retained `ell`, such that

\[
\boxed{
\sum_{u,v,w}
\frac{|c_\ell(u,v,w)|}{(uvw)^{5/8}}
\le K.
}
\]

The point is that the local majorants depend only on absolute coefficient bounds such as `|2 cos(n vartheta)|<=2`; the phase `vartheta=vartheta(ell,p)` disappears before the Euler product is summed. Hence the same `K` works for all retained `ell`.

Fix any integer `m>=0`. Put `n=uvw`. Then

\[
\frac{(1+\log n)^m}{n}
=
\frac{1}{n^{5/8}}
\frac{(1+\log n)^m}{n^{3/8}}.
\]

The elementary function

\[
x\mapsto (1+x)^m e^{-3x/8}
\]

is bounded on `[0,infinity)`. Therefore there exists a constant `C_m`, depending only on `m`, such that

\[
\frac{(1+\log n)^m}{n^{3/8}}\le C_m
\qquad(n\ge1).
\]

Consequently

\[
\boxed{
\sup_{\ell\ge1}
\sum_{u,v,w}
\frac{|c_\ell(u,v,w)|(1+\log(uvw))^m}{uvw}
\le C_m K<\infty.
}
\]

This is the precise uniform logarithmic-moment statement used when replacing, for example,

\[
(\log(X/n))^j-(\log X)^j
\]

by a bound of size

\[
O((1+\log n)(\log X)^{j-1}).
\]

Thus the mixed-log shift estimate and all fixed derivative moments are genuinely uniform in the retained harmonic index.

```text
RETAINED_ELL_LOG_MOMENTS_UNIFORM=true
PHASE_UNIFORM_WIENER_MAJORANT_IMPLIES_LOG_MOMENTS=true
```

---

## 3. Epsilon-form overlap squeeze

For a fixed direction `q`, let

\[
D_q=\frac{\kappa I_q}{3\pi^3}>0.
\]

For `k>=1`, choose distinct inert primes `p_1,...,p_k>=7` and put

\[
S_k=\{p_1,\ldots,p_k\}.
\]

Gate R07-B gives, for this fixed finite set,

\[
A^{\rm tag}_{q,S_k}(B)
=2D_q\left(\prod_{p\in S_k}\lambda_p\right)B(\log B)^3
+o_{S_k}(B(\log B)^3),
\]

with

\[
\lambda_p\le\frac34.
\]

Every genuine pair overlap injects into this accepted tagged set, so

\[
0\le O_{qr}(B)\le A^{\rm tag}_{q,S_k}(B).
\]

To prove the little-`o` statement in its epsilon definition, let `epsilon>0` be arbitrary.

1. Choose `k` so large that
   \[
   2D_q\left(\frac34\right)^k<\frac\epsilon2.
   \]
2. Hold this `k`, and therefore `S_k`, fixed. By the fixed-`S_k` asymptotic there exists `B_0=B_0(k,epsilon)` such that for every `B>=B_0`,
   \[
   \left|
   \frac{A^{\rm tag}_{q,S_k}(B)}{B(\log B)^3}
   -2D_q\prod_{p\in S_k}\lambda_p
   \right|<\frac\epsilon2.
   \]
3. Hence for `B>=B_0`,
   \[
   0\le
   \frac{O_{qr}(B)}{B(\log B)^3}
   <\frac\epsilon2+\frac\epsilon2
   =\epsilon.
   \]

Therefore

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}.
\]

Since the triple overlap is a subset of every pair overlap,

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

The order of quantifiers is exactly

```text
for epsilon>0
-> choose fixed k (hence fixed S_k)
-> choose B0 depending on that fixed k
-> B >= B0.
```

There is no `k=k(B)` and no residue modulus growing with `B`.

```text
OVERLAP_SQUEEZE_EPSILON_FORM_EXPLICIT=true
LIMIT_ORDER=FIX_S_THEN_B_TO_INFINITY_THEN_ENLARGE_S
GROWING_MODULUS_THEOREM_USED=false
```

---

## 4. Stage12 projection fiber: exact object-level wording

The frozen Stage12 object is a **primitive oriented distinguished-face record**. It retains a chosen integral face and an order on the two legs of that face before the physical cuboid is canonically sorted.

For canonical face direction `q`, let `A_q(B)` count raw Stage13 incidences with that distinguished canonical face. The projection from Stage12 records to one canonical raw incidence has exactly the two preimages

\[
(x,y)\qquad\text{and}\qquad(y,x)
\]

for the ordered legs of the distinguished face.

These are **two Stage12 records of the same projected canonical incidence**, not two different canonically ordered cuboids. Only the projected Stage13 object is required to satisfy the canonical order `a<b<c`; the two oriented preimages live before that sorting operation.

Therefore, for every finite `B`,

\[
\boxed{C_{\rm prim,q}^{\rm proj}(B)=2A_q(B)}
\]

and hence

\[
\boxed{C_{\rm prim}(B)=2\sum_q A_q(B)}.
\]

There is no additional factor from `r<s`, OE/EE parity, or 2-adic normalization. The same two-element oriented-leg fiber holds branchwise.

For a multi-face cuboid, the distinguished-face incidence convention is preserved: an exactly-two-face cuboid contributes two Stage13 raw incidences and four Stage12 oriented records; an exactly-three-face cuboid contributes three incidences and six Stage12 records. Thus the factor two is exact before and after inclusion-exclusion.

```text
STAGE12_COUNTING_TARGET=PRIMITIVE_ORIENTED_DISTINGUISHED_FACE_RECORDS
STAGE13_PROJECTION_FIBER=2
PROJECTION_FIBER_REASON=TWO_ORDERS_OF_DISTINGUISHED_FACE_LEGS
TWO_PREIMAGES_ARE_NOT_TWO_CANONICAL_CUBOIDS=true
PROJECTION_PARITY_STRATIFIED=true
EXTRA_2ADIC_PROJECTION_FACTOR=false
MULTI_FACE_FACTOR_TWO_EXACT=true
```

---

## 5. R07 hardening status

The theorem-level repair gates were already closed by `13-13fq`, `13-13fr`, and `13-13fs`. This stage closes the remaining Gate D hardening obligations without changing the theorem.

```text
STAGE13_13FT=COMPLETE_R07_EXACT_ARITHMETIC_AND_QUANTIFIER_HARDENING
R07_GATE_D=COMPLETE
R07_GATES_A_B_C_D_COMPLETE=true
R07_REPAIR_BLOCKERS_OPEN=0
R07_HARDENING_OBLIGATIONS_OPEN=0
WIENER_529_PROVED_BY_INTEGER_INEQUALITY=true
WIENER_P5_432_PROVED_BY_INTEGER_INEQUALITY=true
RETAINED_ELL_LOG_MOMENTS_UNIFORM=true
OVERLAP_SQUEEZE_EPSILON_FORM_EXPLICIT=true
STAGE12_ORIENTED_TWO_FIBER_WORDING_EXPLICIT=true
SUM_IQ_ANALYTIC_IDENTITY_REOPEN_REQUIRED=false
FINITE_SUM_CAN_RESTORE_ABSENT_HIGHER_POLE=false
TAGGED_SHARED_EDGE_INJECTION_REOPEN_REQUIRED=false
STAGE12_TWO_ORIENTED_PREIMAGES_REOPEN_REQUIRED=false
R06_IMMUTABLE=true
R07_CANONICAL_SYNTHESIS_READY=true
R07_FRESH_EXTERNAL_REVIEW_REQUIRED=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13fu
```
