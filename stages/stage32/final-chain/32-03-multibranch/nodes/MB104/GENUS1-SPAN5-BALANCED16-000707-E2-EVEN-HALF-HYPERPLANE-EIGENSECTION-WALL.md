# Stage32 MB104 — `000707000f0f` e=2 even half-hyperplane eigensection wall

Status: **RETAINED EXACT RR EFFECTIVITY WALL / EVEN-l ANTIINVARIANT EIGENSECTION NONVANISHING IS AUTOMATIC / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The retained half-hyperplane factorization shows, conditionally on the retained ambient-H1 linearization, that for even

```text
l=2*m,  m>=1,
```

the relevant square-root line bundle is the pure pullback

```text
Lambda_(2m) ~= pi^* O_S(7*m*H).
```

Because the two effective members are distinct and exchanged by the residual deck involution, both deck eigenspaces of sections must occur. The potentially useful extra requirement was

```text
H^0(S, O_S(7*m*H) tensor L_abs^(-1)) != 0.    (ANTI-H0)
```

This note checks `(ANTI-H0)` exactly and shows that it is automatic by Riemann--Roch. Thus the standalone global-eigenspace-effectivity route does not obstruct `e=2`.

## 1. Canonical surface invariants

The retained Stoll--Testa source note gives for the minimal resolution `S` of the cuboid surface

```text
K_S=H,
H^2=16,
chi(O_S)=8,
```

with `H` big and nef and `H.E=0` for every exceptional `(-2)`-curve contracted by the canonical morphism.

## 2. The absent half-line has square `-8`

For the support mask `000707000f0f`, the residual double cover

```text
pi:Y->S
```

is branched exactly along the sixteen exceptional curves of the absent node type. Write

```text
B_abs=sum_(p in A_abs) E_p,
|A_abs|=16,
2*L_abs ~ B_abs.
```

The exceptional curves are pairwise disjoint and each has square `-2`. Therefore

```text
B_abs^2=16*(-2)=-32,
H.B_abs=0,
L_abs^2=-8,
H.L_abs=0.                                     (LABS)
```

No choice of half-line representative changes these numerical identities.

## 3. Riemann--Roch for the anti-invariant eigensheaf

Put

```text
D_m=7*m*H-L_abs.
```

Using `(LABS)` and `K_S=H`,

```text
D_m^2
 =49*m^2*H^2+L_abs^2
 =784*m^2-8,

D_m.K_S
 =7*m*H^2
 =112*m.
```

Surface Riemann--Roch gives

```text
chi(O_S(D_m))
 =chi(O_S)+(D_m.(D_m-K_S))/2
 =8+(784*m^2-8-112*m)/2
 =392*m^2-56*m+4.                              (RR)
```

For every integer `m>=1`, this is strictly positive; already at `m=1` it equals `340`.

## 4. The Serre-dual H2 term vanishes

By Serre duality,

```text
h^2(D_m)=h^0(K_S-D_m).
```

Now

```text
K_S-D_m=(1-7*m)H+L_abs,
```

and its intersection with the big and nef class `H` is

```text
H.(K_S-D_m)=16*(1-7*m)<0
```

for every `m>=1`.

An effective divisor has nonnegative intersection with a nef divisor. Hence `K_S-D_m` cannot be effective and

```text
h^0(K_S-D_m)=0,
h^2(D_m)=0.                                    (H2)
```

Combining `(RR)` and `(H2)`,

```text
h^0(D_m)
 =chi(D_m)+h^1(D_m)
 >=392*m^2-56*m+4
 >0.                                           (H0)
```

Thus the anti-invariant eigensection required by the even-l half-hyperplane factorization exists automatically at the level of the unrestricted linear system.

## 5. Route consequence

The condition

```text
H^0(S,O_S(7*m*H) tensor L_abs^(-1)) != 0
```

cannot by itself exclude any even `l=2m` realization: it follows formally from the surface invariants and the absent half-line intersections.

The load-bearing information must therefore include the **prescribed exceptional/conductor vanishing of the particular eigensections**, not just nonzero global sections of their ambient eigensheaves.

If `s_+,s_-` denote the invariant and anti-invariant eigen-sections whose sum/difference cut out the two conjugate divisors, then at a supported node the multiplicity pair `(y_j,4l-y_j)` forces both eigen-sections to vanish to at least

```text
mu_j=min(y_j,4*l-y_j)=2*l-|b_j|
```

along the downstairs exceptional `E_j` after descent. Therefore a sharper continuation is to test effectivity of the allocation-sensitive classes

```text
7*m*H - sum_j mu_j E_j,
7*m*H - L_abs - sum_j mu_j E_j
```

for `l=2m` (with notation adjusted so that `mu_j` is measured in the same divisor normalization).

That jet/vanishing problem may carry information that unrestricted Riemann--Roch necessarily loses.

## Firewalls

- This wall addresses only unrestricted anti-invariant eigensection nonvanishing for even `l`.
- It does not prove the allocation-sensitive vanishing classes effective.
- It does not identify a conductor residual sheet.
- It does not supply a weighted-cut upper bound.
- It does not alter the candidate status of the ambient-H1 linearization used to reach the half-hyperplane factorization.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- Active leaf remains unchanged.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
