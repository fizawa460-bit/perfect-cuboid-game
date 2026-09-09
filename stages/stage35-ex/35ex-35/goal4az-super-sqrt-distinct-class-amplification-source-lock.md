# Stage35-EX Goal4AZ source lock — super-sqrt distinct-class amplification boundary

Scope: execute the Goal4AS candidate `SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION_OR_STRONGER_COUNTING` against the exact Stage35-EX source stack. Audited authority remains V74 / Goal4AK. Goal4AZ is provisional and grants no E1, Stage35, endpoint, or Perfect Cuboid credit.

## Parent and counting theorem

Goal4M gives, for the number `T(B)` of primitive canonical positive perfect-cuboid classes whose primitive integer space diagonal is at most `B`,

```text
T(B) << B^(1/2+o(1)).
```

Equivalently, for every `epsilon>0` there are constants `C_epsilon,B_epsilon` such that

```text
T(B) <= C_epsilon * B^(1/2+epsilon)
```

for `B>=B_epsilon`.

Goal4N already isolated the only way an amplification argument can contradict this upper bound: from one hypothetical endpoint, construct quantitatively many **distinct primitive canonical endpoint classes** below a controlled height. Positive scaling, edge permutation, and source-pair swap do not count as new classes.

Goal4AY is the exact-green parent candidate for nonlinear self-maps. Its strongest classical operator is the primitive derived-cuboid involution.

## Exact exponent gate

Fix one hypothetical primitive canonical endpoint `P`. A polynomial amplifier would have to provide, for arbitrarily large integers `N`, a set `Amp_P(N)` of primitive canonical endpoint classes with constants `c_P,C_P>0` and exponents `rho,kappa>0` such that

```text
#Amp_P(N) >= c_P*N^rho,                         (AZ-1)
H(Q) <= C_P*N^kappa for every Q in Amp_P(N),   (AZ-2)
```

where `H` is the same primitive integer space-diagonal height used by Goal4M, and all classes in `Amp_P(N)` are pairwise distinct after primitive canonicalization.

Then with `B=C_P*N^kappa`,

```text
T(B) >= c_P*N^rho.
```

Goal4M gives for every `epsilon>0`

```text
T(B) <= C_epsilon*C_P^(1/2+epsilon)
        * N^(kappa*(1/2+epsilon)).               (AZ-3)
```

Hence an asymptotic contradiction follows whenever

```text
rho/kappa > 1/2.                                 (AZ-4)
```

Indeed choose `epsilon>0` with

```text
rho > kappa*(1/2+epsilon).
```

The equality case `rho/kappa=1/2` does **not** contradict the retained `B^(1/2+o(1))` upper bound. Therefore a merely square-root-scale orbit is insufficient; the exponent must be strictly super-square-root after translating to the Goal4M endpoint height.

For a linear-size orbit (`rho=1`) this requires a polynomial height exponent

```text
kappa < 2.                                       (AZ-5)
```

This gate is exact and independent of any particular proposed amplifier.

## Available mechanism audit

### 1. Scaling and finite source symmetries

Positive rational scaling is killed by primitive canonicalization. Edge permutations are also killed by the canonical class convention. The retained source-pair swap is an equivalence in the audited E1 endpoint relation.

Thus these operations contribute at most one primitive canonical class:

```text
rho=0.
```

They are not amplifiers.

### 2. Goal4AY derived-cuboid operator

In raw variables the classical derived operator is

```text
D_raw(A,B,C)=(AB,AC,BC).
```

Applying it twice gives

```text
D_raw^2(A,B,C)
  =(A^2*B*C, A*B^2*C, A*B*C^2)
  =A*B*C*(A,B,C).                                (AZ-6)
```

After quotienting by positive scaling this is exactly an involution. Goal4AY sharpened this in the primitive six-variable dictionary to

```text
D:(x,y,z ; a,b,c) -> (a,b,c ; x,y,z),
D^2=id.
```

Moreover Goal4AY does not prove that `D` preserves the fourth-square equation at all.

Consequently, even under the stronger hypothetical assumption that `D` were total on full endpoints, every primitive canonical orbit has size at most two:

```text
#Orbit_D(P) <= 2.                                (AZ-7)
```

Thus the strongest currently source-locked nonlinear operator gives `rho=0` and cannot amplify against Goal4M.

### 3. AU/AV marked Kummer package

Goal4AU gives three marked residual Kummer classes with

```text
d_A*d_B*d_C=1,
```

and Goal4AV packages them into a biquadratic coefficient extension of degree at most four. This is a finite coefficient package, not a map producing new endpoint classes. Its finite degree cannot produce polynomially growing distinct endpoint classes as `N` grows.

No exponent pair `(rho,kappa)` for endpoint amplification is supplied.

