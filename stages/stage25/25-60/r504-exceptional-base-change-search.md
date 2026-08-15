# Stage25-60 R504 exceptional base-change search

STATUS=SUPERSEDED_IN_PART_BY_COMPLETE_Q_DESCENT
ROUTE=R504
CHECKPOINT=60

The previous symbolic calculations in the family
\[
\phi_{a,b}(u)=\frac{a u^2+b}{u^2+1}
\]
remain valid **inside that strict split subfamily**. They are not a complete classification of all Q-rational degree-two base changes.

Accepted retained results in that subfamily:

```text
R504_EVEN_SUBFAMILY_BC3_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
R504_EVEN_SUBFAMILY_BC4_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
R504_EVEN_SUBFAMILY_BC5_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
R504_EVEN_SUBFAMILY_EXTRA_INVOLUTION_SYMBOLIC_CERTIFICATE=RETAINED
```

The complete Q source-descent is now proved separately in `r504-q-degree2-complete-descent.md`:

- split: `(A*u^2+B)/(C*u^2+D)`;
- nonsplit squareclass `d`: `(A*(u^2+d)+B*u)/(C*(u^2+d)+D*u)`.

Therefore the remaining live work is broader than the previous Prym locus:

```text
R504_FULL_SPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_NONSPLIT_NORMAL_FORM_ANALYSIS_REQUIRED=true
R504_PRYM_AS_SOLE_DEGREE2_RESIDUAL_ACCEPTED=false
R504_GENERAL_DEGREE2_FULL_RANK_JUMP_CLASSIFICATION_PROVED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```

The earlier claim that `(a*u^2+b)/(u^2+1)` is a complete Q-degree-two normal form is withdrawn.
