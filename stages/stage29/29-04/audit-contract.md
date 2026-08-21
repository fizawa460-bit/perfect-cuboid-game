# Stage29-04 hostile audit contract

Fresh audit must verify the following load-bearing points before merge.

## A. Exhaustive physical partition

1. `U(B)` uses the same primitive/canonical `R<=B` physical convention as the frozen population program.
2. The four Boolean predicates `F_ab,F_ac,F_bc,S` really give an exhaustive disjoint `2^4=16` partition.
3. The exact-stage identifications are objectwise:
   - `E1=M1`, `E1 and S=N1`;
   - `E2=M2`, `E2 and S=N2`;
   - `E3=M3`, `E3 and S=P`.
4. In particular `M3=(E3 and not S) disjoint_union P`; the submission must not silently assume `P=0` globally.

## B. Nested-host semantics

Verify

```text
H_ge1=M1+M2+M3
H_ge2=M2+M3
H_ge3=M3
H_ge3 subset H_ge2 subset H_ge1 subset U
```

and

```text
S intersect H_ge1 = N1+N2+P
S intersect H_ge2 = N2+P
S intersect H_ge3 = P
```

The auditor should reject any conversion of the disjoint exact strata `M1 -> M2 -> M3` into a literal objectwise survival chain.

## C. Ratio semantics

Confirm that these are literal subset ratios:

```text
N1/M1
N2/M2
P/M3
H_ge1/U
H_ge2/H_ge1
H_ge3/H_ge2
```

and that these are not literal objectwise survival probabilities without an explicit host adapter:

```text
M2/M1
M3/M2
N2/N1
M3/N2
```

Cross-check Stage22, Stage26 and Stage28 semantics.

## D. Theorem-surface provenance

Fresh-check the imported current strongest population surface, especially:

- `M1 ~ 3/(4*pi^2) B^2 log B` rather than the older Stage16-only `asymp` statement;
- `N1 ~ kappa/(24*pi) B(log B)^3`;
- `M2 ~ C_M2 B(log B)^5`;
- current Stage28 `N2` lower exponent `1/4` and upper `1/2+epsilon`;
- current Stage28 `M3` one-third construction scale / liminf statement and upper `eta<1/46`;
- exact finite endpoint zero only through `B=10^9`.

If any displayed lower-bound quantifier needs epsilon-loss repair, repair the matrix rather than upgrading the theorem.

## E. Derived cost matrix

Independently rederive:

1. `H_ge1~M1`;
2. `H_ge2~M2`;
3. `H_ge1/U ~ 27*zeta(3)/pi^3 * (log B)/B`;
4. `H_ge2/H_ge1 ~ (4*pi^2*C_M2/3)(log B)^4/B`;
5. Stage26 literal completion observable `Phi=M3/(M2+M3)->0` with its certified corridor;
6. Stage21 `N1/M1 ~ (kappa*pi/18)(log B)^2/B`;
7. `N2/M2` corridor follows only from compatible lower/upper numerator bounds and `M2` asymptotic, with no multiplication of independent theorem species;
8. no global cost for `P/M3` is inferred.

## F. 16-cell versus 64-sheet firewall

The auditor must attack any suggestion that the physical Boolean partition and the sign/Kummer cover are the same object.

```text
PHYSICAL_BOOLEAN_CELL_COUNT=16
SIGN_KUMMER_GENERIC_DEGREE=64
BOOLEAN_16_EQUALS_SIGN_64=false
R29_KUM4_EXACT_ADAPTER_PROVED=false
```

29-04 may sharpen the receiver but may not discharge it.

## G. Backflow and advancement

No frozen Stage16-28 contract is reopened merely because the new host ledger is cleaner.

Expected safe submission state:

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
R29_KUM4_CONDITIONAL_BACKFLOW_WATCH=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage29-audit
```

The canonical Stage29 controller should be updated only during/after fresh audit while preserving all prior audited metadata.