### 4. Goal4AX six-norm torus chart

Goal4AX puts the three face norms and three space couplings into a simultaneous Gaussian/Hilbert–90 chart. The chart has an explicit rational section supplied by the endpoint itself, and its four cross-coordinate compatibility relations reconstruct the endpoint ratios.

Therefore moving inside the chart without an additional arithmetic constraint is a reparameterization of the same endpoint receiver, not a certified map

```text
endpoint -> many distinct primitive endpoint classes.
```

No distinct-class amplifier is obtained.

### 5. Elliptic multiplication on Goal4L receiver

Goal4L maps every physical endpoint to a non-torsion rational point on

```text
E_q: Y^2=X*(X-1)*(X+q^2).
```

Hence the elliptic group law produces infinitely many rational receiver points `[n]P` on the same specialized elliptic curve.

This is **not** presently an endpoint amplifier. Goal4L's exact credit boundary states

```text
Goal4K_receiver_endpoint_equivalence_claimed=false.
```

The birational inverse returns rational points of the Goal4K quartic receiver, but the source stack does not prove that an arbitrary `[n]P` reconstructs all three rational face diagonals plus the rational space diagonal of a new physical endpoint.

There is also no source-locked polynomial transfer

```text
H_endpoint([n]P) <= C*n^kappa
```

for the Goal4M primitive space-diagonal height. Therefore neither endpoint distinctness nor the height exponent `kappa` required by `(AZ-4)` is available.

The exact canonical-height identity `hhat([n]P)=n^2*hhat(P)` by itself would only concern receiver canonical height and does not supply the missing endpoint-height adapter. It must not be substituted for `(AZ-2)`.

### 6. Euler-brick quadratic jumps / rational-box transformations

A scoped literature check found the MathOverflow thread *Boxing the rational box* (H. Reddmann, 2011), which constructs rational transformations on an Euler-box surface. The post explicitly says the **space diagonal does not have to be rational**. Therefore those transformations act on the three-face Euler-brick population and cannot be imported as perfect-cuboid endpoint amplification without a separate fourth-square preservation theorem.

Source:

```text
https://mathoverflow.net/questions/67128/boxing-the-rational-box
```

No full-endpoint amplifier is imported from that discussion.

### 7. Cuboid-factor elliptic families

A scoped literature check also found Sharipov, *A note on rational and elliptic curves associated with the cuboid factor equations* (arXiv:1209.5706). It expresses parametric cuboid-factor solutions through rational and elliptic curves arranged in families. The located source does not state that one hypothetical perfect-cuboid endpoint generates a polynomially large family of distinct perfect-cuboid endpoint classes with controlled primitive space-diagonal height.

Source:

```text
https://arxiv.org/abs/1209.5706
```

Thus no amplification theorem is imported from this source.

## Exact current verdict

The current source stack provides no mechanism satisfying the exact amplifier gate `(AZ-1)`--`(AZ-4)`.

What is proved:

```text
SUPER_SQRT_EXPONENT_GATE_DERIVED=true;
DERIVED_OPERATOR_PRIMITIVE_ORBIT_AT_MOST_TWO=true;
FINITE_KUMMER_PACKAGE_NOT_AMPLIFIER=true;
AX_TORUS_CHART_NOT_DISTINCT_ENDPOINT_AMPLIFIER=true;
ELLIPTIC_MULTIPLICATION_ENDPOINT_RECONSTRUCTION=false;
ELLIPTIC_MULTIPLICATION_ENDPOINT_HEIGHT_TRANSFER=false.
```

What is not proved:

```text
ALL_POSSIBLE_AMPLIFIERS_IMPOSSIBLE=false;
STRICT_SUBSQRT_UPPER_BOUND=false;
SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION=false;
EVENTUAL_ZERO=false;
E1=false.
```

Route classification:

```text
SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION_OR_STRONGER_COUNTING
  -> FAIL_CLOSE_CURRENT_SOURCE_LOCKED_AMPLIFICATION_MECHANISMS
  -> exact threshold: rho/kappa > 1/2
  -> strongest current full-source orbit: O(1).
```

This is a fail-close of the **current source-locked mechanisms**, not a theorem that no future amplifier can exist.

## Next exact leaf

After Goal4AZ, the fresh Goal4AS ledger still contains a finite additional Brauer shortcut as an untested distinct lens. The next unit is

```text
35EX-35_GOAL4BA_FINITE_ADDITIONAL_BRAUER_SHORTCUT_EXHAUSTION_PREFLIGHT
```

Question: using the now explicit algebraic Brauer/unit-character layer and the source-marked local population, can a single new finite Brauer class or finite explicitly generated subgroup force an empty source-admissible adelic set without requiring full endpoint-equivalent Brauer completeness?

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
