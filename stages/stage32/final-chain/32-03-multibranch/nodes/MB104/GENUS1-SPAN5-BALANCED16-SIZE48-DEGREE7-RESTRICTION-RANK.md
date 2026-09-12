# Stage32 MB104 — primitive degree-7 restriction rank on the two size-48 balanced orbits

Status: **RETAINED EXACT FINITE-FIELD LOWER-BOUND CERTIFICATE / ZERO QUARTICS NONFIXED ON BOTH SIZE-48 ORBITS / UNIFORM ALL-l CONSEQUENCE / BALANCED16 OPEN / MB104 INCOMPLETE / NO CREDIT**

## Goal

The surviving size-48 support orbits are

```text
0000770000ff,
00007b0000ff.
```

Each has four zero-pairing elliptic quartics.  The previous null-union leaf proves that their strict transforms are pairwise disjoint and that

```text
O_Q(D_l) ~= O_Q
```

on each component, but it does not decide the global restriction map.

Because

```text
D_l = l*A,
A = 7H - 4 sum_(i in Sigma) E_i,
```

it is enough to prove nonzero restriction at `l=1`: if `s in H^0(S,O(A))` restricts nontrivially to `Q`, then `s^l` restricts nontrivially for every `l>=1`.

## Canonical degree-7 model

On the canonical model the coordinate ring is

```text
R = k[a1,a2,a3,b1,b2,b3,c]/(q1,q2,q3,q4),
```

with

```text
b3^2=a1^2+a2^2,
b1^2=a2^2+a3^2,
b2^2=a1^2+a3^2,
c^2 =a1^2+a2^2+a3^2.
```

The four leading monomials `b1^2,b2^2,b3^2,c^2` are pairwise coprime, so the displayed quadrics form a Groebner basis for a compatible term order.  A degree-7 basis is therefore given by monomials in which each of `b1,b2,b3,c` has exponent at most one.  Its cardinality is exactly

```text
h^0(bar S,O_barS(7)) = 344.
```

## Four-jet condition at an A1 node

The minimal resolution of an A1 point is the blowup of its maximal ideal and

```text
m_p O_S = O_S(-E_p).
```

Consequently a degree-7 section represents a section of

```text
A = 7H - 4 sum_(p in Sigma) E_p
```

iff its local class lies in `m_p^4` at every supported node.

For a projective affine patch at a box node, translate the six affine coordinates to the node and truncate at total local degree `<4`.  There are

```text
1+6+21+56 = 84
```

ambient truncated monomials.  Multiplying the four translated surface quadrics by local monomials as needed through degree three gives a relation space of rank `68`, hence

```text
dim O_(bar S,p)/m_p^4 = 84-68 = 16,
```

as expected for an A1 singularity.

The verifier performs this local quotient construction directly; no pre-tabulated jet matrix is imported.

## Good finite-field specialization

Use

```text
p=1097,
i -> 341,
341^2 = -1 mod 1097.
```

This is odd good characteristic for the displayed complete intersection and the exact 48-node model remains separated.  The local four-jet quotient has dimension `16` at every node used by the two supports.

The verifier builds the `224 x 344` four-jet evaluation matrix for each 14-node support.  In both cases the exact modular rank is

```text
rank_p(jet)=220.
```

A nonzero minor modulo a good prime remains nonzero in characteristic zero, so

```text
rank_0(jet) >= 220,
h^0(S,O(A)) <= 344-220 = 124.
```

On the other hand the retained null-union cohomology wall gives, on each size-48 support,

```text
chi(O(A))=120,
H^2(O(A))=0,
h^1(O(A))>=4.
```

Therefore

```text
h^0(O(A))>=124.
```

Combining the two bounds gives the exact characteristic-zero values

```text
h^0(O(A))=124,
h^1(O(A))=4,
rank_0(jet)=220.
```

## Restriction rank is positive

For the four quartics

```text
Q_(s,t): b1=0, a2+s*i*a3=0, a1+t*c=0,
s,t in {+1,-1},
```

the verifier chooses one smooth finite-field point away from the 48 box nodes on each component and appends the four evaluation rows to the jet matrix.

For both size-48 support representatives:

```text
rank_p(jet + four component evaluations) = 222.
```

Thus the corresponding characteristic-zero augmented map has rank at least `222`.  Since the characteristic-zero jet rank is exactly `220`, the restriction map

```text
H^0(S,O(A)) -> H^0(Z_4,O_Z4(A)) ~= k^4
```

has rank at least `2`; in particular it is nonzero.

The retained support-stabilizer certificate says that the stabilizer is transitive on the four zero quartics and that individual fixedness is all-or-none.  A nonzero total restriction therefore implies that **every one of the four zero quartics is nonfixed** on each size-48 support orbit.

## All multiples

For every zero quartic `Q`, choose a primitive section `s` with `s|_Q != 0`.  Since `O_Q(A)` is trivial, `s|_Q` is nowhere zero.  Hence for every `l>=1`,

```text
(s^l)|_Q != 0
```

as a section of `O_Q(lA)=O_Q(D_l)`.

Therefore none of the zero quartics is a fixed component of `|D_l|` for **any** `l>=1` on either size-48 orbit.

## Consequence

The zero-quartic fixed-component route is completely removed for the two size-48 balanced support orbits.  They remain open for a different reason: an effective irreducible normalization-genus-one member with the required singularity/conductor packet is not constructed or excluded.

The size-768 survivor `000707000f0f` is not claimed by this certificate.  Its modular primitive calculation is deliberately left outside the retained claim because the present cohomological lower bound there is only `h^1(A)>=3`, which is insufficient to identify the characteristic-zero jet rank from the same one-prime calculation.

## Firewalls

- This is a nonfixedness result, not an existence proof for an irreducible genus-one carrier.
- No support orbit is closed by this leaf.
- No conclusion is made for `000707000f0f`.
- Arbitrary unequal exceptional coefficients remain open.
- Whole span5, MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain open/zero.
- No merge authorization.
