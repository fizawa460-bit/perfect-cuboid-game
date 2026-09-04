# Stage35-EX 35EX-18 — Gaussian relative orientation and Master-unit freeze

## Scope

Continue from the hostile-audited and merged 35EX-17/17B Gaussian coordinate-gcd hook. Work conditionally under a hypothetical full E1 counterexample, so

```text
Lminus=x^2,
Lplus=y^2.
```

This leaf asks exactly whether the primitive `p*d`-twisted Gaussian norms from 35EX-17B, together with the normalized Master Gaussian square, force a contradictory split-prime orientation.

They do not. The two E1 Gaussian products force the **relative** `p*d` orientation exactly, but the Master Gaussian is a unit at every prime over `p*d`; its remaining information is a moving source-unit Legendre condition, not an orientation contradiction.

No E1, receiver, Stage35 MAIN, Stage29-parent, or endpoint credit is claimed.

## 1. Normalized Gaussian coordinates

Put

```text
alpha = a*m-b*n,
beta  = a*n-b*m,
gamma = a*m+b*n,
delta = a*n+b*m,

zminus = alpha+i*beta,
zplus  = gamma+i*delta.
```

Let

```text
gminus=gcd(alpha,beta),
gplus =gcd(gamma,delta).
```

35EX-17B proves

```text
gminus*gplus=c,
gcd(gminus,gplus)=1.
```

Define primitive coordinates

```text
alpha0=alpha/gminus,
beta0 =beta/gminus,
gamma0=gamma/gplus,
delta0=delta/gplus,

zminus0=alpha0+i*beta0,
zplus0 =gamma0+i*delta0.
```

Under the full receiver,

```text
Norm(zminus0)=p*d*X^2,
Norm(zplus0) =p*d*Y^2.
```

Every odd prime dividing `p*d` is `1 mod 4`.

## 2. Two exact E1 Gaussian products

Direct multiplication gives

```text
zminus*zplus
 = W1*U2 + i*U1*V2,                         (P1)

conj(zminus)*zplus
 = U1*W2 + i*V1*U2.                         (P2)
```

Since `gminus*gplus=c`, divide by `c`:

```text
zminus0*zplus0
 = (W1*U2+i*U1*V2)/c,

conj(zminus0)*zplus0
 = (U1*W2+i*V1*U2)/c.                       (P0)
```

For an E1 counterexample, the first canonical primitive odd/even pair gives

```text
(W1*U2+i*U1*V2)/(c*p)=(r+i*s)^2.
```

The index-swapped primitive odd/even pair from 35EX-13 gives

```text
(U1*W2+i*V1*U2)/(c*d)=(x1+i*y1)^2.
```

Therefore exactly

```text
zminus0*zplus0      = p*(r+i*s)^2,          (SQ-p)
conj(zminus0)*zplus0 = d*(x1+i*y1)^2.       (SQ-d)
```

No bounded search is used here.

## 3. Relative split-prime orientation is forced, not free

Let `ell` be an odd prime in the squareclass support of `p*d`, i.e. `v_ell(p*d)` is odd. Then `ell=1 mod4`, so in `Z[i]`

```text
ell = unit * pi * conjugate(pi).
```

Because `zminus0,zplus0` are primitive Gaussian integers and each has norm `p*d` times a rational square, each chooses exactly one of `pi,conjugate(pi)` with odd valuation parity.

The product squareclasses `(SQ-p)` and `(SQ-d)` now determine the relative choice:

- if `v_ell(p)` is odd, `(SQ-p)` has rational squareclass `ell`, so `zminus0` and `zplus0` must choose **opposite** primes over `ell`;
- if `v_ell(d)` is odd, `ell` is absent from the right side of `(SQ-p)`, so the two odd valuation parities must cancel in the product, hence `zminus0` and `zplus0` choose the **same** prime over `ell`.

Since `gcd(p,d)=1`, these cases are disjoint. Thus

```text
P_SQUARECLASS_SUPPORT_RELATIVE_ORIENTATION=OPPOSITE,
D_SQUARECLASS_SUPPORT_RELATIVE_ORIENTATION=SAME.      (REL)
```

So 35EX-18 does sharpen the 35EX-17B hook: the relative orientation vector is not free. It is canonically routed by the `p/d` partition.

This is not a contradiction. It leaves the absolute choice `pi` versus `conjugate(pi)` moving with the source.

## 4. The normalized Master Gaussian in the same coordinates

The reduced Master legs are

```text
A=(V1/q)*(U2/c),
B=(U1/c)*(V2/q),
```

and the normalized Master Gaussian is

```text
G_M=A+i*B=(V1*U2+i*U1*V2)/(c*q).
```

Using `(P1)` and `(P2)` coordinate identities,

```text
V1*U2/c = alpha0*delta0-beta0*gamma0,
U1*V2/c = alpha0*delta0+beta0*gamma0.
```

Hence exactly

```text
G_M
 = (1+i)/q * (alpha0*delta0+i*beta0*gamma0).  (MASTER-BILINEAR)
```

35EX-03 gives the two 2-adic branches:

```text
Branch L: G_M=(u+i*v)^2,
Branch R: G_M=i*(u-i*v)^2.                    (MASTER-SQ)
```

Thus the Master square has been expressed directly in the primitive coordinates of `zminus0,zplus0`.

## 5. Every `p*d` prime is a Master Gaussian unit prime

Let `ell|p`. Then

```text
ell|W1,
ell|V2,
ell does not divide V1*U2*c*q.
```

