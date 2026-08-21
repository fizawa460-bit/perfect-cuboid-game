# Stage29-07 — audited exact sign tower / two-face subcover adapter

```text
ROLE=KUM3A_KUM3B_EXACT_ADAPTER
STATUS=AUDITED_PASS
BASE_FIELD=Q
```

## 1. Exact two-face floor

With

```text
p^2=e^2+x^2,
q^2=e^2+y^2,
```

define

```text
T2bar={e^2+x^2=p^2,e^2+y^2=q^2} subset P4_[e:x:y:p:q].
```

The map

```text
T2bar -> P2_F7,
[e:x:y:p:q] -> [e^2:x^2:y^2]
```

is globally finite of generic degree `16` with generic deck `(Z/2)^4`.

Fresh audit verifies exactly four A1 singularities and independently reconstructs the Stage28 resolution by the anticanonical Pythagorean map. Put

```text
A1=v1^2-u1^2,
A2=v2^2-u2^2,

e=A1*A2,
x=2*u1*v1*A2,
p=(u1^2+v1^2)*A2,
y=2*u2*v2*A1,
q=(u2^2+v2^2)*A1.
```

The five `(2,2)` sections have exactly four common basepoints `A1=A2=0`. Blowing them up gives

```text
Y=Bl_4(P1xP1),
-K_Y=2H1+2H2-E1-E2-E3-E4,
(-K_Y)^2=4.
```

On the dense chart the inverse is recovered from

```text
u1/v1=x/(p+e),
u2/v2=y/(q+e),
```

so the anticanonical map is birational onto the degree-four complete intersection `T2bar`.

```text
R29-KUM3A=DISCHARGED_GLOBAL_NORMAL_SUBCOVER_PLUS_EXACT_STAGE28_RESOLUTION_ADAPTER.
```

## 2. Residual V4

The full endpoint adds exactly

```text
z^2=x^2+y^2,
d^2=e^2+x^2+y^2.
```

Thus

```text
Sbar -> T2bar
```

is globally finite of generic degree `4` with generic deck `(Z/2)^2`. On `e!=0` its two radicands are precisely

```text
f_face=(x/e)^2+(y/e)^2,
f_sp=1+(x/e)^2+(y/e)^2.
```

After base change to `Y`, uniqueness of normalization gives

```text
normalization(Y x_T2bar Sbar)
= normalization of Y in Q(Y)(sqrt(f_face),sqrt(f_sp)),
```

which is the audited joint V4 model.

```text
R29-KUM3B=DISCHARGED_EXACT_RESIDUAL_TWO_ROOT_V4
FULL_64_COVER_FACTORING=16_TIMES_4.
```

## 3. Selected-predicate sign tower

The six F7 projective Kummer classes split as two edge-ratio classes plus three face classes plus one space class. A fixed ordered selected-predicate tower has generic degrees

```text
4 -> 8 -> 16 -> 32 -> 64.
```

This is a literal selected-predicate subcover tower, not an objectwise `M1 -> M2 -> M3` population tower.

```text
SELECTED_PREDICATE_LIFT_TOWER_IS_LITERAL=true
EXACT_M1_M2_M3_ARE_SUCCESSIVE_TOWER_FLOORS=false
BOOLEAN_FAILURE_IS_SIGN_SHEET=false
BOOLEAN_16_EQUALS_SIGN_64=false.
```

## 4. Boundary scope

The exact normal-model factorization closes the bridge-relevant part of the old G1b receiver but not its complete exceptional-curve table.

```text
R29-G1b-CORE=DISCHARGED_GLOBAL_NORMAL_MODEL_AND_PHYSICAL_OPEN
R29-G1b=PARTIAL_DISCHARGE_CORE_DONE
R29-G1b-EXC=DORMANT_BOUNDED_NOT_REQUIRED_FOR_CURRENT_BRIDGE
FULL_EXCEPTIONAL_CURVE_LEDGER_COMPLETE=false.
```
