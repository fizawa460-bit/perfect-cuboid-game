# Stage32 MB104 — `000707000f0f` e=2 etale base-change determinant passport

Status: **RETAINED CANDIDATE ETALE-BASECHANGE MONODROMY REFINEMENT / DETERMINANT RESIDUAL DISCREPANCY FORCED ZERO / NEW BRANCH-COUNT PARITY CONSTRAINTS / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Assume conditionally that the retained dangerous packet is realized in the `e=2` case.  Keep

```text
H=<T',TT'R> ~= (Z/2)^2,
R=C8/H ~= P1_r,
T H in G/H,
T:r->-r,
```

and let

```text
psi_i:E->R,
f_i:Z->C8,
i=1,2,
```

be the two quotient/product projections.  The retained equality-rigidity geometry gives

```text
deg psi_i = deg f_i = n=28l,
g(E)=1,
f_i etale.
```

The purpose here is to convert the etaleness of `f_i` into an exact branch-cycle passport for `psi_i` and then compute the determinant line

```text
epsilon_i=det((f_i)_*O_Z) in J(C8)[2].
```

## 1. `Z` is the normalization of the one-factor base change

Because `H` is the component stabilizer in the `e=2` case,

```text
E=Z/H.
```

The product projection `f_i:Z->C8` is `H`-equivariant, so it descends to `psi_i:E->R=C8/H`.  Hence there is a natural finite map

```text
Z -> E x_R C8.
```

Generically both sides have degree `|H|=4` over `E`, and `Z` is normal and connected.  Therefore

```text
Z = Norm(E x_R C8).                              (BC)
```

for each factor projection.

## 2. The eight branch values of `C8->R`

Use the retained one-factor model

```text
u^2=(r^4+4)/4,
v^2=(r^4-4)/4,
T'   :(r,u,v)->(r,u,-v),
TT'R :(r,u,v)->(r,-u,v).
```

Thus the degree-four `H` quotient

```text
pi_H:C8->R
```

has exactly eight order-two branch values:

```text
r^4=4   (four T'-type values),
r^4=-4  (four TT'R-type values).
```

The residual involution `T` pairs them by

```text
r <-> -r.
```

Choose constants

```text
a^2=2,
b=i*a,
u0^2=2i,
v0=2/u0.
```

Then the four residual pairs are

```text
{+a,-a}, {+b,-b}, {+u0,-u0}, {+v0,-v0}.        (PAIRS)
```

The first two have `r^4=4`; the last two have `r^4=-4`.

## 3. Etaleness of `f_i` forces a simple eight-value passport for `psi_i`

Away from the eight branch values of `pi_H`, the base change `(BC)` is etale on the `C8` side.  Any ramification of `psi_i` there would survive in `f_i`, contradicting etaleness.  Hence `psi_i` is unramified away from the eight values.

At one branch value choose a local coordinate `t` on `R` with

```text
t=u^2
```

on `C8`.  If a point of `E` above it has local ramification index `m`, write

```text
t=v^m.
```

The normalization of `u^2=v^m` maps to the `u`-line with ramification index

```text
m/gcd(m,2).
```

Since `f_i` is etale, this index must be one.  Therefore

```text
m in {1,2}.                                      (SIMPLE)
```

So every ramification point of `psi_i` is simple and lies over one of the eight `H`-branch values.

Riemann--Hurwitz for the degree-`n` map from the elliptic curve `E` to `P1` gives total ramification

```text
sum ramification defects = 2n = 56l.
```

For a branch value `q`, let

```text
u_q = number of unramified points above q,
r_q = number of simple ramification points above q.
```

Then

```text
u_q+2r_q=n.                                      (FIBER)
```

Summing `(FIBER)` over all eight values and using `sum r_q=2n` gives

```text
sum_q nu_q = 8n-2(2n)=4n=112l.                 (UTOTAL)
```

## 4. The supported packet exhausts every unramified point over the eight values

The active packet has exactly

```text
14*(8l)=112l
```

distinct normalization branches at its fourteen supported nodes.

At a supported node the diagonal stabilizer is one of `T'` or `TT'R`.  The same order-two inertia acts on the source component and the corresponding factor point of `C8`; after quotienting both by `H`, the local inertia cancels.  Therefore each supported normalization branch is an **unramified** point of each `psi_i` above one of the eight values in `(PAIRS)`.

Their number equals the entire unramified budget `(UTOTAL)`.  Hence:

```text
the 112l supported branches are exactly all unramified points
of psi_i above the eight H-branch values.         (EXHAUST)
```

Every remaining point above those values is simply ramified.

## 5. Determinant of the etale pullback is the sign character

Over the complement of the eight branch values, `psi_i` is an ordinary degree-`n` covering with monodromy permutations.  By `(BC)`, `f_i` is its pullback to the corresponding unramified part of `C8`.

For a finite etale cover, `f_*O` is analytically locally a direct sum indexed by the sheets and its transition matrices are the sheet permutations.  Therefore

```text
det(f_*O)
```

is exactly the flat order-two line bundle defined by the **sign** of the permutation monodromy.

