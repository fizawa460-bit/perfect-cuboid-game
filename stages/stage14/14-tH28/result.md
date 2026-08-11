# Stage14-tH28 — independent audit of canonical-LPF primitive norm-form projected support

## Frozen audit contract

```text
H_STAGE=Stage14-tH28
AUDITED_THROUGH=Stage14-t108
TARGET_FILE=stages/stage14/14-t108/th28-target.md
REQUESTED_OBJECT=CanonicalLPFPrimitiveSumOfTwoSquaresProjectedPhysicalSupportSieveOrDispersion
TARGET_FROZEN=true
WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false
```

The target was re-read from current `main`. Operational note: the chat handoff described PR #703 as unmerged advisory material, but by dispatch time GitHub records PR #703 as merged. This audit nevertheless treats `th28-target.md` as the immutable mathematical receiver and does not chase later t-route refinements.

## 1. Independent reduction check

Write

```text
n=u^2+v^2,
Q=ell*n,
gcd(u,v)=1.
```

The frozen strong gap gives

```text
ell^2 > 2*h*k0*Q = 2*h*k0*ell*n,
```

hence

```text
ell > 2*h*k0*n >= 2n
```

on every positive integral live packet. Therefore every prime divisor of `n` is strictly smaller than `ell`, and `ell` cannot divide `n`. Consequently

```text
ell=LPF(Q),
v_ell(Q)=1
```

are automatic once `ell` is prime and the strong gap is retained.

Likewise, for a primitive representation `n=u^2+v^2`, an odd prime `p==3 mod 4` dividing `n` would divide both `u` and `v`; thus no such prime occurs. Hence the odd split-prime support of `n` is automatic from primitivity. The nonredundant outer arithmetic kernel can therefore be written

```text
ell prime, ell==1 mod 4,
gcd(u,v)=1,
n=u^2+v^2,
ell > 2*h*k0*n,
ell > 2*sqrt(B),
h*k0*ell*n <= 2B,
P_lambda(u,v;ell,ell*n)=1,
```

up to the frozen two-primary/unit conventions and `B^o(1)` packet labels. The t91 primitive Gaussian orientation-cube description is consistent with this primitive norm-form parameterization; the t89 short-cover archimedean inequalities are consequences of the strong gap and must not be charged again.

Thus the t108 receiver is mathematically coherent, but the canonical-LPF label is not the source of extra thinness after the strong gap: it is a derived property.

## 2. Off-the-shelf theorem audit

### Baier--Bansal, Gaussian sparse-modulus large sieve

Baier--Bansal, *Large sieve with sparse sets of moduli for Z[i]*, arXiv:1811.07300, Theorems 2 and 4, bounds additive-character second moments over prescribed Gaussian moduli; Theorem 4 takes the full family of Gaussian prime moduli in a polynomial norm range. The Stage14 target is instead a positive support projection in `(ell,u,v)` with one rational prime `ell`, a primitive norm value `u^2+v^2`, a strong multiplicative gap, and packet-dependent physical acceptance masks. No identity converts the support cardinality to the required large-sieve second moment with a fixed-power gain. Moreover the live prime/action support exposed by the t-route can be only `B^o(1)`, outside the polynomial-family mechanism needed for a fixed `B^-delta` gain.

Verdict: `NEAR`, not directly applicable.

### Fouvry--Iwaniec / Lam--Schindler--Xiao asymptotic-sieve family

The Fouvry--Iwaniec Gaussian/asymptotic-sieve technology and Lam--Schindler--Xiao, *On prime values of binary quadratic forms with a thin variable*, arXiv:1809.10755, concern prime values of a fixed primitive positive-definite quadratic form with an admissible thin-variable sequence satisfying explicit distribution/bilinear hypotheses. Stage14 does not ask that `u^2+v^2` be prime; it asks that the separate factor `ell` be the dominant prime while `u^2+v^2` is a primitive split-supported cofactor, and retains an existential physical mask depending on the fixed-U packet. No verified Type-I/Type-II or level-of-distribution contract for that masked projected sequence is available.

Verdict: `NEAR`, missing a new distribution adapter.

### Largest-prime-factor results for quadratic polynomials

Grimmelt--Merikoski, *On the greatest prime factor and uniform equidistribution of quadratic polynomials*, arXiv:2505.00493, proves large prime factors and root equidistribution for the one-variable family `n^2+h`, with specific uniformity in `h`. The Stage14 variable is the two-variable primitive norm `u^2+v^2`, multiplied by a separate prime and then projected through packet-dependent physical masks. The theorem's polynomial family, root-mod-prime setup, and uniformity parameter do not match.

Verdict: `BACKGROUND`, not applicable.

## 3. Why the bare sieve kernel cannot itself give a fixed power

After the strong-gap simplification, the arithmetic conditions `primitive sum of two squares + one dominant split prime` are not power-thin by themselves. If one freezes any primitive norm value `n0=u0^2+v0^2` that survives a physical cell, the remaining admissible `ell` lie in a prime interval subject only to

```text
ell==1 mod 4,
ell > max(2*sqrt(B), 2*h*k0*n0),
ell <= 2B/(h*k0*n0).
```

Whenever this interval has polynomial length, the prime number theorem in progressions gives only logarithmic loss, not `B^-delta`. Thus a fixed-power support deficit cannot follow from the displayed LPF/norm/gap architecture alone. It must come from a genuinely thin consequence of the **specific physical mask** or from a new theorem proving a uniform dispersion/density deficit for those masks.

