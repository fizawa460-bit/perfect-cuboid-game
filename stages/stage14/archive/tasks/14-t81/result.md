# Stage14-t81 — projective-character resummation, affine frequency matching, and fractional Kloosterman graph reduction

## Status

`COMPLETE_PROJECTIVE_CHARACTER_RESUMMATION_TO_AFFINE_DIAGONAL_AND_FRACTIONAL_KLOOSTERMAN_GRAPH_KERNEL`

Stage14-t81 consumes merged t80 together with the exact t77 projective ray-class incidence.  The current whole-family theorem is the merged X13 square-root bound

```text
V(B) << B^(1/2+o(1)).
```

Merged s7-42 and 4da further contract the global square-root saturation geometry, but their coefficient space is not cross-promoted into the fixed-packet t-route.  Stage14-t81 proves no new whole-family exponent.  Its purpose is to remove a second artificial analytic freedom from the t80 kernel: the two additive frequencies are not independent after the projective-character family is resummed.

---

## 1. Entering t80 packet

Fix

```text
(U,epsilon,k,h,kappa,beta)
```

and all t78/t79 four-cell, dyadic, beta-tag, and reciprocal/inversion orientations.  Let

```text
M=K/gcd(K,g*k),
d=d(chi)=M/B^o(1)
```

be the near-full active support of a hard projective character.  Merged t80 gives, primewise on `p|d`, an affine Cayley chart

```text
X(x)=[1+i*x]
```

and normalized Fourier coefficients

```text
c_chi(a)=p^-1 sum_x chi(X(x)) e_p(-a*x),
|c_chi(0)|=1/p,
|c_chi(a)|<=2/sqrt(p)  (a!=0).
```

After the t80 zero-frequency peel the hard frequencies are primitive up to `B^o(1)` support.

Merged t77 gives the local class identity

```text
[pi]=C_p * sigma_p([V]),
C_p=[U]^-1 * I_beta,p,
```

where `sigma_p` is identity or inversion.  In the Cayley slope coordinate, write the fixed class `C_p` as slope `c_p` when finite; `[i]` is the point at infinity.

---

## 2. The fixed projective map is one Mobius graph

Let `s_p=+1` when `sigma_p` is the identity and `s_p=-1` when it is inversion.  Projective multiplication in the Cayley chart gives

```text
tau_{c,s}(y)=(c+s*y)/(1-s*c*y)                    (2.1)
```

when `C_p` has finite slope `c`.  If `C_p=[i]`, then

```text
tau_{infty,s}(y)=-s/y.                            (2.2)
```

Thus the t77 local class relation is exactly the graph condition

```text
x_pi=tau_{c_p,s_p}(x_V).                          (2.3)
```

The only affine degeneration is

```text
c_p=0,
```

for which

```text
tau_{0,s}(y)=s*y.                                 (2.4)
```

Every finite nonzero `c_p`, and the infinity class, gives a genuine fractional-linear graph.

```text
PROJECTIVE_CLASS_INCIDENCE_IS_SINGLE_MOBIUS_GRAPH=true
AFFINE_DEGENERACY_IFF_FIXED_CLASS_IDENTITY=true
```

---

## 3. Resumming the local nonprincipal character family

For primitive local frequencies `a,b mod p`, consider the t80 Fourier coefficients with the fixed class and `sigma` twist.  Character orthogonality gives, after the original `1/|G(p)|` normalization,

```text
K_p(a,b)
 = p^-2 * sum_{y affine, tau(y) affine}
       e_p(-a*tau(y)+b*y)
   + principal-subtraction.                       (3.1)
```

The principal subtraction is the product of two affine-chart additive sums divided by `|G(p)|p^2`.  For nonzero `a,b` it is zero at inert primes and `O(p^-3)` at split primes.  It never controls the hard size.

Hence the character family itself has disappeared.  The exact local object is the finite Fourier transform of one projective Mobius graph.

```text
LOCAL_PROJECTIVE_CHARACTER_FAMILY_RESUMMED=true
LOCAL_DUAL_KERNEL_IS_MOBIUS_GRAPH_FOURIER_TRANSFORM=true
```

This is stronger than applying Cauchy independently to the two t80 Fourier expansions.

---

## 4. Genuine fractional cells are classical Kloosterman phases

Assume first that `c!=0` is finite.  Put

```text
u=1-s*c*y.
```

Then

```text
y=s*(1-u)/c,

tau_{c,s}(y)
 =(c^2+1)/(c*u)-1/c.                              (4.1)
```

Therefore

```text
-a*tau_{c,s}(y)+b*y
 = constant
   - a*(c^2+1)/(c*u)
   - b*s*u/c.                                     (4.2)
```

Because `C_p` is a projective unit, `c^2+1` is nonzero whenever the affine class exists.  For primitive `a,b`, both Kloosterman coefficients in (4.2) are nonzero.

At an inert prime, the affine-affine graph is exactly `u in F_p^x`, so (3.1) contains one complete classical Kloosterman sum.  At a split prime the two isotropic affine points are omitted, costing only `O(1)` terms.  Consequently

