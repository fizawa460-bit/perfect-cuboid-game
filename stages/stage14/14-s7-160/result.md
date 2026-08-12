# Stage14-s7-160 — nonunit Q-supported valuation stratification

## Status

`COMPLETE_NONUNIT_Q_VALUATION_TO_REDUCED_MODULUS_STRATIFICATION`

Let

```text
Q=2UV,
f*n=W1(lambda).
```

Fix one prime `ell|Q`. Write

```text
a_ell=v_ell(2U),
b_ell=v_ell(2V),
alpha=v_ell(f),
beta=v_ell(n).
```

For odd `ell`, primitive `gcd(U,V)=1` implies at most one of `a_ell,b_ell` is positive. Put

```text
e_ell=max(a_ell,b_ell).
```

If

```text
k=min(alpha,beta) < e_ell,
```

then the required congruence `n+f == 0 (mod ell^e_ell)` or `n-f == 0 (mod ell^e_ell)` forces

```text
alpha=beta=k.
```

Indeed unequal valuations would give valuation exactly `min(alpha,beta)=k` for the relevant sum/difference, contradicting divisibility by `ell^e_ell`.

After dividing both reciprocal factors by `ell^k`, the residual pair is unit at `ell` and satisfies a unit quotient residue condition modulo

```text
ell^(e_ell-k).
```

If instead

```text
min(alpha,beta) >= e_ell,
```

the local congruence is saturated and contributes no residual modulus at `ell`.

The two-primary place is kept in the already-frozen finite parity/two-primary chart; no odd-prime argument is cross-promoted through it.

Thus every admissible Q-supported valuation pattern `nu` determines exactly:

1. common local powers stripped from `(f,n)` at unsaturated primes;
2. saturated local primes that disappear from the residual congruence;
3. a reduced modulus

```text
Q_nu | Q
```

such that the remaining unsaturated reciprocal quotient is a unit residue class modulo `Q_nu`.

The original unit stratum is the pattern with `Q_nu=Q`. Fully saturated patterns may have `Q_nu=1`.

For a fixed witness, the number of possible valuation allocations is bounded by divisor multiplicity `B^o(1)`, already available from the reciprocal factorization. This is only a pointwise multiplicity statement. Across the charged family the valuation pattern may move, so one global `nu` is not frozen and the `nu`-average must be retained.

```text
Q25_NONUNIT_Q_VALUATION_STRATIFICATION_TEST=PASS_REDUCED_MODULUS_UNIT_RESIDUE_AFTER_LOCAL_STRIPPING
NONUNIT_UNSATURATED_EQUAL_VALUATION_NECESSITY_PROVED=true
NONUNIT_REDUCED_MODULUS_Q_NU_PROVED=true
NONUNIT_VALUATION_PATTERN_AVERAGE_MUST_BE_RETAINED=true
NONUNIT_VALUATION_MULTIPLICITY_RECHARGED=false
TWO_PRIMARY_CHART_PRESERVED=true
S_ROUTE_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-s7-161
```