# Stage27-19-r401a — split-factor genus-one torsor barrier

```text
TASK_ID=Stage27-19-r401a
OWNER_STAGE=Stage27
PARENT_ROUTE=Stage27-19-r401
TRIGGER_CHECKPOINT=40
ROUTE_KIND=LOWER_REENTRY
ROUTE_LABEL=MASTER_SPLIT_GENUS_ONE_TORSOR
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ADVANCE_TO_CHECKPOINT50=false
```

## 1. Audited parent boundary

Stage27-19-r401 hostile audit passed and PR #1031 merged at

```text
05e8768872d69770bc02f42f3324039dab8f5e9b
```

The current lower remains

\[
N_2(B)\gg B^{1/4},
\]

and the accepted progress gate remains `kappa/h>1/4`. The parent route also derived the exact Stage19 master space receiver

\[
\boxed{x^2y^2+1=z^2(x^2+y^2)}.
\]

This subroute asks whether that receiver has a cheap rational section that could supply one physical point for each outer rational parameter.

## 2. Exact split factorization

The master equation is equivalent to

\[
\boxed{(x^2-z^2)(y^2-z^2)=z^4-1.}
\]

The chart `z^2=1` contains no positive nondegenerate Stage19 toric object: the factorization gives

\[
(x^2-1)(y^2-1)=0,
\]

and `x^2=1` or `y^2=1` kills one of the two positive toric edge coordinates. Hence every physical point lies in the chart `z^2!=1`.

Define

\[
\tau:=\frac{x^2-z^2}{z^2-1}.
\]

Then

\[
\boxed{x^2=(\tau+1)z^2-\tau},
\qquad
\boxed{y^2=z^2+\frac{z^2+1}{\tau}}.
\]

A physical point has `tau!=0,-1`: `tau=0` forces `z^4=1` in the excluded chart, while `tau=-1` forces `x^2=1`.

```text
MASTER_SPLIT_FACTORIZATION_PROVED=true
PHYSICAL_Z2_EQ_1_BRANCH_EMPTY=true
PHYSICAL_TAU_ZERO_OR_MINUS_ONE_EXCLUDED=true
```

## 3. Parametrize the first conic exactly

For fixed `tau`, the first equation

\[
x^2=(\tau+1)z^2-\tau
\]

has the rational base point `(x,z)=(1,1)`. Intersect with the line

\[
x=1+u(z-1).
\]

Besides the base point, the second intersection is

\[
D=u^2-\tau-1,
\]

\[
\boxed{z=\frac{\tau+(u-1)^2}{D}},
\]

\[
\boxed{x=\frac{2\tau u-\tau-u^2+2u-1}{D}}.
\]

Substitution into the second square condition gives, after absorbing the square denominator into `V=yD`,

\[
\boxed{
\tau V^2=(u^2+\tau+1)
\Bigl((\tau+2)u^2-4(\tau+1)u+(\tau+1)(\tau+2)\Bigr).
}
\]

Call this generic fiber `C_tau`.

```text
FIRST_CONIC_RATIONAL_PARAMETRIZATION_PROVED=true
GENERIC_FIBER_QUARTIC_MODEL_PROVED=true
```

## 4. Every physical fiber is smooth genus one

Let

\[
G_\tau(u)=(u^2+\tau+1)
\Bigl((\tau+2)u^2-4(\tau+1)u+(\tau+1)(\tau+2)\Bigr).
\]

Direct quartic discriminant calculation gives

\[
\boxed{\operatorname{Disc}_u(G_\tau)=4096\,\tau^2(\tau+1)^8.}
\]

Thus for every physical `tau!=0,-1`, the branch quartic is squarefree. Its smooth projective double cover has genus one.

The classical binary-quartic invariants may be taken as

\[
I=16(\tau+1)^2(\tau^2+\tau+1),
\]

\[
J=64(\tau-1)(\tau+1)^3(\tau+2)(2\tau+1).
\]

Hence

\[
\frac{J^2}{I^3}
=
\frac{(\tau-1)^2(\tau+2)^2(2\tau+1)^2}
{(\tau^2+\tau+1)^3}
\]

is nonconstant. The family is genuinely moving; it is not one fixed elliptic curve with harmless coefficient scaling.

```text
PHYSICAL_GENERIC_FIBER_SMOOTH=true
PHYSICAL_GENERIC_FIBER_GENUS=1
GENUS_ONE_FIBRATION_NONISOTRIVIAL=true
```

## 5. Tau-adic parity obstruction: no rational section

Set

\[
K=\mathbf Q(\tau),
\qquad
K_0=\mathbf Q((\tau)),
\]

with the `tau`-adic valuation `v`. A `K`-rational point would give a `K_0`-rational point, so it is enough to rule out `C_tau(K_0)`.

For an affine point, write the equation as

\[
\tau V^2=G_\tau(u).
\]

The left side always has odd valuation

\[
v(\tau V^2)=1+2v(V).
\]

We show the right side always has even valuation.

