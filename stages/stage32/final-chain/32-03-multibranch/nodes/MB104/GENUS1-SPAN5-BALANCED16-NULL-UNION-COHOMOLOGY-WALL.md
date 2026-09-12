# Stage32 MB104 — surviving balanced16 null-union cohomology wall

Status: **RETAINED EXACT NEGATIVE ROUTE / SIZE-48 FOUR-QUARTIC UNION DISJOINT / 000707 CONNECTED UNION TRIVIAL / BALANCED16 OPEN / MB104 INCOMPLETE / NO CREDIT**

## Scope

Work only with the surviving uniform genus-one support-span-five ray

```text
D_l = 7l H - 4l sum_{i in Sigma} E_i,  |Sigma|=14,  l>=1,
```

after the retained two-quartic gluing obstruction has removed the size-768 orbit `00070b000f0f`.

The surviving support orbits are

```text
0000770000ff   size 48,
00007b0000ff   size 48,
000707000f0f   size 768.
```

The previous Pic^0 leaf proves `O_Q(D_l) ~= O_Q` for every zero-pairing retained elliptic quartic `Q`.

## 1. The four zero quartics on each size-48 support are pairwise disjoint on the resolution

For the incidence-16 size-3 ambient orbit, the representative hyperplane is `b1=0`.  The retained section factorization is

```text
q2 = (a2+i*a3)(a2-i*a3),
q4-q2 = (a1-c)(a1+c)
```

on `b1=0`.  Hence the four reduced elliptic quartics can be indexed by

```text
Q_(s,t):
  b1=0,
  a2+s*i*a3=0,
  a1+t*c=0,
  s,t in {+1,-1}.
```

Consider two distinct members.

### Same `s`, opposite `t`

Their common points satisfy

```text
a1=c=b1=0,
a2+s*i*a3=0.
```

The remaining surface equations give exactly four box nodes.  Near any such node put

```text
x=a1-c,
z=a1+c,
y=b1.
```

The exact surface relation is

```text
q4-q2 = x*z + y^2 = 0.
```

The two quartics are the two local branches

```text
{x=0,y=0},
{z=0,y=0}.
```

On the minimal `A1` resolution these branches meet the exceptional curve at distinct points, so their strict transforms are disjoint.

### Same `t`, opposite `s`

Now their common points satisfy

```text
a2=a3=b1=0,
a1+t*c=0,
```

again giving exactly four box nodes.  Put

```text
x=a2+i*a3,
z=a2-i*a3,
y=b1.
```

Then

```text
q2 = x*z - y^2 = 0,
```

and the two quartics are again the two distinguished local branches.  Their strict transforms separate on the minimal `A1` resolution.

### Opposite `s` and opposite `t`

The combined linear equations force

```text
a1=c=a2=a3=b1=0.
```

Then `q1=q3=0` force `b3=b2=0`, so there is no projective point.  The two quartics are disjoint already on the canonical model.

Therefore the four strict transforms are pairwise disjoint:

```text
Z_4 = Q_1 disjoint_union Q_2 disjoint_union Q_3 disjoint_union Q_4.
```

This applies to both surviving size-48 support orbits because their complete zero-quartic sets are the same four section components and the support stabilizer is transitive on them.

## 2. Consequence: there is no four-component gluing monodromy obstruction

Each component restriction is trivial:

```text
O_Qj(D_l) ~= O_Qj.
```

Because `Z_4` is disconnected, no compatibility constant is imposed between distinct components.  Hence

```text
O_Z4(D_l) ~= O_Z4,
H^0(Z_4,O_Z4(D_l)) ~= k^4.
```

So the successful two-point cycle-monodromy mechanism that closed `00070b000f0f` has no analogue on either size-48 orbit.  The four-quartic union alone does **not** force any of the four quartics to be fixed.

This is a negative route result, not a nonfixedness proof: the global restriction map

```text
H^0(S,O(D_l)) -> k^4
```

may still have rank `0,1,2,3,4`.

## 3. Exact speciality forced by the disconnected null union

Each zero quartic has

```text
Q_j^2=-4,
K_S.Q_j=4,
D_l.Q_j=0.
```

Since the four strict transforms are disjoint,

```text
Z_4^2=-16,
K_S.Z_4=16,
D_l.Z_4=0.
```

Riemann--Roch therefore gives

```text
chi(O(D_l-Z_4)) = chi(O(D_l)).
```

Also `H=K_S` is nef and

```text
H.(K_S-D_l+Z_4)=32-112l < 0
```

for every `l>=1`.  Thus `K_S-D_l+Z_4` is not effective and

```text
H^2(S,O(D_l-Z_4))=0.
```

From

```text
0 -> O(D_l-Z_4) -> O(D_l) -> O_Z4 -> 0
```

we obtain a surjection

```text
H^1(S,O(D_l)) -> H^1(Z_4,O_Z4) ~= k^4.
```

Consequently

```text
h^1(S,O(D_l)) >= 4
```

on each size-48 surviving support.

If `r_4` denotes the global restriction rank to `Z_4`, then

```text
h^0(D_l)=h^0(D_l-Z_4)+r_4,
h^1(D_l)=h^1(D_l-Z_4)+r_4,
0<=r_4<=4.
```

Riemann--Roch alone does not determine `r_4`.

## 4. The surviving size-768 orbit has the analogous connected speciality wall

For `000707000f0f`, the retained pair `Q0,Q1` meets transversely at two smooth points and the previous exact gluing calculation proves

```text
O_(Q0 union Q1)(D_l) ~= O_(Q0 union Q1).
```

Put `Z_2=Q0+Q1`.  Since `Q0.Q1=2`,

```text
Z_2^2=-4,
K_S.Z_2=8,
D_l.Z_2=0,
p_a(Z_2)=3.
```

Hence

```text
chi(O(D_l-Z_2)) = chi(O(D_l))+2,
H^0(Z_2,O_Z2)=k,
H^1(Z_2,O_Z2)=k^3.
```

Moreover

```text
H.(K_S-D_l+Z_2)=24-112l<0,
```

so `H^2(D_l-Z_2)=0`.  Therefore

```text
H^1(D_l) -> H^1(O_Z2)
```

is surjective and

```text
h^1(D_l)>=3.
```

Again this does not decide whether the restriction rank `H^0(D_l)->H^0(O_Z2)=k` is zero or one.

## Retained consequence

The complete null-union gluing route is now exhausted on all three surviving uniform-ray support orbits:

- `0000770000ff`: four zero quartics are disjoint; no gluing monodromy;
- `00007b0000ff`: four zero quartics are disjoint; no gluing monodromy;
- `000707000f0f`: two zero quartics form a connected two-cycle, but the exact monodromy is `1`.

The next lever must be genuinely global: a restriction-rank computation, global degree-`7l` jet/interpolation constraint, conductor/singularity inequality, or a whole-null-locus semiampleness/effective-cone theorem.

## Firewalls

- No surviving orbit is closed by this leaf.
- No zero quartic is proved nonfixed on a surviving orbit.
- No irreducible genus-one carrier is constructed.
- Arbitrary unequal Picard coefficients remain open.
- Whole support-span five, MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain open/zero.
- No merge authorization.