At a branch value `q`, the local permutation of `psi_i` is a product of `r_q` transpositions and `nu_q` fixed points.  Its sign bit is therefore

```text
b_q := r_q mod 2.
```

Since `n=28l` and `n/2=14l` is even, `(FIBER)` gives

```text
b_q = (nu_q/2) mod 2.                           (SIGN)
```

In particular every `nu_q` is even.

## 6. Residual `T` invariance forces the determinant discrepancy to zero

Fix one residual pair `{q,-q}` from `(PAIRS)`.  By `(EXHAUST)`, every unramified point in that pair is one of the supported branches.  At a fixed supported node all `8l` branches choose one of the two residual lifts `q` or `-q`.  Therefore, after summing over all supported nodes belonging to this residual pair,

```text
nu_q + nu_-q = 8l * m_q
```

for some integer `m_q>=0`.

Hence

```text
(nu_q+nu_-q)/2 = 4l*m_q == 0 mod 2.
```

Using `(SIGN)`,

```text
b_q=b_-q                                      (T-SIGN)
```

for all four residual pairs.

Thus the sign character on `R` is invariant under `T:r->-r`.  Pulling it to `C8` gives

```text
T^*epsilon_i = epsilon_i.                       (DET-T)
```

Consequently the residual determinant discrepancy from the preceding one-bit leaf is always the zero option:

```text
epsilon_i tensor T^*epsilon_i ~= O_C8,
O(F_i(TZ)-F_i(Z)) ~= O_C8.                      (ZERO-DIFF)
```

The distinguished class `kappa=tau1+tau5` is **not** realized by these determinant lines.

This is a route conclusion, not an `e=2` contradiction: the pointwise conductor residual-sheet character can remain nontrivial even when the determinant sign local system is `T`-invariant.

## 7. The determinant class actually lies in a two-bit base-character subspace

A `T`-invariant sign character on the eight punctures is specified by four bits, one for each residual pair in `(PAIRS)`.  Pullback to `C8` is unchanged if the base character is multiplied by a character of the deck group `H`.

The two independent characters of

```text
H=<T',TT'R>
```

toggle simultaneously the two residual pairs of the corresponding inertia type.  Therefore the pulled-back determinant class is determined by only two pair-difference bits:

```text
d_+ = b_(+/-a pair) + b_(+/-b pair),
d_- = b_(+/-u0 pair) + b_(+/-v0 pair).          (DET2)
```

Thus the determinant lines arising from this e=2 base-change geometry occupy at most four classes inside the previously computed 32-element group `J(C8)^G[2]`.

The exact node table sharpens this separately for the two projections.

### First factor

The residual pairs receive supported nodes as

```text
{+/-a}: P0,P1,P2,P3,
{+/-b}: P24,P25,P26,
{+/-u0}: P8,P9,P10,P11,P32,P33,P34,
{+/-v0}: none.
```

The retained Q1 saturation equation gives

```text
x8+x9+x10+x11+x32+x33+x34=28l,
```

so the `u0` sign bit is zero and the `v0` bit is zero.  Hence the first-factor determinant has only one unresolved base-character bit:

```text
d_-(f1)=0,
d_+(f1)=((x0+x1+x2+x3+x24+x25+x26)/2) mod 2.   (F1BIT)
```

### Second factor

For the second factor the first-type pair is completely saturated:

```text
nu_(+a)=28l,
nu_(+b)=0,
```

by the retained Q0 equation, so

```text
d_+(f2)=0.
```

The remaining bit is

```text
d_-(f2)
 =((x8-x9+x10-x11-x32+x33-x34)/2) mod 2.       (F2BIT)
```

The numerator is even by the retained Q1 total equation.

No equality between `(F1BIT)` and `(F2BIT)` is claimed.

## 8. New parity constraints on the branch allocations

Because every `nu_q` is even, the node table gives two independent parity conditions beyond the integer saturation equations:

```text
x0+x1+x2+x3 == 0 mod 2,                        (PAR0)
x8+x9+x10+x11 == 0 mod 2.                     (PAR1)
```

The complementary three-node sums are then also even by the retained seven-node saturation equations.

The balanced formal allocation `x_j=4l` satisfies `(PAR0)/(PAR1)`, so these congruences do not close `e=2`.  They are retained because any future conductor-preimage enumeration must satisfy them.

## Route consequence

The hoped-for implication

```text
nontrivial determinant residual bit
 -> pointwise conductor residual-sheet parity
```

cannot be used here: the determinant residual bit is forced to zero by the exact etale base-change passport.

The remaining live object is still the singular-curve conductor/gluing character itself.  Future work should use the exact branch-cycle passport and congruences `(PAR0)/(PAR1)` as constraints, but must not identify them with the weighted conductor cut without a separate gluing adapter.

## Firewalls

- `T^*epsilon_i=epsilon_i` does not imply that every conductor pair is same-sheet.
- Determinant monodromy records only the sign of the factor-cover permutation representation; it does not recover the full conductor gluing character.
- The at-most-four determinant classes are not asserted to be all realized.
- `(PAR0)/(PAR1)` are necessary congruences only.
- No weighted-cut upper bound is proved.
- No e=2 closure is claimed.
- e=4 and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
