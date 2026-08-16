# Stage26-10 comparison lattice

```text
exact masks:       M2  -- third face -->  M3       (disjoint strata)
literal host:      H>=2 = M2 + M3  --->  M3       (subset survival Phi)
raw incidences:    P = M2 + 3 M3   --->  3 M3     (incidence survival Theta)
```

All counts use primitive canonical objects, the Euclidean cutoff \(R\le B\), and no space-diagonal condition.

With \(r=M_3/M_2\),

\[
r=\frac{M_3}{M_2},\qquad
\Phi=\frac{r}{1+r},\qquad
\Theta=\frac{3r}{1+3r}.
\]

Hence

\[
r=\frac{\Phi}{1-\Phi}=\frac{\Theta}{3(1-\Theta)},
\quad
\Theta=\frac{3\Phi}{1+2\Phi},
\quad
\Phi=\frac{\Theta}{3-2\Theta}.
\]

Directional raw hosts retain \(P_j=M_{2,j}+M_3\) and \(\Theta_j=M_3/P_j\). They are the primary Stage25 handoff because they remember which shared edge was completed; they must not be summed without the multiplicity-three correction.

```text
NOMINAL_ENDPOINTS_DISJOINT=true
LITERAL_HOST_AVAILABLE=true
RAW_PAIR_MULTIPLICITY_OF_M3=3
EXACT_MEASURE_TRANSLATION=true
PROBABILISTIC_INDEPENDENCE_INFERRED=false
SPACE_DIAGONAL_IMPORTED=false
DOUBLE_CHARGE_FIREWALL=ACTIVE
```

Future checkpoints may compare analytic thin-cover, local squareclass, explicit-construction, K3/fibration, and finite-computation lanes. Checkpoint10 only freezes the lattice; it does not select a winning mechanism.
