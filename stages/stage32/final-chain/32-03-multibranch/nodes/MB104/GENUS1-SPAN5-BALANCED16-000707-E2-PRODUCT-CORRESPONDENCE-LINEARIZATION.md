# Stage32 MB104 — `000707000f0f` e=2 product-correspondence linearization

Status: **RETAINED CANDIDATE CONSEQUENCE OF AMBIENT H1 TORSION KILL / PRODUCT DIVISOR CLASS `Z~TZ` / FULL-`G` CORRESPONDENCE CENTRALIZER / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Assume the candidate ambient topology leaf is valid at the same exact head, so on the smooth residual model `Y`

```text
(C_1-C_2)+sum_(j in Sigma) (d_j/2)F_j ~ 0.       (LIN)
```

Here the fourteen `F_j=E_j^+-E_j^-` are precisely the exceptional divisors over the supported `A1` points of the support-specific intermediate quotient

```text
X_H=(C8 x C8)/H_diag,
H=<T',TT'R>~=(Z/2)^2,
```

and `C_1,C_2` are the two strict-transform valuations of the quotient curves `Gamma,tau Gamma`.

This note records what `(LIN)` forces before any individual conductor pair is evaluated.

## 1. Push `(LIN)` to the normal intermediate quotient

The function fields of the retained smooth residual model and `X_H` agree.  If `f` is a rational function realizing `(LIN)`, then divisorial valuations centered in codimension one on `X_H` see coefficient `+1` on `Gamma` and `-1` on `tau Gamma`.

Every displayed `F_j` is exceptional over an isolated supported `A1` point, so its center on `X_H` has codimension two and it contributes no prime divisor to `div_(X_H)(f)`.  No other nonexceptional component occurs in `(LIN)`.

Therefore on the normal surface `X_H`

```text
div_(X_H)(f)=Gamma-tau Gamma,
Gamma ~ tau Gamma.                               (XH-LIN)
```

This use of principal divisors is birational: it does not require identifying the chosen smooth model with the minimal resolution as schemes.

## 2. Pull back to the product surface

Let

```text
q_H:P=C8 x C8 -> X_H
```

be the degree-four diagonal-`H` quotient.  The retained e=2 equality geometry has component stabilizer exactly `H`, and at the generic point the inertia is trivial.  Hence the retained divisor pullbacks are

```text
q_H^*Gamma=Zbar,
q_H^*(tau Gamma)=Tdiag(Zbar),
```

where `Zbar` denotes the product-surface image of the normalized etale correspondence `Z`, and `Tdiag` is the residual diagonal `T` action.

Pullback of the principal divisor in `(XH-LIN)` gives

```text
Zbar ~ Tdiag(Zbar) in Pic(P).                    (P-LIN)
```

This is strictly stronger than numerical equivalence of the two product-image divisors.

## 3. Exact self-intersection and product-image genus budget

Put

```text
a_j=d_j/2,
x_j=4l+a_j.
```

From the retained lift-energy identity,

```text
C_1^2=168l^2-sum_j a_j^2.
```

At the two supported `A1` lifts above node `j`, the `Gamma` multiplicities are

```text
4l+a_j,
4l-a_j.
```

The Mumford self-intersection correction at an `A1` point is `r^2/2`.  Hence

```text
Gamma^2
 = C_1^2
   + (1/2)sum_j[(4l+a_j)^2+(4l-a_j)^2]
 = (168l^2-sum_j a_j^2)+(224l^2+sum_j a_j^2)
 = 392l^2.                                      (GAMMA2)
```

Projection formula for `q_H` now gives

```text
Zbar^2 = 4 Gamma^2 = 1568l^2.                  (Z2)
```

The equality-rigidity leaf gives

```text
K_P.Zbar=448l,
g(normalization(Zbar))=112l+1.
```

Adjunction on the smooth product surface therefore forces

```text
p_a(Zbar)
 = 1+(Zbar^2+K_P.Zbar)/2
 = 784l^2+224l+1,
```

