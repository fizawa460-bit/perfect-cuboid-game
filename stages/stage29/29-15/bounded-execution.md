# Stage29-15 — mandatory bounded-receiver execution

This file implements the Stage29-15 rule that an OPEN receiver may not remain a vague AMBER merely because it is labelled finite or bounded.

The four execution classes are:

```text
1 EXECUTE_NOW_BOUNDED
2 CURRENT_TOOL_LIMIT_EXECUTED
3 NEW_THEOREM_REQUIRED
4 DORMANT_NONDECISIVE
```

Class 1 is transient: every class-1 receiver must be executed inside 29-15 and end as either `DISCHARGED` or `EXECUTED_NEGATIVE_LIMIT`. No class-1 receiver may be handed to 29-16 as pending work.

Precedence is endpoint-driven. A finite computation that has no current endpoint-decision or route-enabling consequence belongs to class 4, with an explicit reactivation trigger; mathematical finiteness alone does not justify spending the endpoint campaign on nondecisive bookkeeping. A theoretically finite computation that was already reduced to an infeasible current algorithmic wall belongs to class 2, not class 1.

## 1. R29-BEAU2A — executed and discharged

Prior audited state:

```text
R29-BEAU2A=SwapEquivarianceOfBeauvilleV4AlbaneseIsogenyKernel
STATUS=OPEN_BOUNDED
```

Beauville's cuboid specialization has

```text
C0 x C0 -> X_B=(C0 x C0)/Delta(Gamma) -> D x D,
Gamma ~= (Z/2)^2,
```

and the second map is the pullback of an etale V4 isogeny

```text
A_B -> J_D x J_D.
```

The deck group of `X_B -> D x D` is

```text
(Gamma x Gamma)/Delta(Gamma) ~= Gamma,
[(g,h)] |-> g h^{-1}.
```

Factor exchange `tau(p,q)=(q,p)` sends the deck class to

```text
[(g,h)] |-> [(h,g)]
g h^{-1} |-> h g^{-1} = (g h^{-1})^{-1}.
```

Every element of `Gamma` has order dividing two, so inversion is the identity. Therefore factor exchange acts trivially on the V4 deck group. In particular the corresponding V4 isogeny kernel is swap-stable. Functoriality of the Albanese map lifts factor exchange to `A_B` and covers exchange of the two `J_D` factors.

Consequently the Q(i)/Q swap descent used by Stage29-02d preserves the V4 isogeny kernel, and the twisted Albanese target descends exactly as anticipated:

```text
R29-BEAU2A=DISCHARGED_SWAP_EQUIVARIANT_V4_KERNEL
BEAUVILLE_V4_KERNEL_SWAP_STABLE=true
BEAUVILLE_V4_DECK_ACTION_UNDER_SWAP=TRIVIAL
DESCENDED_ALBANESE_Q_ISOGENY_TARGET=Res_{Q(i)/Q}(J_D,Q(i))
```

This is an adapter closure only. It does **not** prove a finite physical twist set, uniform Selmer closure, or endpoint nonexistence. `R29-BEAU2` and `R29-BEAU3` remain live theorem-level arithmetic receivers.

Primary provenance:
- `stages/stage29/29-02d/q-form-adapter.md`
- `stages/stage29/29-02d/albanese-bolza-target.md`
- Beauville, *A tale of two surfaces*, current tower/Albanese statement (current PDF Remark 2; the repository preserves the earlier locator history explicitly).

## 2. R29-KUM-LOC2-2 — executed and discharged

Prior audited state:

```text
R29-KUM-LOC2-2=OPEN_BOUNDED_TWO_ADIC_STATE_AUTOMATON
```

The seven branch forms are

```text
x, y, z, x+y, x+z, y+z, x+y+z.
```

A Q2 lift on the branch-avoiding locus requires the seven nonzero values to lie in one common Q2 squareclass. Branch hyperplanes themselves have Haar measure zero and do not affect the density.

### 2.1 Mod-2 state reduction

