# Stage14-tH6 — abstract power-saving transfer receiver

## Purpose

Stage14-tH1 through tH5 build a roadworks chain which is deliberately independent of the live `t` stage number:

```text
tH1  Gaussian primary/ray-class normalization
  -> tH2 divisor-coupled norm hyperbola
  -> tH3 all-order conductor/shared-modulus adapter
  -> tH4 weighted Mellin/Hecke transfer toolbox
  -> tH5 exact Gaussian-pair coefficient collision energy
```

Stage14-tH6 turns that chain into a reusable **power-saving receiver**.

Its job is not to prove the missing same-modulus theorem.  Its job is to answer the following question exactly:

> If some later theorem supplies a fixed power saving at the shared-modulus analytic interface, how much of that saving survives after every tH roadworks cost and every square-root conversion is charged?

The answer is encoded as an exponent ledger.  In the standard tH1--tH5 path every roadworks contribution is `B^o(1)`, so every fixed positive saving survives.  If a future path introduces a genuine fixed-power overhead, the same ledger states exactly how much margin is lost.

No future live `t` result is required.

---

## 1. Fixed-power exponent convention

Write every analytic quantity in the form

\[
B^{\alpha+o(1)}.
\]

Only the fixed exponent `alpha` is entered in the tH6 ledger.  Polylogarithms, divisor bounds `tau_max(B)=B^{o(1)}`, bounded spectral energy, bounded Mellin kernels, finite sign/orientation states and fixed unit-orbit factors all contribute exponent zero.

For a roadworks factor `R(B)` define

\[
\omega(R)=\inf\{\omega:\ R(B)\le B^{\omega+o(1)}\}.
\]

The tH1--tH5 standard interfaces give

```text
Gaussian unit/orientation normalization exponent       0
finite epsilon/g state exponent                        0
divisor/hyperbola lift exponent                        0
mu4 conductor correction exponent                      0
bounded spectral packet exponent                       0
bounded Mellin/smooth kernel exponent                   0
dyadic/conductor assembly exponent                     0
exact Gaussian-pair collision exponent                 0
```

Thus the standard total roadworks exponent is

\[
\boxed{\Omega_{\rm road}=0.}
\tag{H6.1}
\]

The statement means `B^o(1)`, not an absolute constant.

---

## 2. Generic squared-second-moment input

Let `A(U,V)` be a coefficient vector on an exact tH5 Gaussian-pair block.  Suppose a future **same-modulus** theorem proves

\[
\boxed{
\mathcal M(A)
\le
B^{-\Gamma+o(1)}\,
\mathcal M_0(B)\,\|A\|_2^2,
}
\tag{H6.2}
\]

where

- `M_0(B)` is the no-saving baseline appropriate to that theorem;
- `Gamma>=0` is the fixed saving exponent at the **squared second-moment level**;
- the common auxiliary modulus of `U` and `V` is retained.

Now allow all roadworks layers to contribute a total fixed exponent `Omega>=0` in squared norm.  Then tH4/tH5 transfer gives

\[
\boxed{
\mathcal M_{\rm road}
\le
B^{-(\Gamma-\Omega)+o(1)}
\mathcal M_0(B)\,\|w\|_2^2.
}
\tag{H6.3}
\]

Hence the surviving squared-level saving is

\[
\boxed{
\Gamma_{\rm eff}=\Gamma-\Omega.
}
\tag{H6.4}
\]

A fixed positive saving survives iff

\[
\boxed{\Gamma>\Omega.}
\tag{H6.5}
\]

For the standard tH1--tH5 road,

\[
\boxed{\Gamma_{\rm eff}=\Gamma-o(1).}
\tag{H6.6}
\]

So tH itself does not consume a fixed positive exponent.

---

## 3. One Cauchy/square-root conversion

Many square-sieve, duality and second-moment arguments turn a squared estimate into an amplitude or target-count estimate through one square root.

If the downstream conversion uses exactly one Cauchy square root, then

\[
B^{-\Gamma_{\rm eff}}
\quad\leadsto\quad
B^{-\Gamma_{\rm eff}/2}.
\]

