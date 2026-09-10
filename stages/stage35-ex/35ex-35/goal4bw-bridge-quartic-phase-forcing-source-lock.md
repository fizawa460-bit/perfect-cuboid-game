# Stage35-EX Goal4BW source lock — bridge-local quartic phase forcing boundary

Scope: consume Goal4BV and test the next exact question: do the retained E1 bridge equations force the real quartic phase at an odd bridge prime `ell|e`? They fix the relative root orientation, but at the 35EX-03/08/10/11 bridge-local layer the quartic phase reduces to one residual square-root Legendre bit. This leaf does not rule out a stronger global E1 product relation. Mathematical authority remains V74 / Goal4AK.

## 1. Exact parent and notation

Parent head:

```text
90e281ee9aaba23a0bf4ed5a3f68f3fc19c8178a
```

For an odd `ell|e`, Goal4BV fixes

```text
iota = iota_e(ell) = A*B^(-1) mod ell,
iota^2 = -1 mod ell,
```

where `A=(V1/q)*T`, `B=D*(V2/q)` are the ordered reduced Master legs. Since `ell|e|c|U1` and the first Euclid triple is primitive, `V1,W1` are units modulo `ell`. Put

```text
omega_ell := W1*V1^(-1) mod ell.                      (BW-omega)
```

Using `W1^2-V1^2=U1^2` and `ell|U1`,

```text
omega_ell in {+1,-1}.                                 (BW-sign)
```

Thus `omega_ell` is source-fixed. It records which local factor of `U1=(a-b)(a+b)` vanishes.

Let

```text
rho = r*s^(-1) mod ell,
sigma = u*v^(-1) mod ell.
```

Because `ell|e` divides both primitive hypotenuses `w=r^2+s^2` and `H=u^2+v^2`, all of `r,s,u,v` are units and

```text
rho^2=sigma^2=-1.                                     (BW-roots)
```

## 2. Branch L: the relative root is source-fixed

In Branch L,

```text
(V1/q)*T = u^2-v^2,
D*(V2/q) = 2*u*v.
```

Modulo `ell|H`,

```text
iota=(u^2-v^2)/(2uv)=u/v=sigma.                       (BW-L-iota)
```

The E1 odd equation and Master odd equation give

```text
(W1/p)*T = r^2-s^2 = -2*s^2,
(V1/q)*T = u^2-v^2 = -2*v^2.
```

Writing `x=v/s`, their ratio is

```text
p/q = omega_ell*x^2.                                  (BW-L-ratio)
```

The Branch-L cross equation `p*r*s=q*u*v` gives independently

```text
p/q = (iota/rho)*x^2.
```

Hence

```text
rho = omega_ell*iota.                                 (BW-L-root)
```

So the E1 root above the bridge prime is not a free conjugation choice.

For the Goal4BV numerator `N_L=p*q`, define

```text
z_L = q*v/s mod ell.
```

Then

```text
N_L = omega_ell*z_L^2 mod ell.                        (BW-L-square)
```

## 3. Branch R has the same normal form

In Branch R,

```text
(V1/q)*T = 2*u*v,
D*(V2/q) = u^2-v^2.
```

Therefore modulo `ell|H`,

```text
iota=(2uv)/(u^2-v^2)=-u/v=-sigma.                     (BW-R-iota)
```

The E1 odd equation divided by the Master even equation yields

```text
p/q = omega_ell*iota*x^2,                             (BW-R-ratio)
```

while `2*p*r*s=q*(u^2-v^2)` yields

```text
p/q = rho*x^2.
```

Thus again

```text
rho = omega_ell*iota.                                 (BW-R-root)
```

For `N_R=2*p*q`, use `(1+iota)^2=2*iota` in `F_ell` and define

```text
z_R=(1+iota)*q*v/s mod ell.
```

Then

```text
N_R = omega_ell*z_R^2 mod ell.                        (BW-R-square)
```

Hence both branches have the common bridge-local form

```text
rho = omega_ell*iota,
N_branch = omega_ell*z_branch^2.                      (BW-common)
```

## 4. Exact quartic phase reduction

Let `pi_{e,ell}` be the Goal4BV primary Gaussian prime selected by `iota`. Under the quadratically-good bridge condition, `Q_e(ell)=[N_branch/pi_{e,ell}]_4` is real. From `(BW-common)`,

```text
Q_e(ell) = [omega_ell/pi_{e,ell}]_4 * (z_branch/ell). (BW-Q4)
```

Here `(z_branch/ell)` is the ordinary Legendre symbol. The first factor is explicit from source data; for `omega_ell=-1` it is `(-1)^((ell-1)/4)`.

The retained bridge equations determine `z_branch^2=N_branch/omega_ell`, but they provide no independent condition on the Legendre class of its square root. Because `ell=1 mod4`, replacing `z_branch` by `-z_branch` does not change `(z_branch/ell)`. Thus the residual bit in `(BW-Q4)` is well-defined, but it is not removed by the bridge-local equations themselves.

This is a sharper result than Goal4BV: the relative Gaussian/root orientation is now fixed by the E1 equations, and the exact remaining phase gauge is isolated.

## 5. Bridge-local finite-field diagnostics

The following are deliberately local `F_5` models, not global Master-Hits and not E1 counterexamples. They test only implications of the retained bridge congruences.

Take

```text
ell=5, iota=2, omega=1, q=1.
```

### Branch L

Use `sigma=iota=2`, `rho=omega*iota=2`.

```text
x=1: p=1, N_L=1, Q_e=+1,
x=2: p=4 mod5, N_L=4, Q_e=-1.
```

Both satisfy `p/q=omega*x^2` and the reduced cross equation modulo 5.

### Branch R

Use `sigma=-iota=3`, `rho=omega*iota=2`.

```text
x=1: p=2, N_R=4, Q_e=-1,
x=2: p=3, N_R=1, Q_e=+1.
```

Both satisfy `p/q=omega*iota*x^2` and the reduced Branch-R cross equation modulo 5.

Therefore neither real phase is excluded by the bridge-local congruence system. This is not evidence that global integer E1 counterexamples exist.

## 6. Goal4BW verdict

Certified provisionally:

```text
E1_RELATIVE_BRIDGE_ROOT_ORIENTATION_SOURCE_FIXED=true
BOTH_BRANCHES_REDUCE_TO_N_EQUALS_OMEGA_TIMES_SQUARE=true
BRIDGE_QUARTIC_PHASE_REDUCES_TO_ONE_LEGENDRE_BIT=true
BRIDGE_LOCAL_EQUATIONS_FORCE_FIXED_QUARTIC_PHASE=false
BRIDGE_LOCAL_MODELS_REALIZE_BOTH_REAL_PHASES=true         (BW-VERDICT)
```

Not certified:

```text
global E1 system permits both phases;
global product of bridge quartic phases is free;
universal bad quartic bridge prime;
branch exclusion;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

## 7. Next leaf

The only unspent bridge-quartic possibility is now global rather than single-prime. Form the oriented bridge kernel over the odd squarefree support of `e` and test whether the bridge double-square identities or quartic reciprocity force a product relation among the residual bits in `(BW-Q4)`:

```text
35EX-35_GOAL4BX_BRIDGE_QUARTIC_GLOBAL_PRODUCT_PREFLIGHT
```

If no source-fixed global product exists, freeze the early Pesch bridge-quartic route rather than recycling the later Goal4BF--BO endpoint machinery.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