### Case A: `v(u)<0`

Both quadratic factors have leading valuation `2v(u)`, so

\[
v(G_\tau(u))=4v(u),
\]

which is even.

### Case B: `v(u)>=0` and residue `u_0!=1`

Reducing at `tau=0` gives

\[
G_0(u)=2(u^2+1)(u-1)^2.
\]

Over the residue field `Q`, `u_0^2+1` never vanishes. If `u_0!=1`, the right side is a unit and has valuation `0`.

### Case C: `u=1+w` with `v(w)>0`

The second quadratic factor becomes exactly

\[
\tau^2-2\tau w+(\tau+2)w^2.
\]

If `v(w)>1`, its valuation is exactly `2`. If `v(w)=1`, write `w=a\tau+O(\tau^2)`; the coefficient of `tau^2` is

\[
1-2a+2a^2,
\]

whose discriminant is `-4`, so it is nonzero for every rational residue `a`. Again the valuation is exactly `2`. The first quadratic factor is a unit. Thus the right side has even valuation `2`.

The point `w=0` gives the same valuation `2` directly.

### Points at infinity

After setting `W=1/u` and `Y=V/u^2`, the infinity equation is

\[
Y^2=\frac{\tau+2}{\tau}.
\]

The right side has `tau`-adic valuation `-1`, hence is not a square in `K_0`.

Therefore

\[
\boxed{C_\tau(\mathbf Q((\tau)))=\varnothing}
\]

and consequently

\[
\boxed{C_\tau(\mathbf Q(\tau))=\varnothing.}
\]

So this natural Stage19 genus-one fibration has **no rational section**.

```text
TAU_ADIC_LOCAL_OBSTRUCTION_PROVED=true
GENERIC_FIBER_QTAU_POINT_EXISTS=false
GENERIC_RATIONAL_SECTION_EXISTS=false
```

## 6. Degree-two escape exists, but does not yet improve the lower exponent

At `u=0`, the fiber equation becomes

\[
V^2=(\tau+1)^2\frac{\tau+2}{\tau}.
\]

Thus adjoining

\[
\sqrt{\frac{\tau+2}{\tau}}
\]

produces an explicit quadratic point over the generic base. The extension is genuinely quadratic because `(tau+2)/tau` has odd `tau`-adic valuation.

Hence the cheapest explicit escape from the no-section obstruction is already degree two over the `tau`-line. This is fully compatible with the existence of one-parameter NPC families, which may appear as multisections after a nontrivial base change.

What is **not** proved here is that every degree-two multisection has the R501/R502 degree-eight physical height, or that every possible Stage19 family factors through this `tau`-fibration. Therefore no global `1/4` optimality claim is made.

```text
GENERIC_DEGREE2_CLOSED_POINT_EXHIBITED=true
DEGREE1_SECTION_ROUTE_CLOSED=true
ALL_MULTISECTIONS_CLASSIFIED=false
ALL_STAGE19_PARAMETRIZATIONS_CLASSIFIED=false
MASTER_SURFACE_RATIONALITY_DISPROVED=false
```

## 7. Lower-bound consequence and next exact gate

The parent progress criterion remains

\[
\kappa/h>1/4.
\]

The new structural result removes one tempting shortcut: there is no rational section of the natural split-factor `tau`-fibration that gives one rational Stage19 space point for every rational `tau` at degree one over the base.

The next lower-side task is therefore a **low-degree multisection height audit**:

1. classify or construct degree-two and other low-degree multisections of `C_tau`;
2. compute their induced rational degrees for `x=m/n` and `y=r/s`;
3. pass them through the toric physical height `R<=B`;
4. test the exact `kappa/h>1/4` gate;
5. retain primitive/canonical/exactly-two filters and bounded multiplicity.

A degree-two base change is not automatically a quarter-power theorem and is not automatically exponent-neutral; the physical height ledger must decide.

## 8. Scope firewall

This route is deliberately narrow.

- It proves no `beta>1/4` lower.
- It proves no matching half-power lower.
- It does not prove the master surface is nonrational by every possible birational model.
- It does not identify all rational curves or multisections on the surface.
- It does not identify the true `N2` exponent.
- It does not draw any perfect-cuboid conclusion.
- It is consistent with Stage15's prior moving-genus-one geometry but does not assert that the Stage15 low-core curve is literally the same model.

```text
STAGE27_19_R401A_ATTACK_EXECUTED=true
PARENT_R401_AUDITED_PASS_MERGED=true
MASTER_SPLIT_FACTORIZATION_PROVED=true
PHYSICAL_GENERIC_FIBER_GENUS=1
TAU_ADIC_LOCAL_OBSTRUCTION_PROVED=true
GENERIC_RATIONAL_SECTION_EXISTS=false
DEGREE1_SECTION_ROUTE_CLOSED=true
GENERIC_DEGREE2_CLOSED_POINT_EXHIBITED=true
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_DERIVED_ROUTE=27-19-r401b
NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit
```