Therefore the delivered saving exponent is

\[
\boxed{
\delta_{\rm delivered}
=\frac{\Gamma-\Omega}{2}.
}
\tag{H6.7}
\]

provided `Gamma>Omega`.

The factor `1/2` is not hidden.  A future theorem which works directly at count level must instead use the direct-count channel in section 4.

```text
SECOND_MOMENT_TO_AMPLITUDE_ROOT_LOSS=2
ROOT_LOSS_HIDDEN=false
```

---

## 4. Direct-count input channel

Some later arguments may already prove a target-count estimate on a physical block:

\[
\boxed{
N_{\rm target}(\mathcal B)
\le
B^{-\Delta+o(1)}
N_{\rm ambient}(\mathcal B).
}
\tag{H6.8}
\]

If post-theorem roadworks/recombination costs a fixed exponent `Omega_count`, then

\[
\boxed{
\delta_{\rm count,eff}
=\Delta-\Omega_{\rm count}.
}
\tag{H6.9}
\]

Again a fixed positive saving survives iff

\[
\Delta>\Omega_{\rm count}.
\]

For standard tH recombination,

\[
\Omega_{\rm count}=0
\]

at the fixed-power level.

The squared-second-moment and direct-count channels must not be mixed.  Every future application must state which exponent it is supplying.

---

## 5. Canonical tH6 saving ledger

A later stage should publish the following record before claiming any transferred saving:

```text
PowerSavingTransferLedger:
  input_channel:
    kind: squared_second_moment | direct_count
    raw_saving_exponent
    baseline_quantity

  fixed_power_overheads:
    gaussian_normalization
    finite_state_sum
    divisor_hyperbola_lift
    conductor_adapter
    spectral_energy
    mellin_kernel
    dyadic_assembly
    exact_pair_collision
    other_declared

  total_overhead_exponent: Omega

  conversion:
    root_loss = 2     # only for squared_second_moment channel

  output:
    effective_squared_saving
    delivered_count_or_amplitude_saving
    positive_fixed_saving_survives
```

No cost is allowed to disappear into an unspecified `harmless factor` if it can grow like a fixed power of `B`.

---

## 6. Standard tH1--tH5 overhead ledger is zero

The previous roadworks stages give the following exact fixed-power classification.

### tH1
Primary associates, Gaussian units, conjugate orientations and the finite `(1+i)` correction are finite-state effects.  For the live `mu_4`-trivial specialization tH3 in fact gives `e2=0` exactly.

\[
\omega_{\rm tH1}=0.
\]

### tH2
The number of dyadic hyperbola blocks is polylogarithmic.  Divisor multiplicity is `B^{o(1)}`.

\[
\omega_{\rm tH2}=0.
\]

### tH3
The joint conductor is an `lcm`, and a shared oriented Gaussian prime is counted once.  No artificial second modulus or fixed conductor power is introduced.

\[
\omega_{\rm tH3}=0.
\]

### tH4
Masks and unit phases are `L^2`-contractive/isometric; divisor and Gaussian-representation lifts are divisor-bounded; conductor bands and block assembly are polylogarithmic.  Under the declared bounded/subpolynomial spectral and Mellin budgets,

\[
\omega_{\rm tH4}=0.
\]

### tH5
Exact `(U,V)` coefficient collisions have multiplicity at most `tau_max`, hence exact pair collapse has `B^{o(1)}` energy overhead.

\[
\omega_{\rm tH5}=0.
\]

Therefore

\[
\boxed{
\Omega_{\rm road}
=\omega_{\rm tH1}+\cdots+\omega_{\rm tH5}=0.
}
\tag{H6.10}
\]

This is the central tH6 transfer statement.

---

## 7. Stage14 post-local threshold translation

The closed local Stage14 bound is

\[
\#Q_B\ll B^{41/42+o(1)}.
\]

A **direct physical count saving** `delta_post` would produce

\[
\#Q_B\ll B^{41/42-\delta_{\rm post}+o(1)}.
\tag{H6.11}
\]

Since

\[
\frac{41}{42}-\frac12=\frac{10}{21},
\]

the square-root upper-bound threshold is

