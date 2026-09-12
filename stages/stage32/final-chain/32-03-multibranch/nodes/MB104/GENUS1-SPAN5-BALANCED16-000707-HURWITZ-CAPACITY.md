# Stage32 MB104 — `000707000f0f` equality Hurwitz-capacity passports

Status: **RETAINED CURRENT-FRONTIER GLOBAL REDUCTION / SUPPORTED 112l BRANCHES SATURATE QUOTIENT CAPACITY / e=2,4 BOTH STILL OPEN / NO CREDIT**

## Scope

Work only with the surviving balanced orbit

```text
Sigma = 000707000f0f,
|Sigma|=14,
node-type counts = (7,7,0),
D_l=7lH-4l sum_(p in Sigma)E_p,
d=r_odd=112l.
```

Assume conditionally that an integral normalization-genus-one member realizing the uniform minimal-branch packet exists.

The retained equality-rigidity and current node-type quotient leave exactly two product-cover cases:

```text
e=2:  Z -> C8 etale of degree n=28l,
e=4:  Z -> C8 etale of degree n=56l.
```

Here `e=deg(Z->Y)`, where `Y` is the connected Beauville pullback.

Let the two occurring singular stabilizer involutions be `s1,s2`.

## Case A: `e=2`

The stabilizer of the connected product-cover component has order `2e=4`.  Since it contains `s1,s2`, it is exactly

```text
K=<s1,s2>={1,s1,s2,h},
h=s1*s2 in G0.
```

The element `h` is fixed-point-free on `C8`.  Each `s_j` has exactly eight fixed points, and their fixed sets are disjoint because a common fixed point would also be fixed by `h`.

Riemann--Hurwitz for the order-four quotient gives

```text
8 = 4(2g(C8/K)-2) + 8 + 8,
```

hence

```text
C8/K ~= P^1.
```

Each `s_j` fixed-point set breaks into four `K`-orbits, so the quotient has exactly

```text
4 branch values of type s1,
4 branch values of type s2,
```

all with inertia order two.

The `K`-equivariant etale map `Z->C8` descends to

```text
phi_2 : E=Z/K -> C8/K ~= P^1
```

of degree

```text
n=28l.
```

Over any of the eight branch values, let

```text
u_q = number of unramified points of phi_2,
r_q = number of simple ramification points.
```

Etaleness upstairs and quotient stabilizers give only the two local possibilities, so

```text
u_q + 2 r_q = 28l.                       (A1)
```

Since `E` has genus one, Riemann--Hurwitz gives

```text
sum_q r_q = 2n = 56l.                    (A2)
```

Summing `(A1)` over the eight values yields

```text
sum_q u_q = 112l.                        (A3)
```

The uniform packet contains exactly `112l` distinct supported odd/minimal normalization branches.  A branch of type `s_j` gives an unramified point of `phi_2` over a branch value of type `s_j`: its stabilizer downstairs and upstairs is the same order-two group.  Distinct normalization branches give distinct points of `E`.

Thus the supported branches inject into a set of cardinality exactly `112l`; hence they exhaust it.

Consequently

```text
sum_(q of type s1) u_q = 56l,
sum_(q of type s2) u_q = 56l,            (A4)
```

and there are no other unramified points over the eight branch values.

For each q,

```text
0 <= u_q <= 28l,
u_q is even,
r_q=(28l-u_q)/2.
```

No stronger per-node divisibility of `u_q` is claimed.

## Case B: `e=4`

Now the component stabilizer has order eight, hence is the full group

```text
K=G ~= (Z/2)^3.
```

The three singular stabilizer involutions each have eight fixed points on `C8`; all three elements of `G0` are fixed-point-free.  Riemann--Hurwitz forces the fourth element of `G\G0` to be fixed-point-free and gives

```text
C8/G ~= P^1.
```

Each singular type contributes two branch values, so there are six order-two branch values in total.

The descended map is

```text
phi_4 : E=Z/G -> C8/G ~= P^1,
deg(phi_4)=56l.
```

For each of the six branch values,

```text
u_q + 2 r_q = 56l.                       (B1)
```

Riemann--Hurwitz on the genus-one domain gives

```text
sum_q r_q = 112l,
sum_q u_q = 112l.                        (B2)
```

Again the `112l` supported odd branches are unramified points over branch values of their own node type, so they exhaust the entire unramified capacity.

Because the support uses only `s1,s2`, with `56l` branches of each type, while the third singular type `s3` is absent,

```text
sum_(two s1 values) u_q = 56l,
sum_(two s2 values) u_q = 56l,
u_q=0 on both s3 branch values.           (B3)
```

Hence the two absent-type local monodromies are fixed-point-free involutions:

```text
r_q=28l
```

at each of the two `s3` values.

For the four used-type branch values,

```text
0 <= u_q <= 56l,
u_q is even,
r_q=(56l-u_q)/2,
```

with pair sums specified in `(B3)`.

## Group-action saturation upstairs

The same equality can be read directly on `Z`.

- If `e=2`, `g(Z)=112l+1`.  Each of `s1,s2` fixes exactly `112l` points of `Z`, while `h=s1s2` is free.  Their total fixed-point contribution is `224l=2g(Z)-2`, exactly the amount required by the `K`-quotient of genus one.
- If `e=4`, `g(Z)=224l+1`.  Each of `s1,s2` fixes exactly `224l` points of `Z`; all other nontrivial elements of `G` act freely on `Z`.  The total fixed contribution is `448l=2g(Z)-2`, again exact.

Thus there is no hidden fixed-point slack available to create additional quotient ramification.

## Consequence

The `000707` realization problem has been reduced to two exact Hurwitz-capacity regimes:

```text
e=2: degree 28l genus1 cover of P1 with 8 involutory branch values,
     four values of each used node type,
     total unramified capacity 112l, fully occupied by the supported branches;

e=4: degree 56l genus1 cover of P1 with 6 involutory branch values,
     two values per singular type,
     the absent third type is forced fixed-point-free in monodromy.
```

Neither numerical passport is contradictory by itself.  The next lever must use the **equivariant lift to the etale correspondence `Z->C8`**, not just coarse Riemann--Hurwitz counts.

## Firewalls

- No assertion that all `8l` branches at one box node land over one quotient branch value.
- No unsupported `u_q` divisibility by `8l` is used.
- Both `e=2` and `e=4` remain open.
- No actual carrier or etale correspondence is constructed.
- No surviving orbit is closed; MB104/receiver/theorem/endpoint credit remains zero.
- No merge authorization.
