# Stage14-tH25 — fixed-discriminant ring-class prime-value applicability audit

## Status

```text
STAGE14_TH25=COMPLETE_T86_SNAPSHOT_FIXED_DISCRIMINANT_RING_CLASS_PRIME_VALUE_APPLICABILITY_AUDIT
```

This is the immutable Stage14-t86 snapshot audit requested by

```text
stages/stage14/14-t86/th25-target.md
```

under `stages/stage14/H-PROTOCOL.md`.

```text
H_STAGE=Stage14-tH25
AUDITED_THROUGH=Stage14-t86
SOURCE_SNAPSHOT_SHA=798191aa5071a344cf642a1be265f1ad8e373fd5
TARGET_FILE=stages/stage14/14-t86/th25-target.md
REQUESTED_OBJECT=FixedUFixedDiscriminantMinus4dSquaredFixedCofactorPrimeValueFormPhysicalSieve
TARGET_FROZEN=true
```

Later t87+ work is not part of this mathematical audit.

The current whole-family context at dispatch is still

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

No global exponent change is claimed here.

---

## 1. Frozen t86 receiver

Fix

```text
(U,epsilon,k,h,kappa,beta),
U=R+iS,
eta in {1,2},
k0=eta*k,
d|D_Ubeta|R*S,
d odd squarefree.
```

For each physical point t86 gives

```text
delta0 odd,
gcd(d,k0*delta0)=1,
rho^2 == -1 mod delta0,
T=rho*d*j+delta0*s,
D=d*j,
gcd(s,d*j)=1,
```

and the primitive positive-definite form

```text
F(s,j)
 = delta0*s^2
   + 2*rho*d*s*j
   + ((rho^2+1)/delta0)*d^2*j^2
```

with

```text
Disc(F)=-4*d^2,
F(s,j)=k0*ell,
ell prime,
ell=LPF(F),
v_ell(F)=1,
ell>2*k0*delta0.
```

The full t86 physical inequalities and reconstructed-cover filters are retained throughout this audit. In particular, no moving short cofactor is restored to the value side and no independent `pi x V` multiplicity is reopened.

```text
T86_FIXED_DISCRIMINANT_RETAINED=true
T86_FORM_DISCRIMINANT=-4*d^2
T86_FIXED_VALUE_COFACTOR_RETAINED=true
T86_MOVING_DELTA_VALUE_SIDE_ELIMINATED=true
T86_FORM_CLASS_FAMILY_RETAINED=true
T86_GAUSSIAN_IDEAL_FACTORIZATION_RETAINED=true
T86_FIXED_K_PEEL_RETAINED=true
BILINEAR_PI_V_MULTIPLICITY_REOPENED=false
```

---

## 2. The pair `(delta0,rho)` is a ring-class label, not a harmless coefficient

Let

```text
O_d = Z + d*i*Z
```

be the order of conductor `d` in `Q(i)`. Its discriminant is exactly

```text
Disc(O_d)=-4*d^2.
```

For the t86 form

```text
[delta0, 2*rho*d, c*d^2],
c=(rho^2+1)/delta0,
```

the standard proper-ideal representative is, up to the harmless sign convention on `rho`,

```text
A_{delta0,rho}
 = (delta0, d*(i-rho)) subset O_d.
```

Because

```text
gcd(delta0,d)=1,
rho^2==-1 mod delta0,
```

this is an invertible proper `O_d`-ideal of norm `delta0`. Hence varying `(delta0,rho)` varies a genuine proper ring-class label.

```text
T86_FORM_CLASS_IDENTIFIED_WITH_RING_CLASS=true
T86_FORM_CLASS_ORDER=Z_PLUS_d_i_Z
DELTA0_RHO_ARE_RING_CLASS_DATA=true
```

This is the first obstruction that must be charged correctly before any prime theorem can yield a packet saving.

---

## 3. Ambient class number has polynomial `d` scale

For odd squarefree `d>1`, the class number of the order `O_d` is

