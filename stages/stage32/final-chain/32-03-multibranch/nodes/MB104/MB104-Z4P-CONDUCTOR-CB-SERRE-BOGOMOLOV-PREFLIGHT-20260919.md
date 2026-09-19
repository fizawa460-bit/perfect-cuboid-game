# MB104 Z4' — conductor-scheme Cayley--Bacharach / Serre-bundle preflight — 2026-09-19

Status: **Z1--Z30 REACTIVATION / PRE-AUDIT BEST-CASE SERRE NO-GO / NO CREDIT**

## Scope

This note returns to the original Z4' localization/collision route only.

Later assets are used only as input facts:

```text
C in |lP|, l>=1,
normalization genus(E)=1,
delta(C)=168l^2+56l,
Z_cond subset S is the conductor scheme,
length(Z_cond)=delta(C),
Supp(Z_cond) lies in the smooth interior.
```

The purpose is to test whether the now-exact quadratic conductor scheme can be converted,
through Cayley--Bacharach/Serre construction and Bogomolov instability, into the missing
equality-breaking global obstruction.

## 1. The conductor scheme supplies the right quadratic scale

The exact conductor-scheme adapter gives

```text
length(Z_cond)
 = delta(C)
 = 168l^2+56l.
```

Since

```text
C^2=336l^2,
K_S.C=112l,
```

this is exactly

```text
2 length(Z_cond)=C^2+K_S.C.                    (COND-ADJ)
```

Thus Z4' no longer lacks a quadratic zero-dimensional singularity object.

## 2. Cayley--Bacharach is not yet source-complete in this exact setting

There is substantial literature relating conductor/adjoint schemes and Cayley--Bacharach
postulation, including conductor schemes arising from plane projections and projectively
Gorenstein situations.

However the exact MB104 object is:

```text
an intrinsic conductor scheme of an arbitrary integral Cartier divisor C on the fixed smooth
cuboid resolution S.
```

The retained source packet does not currently prove that this intrinsic Z_cond satisfies the
Cayley--Bacharach condition with respect to

```text
|K_S+C|.
```

The adjoint/conductor exact sequence and the exact independence statement

```text
H0(K_S+C) -> H0(O_Zcond(K_S+C))
```

being surjective do not by themselves imply the Cayley--Bacharach property required by the
Hartshorne--Serre correspondence.

Therefore no Serre bundle is claimed unconditionally.

## 3. Best-case Serre calculation

Nevertheless, test the strongest favorable scenario.

Assume that Z_cond does satisfy the Cayley--Bacharach condition required to construct a rank-two
bundle V with

```text
0 -> O_S -> V -> I_Zcond(C) -> 0.
```

Then

```text
c1(V)=C,
c2(V)=length(Z_cond)=delta(C).
```

Its Bogomolov discriminant is

```text
Delta(V)
 = 4c2(V)-c1(V)^2
 = 4(168l^2+56l)-336l^2
 = 336l^2+224l
 = 112l(3l+2)
 >0.                                             (SERRE-DISC)
```

So even in the best-case CB/Serre scenario, the Chern numbers do **not** force Bogomolov
instability.

Equivalently,

```text
c1(V)^2 - 4c2(V)
 = -336l^2-224l
 <0.
```

Thus the standard Reider/Bogomolov destabilization mechanism cannot produce an effective
decomposition or a degree bound from the conductor scheme at this determinant.

## 4. Why changing only the determinant is not currently legal

A Hartshorne--Serre construction with another determinant L would require the corresponding
Cayley--Bacharach condition with respect to

```text
|K_S+L|.
```

The retained conductor/adjoint package naturally relates Z_cond to K_S+C.  It does not supply
CB conditions for a smaller determinant L chosen merely to make

```text
L^2 > 4 length(Z_cond)
```

hold.

Therefore one cannot optimize the determinant numerically without a new theorem.

## 5. Z4' disposition

The later conductor result genuinely reopens Z4' enough to replace the old vague
"quadratic singularity localization unknown" statement by:

```text
quadratic conductor scheme exists exactly,
length = 168l^2+56l,
support lies in the smooth interior.
```

But the first natural global vector-bundle attack closes negatively:

```text
intrinsic conductor CB for exact surface setting = not source-locked,
best-case Serre determinant C                    = no Bogomolov instability,
alternate determinant CB                         = not available.
```

So the next useful Z4' theorem must constrain the *postulation/regularity structure* of
Z_cond more strongly than its length and natural adjoint determinant.

In particular, useful future shapes include:

```text
- a source-valid CB/regularity theorem for this intrinsic conductor scheme with a smaller
  effective determinant;
- a uniform bound on the regularity or minimal generators of the conductor ideal on S;
- a decomposition theorem forcing Z_cond onto controlled divisors or fibers.
```

Without one of these, Serre/Reider/Bogomolov is exhausted.

## External source anchors

- Tan--Viehweg, Cayley--Bacharach criteria for zero-dimensional schemes and rank-two bundles.
- Chiarli--Greco--Notari, postulation/Cayley--Bacharach properties of conductor schemes in
  projective-curve projection settings.
- Eisenbud--Ulrich, conductor regularity under projectively Gorenstein hypotheses.

These sources do not by themselves verify the exact intrinsic MB104 Cayley--Bacharach hypothesis.

## Firewalls

```text
quadratic_conductor_scheme_exact=true
intrinsic_conductor_CB_exact_setting_proved=false
serre_bundle_constructed_unconditionally=false
best_case_serre_bogomolov_instability=false
alternate_determinant_CB_available=false
finite_degree_window_proved=false
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
