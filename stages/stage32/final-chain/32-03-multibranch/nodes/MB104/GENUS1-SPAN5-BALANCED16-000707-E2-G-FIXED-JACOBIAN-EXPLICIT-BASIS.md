# Stage32 MB104 — `000707000f0f` e=2 explicit basis of `J(C8)^G`

Status: **RETAINED CANDIDATE COORDINATE MATERIALIZATION / FIVE EXPLICIT FIXED 2-TORSION GENERATORS / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The preceding integral-homology replay proved

```text
J(C8)^G ~= (Z/2)^5.
```

This note materializes a deterministic basis for those five fixed points in the exact Reidemeister--Schreier coordinates used by the verifier. It does **not** yet identify the five points with explicit algebraic divisors on `C8`.

## 1. Deterministic homology coordinates

Use the same topological passport and conventions as the retained integral-homology leaf:

```text
G=(Z/2)^3,
branch monodromy=(e1,e1,e2,e2,e3,e3),
t_(a,b,c)=x1^a x3^b x5^c.
```

Let `S(g,i)` be the nontrivial Schreier generators in lexicographic `g` order and increasing `i`. Apply the retained deterministic unit-pivot integer elimination to the `56 x 41` abelian relation matrix. The final ten free columns define an integral basis

```text
h1,...,h10
```

of `H_1(C8,Z)`.

All coordinate vectors below refer to this exact basis and therefore are replayable without period approximations.

## 2. Five fixed 2-torsion generators

The fixed-torus Smith reduction gives the following five half-lattice representatives. Since adding an integral vector does not change a point of the Jacobian, write only the reduced mod-two numerator vectors:

```text
v1 = (1,1,0,1,1,1,0,0,0,0),
v2 = (0,1,0,0,0,0,1,1,0,0),
v3 = (0,0,0,1,0,0,0,0,0,1),
v4 = (0,1,1,0,0,0,0,0,0,0),
v5 = (0,0,0,0,0,0,0,1,1,0).
```

Define

```text
tau_j = (1/2) v_j  mod H_1(C8,Z).
```

Exact matrix replay verifies, for each of the three standard deck generators `e_i`,

```text
(e_i-1) tau_j in H_1(C8,Z),
```

so every `tau_j` is `G`-fixed and 2-torsion. The five numerator vectors have rank five over `F_2`, hence

```text
J(C8)^G = <tau_1,...,tau_5> ~= (Z/2)^5.
```

Therefore every `G`-invariant degree-`28l` factor class from the preceding external-product leaf has a unique binary label

```text
A = A_ref(l) tensor tau(epsilon),
tau(epsilon)=sum_(j=1)^5 epsilon_j tau_j,
epsilon in F_2^5,
```

and similarly for `B`. The 1024 ordered factor-class pairs are now canonically labeled by

```text
(epsilon,delta) in F_2^5 x F_2^5.
```

## 3. Important branch-divisor anti-shortcut

The six reduced ramification divisors of `C8 -> C8/G` do **not** directly give five independent generators.

Let `R_i` be the reduced degree-four ramification divisor over branch value `a_i`, with inertia pattern

```text
(e1,e1,e2,e2,e3,e3).
```

The three quadratic subcover characters give rational square roots with divisors

```text
R1-R2,
R3-R4,
R5-R6,
```

so

```text
R1 ~ R2,
R3 ~ R4,
R5 ~ R6.
```

Characters nontrivial on two inertia types also give, for example,

```text
R1+R2-R3-R4 ~ 0,
R1+R2-R5-R6 ~ 0.
```

Thus coarse reduced branch-orbit differences have substantial principal relations and cannot be substituted for the five `tau_j` above. Any algebraic-divisor realization of the fixed Jacobian basis must respect these relations rather than treating the six branch values as a free `F_2^5` source.

This anti-shortcut is load-bearing: it prevents a false identification of residual-sheet data with a naive branch-divisor basis.

## 4. Next finite target

The factor-class ambiguity is now fully enumerated at the abstract Jacobian level:

```text
1024 ordered labels (epsilon,delta).
```

The next useful refinement is to construct an algebraic realization, theta characteristic, or equivalent modular coordinate for the five `tau_j`, and then evaluate the retained residual-cover/conductor character on those labels. Without that adapter, the binary labels cannot yet be converted into conductor-preimage `R=C8/H` sheet values.

## Firewalls

- The five `tau_j` are exact topological/Jacobian coordinates, not yet explicit effective divisors.
- No claim that the 1024 factor pairs all admit the required irreducible product divisor.
- No branch-divisor shortcut is permitted.
- No conductor pair is assigned a residual `G/H` sign.
- No weighted opposite-sheet bound is proved.
- No e=2 closure is claimed.
- e=4 and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
