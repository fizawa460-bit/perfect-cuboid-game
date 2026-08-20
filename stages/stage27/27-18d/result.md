# Stage27-18d — Stage18 mass localization

```text
TASK_ID=Stage27-18d
ROLE=MASS_LOCALIZATION
STATUS=RECEIVER_EXTRACTED
```

Let `Omega18(B)` be the literal Stage18 physical source population and give every object unit mass.  Via 27-18b, attach to each object its unique frozen toric representative and the invariants

- paired Gaussian norms `(A,D)`;
- common squarefree-kernel candidate coordinates;
- primitive scaling/core `G` and reduced-direction data from the Stage19 normal form;
- dyadic sizes of `A,D,G` and reduced-direction height.

For any dyadic packet `T` in these invariants define

`M18,T(B) = # {omega in Omega18(B): omega lies in T}`.

These packets form a disjoint (up to boundary conventions) partition of the same physical Stage18 measure, so

`sum_T M18,T(B) = M2(B) ~ C_M2 B (log B)^5`.

No independence is asserted between packet coordinates.  No packet receives a fixed-power estimate merely from the global asymptotic.

The localization question relevant to Stage19 is now exact: for each packet define the survivor mass

`S_T(B)=# {omega in Omega18(B) in T : sf(A)=sf(D)}`.

Then

`N2(B)=sum_T S_T(B)`

with no population or multiplicity adapter.

This exposes two mathematically distinct ways forward:

- **upper survival:** prove `S_T <= B^{-delta+o(1)} M18,T` on all packets carrying all but `B^{-delta0}` of the Stage18 mass, with a separately controlled exceptional packet mass;
- **lower survival:** exhibit a positive-dimensional physical subfamily contained in high-mass packets for which the squareclass equality holds and height/multiplicity are controlled.

The current repository does not contain a packetwise asymptotic for `M18,T`; deriving one is a genuine new localization theorem, not a corollary of `M2(B)~C B(log B)^5`.  Accordingly 27-18d stops at the exact same-measure localization ledger rather than inventing a distribution law.

```text
GLOBAL_MASS_PARTITION_EXACT=true
PACKETWISE_STAGE18_ASYMPTOTIC_PROVED=false
SURVIVOR_SUM_IDENTITY_EXACT=true
MEASURE_CHANGE=false
NEXT_DERIVED_ROUTE=Stage27-18e
```