```text
|K_p(a,b)| <= (2*sqrt(p)+O(1))/p^2
            = p^(-3/2)*B^o(1)                    (4.3)
```

on every genuine fractional cell.

For `C_p=[i]`, (2.2) gives directly

```text
-a*tau(y)+b*y = a*s/y+b*y,
```

again a Kloosterman phase with the same bound.

Thus each genuine fractional active prime gives an **extra local `p^-1/2` gain** compared with the natural two-Fourier-coefficient scale `p^-1`.

```text
FRACTIONAL_PROJECTIVE_GRAPH_IS_KLOOSTERMAN=true
FRACTIONAL_LOCAL_NORMALIZED_BOUND=p^(-3/2)*Bo1
FRACTIONAL_LOCAL_EXTRA_GAIN=p^(-1/2)*Bo1
```

No incomplete prime/cover large sieve is used in this local statement.

---

## 5. Affine cells force frequency matching

Now let `c=0`.  Then `tau(y)=s*y`, so the graph sum is

```text
sum_{y affine} e_p((b-s*a)*y).                    (5.1)
```

If `p==3 mod 4`, every finite slope is affine and

```text
K_p(a,b)=0                         if b != s*a mod p,
K_p(a,b)=p^-1*(1+O(1/p))           if b == s*a mod p.  (5.2)
```

If `p==1 mod 4`, two isotropic affine points are omitted.  Hence

```text
|K_p(a,b)| <= p^-1*(1+O(1/p))      if b == s*a mod p,
|K_p(a,b)| <= O(p^-2)               otherwise.       (5.3)
```

Thus an affine split-prime mismatch gives an extra `p^-1` gain, while an affine inert-prime mismatch vanishes exactly.

```text
AFFINE_INERT_FREQUENCY_MISMATCH_VANISHES=true
AFFINE_SPLIT_FREQUENCY_MISMATCH_EXTRA_GAIN=p^-1*Bo1
AFFINE_MATCH_CONGRUENCE=b=s*a_mod_p
```

---

## 6. CRT global graph kernel

Because `d` is squarefree and all orientations are fixed primewise, the local graph kernels tensorize.

Define

```text
d_frac = product_{p|d : C_p != identity} p,

d_aff  = d/d_frac.
```

On the affine support define the fixed sign vector

```text
s_d^2=1 mod d_aff,
s_d=s_p mod p.
```

For a primitive frequency pair `(a*b,d)=1`, let

```text
d_mis
 = product_{p|d_aff : b != s_p*a mod p} p.         (6.1)
```

If `d_mis` contains any inert prime, the full kernel is zero.  Otherwise (4.3), (5.2), and (5.3) give

```text
boxed:
|K_d(a,b)|
 <= d^-1 * d_frac^-1/2 * d_mis^-1 * B^o(1).       (6.2)
```

The factor `d^-1` is the natural matched-frequency scale; `d_frac^-1/2` and `d_mis^-1` are genuine additional gains obtained before any incomplete physical summation.

```text
GLOBAL_GRAPH_KERNEL_CRT_FACTORIZATION_PROVED=true
GLOBAL_GRAPH_KERNEL_BOUND=d^-1*d_frac^-1/2*d_mis^-1*Bo1
```

---

## 7. Hard support is almost affine and almost frequency-diagonal

Equation (6.2) gives an automatic fixed-power saving whenever

```text
d_frac^(1/2) * d_mis = B^(positive power+o(1)).    (7.1)
```

Therefore a t-route packet that can still contribute at the unsaved fixed-packet scale must satisfy

```text
d_frac=B^o(1),
d_mis=B^o(1).                                      (7.2)
```

Combined with t79/t80, the hard chain is now

```text
inactive character support        = B^o(1),
zero additive-frequency support   = B^o(1),
fractional fixed-class support    = B^o(1),
affine frequency-mismatch support = B^o(1).        (7.3)
```

Let

```text
d_diag=d/(d_frac*d_mis)=d/B^o(1).
```

Then exactly

```text
b == s_d*a (mod d_diag).                           (7.4)
```

For fixed primitive `a mod d`, the number of primitive `b mod d` satisfying (7.4) is at most

```text
d/d_diag = B^o(1).                                 (7.5)
```

Hence the two t80 additive frequencies collapse to one primitive frequency at endpoint-small multiplicity.

```text
HARD_GRAPH_SUPPORT_ALMOST_AFFINE=true
HARD_FREQUENCY_PAIR_ALMOST_DIAGONAL=true
TWO_ADDITIVE_FREQUENCIES_COLLAPSE_TO_ONE=Bo1
```

---

## 8. Fixed-class affine degeneration has an exact arithmetic meaning

Recall

```text
C_p=[U]^-1*I_beta,p.
```

Therefore

```text
C_p=identity
<=> [U]=I_beta,p.                                  (8.1)
```

Since `I_beta,p` is either `1` or `[i]`, the affine-degenerate primes are fixed-coordinate selectors:

```text
I_beta,p=1   => Im(U)==0 mod p,
I_beta,p=[i] => Re(U)==0 mod p.                    (8.2)
```

Thus the only support on which the Kloosterman `p^-1/2` gain disappears is not a new moving modulus.  It is a divisor of the beta-selected coordinate support of the already-fixed Gaussian factor `U`.

Stage14-t81 does not yet prove that this affine-degenerate support is endpoint-small uniformly over the moving fixed-U packets.  It records it as the remaining arithmetic specialization.

```text
AFFINE_DEGENERACY_IS_FIXED_U_BETA_COORDINATE_SUPPORT=true
AFFINE_DEGENERACY_NEW_MOVING_MODULUS=false
AFFINE_DEGENERATE_SUPPORT_UNIFORMLY_ENDPOINT_SMALL_PROVED=false
```

---

## 9. Refined physical receiver

After the automatic fractional/mismatch gains, the genuinely unsaved branch is

```text
SharedUBalancedNearFullSupport
AffineDegenerateAlmostDiagonal
SinglePrimitiveFrequencyCanonicalPrimeShortCoverInverseFractionEnergy
```

with

```text
d_diag=d/B^o(1),
b=s_d*a mod d_diag,
(a,d)=1,
```

and all t80 physical masks retained:

```text
ell=N(pi) canonical Gaussian direction prime,
ell^2>4B,
small angular-g four-cell weights,
balanced primitive cover,
gcd(r,t) in {1,2},
r,t<sqrt(ell),
ell*odd(h)*odd(r)*odd(t)<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U,
fixed beta and reciprocal orientation.
```

No strict sub-square-root saving is claimed here.

---

## 10. tH decision

The tH23 requested by t80 is still needed, but its theorem adapter should now use the narrower post-t81 object.  The two-frequency projective-character family no longer needs to be estimated directly.

Refined target:

```text
AffineDegenerateAlmostDiagonalSingleFrequencyCanonicalPrimeShortCoverInverseFractionLargeSieve
```

The tH23 audit should separately recognize:

1. `d_frac` fixed-power support is already saved locally by complete Kloosterman/Weil;
2. affine frequency mismatch is already saved locally;
3. only the `d/B^o(1)` matched sign line needs an incomplete physical estimate;
4. the affine-degenerate modulus is beta-selected fixed-`U` coordinate support.

```text
TH23_NEEDED=true
TH23_TARGET_REFINED_BY_T81=true
TH24_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH23=false
```

The refinement request is recorded in

```text
stages/stage14/14-t81/th23-refinement.md
```

---

## 11. Current global ledger

Latest merged global work remains at square-root scale:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T81_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t82
```

The fixed-U t-route is not cross-promoted into the global X/s/4d saturation ledger without an explicit quantifier bridge.

---

## Locked boundary

```text
STAGE14_T81=COMPLETE_PROJECTIVE_CHARACTER_RESUMMATION_TO_AFFINE_DIAGONAL_AND_FRACTIONAL_KLOOSTERMAN_GRAPH_KERNEL
MERGED_T80_IMPORTED=true
PROJECTIVE_CLASS_INCIDENCE_IS_SINGLE_MOBIUS_GRAPH=true
AFFINE_DEGENERACY_IFF_FIXED_CLASS_IDENTITY=true
LOCAL_PROJECTIVE_CHARACTER_FAMILY_RESUMMED=true
LOCAL_DUAL_KERNEL_IS_MOBIUS_GRAPH_FOURIER_TRANSFORM=true
FRACTIONAL_PROJECTIVE_GRAPH_IS_KLOOSTERMAN=true
FRACTIONAL_LOCAL_NORMALIZED_BOUND=p^(-3/2)*Bo1
FRACTIONAL_LOCAL_EXTRA_GAIN=p^(-1/2)*Bo1
AFFINE_INERT_FREQUENCY_MISMATCH_VANISHES=true
AFFINE_SPLIT_FREQUENCY_MISMATCH_EXTRA_GAIN=p^-1*Bo1
AFFINE_MATCH_CONGRUENCE=b=s*a_mod_p
GLOBAL_GRAPH_KERNEL_CRT_FACTORIZATION_PROVED=true
GLOBAL_GRAPH_KERNEL_BOUND=d^-1*d_frac^-1/2*d_mis^-1*Bo1
HARD_GRAPH_SUPPORT_ALMOST_AFFINE=true
HARD_FREQUENCY_PAIR_ALMOST_DIAGONAL=true
TWO_ADDITIVE_FREQUENCIES_COLLAPSE_TO_ONE=Bo1
AFFINE_DEGENERACY_IS_FIXED_U_BETA_COORDINATE_SUPPORT=true
AFFINE_DEGENERATE_SUPPORT_UNIFORMLY_ENDPOINT_SMALL_PROVED=false
SINGLE_FREQUENCY_PHYSICAL_INVERSE_FRACTION_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T81_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
TH23_NEEDED=true
TH23_TARGET_REFINED_BY_T81=true
TH24_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH23=false
NEXT=Stage14-t82
```