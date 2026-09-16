# Stage32 MB104 — `000707000f0f` e=2 special-grid tangency evaluator

Status: **RETAINED EXACT TANGENCY REDUCTION / SUPPORTED BRANCHES SMOOTH / INTRINSIC BRANCH DELTA ZERO / TANGENCY BECOMES A KUMMER-RATIO COLLISION / e=2 OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The preceding special-grid delta-capacity wall showed that branch count alone leaves at least `48 l^2` of delta headroom for the birational image

```text
Psi=(psi_z,psi_w): E -> C subset R x R=P1 x P1,
[C]=(28l,28l),
g(E)=1.
```

That wall left three possible ways to strengthen the local special-point delta: intrinsic delta of individual branches, pairwise tangency/higher intersection, or extra singularities away from the special grid.  This note removes the first option and gives an exact evaluator for the second.

## Source-locked inputs

Use only the retained exact/candidate boundaries already present on this leaf:

- `GENUS1-SPAN5-BALANCED16-000707-E2-ETALE-BASECHANGE-DETERMINANT-PASSPORT.md`:
  every supported normalization branch is unramified for both degree-`n=28l` maps `psi_z,psi_w:E->R`; the only branch values of `C8->R` are
  ```text
  r^4=4    (T'-type),
  r^4=-4   (TT'R-type).
  ```
- `GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL.md`:
  ```text
  V^2=((r_z^4-4)(r_w^4-4))/16,
  U^2=((r_z^4+4)(r_w^4+4))/16.
  ```
- `GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE.md`:
  all fourteen supported nodes map to exact simultaneous-sign special points in `R x R`.
- `BTVA-13FORM-PRINCIPAL-PART.md`:
  order-two principal parts have rank three at every A1 node, but this saturates after three **distinct** landing directions and does not bound the number of possible landing directions.

## 1. Every supported branch of `C` is smooth

Let `x in E` be one of the supported normalization points.  By the retained etale-basechange passport,

```text
d psi_z(x) != 0,
d psi_w(x) != 0.
```

Hence the differential of the joint map

```text
d Psi_x=(d psi_z(x),d psi_w(x))
```

is nonzero.  Therefore `Psi` is an immersion on that branch and its image branch in the smooth surface `R x R` is smooth.

Consequently every supported individual branch has

```text
intrinsic delta(branch)=0.                     (SMOOTH)
```

Thus the `intrinsic branch delta` option left open by the preceding delta-capacity wall is unavailable on the supported packet.  Any improvement over the ordinary branch-count contribution must come from pairwise intersection multiplicities `I_ij>1` or from singularities away from these sixteen special points.

## 2. Exact Kummer-ratio functions

For the `T'` branch values `r^4=4`, define on the normalization wherever written and then by rational continuation

```text
A_T' := v_z/v_w
      = 4 V/(r_w^4-4).
```

The intermediate-quotient equation gives

```text
(A_T')^2=(r_z^4-4)/(r_w^4-4).                  (AT)
```

For the `TT'R` branch values `r^4=-4`, define

```text
A_TT'R := u_z/u_w
        = 4 U/(r_w^4+4),
```

so

```text
(A_TT'R)^2=(r_z^4+4)/(r_w^4+4).                (AU)
```

These ratios are invariant under diagonal `H`: for `T'`, both `v_z,v_w` change sign; for `TT'R`, both `u_z,u_w` change sign.  Thus they are legitimate rational functions on the corresponding intermediate-quotient curve, not choices of an individual product lift.

At a supported branch both numerator and denominator in `(AT)` or `(AU)` vanish simply, because `psi_z` and `psi_w` are unramified and every root of `r^4=+/-4` is simple.  Therefore the square ratio has valuation zero.  Since `E` is smooth, `A_T'` or `A_TT'R` extends at that normalization point to one finite nonzero value.

## 3. The ratio is exactly the tangent-slope evaluator

Let a supported branch map to the special point

```text
(q_z,q_w) in R x R,
q_z^4=q_w^4=c,
c in {4,-4}.
```

Choose a normalization parameter `s` at `x` and write

```text
r_z=q_z+a_z s+O(s^2),
r_w=q_w+a_w s+O(s^2),
a_z a_w != 0.
```

For

```text
F_c(r)=r^4-c,
```

the first-order quotient is

```text
F_c(r_z)/F_c(r_w)
 -> (q_z^3 a_z)/(q_w^3 a_w).
```

Combining with `(AT)/(AU)` gives

```text
A(x)^2=(q_z^3 a_z)/(q_w^3 a_w),
```

