# MB104 Z45 — full-null-boundary Sabatino reoptimization — 2026-09-19

Status: **PRE-AUDIT EXACT ACTUAL-NULL-BOUNDARY THEOREM NO-GO / NO CREDIT**

## Setup

Let C be a hypothetical irreducible genus-one carrier in |lP| on one of the three surviving
balanced supports.

The complete null locus D is now known exactly, and C is disjoint from D.

Retained exact data:

```text
C^2=336l^2,
K.C=112l,
normalization genus(C)=1,
D.C=0,
e(C\D)=0,
e(S\D)=e(Y_reg)=16.
```

Sabatino Theorem 1.1(i) gives for alpha in [0,1]:

```text
F(alpha)
 = (alpha^2/2)[C^2+3(K+D).C+3e(C\D)]
   -2alpha[(K+D).C+(3/2)e(C\D)]
   +3e(S\D)-(K+D)^2
 >=0.
```

Since D.C=0,

```text
(K+D).C=112l.
```

## Size-48 supports

For either 0000770000ff or 00007b0000ff,

```text
D = 34 unsupported (-2)-curves + 4 elliptic (-4)-quartics.
```

The four quartics contribute K.D=16. The complete graph has four quartic-exceptional edges.

Hence

```text
D^2
 = 34(-2)+4(-4)+2*4
 = -76,

(K+D)^2
 = 16+2*16-76
 = -28.
```

Therefore

```text
F_48(alpha)
 = 168l(l+1)alpha^2
   -224l alpha
   +76.
```

The vertex is

```text
alpha_* = 2/[3(l+1)] in [0,1].
```

Thus

```text
min F_48
 = 76 - (224/3) l/(l+1)
 = 4(l+57)/[3(l+1)]
 > 4/3.
```

The margin tends monotonically to 4/3 as l grows.

So the actual complete null boundary makes the open-surface inequality nearly sharp, but it never
becomes negative.

## Size-768 support

For 000707000f0f,

```text
D = 34 unsupported (-2)-curves + A+B,
```

where A,B are elliptic (-4)-quartics, A.B=2, and two unsupported exceptional leaves attach one to
each quartic.

Hence

```text
K.D=8,

D^2
 =34(-2)+2(-4)+2*(A.B + two leaf edges)
 =-68,

(K+D)^2
 =16+16-68
 =-36.
```

Therefore

```text
F_768(alpha)
 =168l(l+1)alpha^2
  -224l alpha
  +84.
```

At the same vertex,

```text
min F_768
 =84-(224/3)l/(l+1)
 =28(l+9)/[3(l+1)]
 >28/3.
```

## Consequence

The exact actual-contraction boundary improves Z35 substantially but still does not exclude any
surviving orbit.

The key quantitative output is:

```text
size48 asymptotic theorem margin: 4/3,
size768 asymptotic theorem margin: 28/3.
```

Thus any source-valid strengthening of the same open-surface inequality would need to improve the
size-48 constant by more than 4/3 asymptotically to create a contradiction.

No such correction is imported here.

## Next leaf

The size-48 margin is small enough to justify one final shallow check:

```text
MB104-Z46-LOG-BOGOMOLOV-MIYAOKA-CORRECTION-PREFLIGHT
```

Target: determine whether a source-valid refinement of the open-surface inequality for the actual
Q-Gorenstein contraction contributes an additional local term at the two non-lc graph singularities
that has a known sign/magnitude exceeding 4/3. If only quotient/log-canonical local corrections are
available, freeze immediately.

## Firewalls

```text
size48_Sabatino_contradiction=false
size768_Sabatino_contradiction=false
finite_l_window=false
surviving_orbits_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