`P^2(F_2)` has seven primitive parity cylinders, all of equal normalized Haar mass `1/7`.

If two or three of `x,y,z` are odd, two odd branch values have the same squareclass only if their ratio is a unit square, but their sum has 2-adic valuation one. Hence no common-squareclass lift is possible.

Exactly three parity cylinders survive: those with a unique odd coordinate.

By symmetry take `y` odd, scale to `y=1`, and put

```text
X=x/y in 2 Z_2,
Z=z/y in 2 Z_2.
```

The conditions become that

```text
X, Z, 1+X, 1+Z, X+Z, 1+X+Z
```

are Q2-squares.

### 2.2 One-variable states

A nonzero Q2 number is a square iff its valuation is even and its odd unit is `1 mod 8`.

For `X in 2Z_2`, if `v2(X)=2`, then a square `X` has `X=4 mod 32`, so `1+X=5 mod 8` and is not a square. Therefore `X` and `1+X` are simultaneously squares exactly on states

```text
v2(X)=2a, a>=2,
odd-unit(X)=1 mod 8.
```

Conditional on `X in 2Z_2`, the mass of state `a` is

```text
w_a=2^(-2a-2),  a>=2,
sum w_a = 1/48.
```

The same holds for `Z`. For these states, `1+X`, `1+Z`, and `1+X+Z` are automatically unit squares because `X,Z` are divisible by 16.

### 2.3 The correlated X+Z condition

Write `v2(X)=2a`, `v2(Z)=2b` with square odd unit parts.

- `a=b`: the odd unit parts add to `2 mod 8`, so `v2(X+Z)` is odd; fail.
- `|a-b|=1`: after factoring the smaller square, the residual unit is `1+4u = 5 mod 8`; fail.
- `|a-b|>=2`: the residual unit is `1 mod 8`; pass.

Thus the conditional success mass in one surviving parity cylinder is

```text
(1/48)^2
 - sum_{a>=2} w_a^2
 - 2 sum_{a>=2} w_a w_{a+1}

= 1/2304 - 1/3840 - 1/7680
= 1/23040.
```

Multiplying by the three surviving mod-2 projective cylinders gives the exact normalized local density

```text
Delta_2 = (3/7)*(1/23040) = 1/53760.
```

Therefore

```text
R29-KUM-LOC2-2=DISCHARGED_EXACT_TWO_ADIC_STATE_DENSITY
DELTA_2=1/53760
TWO_ADIC_LOCAL_OBSTRUCTION_EMPTY=false
```

The audited point `[44^2:117^2:240^2]` is consistent with the formula: relative to the odd coordinate `117^2`, the two even square valuations are 4 and 8, whose half-valuations differ by two and therefore lie in the accepted state.

This is **local infrastructure only**. It does not provide a global Euler product, physical-height equidistribution, primitivity/canonical transfer, or endpoint nonexistence. The global receiver `R29-KUM-LOC3` remains open.

## 3. R29-MOD1C — promoted from class 2, executed, and discharged

Prior audited state:

```text
K8=ker(SL2(Z/8)->SL2(Z/4)) ~= (Z/2)^3,
|K8|=8,
ordinary full-symplectic conjugacy orbit sizes=1,3,3,1,
R29-MOD1C=OPEN_TWISTED_SIGMA_ACTION.
```

The earlier bounded stop was too conservative. The exact Stage29-02g level-4 condition already supplies enough data to compute the sigma action.

Write

```text
K8={I+4A mod 8 : A in sl2(F2)}.
```

Relative to the retained level-4 marking, the conjugate-self correspondence has sign matrix

```text
D=diag(1,-1) mod 4.
```

Any lift `M mod 8` of this correspondence satisfies

```text
M mod 2 = I.
```

For every `k=I+4A in K8`, conjugation modulo 8 depends only on `M mod 2`:

```text
M k M^{-1}
 = I + 4 (M A M^{-1})
 = I + 4A                     mod 8.
```