```text
h(-4*d^2)
 = (d/2) * product_{p|d} (1-chi_4(p)/p),
```

where `chi_4(p)=+1` for `p==1 mod 4` and `-1` for `p==3 mod 4`. For `d=1`, the class number is one.

Thus uniformly

```text
h(-4*d^2)=d*B^o(1)
```

on polynomial Stage14 ranges.

The deterministic tH25 audit independently enumerates reduced primitive forms for

```text
d=3,5,7,11,15,21,33,35,55,65,77
```

and verifies the exact conductor class-number formula in every sample.

```text
RING_CLASS_NUMBER_SCALE=d*Bo1
RING_CLASS_NUMBER_IS_NOT_UNIFORMLY_BO1=true
```

Therefore a `1/h(-4d^2)` prime density for one fixed class can only become a physical packet saving if the Stage14 forms occupy power-fewer than `h(-4d^2)` classes.

---

## 4. The t86 form shape is capable of spanning the full ring class group

The class-family issue is not a cosmetic worst-case concern.

For a fixed conductor `d`, every proper form class of discriminant `-4d^2` represents infinitely many rational primes away from `2d`. For such a represented prime `q`, necessarily

```text
q==1 mod 4.
```

Choose a representative in that class with leading coefficient `q`:

```text
[q,b,c].
```

Because `gcd(q,d)=1`, a proper-equivalence shear

```text
b -> b + 2*q*t
```

can be chosen by CRT so that

```text
2*d | b.
```

Write

```text
b=2*rho*d.
```

The discriminant identity

```text
b^2-4*q*c=-4*d^2
```

then gives

```text
rho^2==-1 mod q,
```

so this representative is exactly of the t86 shape with

```text
delta0=q.
```

Hence the unrestricted family of forms

```text
[delta0,2*rho*d,((rho^2+1)/delta0)*d^2],
rho^2==-1 mod delta0,
gcd(delta0,d)=1,
```

is capable of realizing every proper class of discriminant `-4d^2`.

```text
UNRESTRICTED_T86_FORM_SHAPE_SPANS_FULL_RING_CLASS_GROUP=true
```

This statement does **not** assert that the Stage14 physical upper bounds on `delta0` reach every class for every packet. It shows instead that there is no hidden one-class, one-genus, or `B^o(1)` collapse coming merely from the algebraic shape.

The t86 target gives only

```text
ell*eta*delta0<=Y_U,
2*epsilon*eta*d*delta0<sqrt(B),
4*epsilon*eta^2*d*delta0^2<Y_U,
```

and does not prove that the surviving physical `(delta0,rho)` labels occupy `B^o(1)` classes or a fixed-power-small fraction of the ring class group.

The deterministic audit gives a finite adversarial regression: with `delta0<=4000`, the t86-shaped forms already hit **every** reduced class for each sample conductor through `d=77`; this is used only as a no-collapse regression, not as an asymptotic theorem.

```text
PHYSICAL_FORM_CLASS_SUBFAMILY_BO1_PROVED=false
PHYSICAL_FORM_CLASS_POWER_SPARSE_PROVED=false
FORM_CLASS_FAMILY_POWER_COST_CONTROLLED=false
```

This is the decisive tH25 obstruction.

---

## 5. The fixed `k0` factor can be peeled at class level, but this does not save a class factor

The t86 point has

```text
F(s,j)=k0*ell,
gcd(d,k0)=1
```

apart from the already-conditioned `O(1)` 2-primary branch. Since the odd primes of the physical norm are split and prime to the conductor, the proper invertible ideal attached to a primitive representation factors as

```text
A_k * P_ell,
N(A_k)=oddpart(k0),
N(P_ell)=ell.
```

Conditioning the split-prime orientations of `A_k` costs at most

```text
2^omega(k0)=B^o(1).
```

Composition with `A_k^{-1}` therefore translates the ring-class label and leaves a prime-ideal class of norm `ell`.

