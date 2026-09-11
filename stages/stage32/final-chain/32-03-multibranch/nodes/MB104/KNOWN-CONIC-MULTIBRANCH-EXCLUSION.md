# Stage32 MB104 — known 32 plane conics are not multibranch carriers

Status: **RETAINED EXACT ADAPTER / NO RECEIVER CREDIT**

## Source lock

Michael Stoll's verification source constructs the 32 known `a`-conics as `C1s` in

```text
repository = MichaelStollBayreuth/Verification
commit     = 51233ed5ef2bf228fac9416c66db9adc0ebcaadd
path       = Cuboids/cuboids.magma
blob_sha1  = 0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

The same 32 curves are the van Luijk plane conics appearing as the exceptional genus-zero family in BTVA Theorem 1.2.

## Representative calculation

Take the first source family

```text
a1 = 0,
a2 = -e1*b3,
a3 = -e2*b2,
b1 = -e3*c,
```

with `e1,e2,e3 in {+1,-1}`. Substitution into the box-surface quadrics reduces all nontrivial equations to

```text
b2^2 + b3^2 - c^2 = 0
```

inside the projective plane with coordinates `(b2:b3:c)`.

Its gradient is

```text
(2*b2, 2*b3, -2*c),
```

which cannot vanish at a projective point in characteristic zero. Hence this plane conic is smooth and geometrically integral. The other three eight-element source families are obtained by the same coordinate/sign symmetries and have the same conclusion.

Therefore all 32 known plane conics are smooth curves.

## Normalization consequence

For a smooth integral curve `C`, the normalization map

```text
nu: C_tilde -> C
```

is an isomorphism. Consequently, for every surface point `P` on one of these conics,

```text
# nu^{-1}(P) = 1.
```

In MB101 notation this means every met box node has

```text
r_i=1.
```

Thus none of the known 32 plane conics satisfies the multibranch receiver condition

```text
exists i with r_i>=2.
```

## MB104 consequence

BTVA Theorem 1.2 states that every genus-zero curve other than these 32 conics passes through at least seven nodes spanning `P^6`. Since the 32 conics are now excluded from `R29-LG2-MB`, every geometric-genus-zero multibranch carrier necessarily satisfies

```text
N>=7,
dim span(Sigma(D))=6.
```

This removes the only BTVA genus-zero exception from the multibranch population. It does not give a canonical-degree upper bound in the remaining full-span sector.

## Firewalls

This is a population adapter only. It does not discharge `R29-LG2-MB`, prove MB104 finite degree, release MB105, or grant receiver/effectivity/theorem/endpoint/Perfect-Cuboid/merge credit.
