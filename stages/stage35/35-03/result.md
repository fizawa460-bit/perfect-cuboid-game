# Stage35 35-03 — residual-space lift interface

```text
UNIT=35-03_RESIDUAL_SPACE_LIFT_INTERFACE
VERDICT=PASS_DIRECT_FULL_ENDPOINT_RECONSTRUCTION
SELECTED_FIBRATION=TS-S-R3-Q1
ADDITIONAL_RESIDUAL_SQUARECLASS_CONDITION=false
DIRECT_ENDPOINT_RECONSTRUCTION_COMPLETE=true
R29_FIB2_CLOSED=false
NEW_THEOREM_CREDIT=false
NEXT=35-04_MINIMAL_UNIFORM_THEOREM_STATEMENT
```

For the selected direct full-endpoint fibration, the historical K3 marginal residual-space-square lift is not an extra condition. With

```text
t=(e+d)/z,
e=((t^2-1)/(t^2+1))*d,
z=(2t/(t^2+1))*d,
```

the identity `e^2+z^2=d^2` is automatic. The remaining three cuboid equations become exactly the three diagonal quadrics in `direct-endpoint-reconstruction.json` on `[x:y:p:q:d]`.

Conversely, every nondegenerate physical endpoint gives finite `t in Q`, and in the positive physical normalization `t>1`; the same formulas recover `e,z`. Thus a rational point in the physical open of the selected fiber is an exact endpoint point, not merely a quotient or marginal point.

The Arsenal router was consulted at this leaf. `S34-W01` is not applied because no residual squareclass predicate remains. `S34-W03` is not applied because the selected fiber is already the exact endpoint family rather than a larger auxiliary cover with an extra receiver condition.

The remaining wall is now purely uniform: prove that for every rational physical parameter `t>1` the selected genus-5 fiber has no rational point in the physical open, or prove another exact replacement theorem with the same receiver consequence. That theorem statement is the 35-04 target.
