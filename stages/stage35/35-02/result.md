# Stage35 35-02 — Q-field / physical fibration ledger

```text
UNIT=35-02_Q_FIELD_PHYSICAL_FIBRATION_LEDGER
VERDICT=PASS_SELECTED_ROUTE
SELECTED_FIBRATION=TS-S-R3-Q1
SELECTED_FIBRATION_Q_DEFINED=true
SELECTED_FIBRATION_GLOBAL_PHYSICAL_ENDPOINT_COVERAGE=true
HISTORICAL_R29_FIB1_ALL_FIBRATIONS_CLOSED=false
NEW_THEOREM_CREDIT=false
R29_FIB2_CLOSED=false
NEXT=35-03_RESIDUAL_SPACE_LIFT_INTERFACE
```

Stage35 does not need to classify the fields of all 28 geometric full-endpoint fibrations before starting arithmetic. A single rank-3 fibration is already defined over `Q` and is a direct fibration of the full endpoint surface.

The selected representative is

```text
TS-S-R3-Q1
a1^2+b1^2=c^2
t=(a1+c)/b1
```

with exact Stage29 physical dictionary

```text
[a1:a2:a3:b1:b2:b3:c]=[e:x:y:z:q:p:d],
```

hence

```text
t=(e+d)/z.
```

For a nondegenerate physical endpoint, `e,z,d>0`, so `t` is finite and `t>1`. The eight base points requiring blow-up are singular points of the canonical surface and are outside the physical open. Thus every physical endpoint `Q`-point maps to a rational parameter of this selected family.

This is only the coverage/field adapter needed by Stage35. The global geometric firewalls remain: all 28 genus-5 fibrations are not certified over `Q`; all 15 Euler-K3 elliptic fibrations are not certified over `Q`; the first rank-4 endpoint pair is over `Q(i)`; and the historical all-fibration `R29-FIB1` ledger is not declared closed.

35-03 must now write the exact point-level reconstruction between a `TS-S-R3-Q1` fiber point and Stage29 endpoint coordinates. Because the selected family lives directly on the full endpoint surface, this route may replace the K3 marginal residual-square lift by an exact direct reconstruction, but that implication must be certified before any receiver credit.
