# Stage32 MB104 — `000707000f0f` primitive rank and zero-quartic nonfixedness

Status: **RETAINED EXACT PRIMITIVE DIMENSION / ZERO QUARTICS NONFIXED FOR ALL MULTIPLES / UNIFORM-P5 BALANCED CORE STILL OPEN / MB104 INCOMPLETE / NO CREDIT**

## Scope

This leaf treats only the surviving balanced support orbit represented by

```text
Sigma = 000707000f0f,
|Sigma|=14,
A = 7H - 4 sum_(p in Sigma) E_p,
D_l=lA, l>=1.
```

The two retained zero-pairing elliptic quartics are

```text
Q0: b1=0,  i*a2-a3=0,  a1-c=0,
Q1: b2=0,  i*a3+a1=0,  a2-c=0.
```

Previous leaves prove `O_Qj(A) ~= O_Qj`, the two quartics form one support-stabilizer orbit, and the connected two-quartic gluing line bundle is trivial.  They did not decide the global restriction rank.

## 1. Canonical degree bases and jet lengths

Use

```text
R = Q(i)[a1,a2,a3,b1,b2,b3,c]/(q1,q2,q3,q4)
```

with leading monomials `b1^2,b2^2,b3^2,c^2`.  Normal degree-`d` monomials therefore have exponent at most one in `b1,b2,b3,c`.

The verifier recomputes

```text
dim R_7 = 344,
dim R_6 = 248.
```

At every supported A1 node, order-four vanishing means membership in `m_p^4`; the local quotient has length `16`.  Order-three vanishing has quotient length `9`.

All modular rank computations use the good specialization

```text
p=1097,
i -> 341,
341^2=-1 mod 1097.
```

## 2. Degree six with triple vanishing is exactly 122-dimensional

Put

```text
C = 6H - 3 sum_(p in Sigma) E_p.
```

The exact `14*9 x 248 = 126 x 248` triple-jet matrix has modular rank

```text
rank_1097 = 126.
```

Hence its characteristic-zero rank is at least `126` and

```text
h0(C) <= 248-126 = 122.
```

On the resolved cuboid surface

```text
H^2=16,
K=H,
chi(O_S)=8,
E_p^2=-2.
```

Therefore

```text
C^2=324,
K.C=96,
chi(O(C))=8+(324-96)/2=122.
```

Also `H.(K-C)=16-96<0`; since `H` is nef, `K-C` is not effective, so `h2(C)=0`.  Riemann--Roch gives `h0(C)>=122`.  Thus

```text
h0(C)=122,
h1(C)=0.
```

## 3. The support hyperplane gives a 122-dimensional subspace of `H0(A)`

The canonical support lies in

```text
L = c-a1-a2-i*a3 = 0.
```

The verifier checks `L(p)=0` at all fourteen support nodes.  Multiplication by `L` raises the local maximal-ideal order by at least one, so it maps the triple-vanishing degree-six space into `H0(A)`.

The full multiplication map

```text
R_6 --*L--> R_7
```

has rank `248` modulo `1097`.  Since `dim R_6=248`, it is injective in characteristic zero.  Hence the image of `H0(C)` contributes exactly `122` independent sections of `A`.

## 4. Two exact primitive sections outside the `L`-multiple subspace

The verifier contains two explicit Gaussian-integer degree-seven forms `F` and `G` with respectively `26` and `34` normal monomials.  It verifies over `Q(i)`, node by node, that their local classes lie in `m_p^4` at every `p in Sigma`.  Thus

```text
F,G in H0(S,O(A)).
```

The verifier then reduces multiplication by `L` and `F,G` modulo `1097` and obtains

```text
rank(span(L*R_6)) = 248,
rank(span(L*R_6,F,G)) = 250.
```

A nonzero minor modulo a good prime remains nonzero in characteristic zero.  Therefore the classes of `F` and `G` are independent modulo the full `L`-multiple subspace, and in particular independent modulo `L*H0(C)`.

Consequently

```text
h0(A) >= 122+2 = 124.
```

## 5. Exact primitive dimension

The verifier independently recomputes the degree-seven four-jet matrix for the fourteen supported nodes and finds

```text
rank_1097(jet_4)=220.
```

Hence in characteristic zero

```text
h0(A) <= 344-220 = 124.
```

Combining with the explicit lower bound gives

```text
h0(A)=124,
rank_Q(i)(jet_4)=220.
```

Riemann--Roch gives `chi(O(A))=120`, and `H.(K-A)=16-112<0` gives `h2(A)=0`, so

```text
h1(A)=4.
```

This resolves the one-dimensional ambiguity left by the earlier one-prime calculation.

## 6. Exact nonzero restriction to `Q0`

Under

```text
Q0: b1=0, a3=i*a2, c=a1,
```

the explicit section `F` has the nonzero normal form

```text
2*a2^7
+ 2*a2^6*b3
- a1^2*a2^4*b3
+ 2*i*a2^6*b2
+ i*a1^2*a2^4*b2
+ 2*i*a2^5*b2*b3.
```

Therefore `F|Q0` is not identically zero.  Since the retained Picard calculation gives `O_Q0(A) ~= O_Q0`, this proves that `Q0` is not fixed in `|A|`.

The support stabilizer is transitive on `{Q0,Q1}` and preserves `A`, so `Q1` is also nonfixed.

For every `l>=1`, a primitive section nonzero on a given zero quartic remains nonzero after taking its `l`-th power.  Hence

```text
Q0 and Q1 are nonfixed in |D_l| for every l>=1.
```

## Consequence

Together with the retained size-48 primitive-rank leaf, every zero-pairing quartic on all three surviving balanced support orbits

```text
0000770000ff   size 48,
00007b0000ff   size 48,
000707000f0f   size 768
```

is now proved nonfixed for every `l>=1`.

Thus the zero-quartic fixed-component/restriction route is completely exhausted on the surviving `864` uniform-ray supports.  The remaining problem is genuinely global: determine whether an integral normalization-genus-one member of `|D_l|` with the required singularity/conductor packet can exist.  Lu--Miyaoka already forces at least `max(0,112l-224)` ordinary nodes/triples for any such hypothetical member.

## Firewalls

- Nonfixedness of the known zero quartics does not construct an irreducible genus-one carrier.
- No surviving support orbit is closed by this leaf.
- Arbitrary unequal exceptional coefficients remain open.
- Whole support-span five, genus-one P6, genus-zero P6, MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain open/zero.
- No merge authorization.