```text
FIXED_K_IDEAL_COMPOSITION_ADAPTER_PROVED=true
FIXED_K_IDEAL_COMPOSITION_LOSS=Bo1
FIXED_K_COMPOSITION_REDUCES_CLASS_FAMILY=false
```

The last line matters: multiplication by one fixed class is a bijection of the class group. Peeling `k0` does not reduce the number of possible t86 classes. It also does not by itself convert the original `(s,j)` physical box and reconstructed-cover filters into a standard reduced-form box.

Thus t86 successfully removes the moving value cofactor, but the ring-class-family cost survives intact.

---

## 6. Single-form growing-discriminant prime bounds are relevant but not a uniform t86 adapter

Asif Zaman's uniform upper-bound theorem for primes represented by a primitive positive-definite form of discriminant `-D` gives the expected single-class scale

```text
pi_f(x) << x/(h(-D)*log x)
```

in an explicit polynomial range in `D`. Unconditionally, the form-independent corollary requires roughly

```text
x >= D^(2+epsilon).
```

For the t86 discriminant magnitude

```text
D=4*d^2,
```

this generic condition is roughly

```text
ell >= d^(4+epsilon).
```

The sharper reduced-form theorem depends on the reduced leading coefficient, but the t86 target does not force its corresponding unconditional range either.

A deterministic exponent witness retained in the audit is

```text
d=B^(3/20),
delta0=B^(3/20),
ell=B^(1/5),
Y_U=B^(47/100),
```

with fixed packet constants. It satisfies the target's scale inequalities

```text
d*delta0 < B^(1/2),
d*delta0^2 < Y_U,
ell*delta0 < Y_U,
ell > delta0
```

at exponent level, while

```text
ell << d^3 << d^4.
```

Thus the t86 range does not force even the best unconditional single-form scale needed by the known general theorem.

More importantly, where a single-form theorem does apply, its class-number gain is

```text
1/h(-4*d^2)=d^-1*B^o(1).
```

The t86 form family has not been proved to use power-fewer than `h(-4*d^2)` classes. Summing a single-class estimate over a full `d*B^o(1)` class family can therefore consume the entire class-number gain.

```text
SINGLE_FORM_GROWING_DISCRIMINANT_PRIME_BOUND_RELEVANT=true
TARGET_FORCES_ZAMAN_UNCONDITIONAL_RANGE=false
GROWING_DISCRIMINANT_FORM_PRIME_THEOREM_APPLICABLE=false
RING_CLASS_PRIME_THEOREM_APPLICABLE=false
```

---

## 7. Ring-class / class-group large-sieve results do not fit the frozen family

Ditchen proves Bombieri--Vinogradov and Barban--Davenport--Halberstam analogues for primes represented by form classes by developing a large sieve for complex ideal-class characters. The proved family averages over **fundamental** negative discriminants in long ranges.

The frozen t86 discriminants are instead

```text
-4*d^2,
```

which are nonfundamental and carry the square conductor `d^2`. Ditchen explicitly notes that square factors in nonfundamental discriminants introduce substantial additional difficulties. The t86 quantifier order also fixes `U` and then one divisor conductor `d`; it does not supply the discriminant average used by that theorem.

A generic class-character orthogonality expansion is formally available, but using it without a matching nonfundamental-conductor large sieve would pay the class-family dimension just identified above.

```text
RING_CLASS_CHARACTER_ORTHOGONALITY_FORMALLY_VALID=true
DItCHEN_FUNDAMENTAL_DISCRIMINANT_AVERAGE_MATCHES_T86=false
RING_CLASS_LARGE_SIEVE_APPLICABLE=false
```

No located off-the-shelf theorem gives the required fixed-power cancellation for the complete t86 nonfundamental ring-class family with the physical `(delta0,rho)` range retained.

---

## 8. Chebotarev and Gaussian-prime distribution do not remove the same obstruction