hence the tangent slope of the image branch is exactly

```text
dr_w/dr_z at x
 = a_w/a_z
 = q_z^3/(q_w^3 A(x)^2).                       (SLOPE)
```

The same formula applies to both inertia types; only the definition of `A` changes.

Wolfram exact symbolic replay gives

```text
coefficient_s[(q+a s)^4-q^4] = 4 a q^3,
A^2 = (a_z q_z^3)/(a_w q_w^3)
 => a_w/a_z = q_z^3/(q_w^3 A^2).
```

## 4. Tangency is exactly collision of the `A^2` values

Take two distinct smooth normalization branches `x,x'` mapping to the **same** residual special point `(q_z,q_w)` in `R x R`.  Since the ambient surface is smooth, their local intersection multiplicity satisfies

```text
I_x,x' = 1
```

iff their tangent lines are distinct, and

```text
I_x,x' >= 2
```

iff their tangent lines agree.

The constants `q_z,q_w` are common to the two branches.  By `(SLOPE)`, therefore,

```text
I_x,x' >= 2
iff
A(x)^2=A(x')^2.                                (TANGENCY-TEST)
```

So the missing extra special-grid delta has a concrete exact target: prove collisions among the branchwise values of `A_T'^2` or `A_TT'R^2` at one of the sixteen residual special points.  Merely knowing the branch masses does not supply such collisions.

## 5. Divisor size does not force a collision

Fix one inertia type and write `F(r)=r^4-4` or `r^4+4`.  There are seven supported box nodes of that type, with `8l` normalization branches each.  Thus the common supported divisor on `E` has degree

```text
7*(8l)=56l=2n,
n=28l.
```

For either projection, `F o psi_i` has zero divisor of total degree `4n`.  After the `2n` common supported simple zeros are removed, the retained simple-ramification passport leaves double zeros at a ramification divisor `R_i` of degree `n`.  If `P_i=psi_i^*(infinity)` has degree `n`, then

```text
div(F o psi_i)=S_type+2R_i-4P_i.
```

Taking the quotient and using `A^2=(F o psi_z)/(F o psi_w)` gives

```text
div(A)=R_z-R_w-2P_z+2P_w.                     (DIV-A)
```

In particular

```text
deg(A:E->P1) <= n+2n=3n=84l.                  (A-DEG)
```

The supported divisor of one type has only `2n=56l` points counted with branch multiplicity.  Therefore this coarse degree count cannot force two supported points to have the same `A` or `A^2` value.  It is an evaluator, not yet a pigeonhole obstruction.

## 6. Why the old BTVA rank-three fact does not force tangency

The retained BTVA principal-part leaf says that at an A1 node the order-two pole polynomial is an arbitrary binary quadratic and that three distinct landing directions already force the whole principal part to vanish.  Additional directions then impose no further order-two conditions.

This is a **saturation of the differential constraints**, not a theorem that only three landing directions are geometrically possible.  Hence it cannot be combined with `(TANGENCY-TEST)` to claim that many branches must share one `A^2` value.  Such a claim would require a new global jet/landing theorem.

## Routing consequence

The special-grid singularity route is now narrowed to

```text
branch count alone                         EXHAUSTED,
intrinsic delta of supported branches      ZERO,
forced tangency/higher contact             LIVE, with exact A^2 evaluator,
forced non-special singularities           LIVE.
```

A useful continuation must therefore do at least one of:

1. constrain the branchwise values of `A_T'^2` or `A_TT'R^2` strongly enough to force collisions;
2. compute higher jets after an `A^2` collision to quantify `I_ij` beyond two;
3. obtain a Nielsen/monodromy relation coupling these slope values globally;
4. return to the actual conductor-loop comparison with `0` versus `gamma_Q`.

The active leaf and its conductor-loop obligation remain unchanged.

## Firewalls

- `A` is a tangent/exceptional-direction evaluator; it is **not** the residual `G/H` sheet character.
- Equality of `A^2` is asserted to detect tangent coincidence only for two smooth branches through the same residual point.
- No collision of `A^2` values is proved.
- No additional delta beyond branch count is claimed.
- No conductor loop is evaluated and no branch is assigned `0` or `gamma_Q`.
- No branch allocation is claimed geometrically realizable.
- No weighted-cut upper bound or `e=2` closure is claimed.
- `e=4`, `000707000f0f`, MB104, span5, finite-window, receiver, effectivity, theorem, endpoint and Perfect-Cuboid credit remain open/zero.
- No heavy compute is armed.
- No merge or rebase authorization.