\[
\boxed{
\delta_{\rm post}\ge\frac{10}{21}.
}
\tag{H6.12}
\]

If the only analytic input is a squared-second-moment saving `Gamma` and exactly one square-root conversion is required, the standard tH road has `Omega=0`, so

\[
\delta_{\rm post}=\frac\Gamma2.
\]

Thus the corresponding conditional threshold is

\[
\boxed{
\Gamma\ge\frac{20}{21}.
}
\tag{H6.13}
\]

More generally, with fixed-power road overhead `Omega`, one needs

\[
\boxed{
\Gamma-\Omega\ge\frac{20}{21}.
}
\tag{H6.14}
\]

This is only an exponent-conversion statement.  tH6 does **not** prove such a same-modulus theorem and does not prove `#Q_B << B^(1/2+o(1))`.

---

## 8. Margin classes

For automated routing define the second-moment margin

\[
\mathfrak m_2=\Gamma-\Omega
\]

and the direct-count margin

\[
\mathfrak m_1=\Delta-\Omega_{\rm count}.
\]

Classify:

```text
margin < 0   -> FAIL: road overhead exceeds claimed saving
margin = 0   -> CRITICAL: no fixed positive saving survives
margin > 0   -> POSITIVE: a fixed saving survives
```

For one-root second-moment transfer the delivered saving is `m_2/2`.

This simple classification is useful because a later live proof may improve the raw analytic exponent while the roadworks ledger remains frozen.

---

## 9. Stress-test scenarios

The tH6 audit freezes exact rational test cases.

### Squared-second-moment channel

```text
Gamma      Omega      effective squared    delivered after sqrt
1/3        0          1/3                  1/6
20/21      0          20/21                10/21
1          1/21       20/21                10/21
1/2        1/6        1/3                  1/6
1/4        1/4        0                    0
1/5        1/4       -1/20                 FAIL
```

### Direct-count channel

```text
Delta      Omega_count   delivered
1/5        0             1/5
10/21      0             10/21
1/2        1/42          10/21
1/4        1/4           0
```

The audit uses exact `Fraction` arithmetic, so threshold comparisons do not depend on floating point.

---

## 10. What tH6 closes and what it does not

Closed:

1. exact fixed-power bookkeeping for all tH1--tH5 roadworks layers;
2. proof that the standard road has total fixed exponent zero;
3. exact transfer formula from squared same-modulus saving to post-road squared saving;
4. exact one-square-root conversion formula;
5. exact direct-count transfer formula;
6. exact translation of the Stage14 `10/21` post-local requirement into a conditional `20/21` squared-second-moment requirement under one root loss.

Not closed:

1. the missing same-modulus joint theorem itself;
2. any claim that a particular live `t` stage supplies `Gamma>0` in the tH6 sense;
3. same-modulus residue-collision energy in full generality;
4. global `A_11` power saving;
5. the square-root upper bound;
6. a perfect-cuboid nonexistence theorem.

The next roadworks task should therefore be a stress-test/PARK stage: verify that tH1--tH6 exposes every input required by several plausible future same-modulus theorems and identify any missing adapter before parking the roadworks line.

---

## Boundary

```text
STAGE14_TH6=COMPLETE_ABSTRACT_POWER_SAVING_TRANSFER_RECEIVER
TH_REQUIRES_FUTURE_T_RESULT=false
STANDARD_TH1_TH5_FIXED_POWER_OVERHEAD=0
SQUARED_SECOND_MOMENT_EFFECTIVE_SAVING=Gamma-Omega
ONE_ROOT_DELIVERED_SAVING=(Gamma-Omega)/2
DIRECT_COUNT_EFFECTIVE_SAVING=Delta-Omega_count
POSITIVE_FIXED_SAVING_SURVIVES_IFF_RAW_GT_OVERHEAD=true
CURRENT_LOCAL_CLASS_B_EXPONENT=41/42
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
ONE_ROOT_SQUARED_SAVING_REQUIRED_FOR_SQRT_B=20/21+Omega
SAME_MODULUS_JOINT_SECOND_MOMENT_THEOREM_PROVED=false
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-tH7
```