Hence the sigma transport action on `K8` is **trivial**. Also `K8` is abelian, so twisted conjugacy

```text
k ~ g^{-1} k sigma(g)
```

is equality for the marked level-4 datum. Therefore the exact arithmetic defect decomposition has eight singleton classes, not the four ordinary conjugacy classes obtained only after forgetting the retained marking.

```text
R29-MOD1C=DISCHARGED_TRIVIAL_SIGMA_ACTION_ON_K8
SIGMA_ACTION_ON_K8=TRIVIAL
MARKED_ARITHMETIC_DEFECT_CLASS_COUNT=8
ORDINARY_UNMARKED_CONJUGACY_CLASS_COUNT=4
ORDINARY_1_3_3_1_EQUALS_ARITHMETIC_STRATA=false
```

This does not eliminate any defect element. It removes the ambiguity about the arithmetic action and sharpens the modular route to eight explicit marked defect cases. `R29-KUM5` remains open because identifying the modular residual `S4` with the F7/arrangement `S4` at action/cocycle level is a different problem.

## 4. R29-MOD1D — promoted from class 4, executed, and discharged

Prior audited state:

```text
R29-MOD1D=CuspStabilizerAndPhysicalOpenRemoval.
```

Testa--Stoll's genus-5 `X(8)` model is

```text
u^2=xy,
v^2=x^2-y^2,
w^2=x^2+y^2.
```

The six branch values on the base P1 are

```text
0, infinity, +1, -1, +i, -i.
```

Their preimages are exactly the 24 cusps of `X(8)`; equivalently the cusp locus is `uvw=0`. The kernel `G0~=(Z/2)^3` acts by independent sign changes of `u,v,w`. Off `uvw=0`, no nontrivial sign change has a fixed point, so the action is free on the noncuspidal locus.

In the exact diagonal quotient model used for the cuboid surface, the invariant products satisfy

```text
U=u1*u2=2*b1,
V=v1*v2=2*b2,
W=w1*w2=2*b3.
```

A physical endpoint has positive nonzero face diagonals, hence

```text
b1*b2*b3 != 0.
```

Therefore `U,V,W` are all nonzero, forcing `u1u2v1v2w1w2 != 0`. Both `X(8)` factors are noncuspidal and the diagonal `G0` action is stabilizer-free on every physical endpoint preimage.

Thus the generic noncusp modular datum of Stage29-02g already covers the full physical endpoint open:

```text
R29-MOD1D=DISCHARGED_PHYSICAL_OPEN_NONCUSP_STABILIZER_FREE
PHYSICAL_ENDPOINT_INTERSECTS_MODULAR_CUSP_LOCUS=false
PHYSICAL_ENDPOINT_MODULAR_G0_STABILIZER_TRIVIAL=true
```

This does not make the generic degree-24 compactification an everywhere finite map; `R29-MOD2B` remains dormant unless a future arithmetic argument actually needs boundary extension.

## 5. Verification

`verify_bounded_execution.py` independently checks:

```text
R29-BEAU2A: V4 swap action
R29-KUM-LOC2-2: conditional_pair_mass=1/23040 and Delta_2=1/53760
R29-MOD1C: |K8|=8 and every lift of diag(1,-1) mod 4 centralizes K8
R29-MOD1D: no nontrivial sign stabilizer survives when u*v*w != 0
```

The modular finite check enumerates all 8 elements of `K8` and all invertible mod-8 lifts of the retained level-4 sign matrix satisfying the specified reduction; every such lift centralizes `K8`.

## 6. Class-1 exit condition

After the four executions above:

```text
CLASS1_IDENTIFIED_COUNT=4
CLASS1_EXECUTED_COUNT=4
CLASS1_PENDING_COUNT=0
NEW_RECEIVERS_DISCHARGED_BY_29_15_BOUNDED_EXECUTION=4
```

Any audit discovery of another class-1 receiver must trigger execution on this same PR before 29-15 may pass.
