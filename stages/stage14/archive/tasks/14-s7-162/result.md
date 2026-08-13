# Stage14-s7-162 — reduced-modulus character-family complexity test

## Status

`COMPLETE_REDUCED_MODULUS_CHARACTER_FAMILY_COMPLEXITY_NO_COLLAPSE`

This stage consumes merged Stage14-s7-159..161 and merged Stage14-Work-cnX52/q26 at final-batch start main

```text
9632d760afcf529aeae5e56a40820b6cfbced44c
```

and preserves the exact valuation-averaged decomposition

```text
J_ccs = sum_nu J_nu = P_red + E_red,
Q_nu | Q=2UV.
```

For one admissible valuation pattern `nu` with `Q_nu>1`, let

```text
S_nu(a)
```

be the retained nonnegative filtered-tau3/common-core weight whose stripped reciprocal quotient is the unit class `a mod Q_nu`. Then

```text
A_nu,chi = sum_a S_nu(a) chi(a)
```

and the exact character expansion uses every Dirichlet character modulo `Q_nu`. Thus its algebraic character count is

```text
phi(Q_nu).
```

The `B^o(1)` statement from Stage14-s7-160 concerns the number of valuation allocations over one fixed witness. It does not bound `phi(Q_nu)`, does not freeze one reduced modulus across the charged family, and does not turn the union of character groups into a `B^o(1)` family.

In particular, the unit valuation pattern, whenever it has retained mass, has

```text
Q_nu=Q,
character count=phi(Q).
```

It has not been proved uniformly empty. On any retained cell with

```text
Q=B^(q+o(1)), q>0,
```

the standard lower order for Euler's totient gives

```text
phi(Q)=Q^(1-o(1))=B^(q+o(1)),
```

so the full character expansion is polynomial rather than subpolynomial. Reduced nonunit patterns may also retain positive-exponent moduli. No merged identity confines all mass to saturated `Q_nu=B^o(1)` patterns.

This does not assert that the characters are statistically independent or that every possible pattern occurs with positive density. It proves the narrower decision needed here: the existing exact algebra does not collapse the required uniform character family to `B^o(1)` complexity, so a character-by-character estimate cannot be summed at zero power cost.

```text
Q26_REDUCED_MODULUS_CHARACTER_FAMILY_COMPLEXITY_TEST=FAIL_NO_UNIFORM_BO1_COLLAPSE
VALUATION_PATTERN_POINTWISE_FIBER_COMPLEXITY=Bo1
VALUATION_PATTERN_BO1_IMPLIES_CHARACTER_FAMILY_BO1=false
CHARACTER_COUNT_PER_NONSATURATED_PATTERN=phi_Qnu
UNIT_PATTERN_CHARACTER_COUNT=phi_Q
UNIT_PATTERN_UNIFORMLY_EMPTY_PROVED=false
POSITIVE_Q_EXPONENT_IMPLIES_POLYNOMIAL_CHARACTER_COUNT=true
ALL_RETAINED_MASS_ON_SUBPOLYNOMIAL_REDUCED_MODULI_PROVED=false
REDUCED_MODULUS_CHARACTER_FAMILY_COMPLEXITY_BO1_PROVED=false
FULL_PHYSICAL_PACKET_PRESERVED=true
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-163
```
