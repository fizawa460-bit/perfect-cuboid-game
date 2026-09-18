# Stage32 MB104 — H8 logarithmic-boundary inequality shallow gate — 2026-09-18

Status: **H8 SHALLOW GATE FAIL / PARKED / H5 NEXT / NO MATHEMATICAL CREDIT**

## Target

H8 asks whether the fourteen supported exceptional curves, together with the exact balanced packet

```
D_l=7lH-4l sum_(p in Sigma)E_p,
|Sigma|=14,
D_l.E_i=8l,
Delta=168l^2+56l,
```

can be inserted into a log/orbifold BMY inequality to force an all-`l` or large-`l` contradiction.

The external theorem shape is recorded in `MB104-H8-LOG-BMY-SOURCE-NOTE-20260918.md`.

## Exact log-square contribution of the exceptional boundary

Let `C` be a hypothetical carrier and write

```
B=aC+sum_i b_i E_i,
0<=a,b_i<=1.
```

Put

```
S1=sum_i b_i,
S2=sum_i b_i^2.
```

Using

```
K^2=16,
K.C=112l,
C^2=336l^2,
K.E_i=0,
C.E_i=8l,
E_i^2=-2,
```

one gets exactly

```
(K+B)^2
 =16+224al+336a^2l^2+16al*S1-2S2.        (H8-LHS)
```

The new exceptional-boundary contribution is only linear in `l`; the only fixed quadratic term is still the carrier term `336a^2l^2`.

## Formal nodal compatibility witness

The retained packet fixes the exceptional contacts and the total genus defect, but it does not classify the analytic types of the off-exceptional singularities. The historical Picard-realizability leaf explicitly leaves the positive `Delta_off` unconstrained.

Therefore the shallow gate must allow the following **formal compatibility witness**:

- all `Delta=168l^2+56l` off-exceptional defect is realized by ordinary nodes;
- the normalization has genus one;
- each `E_i` meets `C` in `8l` distinct transverse smooth points;
- the fourteen `E_i` remain disjoint `(-2)` curves.

This does **not** assert that an actual effective cuboid-surface carrier with these nodes exists. It tests whether the retained aggregate interface alone forces violation of log BMY.

For this ordinary-node/transverse arrangement, Euler stratification gives

```
e_orb(S,B)
 =80 - 2S1 + 8la*S1 + a^2*Delta.          (H8-RHS)
```

Hence

```
3e_orb-(K+B)^2
 =224-6S1+2S2
  +8al*S1-224al
  +168a^2l^2+168a^2l.                     (H8-SLACK)
```

## Uniform positivity for every boundary weight

Set `x=al>=0`. For one exceptional coefficient,

```
q_x(b)=2b^2+(8x-6)b,  0<=b<=1.
```

Its exact minimum is

```
8x-4                         for 0<=x<=1/4,
-(8x-6)^2/8                 for 1/4<=x<=3/4,
0                            for x>=3/4.
```

After summing fourteen copies and temporarily dropping the extra nonnegative term `168a^2l`, the three regions give respectively

```
168x^2-112x+168            >= 301/2,
7(8x^2-8x+23)              >= 147,
168x^2-224x+224            >= 301/2.
```

Therefore, uniformly for every `l>=1` and every coefficient choice `0<=a,b_i<=1`,

```
3e_orb(S,B)-(K+B)^2 >= 147 > 0.            (H8-WITNESS)
```

In particular all published discrete orbifold coefficients `1` or `1-1/m` lie inside a region where this retained-data-compatible nodal witness satisfies the BMY inequality strictly.

## What this means

The fourteen exceptional curves and the exact `8l` contacts do not provide the missing quadratic obstruction. A log-BMY proof could still become useful only after a **new** theorem forces the off-exceptional singularities into a much narrower analytic class whose local orbifold terms cannot behave like the nodal witness.

Without such input, H8 would silently replace the actual missing global singularity theorem by an assumption on the off-exceptional singularities.

Thus

```
H8 shallow gate = FAIL
H8 = PARKED
finite degree window = NOT PROVED
heavy computation = NOT RELEASED
next shallow gate = H5 exact etale-correspondence quotient rigidity
```

No actual carrier is constructed by the witness. No MB104, receiver, effectivity, theorem, endpoint, Perfect-Cuboid, or merge credit changes.
