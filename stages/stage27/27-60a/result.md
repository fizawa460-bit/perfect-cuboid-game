# Stage27-60a — Stage18 -> Stage19 causal decomposition contract

```text
TASK_ID=Stage27-60a
CHECKPOINT=60
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
CURRENT_STAGE27_SCOPE=Stage18 -> Stage19 reentry refinement
ROUTE_KIND=CAUSAL_DECOMPOSITION
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

For the present Stage27 campaign, retain the already-frozen Stage18 -> Stage19
population contract rather than reinterpreting Stage27 as a new Stage16 -> Stage20
counting problem.

Source:

\[
M_2(B)=\#\{\text{primitive canonical exactly-two-face cuboids},\ R\le B\}.
\]

Target:

\[
N_2(B)=\#\{\text{the same physical objects with integral space diagonal}\}.
\]

Thus this is a literal subset transition under the same physical measure and cutoff:

\[
N_2(B)=M_2(B)\cap\{R\in\mathbf Z\}.
\]

The current certified theorem surface after the Stage27 r5--r10 campaign is

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}.
\]

Hence the current survivor corridor is

\[
B^{-3/4}(\log B)^{-5}
\ll \frac{N_2(B)}{M_2(B)}
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

The ratio tends to zero, but the true target exponent and the true polynomial cost
of the added space-diagonal condition remain unknown.

Checkpoint60 is therefore not an exponent-fitting exercise.  Its roadmap role is
to decompose **why** the Stage18 population thins when the integral-space condition
is added, and to separate:

1. the genuinely new space-square restriction;
2. equivalent reformulations of that same restriction;
3. auxiliary local/geometric mechanisms proving rarity;
4. quantitative mechanisms responsible for the current upper bound;
5. constructive mechanisms responsible for the current lower bound;
6. restrictions already charged earlier and therefore unavailable for a second
   power saving.

```text
ROADMAP_CHECKPOINT60_ROLE=CAUSAL_DECOMPOSITION
SOURCE_POPULATION=M2
TARGET_POPULATION=N2
ADDED_CONDITION=integral space diagonal
CURRENT_N2_LOWER_EXPONENT=1/4
CURRENT_N2_UPPER_EXPONENT=1/2_PLUS_EPSILON
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-60b
```