and the total normalization defect of the product image is

```text
delta(Zbar)
 = p_a(Zbar)-g(Z)
 = 784l^2+112l.                                 (Z-DELTA)
```

This is an exact global singularity budget for any e=2 realization satisfying `(LIN)`.  It is not a construction of such a curve.

## 4. Jacobian correspondence consequence

The divisor `Zbar` determines the usual correspondence homomorphism

```text
Phi_Z=(f_2)_* f_1^*: J(C8)->J(C8),
```

where `f_1,f_2` are the two degree-`28l` etale projections from the normalization.

Linear equivalence of correspondences induces the same homomorphism on `Pic^0`.  Since `Tdiag(Zbar)` induces

```text
T_* Phi_Z T_*^(-1),
```

`(P-LIN)` implies

```text
Phi_Z T_* = T_* Phi_Z.                          (T-CENT)
```

The component itself is stabilized by diagonal `H`, so the same functoriality gives commutation with `H`.  Because `G=<H,T>`,

```text
Phi_Z in End(J(C8))^G.                          (G-CENT)
```

Thus a surviving e=2 correspondence is not an arbitrary common etale cover: its induced Jacobian correspondence lies in the full `G`-centralizer.

## 5. Exact holomorphic-character shape of that centralizer

Use the finite group coordinates

```text
G=(Z/2)^3,
s1=T',
s2=TT'R,
s3=T.
```

The three singular involutions `s1,s2,s3` each have eight fixed points on the genus-five curve `C8`, so Riemann--Hurwitz gives quotient genus one.  The other four nonidentity elements are fixed-point-free, hence their quotient genus is three.  Also `C8/G~=P1`.

For `V=H^0(C8,K_C8)`, this means

```text
trace(1|V)=5,
trace(s_i|V)=-3  for the three singular involutions,
trace(g|V)=+1    for the four free nonidentity elements.
```

Fourier inversion on `G` gives the exact isotypic multiplicity pattern

```text
5 = 1+1+1+2,
```

with the trivial character absent.  In the `(rho,tau,upsilon)` convention of the retained modular character leaf, the nonzero multiplicities are

```text
m_(0,0,1)=1,
m_(0,1,0)=1,
m_(0,1,1)=1,
m_(1,1,1)=2,
```

and all other character multiplicities are zero.

Consequently every complex-linear endomorphism commuting with `G` is block diagonal on holomorphic differentials with three scalar one-dimensional blocks and one `2 x 2` block.  The algebraic correspondence `Phi_Z` must lie in the integral/algebraic subring of this centralizer.

This is a routing constraint only.  No claim is made here that the centralizer condition alone excludes degree `28l`.

## Route consequence

The candidate ambient torsion kill has a stronger downstream meaning than only `w~0`:

```text
w~0
 -> Gamma~tau Gamma on X_H
 -> Zbar~Tdiag(Zbar) on C8 x C8
 -> Phi_Z commutes with full G.
```

The active e=2 problem may therefore be attacked without reconstructing every conductor sign if one can show that no degree-`28l` etale self-correspondence with the required support passport can occupy the integral full-`G` centralizer class above.

Useful next inputs are:

1. an exact endomorphism-ring/Jacobian decomposition of the Wiman modular curve `X(8)` compatible with this `G` action;
2. a modular correspondence theorem identifying the allowable integral elements of `End(J(C8))^G` arising from common etale covers;
3. a direct divisor-class calculation of `O_P(Zbar)` in `Pic(P)` that violates `(P-LIN)` for the retained support passport.

## Firewalls

- This note depends on the candidate ambient `H_1`/torsion-kill leaf and inherits its audit status.
- `Zbar` is the product-surface image; its normalization is the smooth common etale cover `Z`.
- The arithmetic-genus calculation does not use the geometric genus in the adjunction formula.
- No claim that `Zbar` itself is smooth.
- No conductor pair is assigned a sign.
- No weighted-cut upper bound is claimed.
- No e=2 closure is claimed.
- e=4 and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
