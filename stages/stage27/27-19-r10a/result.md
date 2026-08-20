# Stage27-19-r10a — targeted external lower-construction rematch: Peschmann 2026

```text
TASK_ID=Stage27-19-r10a
PARENT_ROUTE=Stage27-19-r9c
ROUTE_KIND=TARGETED_EXTERNAL_LOWER_CONSTRUCTION_SEARCH
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_LOWER_EXPONENT=1/4
CURRENT_UPPER_MU=1/2
```

Targeted 2026 literature search surfaced a closely matched recent sequence by René Peschmann:

1. `arXiv:2604.09328`, *Quartic reductions and elliptic obstructions for perfect Euler bricks*;
2. `arXiv:2604.28072`, *A torsion-intersection proof of perfect-cuboid nonexistence on 1,072 explicit master-tuple fibers*;
3. `arXiv:2605.00573`, *Exponent-one blockers and a Mordell-Weil construction of Euler bricks*.

These papers work with two coprime Pythagorean pairs in Euclid form (the “Master-Hit” framework). The April quartic-reduction paper states an equivalence between the perfect-cuboid condition and simultaneous squareness of two explicit quartic expressions and reduces the resulting square condition to a one-parameter genus-3 family

\[
C_A: w^2=\lambda^8+A\lambda^4+1.
\]

The May Mordell-Weil paper then fixes one Euclid pair `(m,n)`, obtains a genus-one quartic / elliptic model `E_{m,n}`, and uses Mordell-Weil combinations to generate many further Euler bricks satisfying the three face conditions. The lift condition is that a rational function `tau(P)` on `E_{m,n}` be a positive rational square.

For the current Stage27 lower receivers this is **not yet a direct breakthrough**:

- the construction produces many Euler bricks, not a proved positive-density / polynomially thick subfamily with integral space diagonal;
- the reported exponent-one blocker phenomenon is computationally verified on a large data set, not a theorem yielding a new physical lower family;
- the 1,072-fiber torsion-intersection result is finite-fiber exclusion, not a construction theorem.

However the framework is materially closer to the remaining r8/r9 lower gate than the older Saunderson family because the space-diagonal square is built directly into the elliptic/genus-3 lift equation rather than appended afterward.

The new repo receiver is therefore:

> Determine whether the Peschmann Master-Hit elliptic fibration admits a **moving algebraic section/multisection or positive-dimensional rational subfamily** on which `tau(P)` is automatically a rational square, with physical height/source-count ledger satisfying `rho/h>1/4` or a one-parameter specialization with `h_alg<=7`.

A second, weaker receiver is:

> Determine whether the simultaneous quartic-square equations possess a rational cross-divisibility specialization lowering the Stage27 toric physical degree below eight.

```text
PESCHMANN_2026_SEQUENCE_FOUND=true
DIRECT_STAGE19_LOWER_BREAKTHROUGH_FOUND=false
MASTER_HIT_FIBRATION_CLOSE_TO_RECEIVER=true
PRIMARY_NEW_GATE=MovingMasterHitSquareLiftSectionOrMultisection
SECONDARY_NEW_GATE=MasterHitQuarticCrossCancellationHeightBelow8
NEXT_DERIVED_ROUTE=27-19-r10b
ADVANCE_TO_CHECKPOINT50=false
```
