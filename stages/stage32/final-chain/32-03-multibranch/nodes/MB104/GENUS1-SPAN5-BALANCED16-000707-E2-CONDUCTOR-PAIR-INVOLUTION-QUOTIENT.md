# Stage32 MB104 — `000707000f0f` e=2 conductor-pair involution quotient

Status: **RETAINED EXACT RELATIVE-SHEET RECEIVER / CONDUCTOR `0` VS `gamma_Q` BIT IS A CANONICAL ALGEBRAIC `mu_2` COORDINATE / POINTWISE EVALUATION STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The retained boundary has a residual degree-two cover on the complement of the absent divisor

```text
q:R_U -> U=S\B_abs,
```

with explicit Kummer generator

```text
r0^2 = h,
h=2*f_t,
tau(r0)=-r0.
```

For the active e=2 normalization there is a map

```text
psi:E -> R_U,
q o psi = phi:E -> C subset U,
```

and conductor-identified normalization points `x_i,x_j in E` satisfy

```text
phi(x_i)=phi(x_j)=p.
```

The open `U` is etale for the residual cover, so `h(p)` is a unit in an appropriate Kummer chart.

This note materializes the exact algebraic receiver for the remaining relative-sheet bit. It is inspired by the receiver-involution pattern of arsenal card `S35-PW02`, but no Stage35 source is load-bearing and no Stage35 credit is imported.

## 1. The double-cover pair receiver splits into two exact components

Over one Kummer chart write the two lifts over the same base point as

```text
r_i^2=h,
r_j^2=h.
```

Subtracting gives

```text
(r_i-r_j)(r_i+r_j)=0.                            (SPLIT)
```

Because the cover is etale on `U`, `h!=0`; in characteristic zero the two factors are disjoint on geometric fibres. Thus

```text
R_U x_U R_U
 = Delta  disjoint_union  Gamma_tau,

Delta     : r_j=r_i,
Gamma_tau : r_j=-r_i.                            (PAIR)
```

Equivalently, `Delta` is the same-sheet component and `Gamma_tau` is the deck-twisted component.

## 2. Canonical quotient coordinate

Define

```text
chi_ij := (r_i*r_j)/h.                           (CHI)
```

Using `r_i^2=r_j^2=h`,

```text
chi_ij^2=1,
chi_ij=+1 on Delta,
chi_ij=-1 on Gamma_tau.                          (VALUES)
```

The simultaneous residual deck involution acts by

```text
(r_i,r_j) -> (-r_i,-r_j),
```

and leaves `(CHI)` fixed. Interchanging `i,j` also leaves it fixed.

The coordinate is independent of the chosen Kummer generator. If on an overlap

```text
r0' = a*r0,
h'  = a^2*h
```

for an invariant unit `a`, then

```text
(r_i'*r_j')/h'=(r_i*r_j)/h.
```

Hence `chi_ij` is an intrinsic relative-position coordinate on the pair receiver; it is not a choice of square-root sign.

This is the exact order-two quotient/converse dictionary:

```text
chi_ij=+1  <=>  same residual lift,
chi_ij=-1  <=>  deck-twisted residual lift.      (IFF-SHEET)
```

## 3. Conductor pair map

Let `CondPair(C)` denote the reduced conductor branch-pair relation on the normalization: a point is a pair `(x_i,x_j)` of distinct normalization branches with the same image in `C`.

The maps above give a canonical morphism on the retained etale open

```text
Theta:
CondPair(C)
 -> R_U x_U R_U,
(x_i,x_j) |-> (psi(x_i),psi(x_j)).               (THETA)
```

Composing with `(CHI)` gives

```text
chi_C : CondPair(C) -> mu_2={+1,-1}.             (COND-CHI)
```

The remaining research problem is therefore no longer to define the relative sheet bit. It is to evaluate `(COND-CHI)` on the actual conductor pair relation of a hypothetical `000707` carrier.

The current retained data do not materialize `CondPair(C)` or the values of `psi` on its points, so no pointwise sign is asserted here.

## 4. Exact comparison with `0` and `gamma_Q`

The ambient-complement computation gives

