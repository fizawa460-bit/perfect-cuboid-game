# Stage32 MB104 — `000707000f0f` e=2 generalized-Jacobian gluing character

Status: **RETAINED EXACT NORMALIZATION-KERNEL REDUCTION / RESIDUAL Pic0 CHARACTER SEPARATED FROM CONDUCTOR GLUING / e=2,e=4 OPEN / NO CREDIT**

## Scope

Continue the dangerous equality packet and the retained `e=2` split-normalization case.  Let

```text
nu:E -> C
```

be the normalization of the hypothetical carrier and let

```text
pi:Y -> S
```

be the absent-type double cover defined by the half-class `L_abs`, branched along `B_abs`.

The carrier is disjoint from `B_abs`, so on `C` the restricted double cover is etale.  Put

```text
M := O_C(L_abs|_C).
```

Because `2L_abs ~ B_abs` and `B_abs|_C=0`,

```text
M^2 ~= O_C.
```

The preceding one-factor leaf identifies

```text
nu^*M = eta = O_E(L_abs|_E) in Pic^0(E)[2].
```

Hence

```text
e=2 <=> nu^*M ~= O_E.
```

This leaf identifies the information that remains after that normalization pullback becomes trivial.

## 1. The missing class lives in the normalization kernel

In the `e=2` case, `M` is not forced to be trivial on the singular curve `C`.  It is only forced into

```text
K_C[2] := Ker(Pic(C)[2] -> Pic(E)[2]).
```

Thus there are two distinct questions:

```text
normalization character: eta = nu^*M,
conductor/gluing character: kappa = class of M in K_C[2] when eta=0.
```

The retained Hodge argument is sensitive to the second datum.  Indeed the normalization of `pi^{-1}(C)` splits into two copies of `E`, while the two corresponding irreducible lifted components may still meet over singular points of `C` because the descent identifications across the conductor can exchange the two sheets.

Therefore

```text
eta=0
```

does **not** imply that the etale double cover of the singular carrier is the disconnected trivial cover.

## 2. Standard normalization-Picard source lock

The required distinction is standard in the Picard theory of singular curves.

For a normalization factorization built from elementary glueing and squishing steps, Stacks Project, Algebraic Curves, Section 53.15 gives:

- glueing two points on the same connected proper component contributes a multiplicative kernel `k^*` to the Picard map;
- squishing a tangent vector contributes an additive kernel `(k,+)`.

See:

```text
Stacks Project, Lemma 53.15.5, tag 0C1M
https://stacks.math.columbia.edu/tag/0C1M

Stacks Project, Lemma 53.15.6, tag 0C1N
https://stacks.math.columbia.edu/tag/0C1N
```

Over characteristic zero, `(k,+)` has no nontrivial 2-torsion, while the multiplicative glueing factor has the sign subgroup

```text
mu_2={+1,-1}.
```

The torsion bookkeeping is summarized in Stacks Project, Section 53.17, tag `0C1Y`.

Thus a 2-torsion class that becomes trivial on the normalization is carried by multiplicative conductor/glueing data, not by the smooth Jacobian of `E` and not by tangent-squishing data.

## 3. Local sign shadow and the retained cross-sheet cut

Fix a trivialization of `nu^*M` in the `e=2` case.  At a singular point `p` of `C`, write the reduced normalization branches as

```text
beta_1,...,beta_r.
```

The conductor descent datum compares the chosen trivialization on these branches.  Its `mu_2` shadow gives labels

```text
epsilon_i in {0,1}.
```

Changing the global trivialization of `nu^*M` flips every label simultaneously and therefore does not change any pairwise cut.

For local branch intersections

```text
I_ij = I_p(beta_i,beta_j),
```

the previous cross-sheet leaf proved

```text
delta_cross,p
 = sum_(i<j, epsilon_i != epsilon_j) I_ij,

y = 2 sum_p delta_cross,p.                    (CUT)
```

Consequently `y` is controlled by the **weighted sign shadow of the singular-curve gluing class `kappa`**.  The smooth-normalization class `eta` only decides whether this gluing problem is reached; it does not determine the cut once `eta=0`.

## 4. Hodge becomes a lower bound on the gluing-character cut

The retained `e=2` Hodge inequality is

```text
y >= 168l^2.
```

Using `(CUT)`, this is exactly

```text
sum_p delta_cross,p >= 84l^2.                (GLUE-HODGE)
```

Thus any `e=2` realization must carry a normalization-kernel two-torsion class whose conductor sign shadow has weighted cut at least `84l^2`.

This is sharper than the statement `eta=0`: it names the singular Picard datum that has to support the quadratic cross-sheet mass.

## 5. Why Pic0(E)[2] and kernel rank alone cannot upper-bound the cut

The normalization-kernel description also explains the previous wall.

A multiplicative glueing step contributes one `k^*`, and its 2-torsion contributes one sign bit.  A single global `Z/2` character may be nontrivial on many conductor identifications; the number of available sign generators does not give a bound on the **intersection-weighted support** of that character.

Likewise, the arithmetic defect budget

```text
Delta(C)=168l^2+56l
```

is already quadratic.  The standard Picard normalization sequence therefore supplies no coefficient `<1/2` for the cross-sheet part merely from the existence or dimension of `K_C[2]`.

In the nodal/multicross specialization this is the familiar dual-graph picture: the multiplicative normalization kernel is the toric gluing part, and its `2`-torsion is a `Z/2` graph character.  For the present carrier, whose singularities are not assumed nodal, only this interpretation is used as a specialization; the retained statement is the normalization-kernel/conductor formulation above.

## 6. Route consequence

The following standalone route is exhausted:

```text
eta=0 in Pic^0(E)[2]
  => control the cross-sheet cut using only smooth-Jacobian data.
```

It loses exactly the conductor/gluing character that creates `C_1.C_2`.

A successful continuation must compute or constrain

```text
kappa in Ker(Pic(C)[2] -> Pic(E)[2])
```

for the **specific surface line bundle**

```text
M=O_C(L_abs|_C),
```

and then bound the weighted cut of its local sign shadow.  Equivalent useful inputs include:

- an explicit conductor normalization sequence for the `000707` carrier with the restriction of `L_abs` tracked through it;
- a modular/commensurator description of the descent signs at conductor branches;
- a global relation forcing most high-intersection branch pairs to have the same sign;
- a singular-Picard or generalized-Jacobian computation that evaluates `M` before pullback to `E`.

The next target is therefore not another calculation in `Pic^0(E)[2]`; it is the singular-curve gluing class and its weighted support.

## Firewalls

- No claim is made that `K_C[2]` is a pure dual-graph group for arbitrary singularities of `C`.
- The dual-graph formulation is invoked only for the nodal/multicross specialization.
- No upper bound for `y` is proved here.
- No `e=2` or `e=4` closure is claimed.
- `000707000f0f` remains open.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104/span5/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No merge authorization.
