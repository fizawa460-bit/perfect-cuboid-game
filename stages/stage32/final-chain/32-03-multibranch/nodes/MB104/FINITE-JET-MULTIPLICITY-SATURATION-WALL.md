# Stage32 MB104 — fixed finite-jet multiplicity saturation wall

Status: **RETAINED LOCAL NO-GO / MB104 INCOMPLETE / NO CREDIT**

## Purpose

MB104 needs a population-wide upper bound

```text
R8 <= alpha*d + beta,  alpha < 1/4,
```

where `R8` counts normalization branches of FSM-minimal type `(A,B)=(1,1)` over the 48 A1 box nodes.

The retained BTVA order-two computation showed saturation after three distinct landing directions. This note isolates the general local obstruction behind that phenomenon: **no fixed finite depth of local branch jets, by itself, can count arbitrary `R8` multiplicity at one A1 node.**

This is a no-go statement for a class of local strategies. It is not a no-go for higher jets combined with global algebraic constraints.

## A1 resolution chart

Use the standard A1 chart

```text
xz = y^2,
x = s,
y = s*t,
z = s*t^2,
E = {s=0}.
```

Fix a nonzero landing coordinate `lambda`. For any integer `J>=0` and any distinct constants `c_1,...,c_r`, consider resolved smooth branch germs

```text
B_c : s=tau,
      t=lambda + c*tau^(J+1).
```

Each branch meets `E` transversely, so its exceptional intersection multiplicity is one. Under contraction,

```text
x = tau,
y = lambda*tau + c*tau^(J+2),
z = lambda^2*tau + 2*lambda*c*tau^(J+2) + c^2*tau^(2J+3).
```

Therefore every `B_c` has the same FSM-leading minimal data `(A,B)=(1,1)` and the same nonzero landing coordinate `lambda`, while distinct `c` give distinct germs.

Most importantly,

```text
j^J(B_c) = j^J(B_c')
```

for every pair `c,c'`: the first coefficient distinguishing them occurs only in the `(J+1)`-st `t`-jet.

Thus, for every prescribed branch multiplicity `r`, the local A1/FSM model admits `r` distinct minimal branch germs that are indistinguishable by all branch data through any fixed finite jet depth `J`.

## Consequence for finite local portfolios

Let `F` be any finite collection of local conditions whose evaluation on a normalization branch factors through its `J`-jet for some fixed `J`. Examples include any fixed finite list of principal-part or Taylor-coefficient functionals of bounded order.

On the family above, every branch produces the same evaluation vector under `F`. Adding more branches therefore does not increase the row rank or the number of independent local conditions seen by `F`.

Hence a fixed finite local jet portfolio cannot, without an additional global input, imply a universal multiplicity estimate of the form

```text
r_i <= constant,
```

or a population-wide linear estimate on

```text
R8 = sum_i r8_i
```

merely by assigning one independent local condition to each minimal branch.

This strengthens the retained order-two saturation wall: the obstruction is not specific to quadratic principal parts.

## Fixed symmetric order: leading pole polynomial

The same mechanism is visible directly for a fixed symmetric order. On the double cover

```text
s=u^2,
v=t*u,
```

consider a constant homogeneous symmetric tensor of order `m`

```text
Q_m = sum_(j=0)^m a_j du^(m-j) dv^j.
```

The coefficient of the most singular `ds^m` term on the resolution is

```text
P_m(t) / (2^m * s^(m/2)),
P_m(t)=sum_(j=0)^m a_j t^j.
```

For even `m` this is compatible with the `(-1)` deck invariance of constant tensors. On a minimal branch, cancellation of this **leading** pole asks only

```text
P_m(lambda)=0.
```

Thus the leading-order landing-direction conditions at fixed `m` have dimension at most `m+1`; repeated branches with the same `lambda` give the same leading row. For `m>2`, subleading poles can depend on higher branch jets, so this note does **not** claim that `P_m(lambda)=0` is sufficient for full regularity. The finite-jet construction above is what controls any fixed bounded collection of those subleading jet conditions.

## What this closes and what remains live

Closed as a standalone MB104 strategy:

- “take a fixed higher symmetric order and expect its local principal parts to count every repeated minimal branch”;
- “take any fixed finite collection of bounded-order local jet conditions and obtain a multiplicity bound solely from local rank growth.”

Still live:

1. a cuboid-specific **global** constraint that prevents arbitrarily many branches from sharing a bounded jet;
2. a conductor/intersection mechanism that charges the high contact forced when jets collide;
3. an adaptive/unbounded jet construction whose effective depth grows with multiplicity or degree and comes with a quantitative global dimension estimate;
4. a high-span geometric restriction on the remaining genus-zero full-span and genus-one span-5/6 sectors.

The local family constructed here is only a compatibility witness inside the A1/FSM local model. No claim is made that an arbitrary such collection globalizes to an actual integral cuboid-surface curve.

## Source locks

- `stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md`, git blob `512fcc70afb1acf16956fd4b7a2b9b935a052150` — A1/FSM chart, minimal `(1,1)` branch, and landing semantics.
- `stages/stage32/final-chain/32-03-multibranch/nodes/MB101/RESULT.md`, git blob `890f80ce208e402b14275d3e3279f9c02d5dc2fa` — exact `R8` population/normalization-profile semantics.

The verifier recomputes both Git blob identities before accepting the certificate.

## Firewalls

- `MB104_complete=false`.
- `absolute_R8_bound_proved=false`.
- `finite_degree_window_proved=false`.
- `finite_picard_enumeration_released=false`.
- no receiver/effectivity/final-milestone/theorem/endpoint credit.
- no Perfect Cuboid existence or nonexistence claim.
- no merge authorization.