Effective Chebotarev theorems and their Brun--Titchmarsh variants give prime-ideal bounds for a **fixed** conjugacy / ideal class in suitable size ranges. Thorner--Zaman also obtain uniform applications to prime values of binary quadratic forms. These are relevant ambient tools, but they do not prove that the moving t86 physical form labels occupy a power-small set of ring classes.

Likewise, Gaussian-prime Bombieri--Vinogradov results in short intervals / sectors work in a fixed number field and average arithmetic progression moduli. The t86 factorization

```text
T+iD=gamma*a*pi',
N(gamma)=delta0,
N(a)=k0,
N(pi')=ell
```

still imposes simultaneously

```text
d | Im(gamma*a*pi'),
N(gamma)=delta0,
physical delta0 hyperbolas,
canonical direction,
reconstructed balanced-cover masks.
```

Treating `pi'` as a free Gaussian prime in residue classes while summing an unrestricted `gamma` family simply re-expresses the same ring-class family; it does not certify a fixed-power saving.

```text
CHEBOTAREV_SINGLE_CLASS_TECHNOLOGY_RELEVANT=true
CHEBOTAREV_FULL_T86_ADAPTER=false
GAUSSIAN_BV_BDH_APPLICABLE=false
GAUSSIAN_SHORT_COFACTOR_PRIME_BILINEAR_APPLICABLE=false
```

---

## 9. Primitivity / congruence sieve technology does not supply the missing power

Modern extensions of Iwaniec's binary quadratic form sieve can retain primitivity and congruence conditions. This confirms that those two masks are not intrinsically incompatible with prime-value sieve arguments.

They do not, however, provide a uniform fixed `B`-power upper saving for a polynomial family of nonfundamental ring classes with the Stage14 conductor and reconstructed-cover masks. Their prime-density effects are logarithmic unless additional class-family or bilinear cancellation is proved.

```text
PRIMITIVITY_CONGRUENCE_SIEVE_TECHNOLOGY_RELEVANT=true
PRIMITIVITY_CONGRUENCE_SIEVE_FIXED_POWER_ADAPTER=false
```

---

## 10. Required physical range ledger

The frozen adapter must simultaneously account for

```text
d:
  fixed after the B^o(1) fixed-U selector-divisor choice,
  odd squarefree,
  ring-order conductor;

conductor discriminant:
  -4*d^2;

delta0:
  odd, gcd(delta0,d*k0)=1,
  constrained by d*delta0 << sqrt(B),
  d*delta0^2 << Y_U,
  ell*delta0 << Y_U;

rho:
  rho^2=-1 mod delta0,
  multiplicity 2^omega(delta0)=B^o(1);

form coefficients:
  a=delta0,
  b=2*rho*d,
  c=((rho^2+1)/delta0)*d^2;

proper class family:
  ambient size h(-4*d^2)=d*B^o(1),
  physical power-sparse subfamily not proved;

(s,j):
  gcd(s,d*j)=1,
  D=d*j,
  0<d*|j|<=sqrt(2B/h),
  quarter-scale min(d,|j|) switch;

prime:
  F(s,j)=k0*ell,
  ell prime,
  ell>2*k0*delta0,
  ell*eta*delta0<=Y_U;

fixed k0:
  class-level ideal composition costs B^o(1),
  does not shrink the class family;

exceptional characters:
  no uniform physical Siegel-zero elimination supplied;

coefficient L2:
  t78/tH23 four-cell bookkeeping remains B^o(1);

physical masks:
  canonical Gaussian direction,
  reconstructed primitive balanced cover,
  small angular-g four-cell weights,
  short ellipse,
  sharp ell*odd(h)*odd(r)*odd(t) hyperbola,
  beta-tag and reciprocal/inversion orientation;

quantifier order:
  fixed U and packet data
  -> B^o(1) selector d
  -> moving (delta0,rho) form class
  -> primitive form point (s,j)
  -> intrinsic prime ell.
```

No audited theorem supplies a fixed-power estimate uniformly across this ledger.

```text
FULL_PHYSICAL_MASKS_RETAINED=true
```

---

