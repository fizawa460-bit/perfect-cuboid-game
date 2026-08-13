# Stage14-t108 — convert orientation support to projected primitive norm-form incidence

## Status

`COMPLETE_PROJECTED_PRIMITIVE_NORM_FORM_RECEIVER_AND_TH28_GATE`

Consumes Stage14-t107 on the same batch branch, merged Stage14-t91, and merged Stage14-t89.

For each orientation witness of

```text
delta0=Q/ell,
```

let

```text
gamma=u+i*v,
N(gamma)=u^2+v^2=delta0,
gcd(u,v)=1.
```

Merged t91 proves that, up to the finite unit/two-primary convention and the `B^o(1)` exceptional labels, primitive Gaussian representations of `delta0` are exactly the split-prime orientation-cube witnesses. Therefore the existential support statement from t107 is equivalent to an existential primitive binary norm-form statement:

```text
Q in S_B
<=>
exists fixed-packet label lambda of B^o(1) complexity,
exists primitive (u,v):
  Q=ell*(u^2+v^2),
  ell=LPF(Q), v_ell(Q)=1,
  all odd p|Q => p==1 mod 4,
  ell^2>4B,
  ell^2>2*h*k0*Q,
  h*k0*Q<=2B,
  P_lambda(u,v;ell,Q)=1.
```

Here `P_lambda` denotes the already-merged physical predicate after the exceptional packet data are frozen. By t89 its archimedean short-cover inequalities are consequences of the strong Q gap and budget, not independent analytic masks. Its remaining inputs are primitive/gcd data, fixed denominator-tag data, reciprocal/inversion orientation, endpoint/four-cell local conditions, positivity and canonical-unit conventions evaluated on the fixed integral linear forms arising from multiplication by the norm-`k0` Gaussian factor.

Thus the outer obstruction is no longer an unspecified Q-dependent bounded weight. It is the projection to Q of a primitive sum-of-two-squares incidence with a canonical largest-prime constraint and frozen physical linear/local masks.

```text
ORIENTATION_WITNESS_TO_PRIMITIVE_NORM_FORM_EQUIVALENCE=true
Q_SUPPORT_IS_PROJECTED_PRIMITIVE_SUM_OF_TWO_SQUARES_INCIDENCE=true
SHORT_COVER_ARCHIMEDEAN_MASKS_REMAIN_AUTOMATIC=true
ARBITRARY_Q_WEIGHT_RECEIVER_ELIMINATED=true
PROJECTED_NORM_FORM_SUPPORT_POWER_SAVING_PROVED=false
```

This is a material receiver change. The next progress requires a theorem-level audit of whether existing sieve/dispersion results can count this projected norm-form support with a fixed-power saving uniformly in the frozen fixed-U packet while retaining the canonical-LPF and physical masks.

## tH28 request

Open a new immutable independent audit:

```text
T_ROUTE_H_NEEDED=true
T_ROUTE_H_REQUEST=CanonicalLPFPrimitiveSumOfTwoSquaresProjectedPhysicalSupportSieveOrDispersion
T_ROUTE_H_TARGET=stages/stage14/14-t108/th28-target.md
T_ROUTE_H_BLOCKING=true
```

Required audit question: determine whether an existing theorem gives a uniform fixed-power saving for

```text
Q=ell*(u^2+v^2)
```

with `gcd(u,v)=1`, `ell=LPF(Q)`, `v_ell(Q)=1`, all odd prime factors split (`1 mod 4`), the strong gaps `ell^2>4B` and `ell^2>2*h*k0*Q`, budget `h*k0*Q<=2B`, and the frozen finite physical linear/congruence/orientation masks. Any theorem that requires deleting those masks or averaging over a different family is advisory only.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFProjectedPrimitiveNormFormPhysicalSupport
NEXT=Stage14-tH28
```