```text
H_1(U,Z) ~= Z/2,
alpha_abs:H_1(U,Z)->F_2
```

as the unique nonzero character. The explicit zero-quartic union supplies the unique nonzero generator

```text
[gamma_Q] != 0,
alpha_abs(gamma_Q)=1.
```

For a conductor loop `lambda_(p;i,j)`, the retained ambient-monodromy identity is

```text
epsilon_i+epsilon_j
 = alpha_abs(lambda_(p;i,j)).                    (MON)
```

On the Kummer pair receiver, `r_i` and `r_j` have the corresponding signs, so

```text
chi_ij
 = (-1)^(epsilon_i+epsilon_j)
 = (-1)^alpha_abs(lambda_(p;i,j)).               (ALG-v-TOPO)
```

Since `H_1(U,Z)` has only two classes,

```text
chi_ij=+1
 <=> [lambda_(p;i,j)]=0,

chi_ij=-1
 <=> [lambda_(p;i,j)]=[gamma_Q].                 (EDGE-v-GEN)
```

This is the requested exact algebraic adapter between the conductor pair and the explicit ambient generator.

## 5. Weighted cut in algebraic pair coordinates

For local branch intersection multiplicities

```text
I_ij=I_p(beta_i,beta_j),
```

the cross-sheet indicator is exactly

```text
1_(opposite sheet) = (1-chi_ij)/2.
```

Therefore the retained conductor cut becomes

```text
delta_cross,p
 = sum_(i<j) I_ij*(1-chi_ij)/2,                  (CHI-CUT)

y/2
 = sum_p sum_(i<j) I_ij*(1-chi_ij)/2.            (GLOBAL-CHI-CUT)
```

The e=2 Hodge requirement is equivalently

```text
sum_p sum_(i<j) I_ij*(1-chi_ij)/2 >= 84*l^2.     (CHI-HODGE)
```

Thus any future explicit conductor calculation can work entirely algebraically with the pair-receiver coordinate `chi_ij`; no separate topological loop representative is required once `chi_ij` is evaluated.

## 6. Local consistency

At a singular point with branches `i,j,k`, the pair receiver automatically satisfies

```text
chi_ii=1,
chi_ij=chi_ji,
chi_ij*chi_jk=chi_ik.                            (COCYCLE)
```

These are identities of relative signs, not additional numerical pruning constraints. They simply prevent treating pair signs at one singular point as independent binary variables.

## 7. Relation to the requested arsenal weapons

`S35-PW02` is the correct reusable pattern: keep the full order-two receiver, quotient only after the involution is transported to the auxiliary square root, and retain an exact converse. Here `(PAIR)` and `(IFF-SHEET)` are that exact quotient/converse.

`S35-PW03` is not needed for this step: it restores existence of a rational source lift lost under quotienting, whereas the active e=2 case already has the normalization lift `psi:E->R_U`.

`S36-PW04` is useful only after a semantic change from a pointwise H1 lift-existence class to a relative Cech transition on a conductor pair. The resulting relative transition is exactly `chi_ij`; the pointwise lift class alone does not determine it.

These arsenal comparisons are routing provenance only. The retained result above depends only on the Stage32 source-locked residual Kummer cover, ambient character, generalized-Jacobian conductor semantics, and explicit `gamma_Q` generator.

## Next exact target

Materialize or constrain the map

```text
CondPair(C) -> R_U x_U R_U
```

for the `000707` carrier. Equivalent concrete targets are:

1. express `r_i*r_j/h(p)` from a source-locked local conductor equation;
2. compute the residual square-root transition on normalization-preimage charts;
3. prove that a specified class of high-intersection branch pairs lands in `Delta` or `Gamma_tau`;
4. derive a strict upper bound for `(GLOBAL-CHI-CUT)` below `84*l^2`.

Without one of these, the pair receiver is an exact adapter but not an e=2 contradiction.

## Firewalls

- No conductor pair is assigned `chi=+1` or `chi=-1`.
- No conductor loop is assigned `0` or `gamma_Q`.
- No branch allocation is claimed geometrically realizable.
- No weighted-cut upper bound is proved.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
