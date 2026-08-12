# Stage15-6at — low-core branch-memory accounting audit

Base: Stage15-6as in the current cycle. The direct explicit twist-height theorem was blocked, so 6at returns to an internal source of information that must not be forgotten: the original Stage15-6ac low-norm-core branch condition.

This is an **accounting audit**. It asks whether retaining that condition, without recharging it as a second spacing saving, already makes the remaining sum over `k` summable.

## 1. Original branch condition

Stage15-6ac fixed a dyadic inner toric box

\[
r\asymp R_0,\qquad s\asymp S_0,
\qquad V=R_0S_0,
\]

and split by the odd norm core

\[
q=k/2^\eta,\qquad \eta\in\{0,1\}.
\]

The low-core descendant that eventually produced the Gaussian-square/quartic route satisfies

\[
\boxed{q^2<V.}
\]

Since `k` is either `q` or `2q`, every descendant still satisfies the legal remembered size condition

\[
\boxed{k^2<4V.}
\]

This condition is metadata of the branch. Retaining it is not an AR-028 recharge; applying the old root-line saving a second time would be.

```text
LOW_CORE_BRANCH_MEMORY_RETAINED=true
LOW_CORE_BRANCH_MEMORY_USED_AS_SECOND_SPACING_SAVING=false
```

## 2. Combine with the later exact global heights

Stage15-6aj and 6am give, on the small-coordinate-core branch,

\[
\boxed{kZW\le2B,}
\]

and

\[
\boxed{\kappa^2<ZW.}
\]

Stage15-6ar further packages

\[
d=sf(2k\kappa),
\]

with `d` determining `k*kappa` up to the exact 2-primary rule.

The available pure size system is therefore

```text
k^2 < 4 V
k Z W <= 2 B
kappa^2 < Z W
k,kappa squarefree and coprime
```

plus the physical polynomial parameter bounds on the original toric box.

## 3. Size-only constraints do not make k subpolynomial

The system above permits polynomially many numerical core scales. This is a **logical sufficiency audit**, not a construction of physical survivors.

For example, take the coordinate-core scale `kappa=1` and fixed dyadic Gaussian scales `Z=W=2`. Then

\[
\kappa^2=1<ZW=4,
\]

and product height only requires

\[
4k\le2B,
\qquad k\le B/2.
\]

For any such numerical `k`, the remembered low-core inequality can be made compatible at the scale level by choosing an inner box with `V>k^2` while `R_0,S_0` remain polynomially bounded whenever `k` is a fixed-power subrange of `B`.

Therefore the inequalities **alone** do not imply

```text
# possible k = B^o(1)
```

or any summable weight stronger than what 6ap already obtained.

This does not assert that every numerical scale is arithmetically populated. It proves the narrower point needed for proof accounting: a global saving cannot be deduced from the currently recorded size inequalities without using an additional arithmetic correlation.

## 4. No legal hybrid reuse of the old modulus

One tempting move would be

```text
remember q^2<V
+ use q again as a root-line modulus
+ combine with 6ap
```

but the second line is exactly the norm-core information already consumed in 6aa--6ac to enter the low branch and derive the square receiver. Stage15-6aq already forbids that recharge.

Thus 6at retains the branch inequality but does not revive AR-009.

## 5. Audit verdict

```text
AUDIT_STAGE=Stage15-6at
AUDIT_TARGET=LOW_CORE_BRANCH_MEMORY_SUFFICIENCY
AUDIT_VERDICT=BLOCK
LOW_CORE_BRANCH_MEMORY_RETAINED=true
REMEMBERED_INEQUALITY=k^2<4*R0*S0
PRODUCT_HEIGHT_RETAINED=true
SMALL_KAPPA_INEQUALITY_RETAINED=true
SIZE_ONLY_NORM_CORE_SUMMABILITY=false
AR009_RECHARGE=false
ADDITIONAL_ARITHMETIC_CORRELATION_REQUIRED=true
```

The correct next theorem species must act on the rational points / coverings themselves, not merely on the three size inequalities.

## 6. Next audit target

The exact 6ar twist packet suggests a targeted literature species:

```text
count squarefree quadratic twists of y^2=x^3-x
that carry a rational point of unusually small height,
with a quantitative bound uniform in the height/twist range.
```

This is materially narrower than generic average-rank or Selmer results and is the target for Stage15-6au.

## 7. Frozen exit

```text
STAGE15_6_SUBSTAGE=6at
STAGE15_6AT_AUDIT=true
STAGE15_6AT_AUDIT_VERDICT=BLOCK
STAGE15_6AT_LOW_CORE_BRANCH_MEMORY_RETAINED=true
STAGE15_6AT_SIZE_ONLY_GLOBAL_k_SUM_PROVED=false
STAGE15_6AT_AR009_RECHARGE=false
STAGE15_6AT_EXIT=SMALL_HEIGHT_TWIST_FAMILY_THEOREM_AUDIT_READY
```