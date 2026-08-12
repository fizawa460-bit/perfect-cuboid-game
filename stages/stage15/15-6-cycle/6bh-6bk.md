# Stage15-6-cycle — 6bh through 6bk

Base: merged PR #851.

## Visible audit ledger

```text
6bh  admissible-S support as independent theorem       BLOCK
6bi  complementary Gaussian-product square receiver   PASS
6bj  equal-hypotenuse / generic square-sieve route     BLOCK
6bk  joint-core endpoint spacing as fresh information  BLOCK
```

### 6bh
Fixed-S fibers are `B^o(1)`, so `|S(B)|` and `N2(B)` are equivalent up to subpolynomial factors. A half-power support theorem is therefore a restatement of the target, not a causal simplification.

### 6bi
The S/O orientation split yields two exact complementary square products

\[
\alpha_0\beta_0=\epsilon_O\delta k_O\Xi_O^2,
\qquad
\alpha_0\overline{\beta_0}=\epsilon_S\delta k_S\Xi_S^2,
\]

both of norm `S^2`. This gives two equal-hypotenuse Pythagorean triples and exact endpoint inversion.

### 6bj
Equal hypotenuse is algebraically equivalent to the rank-one endpoint identity after inversion, so it contributes no independent equation. Generic square-sieve tuple bounds do not automatically become the required physical support bound.

### 6bk
Pushing the complementary core divisibilities through the Stage15-6al four cells gives apparent new root-line congruences, but the cell variables satisfy `m/n=A/B`, `r/s=C/D`. The congruences are exactly the original 6aa S/O two-channel lock in transformed coordinates. Recharging them would violate AR-028.

## Cycle conclusion

The causal audit has now traversed Gaussian squares, genus-one models, 2-descent, physical diagonal support, complementary Gaussian products and four-cell endpoints, and returns exactly to the initial Stage15-6aa obstruction:

```text
moving (k_S,k_O)
+ two-channel root lines
+ physical R<=B measure
--------------------------------
need one legal whole-family global charge
```

No contradiction is present, but no independent second saving was discovered. A future continuation must bring a genuinely new global measure theorem or a new exact variable that fixes the moving channel core before counting. Repackaging the same core through elliptic, S-support, or endpoint coordinates is exhausted.

```text
STAGE15_6_CYCLE_START=6bh
STAGE15_6_CYCLE_END=6bk
STAGE15_6_CYCLE_AUDIT_LEDGER=BLOCK,PASS,BLOCK,BLOCK
STAGE15_6_CYCLE_SUPPORT_BLACKBOX_CIRCULAR=true
STAGE15_6_CYCLE_COMPLEMENTARY_GAUSSIAN_PRODUCTS=true
STAGE15_6_CYCLE_EQUAL_HYPOTENUSE_NEW_SAVING=false
STAGE15_6_CYCLE_ENDPOINT_CORE_ROUTE_NEW_SAVING=false
STAGE15_6_CYCLE_RETURNS_TO_6AA_TWO_CHANNEL_GATE=true
STAGE15_6_CYCLE_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6_CYCLE_EXIT=STABLE_GLOBAL_TWO_CHANNEL_CHARGE_OBSTRUCTION_RECONFIRMED
```