Therefore modulo `ell`, the imaginary component of the raw Master Gaussian vanishes while the real component is nonzero:

```text
V1*U2+i*U1*V2 == V1*U2 != 0 mod ell.
```

So `ell` does not divide `Norm(G_M)`.

Similarly, if `ell|d`, then

```text
ell|V1,
ell|W2,
ell does not divide U1*V2*c*q,
```

and

```text
V1*U2+i*U1*V2 == i*U1*V2 != 0 mod ell.
```

Again `ell` does not divide `Norm(G_M)`.

Consequently for every Gaussian prime `pi` over every odd `ell|p*d`,

```text
v_pi(G_M)=v_conjugate(pi)(G_M)=0.             (MASTER-UNIT)
```

The Master square therefore contributes **no `p*d` valuation parity** capable of reversing or contradicting `(REL)`.

## 6. Exact residue information: a moving `c*q` Legendre condition

The Master square does impose a residue-square condition at `ell|p*d`, but it is orientation-blind.

Let `(./ell)` denote the Legendre symbol. For every odd `ell|p`, primitivity and `ell|W1,V2` give

```text
(V1/ell)=+1,
(U2/ell)=+1.
```

Indeed `a^2+b^2=0 mod ell` implies `a/b` is a square root of `-1`; because `ell=1 mod4`, the character of that root equals `(2/ell)`, so `2ab` is a square. Also `ell|2mn` forces `U2=m^2-n^2` to be `+square` or `-square`, and `-1` is a square.

Hence

```text
(A/ell)=(c*q/ell).                            (A-char)
```

Likewise, for every odd `ell|d`, `ell|V1,W2` gives

```text
(U1/ell)=+1,
(V2/ell)=+1,
```

and therefore

```text
(B/ell)=(c*q/ell).                            (B-char)
```

Reduce `(MASTER-SQ)` modulo a Gaussian prime above `ell`. If `rho^2=-1 mod ell`, then

```text
(rho/ell)=(2/ell).
```

Therefore the exact Master residue table is

```text
             ell|p                  ell|d
Branch L:   (c*q/ell)=+1           (c*q/ell)=(2/ell)
Branch R:   (c*q/ell)=(2/ell)      (c*q/ell)=+1.      (MASTER-CHAR)
```

This condition depends only on the moving source unit `c*q` and the Master 2-adic branch. It does **not** depend on whether the absolute orientation chosen by `zminus0` is `pi` or `conjugate(pi)`.

Thus the normalized Master Gaussian is blind to the remaining absolute `p*d` orientation bit at the exact local level exposed by 35EX-17B.

## 7. Deterministic Master-Hit regression witnesses only

The four channel/branch possibilities in `(MASTER-CHAR)` already occur among genuine Master-Hits:

```text
Branch L, p=5: (a,b,m,n)=(4,3,16,5),  c=7,  q=8,  (c*q/5)=+1.
Branch L, d=5: (a,b,m,n)=(6,5,9,8),   c=1,  q=12, (c*q/5)=-1=(2/5).
Branch R, p=5: (a,b,m,n)=(9,8,6,5),   c=1,  q=12, (c*q/5)=-1=(2/5).
Branch R, d=5: (a,b,m,n)=(8,5,11,2),  c=39, q=4,  (c*q/5)=+1.
```

These witnesses are not E1 counterexamples and are not theorem credit. They only regression-lock that the Master residue table itself is noncontradictory on the source Master population.

## 8. Route boundary

35EX-18 therefore closes the selected Gaussian coordinate-orientation question as follows:

```text
GAUSSIAN_RELATIVE_PD_ORIENTATION_PROVED=true
P_ODD_SQUARECLASS_PRIMES_ROUTE_OPPOSITE=true
D_ODD_SQUARECLASS_PRIMES_ROUTE_SAME=true
MASTER_GAUSSIAN_BILINEAR_COORDINATE_IDENTITY_PROVED=true
MASTER_GAUSSIAN_PD_VALUATION_CONTRADICTION=false
MASTER_PD_LOCAL_RESIDUE_TABLE_PROVED=true
MASTER_PD_LOCAL_RESIDUE_TABLE_ORIENTATION_BLIND=true
ABSOLUTE_PD_SPLIT_PRIME_ORIENTATION_UNIFORMLY_FIXED=false
CURRENT_GAUSSIAN_COORDINATE_ORIENTATION_ROUTE=FROZEN_MOVING_ABSOLUTE_ORIENTATION_AND_SOURCE_UNITS
ALL_DEEPER_GAUSSIAN_OR_RECIPROCITY_ARGUMENTS_RULED_OUT=false
E1_PROVED=false
```

The new `c*q` Legendre table is exact, but its modulus/support moves with `p,d,c,q`; no fixed finite support or source-independent product sign is produced here. It therefore does not by itself reopen theorem credit or close the full receiver.

The fresh 35EX-17B breadth audit already preserved one genuinely distinct untested candidate:

```text
E1-RECEIVER-SPECIFIC-GENUSONE-ELIMINATION.
```

Accordingly the next legal leaf is

```text
35EX-19_RECEIVER_SPECIFIC_GENUSONE_ADAPTER_OR_BLOCKER.
```

It must derive an exact receiver-specific quartic/genus-one model and source-to-curve adapter before any elliptic-curve theorem or Arsenal `S31-W01` machinery may be imported. If no fixed model/adapter can be obtained, freeze that candidate rather than treating generic genus-one language as a theorem.

## Credit firewall

```text
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
