# Stage29-02e — V4 cohomology / cross-trace rematch

```text
ROLE=V4_COHOMOLOGY_AND_CROSS_TRACE_REMATCH
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

## 1. Exact ingredients

Stage29-02b derives the good-prime V4 identity

\[
\#X_{joint}
=
\#X_{face}+\#X_{sp}+\#X_{cross}-2\#Y.
\]

Stage29-02e imports Horie--Yamauchi's exact cohomological description of the full endpoint canonical surface `Sbar ~= X_joint`.

Thus, after compatible model/bad-prime adapters, the cross quotient is not an isolated new local object: its Frobenius trace is determined by

\[
\boxed{
T_{cross}(p)
=T_{endpoint}(p)-T_{face}(p)-T_{sp}(p)+2T_Y(p)
}
\]

with the obvious cohomological normalization corresponding to the point-count identity.

Equivalently at the finite-field point-count level,

\[
\boxed{
\#X_{cross}
=\#Sbar-\#X_{face}-\#X_{sp}+2\#Y.
}
\]

This is the exact receiver `R29-L2` anticipated by 29-02b.

## 2. Endpoint trace is already explicit

For every good odd prime,

```text
T_endpoint(p)
=3 a_p(h16) + a_p(h32) + 3 a_p(h8)
 + p(10+2 chi_-1(p)+chi_-2(p)+3 chi_2(p)).
```

Therefore the only missing pieces for an explicit cross-trace formula are the two **marginal K3 Frobenius traces in the same model convention**.

This is substantially narrower than a fresh joint character-sum problem.

## 3. Multiplicity pattern: suggestive but not yet an identification

Horie--Yamauchi's transcendental endpoint decomposition has multiplicities

```text
3 copies h16,
1 copy h32,
3 copies h8.
```

Testa--Stoll's coordinate-sign quotient geometry has seven natural K3 quotient directions grouped into

```text
3 side-coordinate quotients K_a,
3 face-diagonal quotients K_b,
1 long-diagonal quotient K_c.
```

The Stage20 Euler K3 is the long-diagonal-forgotten quotient `K_c`; the Stage19 space-completion K3 is a face-diagonal-forgotten quotient of the other threefold orbit.

The matching multiplicity pattern `3+1+3` is structurally striking, but Stage29-02e does **not** assign

```text
K_c -> h32
K_a/K_b -> h16 or h8
```

without an explicit quotient-action / trace calculation.  Horie--Yamauchi Theorem 4.4 computes the full representation but does not, in the imported theorem statement, label each modular summand by the Testa--Stoll K3 quotient orbit.

```text
THREE_ONE_THREE_PATTERN_OBSERVED=true
K3_ORBIT_TO_MODULAR_FORM_IDENTIFICATION_PROVED=false
```

## 4. New bounded receiver

The remaining task is now finite and exact:

```text
R29-L3=CoordinateSignK3QuotientFrobeniusModuleIdentification
```

Sufficient outputs are either:

1. identify the Galois representation / L-function of `K_c` and one representative `K_b` directly; or
2. compute their good-prime traces at enough primes to distinguish `h16`, `h32`, `h8` plus their algebraic Tate pieces;
3. preserve the Stage28 physical model and bad-prime conventions.

Once `R29-L3` is solved, the cross-quotient local trace follows by exact subtraction from the known endpoint trace, with no new broad local-character search.

## 5. Relation to Stage29 joint local arithmetic

The cross trace is exactly the global finite-field sum of the cross character `chi(f_face f_sp)` up to the fixed base/boundary model correction.  Therefore:

```text
F4_CROSS_CHARACTER
   <-> X_cross finite-field trace
   <-> V4 subtraction identity
   <-> endpoint modular-form trace minus marginal K3 traces.
```

This gives a concrete arithmetic-geometric bridge between the Stage28 local square tests and the Horie--Yamauchi endpoint L-function.

## Firewalls

- Frobenius trace correlation is not a physical-height counting theorem.
- Good-prime local identities are not multiplied into an Euler product for `P(B)`.
- The `3+1+3` quotient/modular matching remains a hypothesis until `R29-L3` is proved.
- A modular-form description does not decide rational-point existence.

```text
R29_L2_REDUCED=true
R29_L3_NEW_EXACT_RECEIVER=true
GLOBAL_PERFECT_CUBOID_CLAIM=false
```
