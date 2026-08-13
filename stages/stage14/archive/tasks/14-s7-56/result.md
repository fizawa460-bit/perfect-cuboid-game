# Stage14-s7-56 — sparse pair joint-occupancy peel

## Status

`COMPLETE_PAIRWISE_JOINT_OCCUPANCY_SPARSE_LAYER_PEEL`

Consumes merged `Stage14-s7-55`, merged `Stage14-s7-52`, merged `Stage14-4dl`, and merged `Stage14-X15`.

The current whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

For the representative pair `(+,-)` define in each surviving full-conductor conditioning cell

```text
mu_+  = E W_+,
mu_-  = E W_-,
mu_{+-}=E[W_+W_-].
```

The pair-density defect of s7-55 is

```text
Delta_pair = mu_{+-} - mu_+ mu_-.
```

Merged s7-52 already restricts the marginals to the interior dense regime

```text
mu_+=B^(-o(1)),
mu_-=B^(-o(1)),
1-mu_+=B^(-o(1)),
1-mu_-=B^(-o(1)).
```

## 1. Sparse joint occupancy is automatically strict sub-square-root

Fix any `delta>0`.  On a dyadic joint-occupancy layer

```text
mu_{+-}=B^(-delta+o(1)),
```

the actual pair-selected mass in that conditioning cell is the charged-once ambient cell mass multiplied by `mu_{+-}`.  Since the ambient mass is at most

```text
B^(1/2+o(1)),
```

this layer contributes

```text
<< B^(1/2-delta+o(1)).
```

Therefore every fixed-power sparse joint-occupancy layer is strict sub-square-root.

```text
PAIR_JOINT_OCCUPANCY_FIXED_POWER_DEFICIT_STRICT_SUBSQRT=true
PAIR_JOINT_OCCUPANCY_LAYER_EXPONENT=1/2-delta
```

## 2. Square-root pairwise saturation requires dense joint occupancy

Consequently a pairwise branch can survive at square-root scale only if

```text
boxed:
mu_{+-}=B^(-o(1)).
```

Together with s7-52, the surviving pairwise joint-density receiver has simultaneously

```text
mu_+=B^(-o(1)),
mu_-=B^(-o(1)),
mu_{+-}=B^(-o(1)),
1-mu_+=B^(-o(1)),
1-mu_-=B^(-o(1)).
```

Thus neither marginal sparsity nor joint sparsity can support square-root saturation.

This does **not** prove the pair-density defect small: a dense joint occupancy may still differ from `mu_+mu_-` by main-term scale.

## 3. No triple charge across the three pairwise coordinate realizations

Merged s7-54 proves that the three pairwise branches

```text
(+,-), (+,k), (-,k)
```

are fixed-power finite-fiber coordinate realizations of the same primitive Pythagorean two-projection mass.  Hence the sparse-joint peel above is applied to one representative pair only and is not multiplied across the three coordinate descriptions.

```text
PAIRWISE_REPRESENTATIVE_PAIR=(+,-)
PAIRWISE_DOUBLE_CHARGE_ALLOWED=false
```

## 4. Relation to s7-55 centered error

The s7-55 exact decomposition remains

```text
Gamma_{+-}
 = Delta_pair + Err_pair,
```

where `Err_pair` is the masked centered full-conductor inverse-fraction error.

Stage14-s7-56 only removes fixed-power sparse `mu_{+-}` layers.  It does not control `Delta_pair` on dense joint cells and does not control `Err_pair`.

Therefore the current pairwise square-root receiver is

```text
FullConductorInteriorDensePairJointOccupancy
PrincipalDefectPlusCenteredInverseFractionCorrelation.
```

## 5. H decision

No new H is opened.  The next deterministic step is to normalize the dense pair defect against its Bernoulli covariance envelope and separate near-deterministic pair coupling from genuinely oscillatory centered error.

```text
S7_56_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_56=COMPLETE_PAIRWISE_JOINT_OCCUPANCY_SPARSE_LAYER_PEEL
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PAIR_JOINT_OCCUPANCY_FIXED_POWER_DEFICIT_STRICT_SUBSQRT=true
PAIR_JOINT_OCCUPANCY_LAYER_EXPONENT=1/2-delta
PAIRWISE_SQRT_SATURATION_REQUIRES_MU_PAIR=Bo0=true
PAIRWISE_REPRESENTATIVE_PAIR=(+,-)
PAIRWISE_DOUBLE_CHARGE_ALLOWED=false
S7_56_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
NEXT=Stage14-s7-57
```