## 11. Fixed-power verdict

The useful positive result is the exact diagnosis:

1. t86 really has fixed discriminant and fixed value cofactor;
2. `k0` can be peeled at `B^o(1)` class-composition cost;
3. the remaining `(delta0,rho)` parameter is a ring-class label;
4. the ambient ring class group has `d*B^o(1)` classes;
5. the t86 form shape is not intrinsically confined to one class or one small genus-sized family;
6. the physical `delta0` inequalities have not yet been shown to force a power-small subset of those classes.

Therefore no off-the-shelf prime theorem or class-group large sieve can currently be converted into a uniform fixed packet saving.

```text
OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

The whole-family theorem remains

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2.
```

---

## 12. Minimal remaining obstruction and next H decision

The exact internal obstruction is now

```text
MINIMAL_REMAINING_OBSTRUCTION=FixedUPhysicalDeltaRootRingClassFamilyCompressionWithReconstructedCoverMasks
```

The preferred receiver is

```text
PREFERRED_RECEIVER=SharedUFixedSelectorRingClassCompressedFixedCofactorPrimeValuePhysicalEnergy
```

A useful next t-route step should attack the class family **before** asking for another general prime theorem. In particular it should determine whether the physical inequalities and reconstruction force repeated class labels, a short arc/coset, a divisor-switch compression, or a power-small subset of `Cl(-4d^2)`.

No new H request is minimal at this snapshot:

```text
NEXT_H_NEEDED=false
```

If a later t87+ stage proves a genuinely smaller ring-class subfamily and that new receiver still needs external analytic input, H-PROTOCOL assigns it a new H number.

---

## Locked boundary

```text
STAGE14_TH25=COMPLETE_T86_SNAPSHOT_FIXED_DISCRIMINANT_RING_CLASS_PRIME_VALUE_APPLICABILITY_AUDIT
AUDITED_THROUGH=Stage14-t86
SOURCE_SNAPSHOT_SHA=798191aa5071a344cf642a1be265f1ad8e373fd5
TARGET_FROZEN=true
T86_FIXED_DISCRIMINANT_RETAINED=true
T86_FORM_DISCRIMINANT=-4*d^2
T86_FIXED_VALUE_COFACTOR_RETAINED=true
T86_MOVING_DELTA_VALUE_SIDE_ELIMINATED=true
T86_FORM_CLASS_FAMILY_RETAINED=true
T86_GAUSSIAN_IDEAL_FACTORIZATION_RETAINED=true
T86_FIXED_K_PEEL_RETAINED=true
BILINEAR_PI_V_MULTIPLICITY_REOPENED=false
T86_FORM_CLASS_IDENTIFIED_WITH_RING_CLASS=true
RING_CLASS_NUMBER_SCALE=d*Bo1
UNRESTRICTED_T86_FORM_SHAPE_SPANS_FULL_RING_CLASS_GROUP=true
PHYSICAL_FORM_CLASS_SUBFAMILY_BO1_PROVED=false
PHYSICAL_FORM_CLASS_POWER_SPARSE_PROVED=false
FULL_PHYSICAL_MASKS_RETAINED=true
RING_CLASS_PRIME_THEOREM_APPLICABLE=false
GROWING_DISCRIMINANT_FORM_PRIME_THEOREM_APPLICABLE=false
RING_CLASS_LARGE_SIEVE_APPLICABLE=false
GAUSSIAN_SHORT_COFACTOR_PRIME_BILINEAR_APPLICABLE=false
FIXED_K_IDEAL_COMPOSITION_ADAPTER_PROVED=true
FORM_CLASS_FAMILY_POWER_COST_CONTROLLED=false
OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MINIMAL_REMAINING_OBSTRUCTION=FixedUPhysicalDeltaRootRingClassFamilyCompressionWithReconstructedCoverMasks
PREFERRED_RECEIVER=SharedUFixedSelectorRingClassCompressedFixedCofactorPrimeValuePhysicalEnergy
NEXT_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
```
