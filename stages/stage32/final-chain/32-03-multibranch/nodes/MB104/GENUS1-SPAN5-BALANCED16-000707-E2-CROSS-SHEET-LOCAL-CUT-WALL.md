# Stage32 MB104 — `000707000f0f` e=2 cross-sheet local-cut wall

Status: **RETAINED EXACT LOCAL CUT FORMULA / PURELY LOCAL CONDUCTOR UPPER-BOUND ROUTE EXHAUSTED / e=2,e=4 OPEN / NO CREDIT**

## Scope

Continue the dangerous equality packet and assume the `e=2` split-normalization case from the retained Hodge/conductor leaf.

Let

```text
pi:Y->S
```

be the absent-type double cover.  The carrier `C` is disjoint from the branch divisor, so `pi` is etale in a neighborhood of `C`.  Write the two irreducible components of `pi^{-1}(C)` as

```text
C_1,C_2
```

and

```text
y=C_1.C_2.
```

The retained Hodge argument gives

```text
y >= 168l^2.                                  (H)
```

This leaf identifies `y` exactly in terms of the branch-intersection graph of the singular carrier and shows why a **purely local** conductor inequality cannot provide the required strict upper bound.

## 1. Local branch partition

Let `p` be a singular point of `C` on the smooth resolution surface `S`.  Write the reduced normalization branches as

```text
beta_1,...,beta_r.
```

For each branch let `delta_i` be its intrinsic unibranch delta invariant, and for `i<j` let

```text
I_ij = I_p(beta_i,beta_j)
```

be the local intersection multiplicity.  The standard reduced-curve formula is

```text
delta_p(C)
 = sum_i delta_i + sum_(i<j) I_ij.             (D)
```

Because the ambient double cover is etale near `p`, there are two points `p^+,p^-` over `p`, each with a locally identical copy of the curve germ.  In the globally split-normalization case, choose one normalization component.  Relative to the local sheet over `p`, each normalization branch receives a label

```text
epsilon_i in {0,1}.
```

At `p^+`, branches of one label belong to `C_1` and branches of the other label belong to `C_2`; at `p^-` the roles are exchanged.

Define the local cut weight

```text
delta_cross,p
 := sum_(i<j, epsilon_i != epsilon_j) I_ij.
```

## 2. Exact cross-sheet intersection formula

At `p^+`, the intersection multiplicity between `C_1` and `C_2` is exactly `delta_cross,p`.  The same is true at `p^-`.  Therefore

```text
y_p = 2 delta_cross,p.
```

Summing over all singular points of `C`,

```text
y = 2 sum_p delta_cross,p.                    (CUT)
```

Equivalently, with

```text
delta_cross := sum_p delta_cross,p,
```

we have

```text
delta_cross = y/2.
```

The complementary same-sheet defect is

```text
delta_same
 = sum_p [sum_i delta_i
          + sum_(i<j, epsilon_i=epsilon_j) I_ij],
```

so `(D)` gives the exact decomposition

```text
Delta(C)=delta_same+delta_cross.
```

This is the local form of the retained global identity

```text
Delta(C)=delta_same+y/2.
```

## 3. Hodge requirement in local-cut language

The Hodge lower bound `(H)` becomes

```text
delta_cross >= 84l^2.                         (HCUT)
```

Since

```text
Delta(C)=168l^2+56l,
```

the split case requires a macroscopic fraction of the total normalization defect to be carried by pairwise intersections of branches with opposite residual-sheet labels.

Explicitly,

```text
delta_cross/Delta(C)
 >= 84l^2/(168l^2+56l)
 = 3l/(6l+2),
```

which tends to `1/2` from below.

## 4. Sharp local upper bound and wall

From `(D)`, pointwise

```text
0 <= delta_cross,p <= delta_p(C).
```

The upper coefficient `1` is sharp even for the simplest reduced singularity.  For an ordinary node,

```text
r=2,
delta_1=delta_2=0,
I_12=1,
delta_p=1.
```

Assign the two branches opposite sheet labels.  Then

```text
delta_cross,p=1=delta_p.
```

Thus no universal local estimate depending only on the reduced singularity type, branch number, delta invariant, or pairwise branch intersections can improve the coefficient to

```text
delta_cross,p <= c*delta_p + O(local lower-order data)
```

with a uniform `c<1`.  In particular, purely local conductor theory cannot force the global ratio below the approximately `1/2` threshold required to contradict `(HCUT)` without some **additional global restriction on the allowed sheet labeling or singularity distribution**.

The same sharpness remains compatible with ordinary nodes, so the retained Lu--Miyaoka lower bound on the number of ordinary nodes/triple points does not supply the missing upper bound.

## 5. Route consequence

The active `e=2` problem is no longer a generic local-delta estimate.  A useful next input must constrain the sheet labels globally.  Natural possibilities are:

- the monodromy character of the intermediate modular double cover;
- the anti-invariant Neron--Severi lattice of the intermediate surface and the norm condition for a split divisor;
- a global conductor divisor relation tied to the modular fibrations;
- a commensurator/double-coset classification of the etale correspondence.

A local inequality that forgets the global residual character is structurally incapable of closing `e=2`.

## Firewalls

- No assertion that every singularity can simultaneously attain the local sharp example is made.
- No `e=2` or `e=4` closure is claimed.
- The result closes only the **purely local conductor upper-bound route** lacking global sheet information.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104/span5/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No merge authorization.
