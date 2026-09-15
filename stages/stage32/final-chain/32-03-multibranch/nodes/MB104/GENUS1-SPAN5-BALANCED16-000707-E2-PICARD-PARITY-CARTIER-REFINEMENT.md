# Stage32 MB104 — `000707000f0f` e=2 Picard-parity Cartier refinement

Status: **RETAINED EXACT LOCAL-CARTIER CONSEQUENCE OF PICARD64 PARITY / CONDITIONAL CARTIER-PENCIL REFINEMENT THROUGH THE RETAINED H1 LINEARIZATION / NAIVE MOD-4 REPEAT CLOSED / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The exact Picard64 descent verifier has now proved, for all fourteen supported nodes,

```text
x_j == 0 mod 2.                                (P2)
```

The purpose of this refinement is to feed `(P2)` back into the already-retained A1/intermediate-quotient geometry. It does **not** re-open the large retained Picard payload and does not assert a new modulo-four condition.

## 1. Centered variables are multiples of four

Recall

```text
d_j=2*x_j-8*l,
a_j=d_j/2=x_j-4*l.
```

By `(P2)`, write

```text
x_j=2*y_j,
b_j=y_j-2*l.
```

Then exactly

```text
a_j=2*b_j,
d_j=4*b_j.                                    (D4)
```

The two retained zero-quartic saturation equations become

```text
b_8+b_9+b_10+b_11+b_32+b_33+b_34=0,           (Q1-B)

b_0-b_1+b_2-b_3-b_24+b_25-b_26=0.             (Q0-B)
```

and the node ranges give

```text
-2*l <= b_j <= 2*l.
```

The exact A1 energy formulas therefore sharpen arithmetically to

```text
C_1.C_2
 =168*l^2+4*sum_j b_j^2,

weighted opposite-sheet cut
 =84*l^2+2*sum_j b_j^2,

delta_same
 =84*l^2+56*l-2*sum_j b_j^2.                  (ENERGY-2STEP)
```

This is an integrality refinement only. The balanced point `b_j=0` for every `j` still survives.

## 2. Picard64 parity makes the intermediate component Cartier

Let

```text
Gamma subset X_H=(C8 x C8)/H_diag
```

be the retained e=2 intermediate quotient component and `tau Gamma` its residual translate.

At a supported box node there are two A1 points of `X_H`. The retained A1 multiplicity table is

```text
Gamma:      x_j,       8*l-x_j,
tau Gamma:  8*l-x_j,   x_j.
```

For an A1 singularity with exceptional `(-2)`-curve `F`, the Mumford pullback of a reduced Weil divisor germ with strict-transform intersection `r` is

```text
rho^*D=Dtilde+(r/2)F.
```

Equivalently, the local class group is `Z/2`, detected by `r mod 2`: the divisor is locally Cartier exactly when `r` is even.

By `(P2)`, both

```text
x_j,
8*l-x_j
```

are even at every supported node. Hence `Gamma` and `tau Gamma` are locally Cartier at every supported A1 point.

The retained carrier misses every unsupported box exceptional, and the retained intermediate quotient has only isolated A1 quotient singularities. Therefore the component divisors are globally Cartier on the normal intermediate surface:

```text
Gamma and tau Gamma are Cartier divisors on X_H.   (CARTIER)
```

This is a genuine geometric upgrade of the previous use of Mumford/Q-Cartier intersection theory.

## 3. Conditional honest pencil from the retained H1 linearization

The retained ambient-H1 route is still explicitly candidate-level, but conditional on that retained input it proves

```text
Gamma ~ tau Gamma on X_H.                      (LIN-XH)
```

Before `(P2)`, `(LIN-XH)` was used only as a principal-divisor relation between normal-surface Weil divisors. Combining it with `(CARTIER)` gives an honest line bundle

```text
L=O_XH(Gamma) ~= O_XH(tau Gamma).
```

Since `Gamma` and `tau Gamma` are distinct effective divisors, their defining sections are linearly independent. Thus, conditionally on the retained H1 linearization,

```text
h^0(X_H,L) >= 2,
```

and the pair spans an honest pencil

```text
<Gamma,tau Gamma> subset |L|.                  (PENCIL)
```

The common base scheme is supported on `Gamma cap tau Gamma`; no base-point-freeness is asserted.

Because the residual involution exchanges the two divisors, the two-dimensional pencil is `tau`-stable. Choosing a `tau`-linearization of `L`, the sum and difference of the two generating sections are eigen-sections. Their ratio gives a `tau`-anti-invariant rational function. Consequently the pencil supplies another generator of the same quadratic function-field extension

```text
k(X_H)/k(B),
```

up to multiplication by an invariant function in `k(B)^*`.

This is a possible future bridge between the global Cartier/Picard constraint and the explicit retained residual Kummer generator `r_z` (or `r_w`). No such invariant multiplier is evaluated here.

## 4. Why repeating the same descent modulo four is not valid

The exact downstairs descent condition used by the Picard64 verifier is

```text
[D'] in Span_F2{absent exceptional classes}
       subset Pic(S)/2 Pic(S),                 (DESC2)
```

with

```text
D'=7*l*H+sum_supported (x_j-8*l)E_j.
```

By the definition of the quotient `Pic(S)/2Pic(S)`, once `(DESC2)` holds there already exist an integral Picard class `M` and an integral lift `B_J` of an absent-class combination such that

```text
D'=2*M+B_J.
```

Therefore the same invariant-descent statement does **not** supply an additional condition modulo four on the `x_j`. Asking again whether `(D'-B_J)/2` is divisible by two would impose a new hypothesis not contained in the retained double-cover descent argument.

Hence the standalone route

```text
Picard descent mod 2
 -> divide by 2
 -> repeat the identical descent to force x_j mod 4
```

is closed as unjustified.

A true further 2-adic restriction would require new geometry on the half-class `M` (for example effectivity, a second independent descent, a prescribed linearization, or a source-locked restriction condition), not merely repetition of `(DESC2)`.

## 5. Route consequence

The Picard64 result has two safe downstream uses:

1. exact arithmetic lattice refinement `d_j in 4Z` and `(ENERGY-2STEP)`;
2. exact local-to-global Cartierness `(CARTIER)` for the e=2 intermediate component.

Conditional on the already-retained ambient-H1 linearization, the second point upgrades the residual translate relation to the honest pencil `(PENCIL)`. A useful continuation is therefore to identify the anti-invariant pencil generator against the explicit quotient coordinate

```text
r_z^2=2*(C+W3)/(W1-iW2)
```

or `r_w`, and evaluate its specialization at conductor normalization preimages.

The Picard parity itself does not close `e=2`, because `b_j=0` remains a formal solution.

## Firewalls

- The Cartier conclusion uses the exact Picard64 parity result plus the retained A1 local model; it does not claim geometric existence of a carrier.
- The pencil conclusion remains conditional on the retained candidate ambient-H1/linear-equivalence chain.
- No new modulo-four congruence is claimed.
- No individual conductor pair is assigned a residual sign.
- No weighted-cut upper bound is claimed.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- Active leaf remains unchanged.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
