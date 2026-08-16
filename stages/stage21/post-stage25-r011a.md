# Stage21 post-Stage25-r011a geometric receiver

STATUS=AUDITED_PASS_SYNCED_BY_STAGE25_REENTRY_70
HISTORICAL_STAGE21_PASS_REVOKED=false
SOURCE_ROUTE=Stage25-um-r011a
PARENT_PR=1009
BACKFLOW_PR=1010
BACKFLOW_MERGE_COMMIT=e64f21621bb1b7062dfd21f186e6ed1bcc191272

The frozen Stage21 theorem remains

\[
N_1(B)/M_1(B)\sim\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

Audited r011a supplies the structural explanation at the height-geometric invariant level:

- Euler one-face raw source: `(a,b)=(2,2)`;
- integral-space one-face raw target: `(a,b)=(1,4)`.

Hence the transition has

\[
\Delta a=-1,\qquad \Delta b=+2,
\]

matching exactly the proved `B^-1(log B)^2` scale.

The target surface is the `Q(i)`-twisted form of the Stage15 split `4A1` quartic-del-Pezzo model. The induced Galois action on the split `Bl_4(P1xP1)` Picard basis fixes the two ruling classes and pairs the four corner exceptional classes, giving rational Picard invariant rank four.

This closes the Stage21 fine mechanism at the geometric `(a,b)` invariant level only. It does not identify two independent local factors or one log from each of `H(P),L_B(P)`.

```text
FROZEN_STAGE21_THEOREM_CHANGED=false
G21_LOG2_FINE_MECHANISM=CLOSED_AT_GEOMETRIC_INVARIANT_LEVEL
M1_MANIN_INVARIANTS=2,2
N1_MANIN_INVARIANTS=1,4
TWO_INDEPENDENT_LOG_FACTORS_PROVED=false
COMMON_DIRICHLET_POLE_SLOT_LEDGER_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
BACKFLOW_AUDIT_STATUS=PASS
BACKFLOW_SYNCHRONIZED=true
```