This is the decisive no-go point: all currently identified off-the-shelf sieve families can tolerate or analyze some local/congruence/sector restrictions, but none supplies the missing theorem that the full Stage14 projected physical acceptance is power-sparse uniformly in the moving fixed-U packet.

## 4. Mask preservation audit

The frozen receiver requires simultaneous retention of

```text
primitive/gcd,
fixed denominator-tag data,
reciprocal/inversion orientation,
endpoint/four-cell local conditions,
positivity/canonical-unit conventions,
strong gap and budget,
charged-once projection.
```

Finite unit/orientation choices and fixed-modulus congruence cells can individually be expanded at `B^o(1)` cost when their packet moduli stay subpolynomial. Sector/sign windows can also be partitioned without creating a new polynomial variable. But there is no merged theorem proving that the **joint existential projection** of all these masks satisfies the distribution hypotheses of any cited sieve/dispersion theorem uniformly in the fixed-U packet. Replacing the joint predicate by an unmasked sum-of-two-squares or Gaussian-prime sequence therefore loses a required physical condition and is not a legal applicability proof.

For the candidate theorems checked here:

```text
ALL_PHYSICAL_MASKS_PRESERVED=false
```

This means the target masks remain mandatory; it does not authorize deleting them.

## 5. Minimal theorem-ready obstruction

The missing input can be stated as follows.

### Primitive Physical Projected-Norm Dispersion Lemma

There exist absolute `delta>0` and a uniform subpolynomial loss `B^o(1)` such that for every live fixed-U packet, every frozen `B^o(1)` exceptional label `lambda`, and every dyadic block compatible with

```text
ell > 2*h*k0*(u^2+v^2),
ell > 2*sqrt(B),
h*k0*ell*(u^2+v^2)<=2B,
```

the charged-once projection

```text
S_{U,lambda}(B)
 = {Q=ell*(u^2+v^2):
      ell prime, ell==1 mod 4,
      gcd(u,v)=1,
      P_lambda(u,v;ell,Q)=1}
```

obeys a fixed-power deficit relative to its ambient outer-Q length, uniformly in all packet coefficients/moduli allowed by Stage14. Equivalently, one may replace the support statement by Type-I/Type-II (or dispersion) estimates strong enough to imply the same support deficit **with the full `P_lambda` retained**.

The required uniformity must include the fixed-U coefficient matrix of determinant `2*k0`, all endpoint/four-cell moduli and tags, the reciprocal/inversion orientation, sign/positivity windows, and the strong-gap dyadic aspect ratio. A theorem with constants depending polynomially on those packet parameters is insufficient unless that dependence is proved to be `B^o(1)`.

No theorem located in the audited families supplies this lemma.

A sharper internal alternative is to prove a `NoPersistentPrimitiveRayLemma`: every physical cell must forbid a polynomial-length family obtained by fixing one primitive direction/norm and varying the dominant prime, or else no uniform support power saving is possible. Establishing this ray obstruction is logically prior to applying a generic sieve.

## 6. Final verdict

```text
DIRECT_THEOREM_APPLICABLE=false
APPLICABLE_THEOREM=NONE
REQUIRED_REFORMULATION=PrimitivePhysicalProjectedNormDispersionLemma_or_NoPersistentPrimitiveRayLemma
ALL_PHYSICAL_MASKS_PRESERVED=false
UNIFORM_IN_FIXED_U_PACKET=false
UNIFORM_FIXED_POWER_SAVING_PROVED=false
BEST_CERTIFIED_FIXED_U_EXPONENT=NONE
CERTIFIED_B_POWER_SAVING_EXPONENT=0
OBSTRUCTION=no_existing_theorem_controls_the_joint_positive_projected_physical_mask_support_uniformly_in_the_moving_fixed_U_packet;_bare_LPF_primitive_norm_gap_kernel_is_only_logarithmically_thin_and_LPF_is_automatic_under_the_strong_gap
FULL_REQUIRED_MASKS_RETAINED=true
OFF_THE_SHELF_THEOREM_APPLICABLE=false
MINIMAL_REMAINING_OBSTRUCTION=PrimitivePhysicalProjectedNormDispersionOrPersistentRayObstruction
PREFERRED_RECEIVER=SharedUPrimitivePhysicalProjectedNormSupportDispersionOrNoPersistentRay
NEXT_H_NEEDED=false
WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false
```

## 7. Parent-route decision

`tH28` is a completed negative applicability certificate. It does **not** authorize Stage14-t109 to insert a sieve/dispersion saving. The t-route may proceed to `Stage14-t109` only as an **internal reduction stage** whose first task is to decide the persistent-ray question / expose an explicit thin mask or prove the distribution adapter above. If `t109` was intended to consume a positive fixed-U power saving from tH28, it is blocked and must be redefined.

```text
T_ROUTE_MAY_ADVANCE_TO_T109_INTERNAL_REDUCTION=true
T109_MAY_CONSUME_TH28_FIXED_POWER_SAVING=false
T_ROUTE_EXTERNAL_THEOREM_GAP_CLOSED=false
T_ROUTE_H_BLOCKING_RESOLVED_BY_NEGATIVE_VERDICT=true
```
