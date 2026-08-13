# Stage17-50 - lower-bound / construction ledger

Status: SUBMITTED_FOR_FRESH_AUDIT

Population is unchanged: primitive canonical `0<a<b<c`, `gcd=1`, exactly one integral face, integral `R`, `R<=B`, with `d=R`.

Stage13 applies literally and proves

`N_1(B) ~ (kappa/(24*pi)) B(log B)^3`,

so the sharp certified lower bound is

`N_1(B) >> B(log B)^3`.

This matches the audited Stage17-40 upper order.

AR-039 is an explicit Stage17 subfamily. For coprime `m>n`, `m=2 mod 14`, `n=1 mod 14`, it uses

`x=m^2-n^2`, `y=2mn`, `p=m^2+n^2`, `c=(p^2-1)/2`, `d=(p^2+1)/2`.

After canonical sorting it is primitive, exactly-one, and has integral space diagonal. Since `R=d`, the cutoff adapter is identity. AR-039 certifies

`N_1(B) >= sqrt(2)/(120*pi^2) B^(1/2) - O(B^(1/4)log B)`.

Thus Stage13 gives the sharp lower order, while AR-039 supplies a weaker but explicit infinite construction family. They are not multiplied or conflated.

```text
BEST_LOWER_BOUND=N_1(B)>>B(log B)^3
EXPLICIT_CONSTRUCTION=AR-039
CONSTRUCTION_CUTOFF_ADAPTER=IDENTITY via R=d
NEW_ANALYTIC_INPUT=false
EVIDENCE_LEVEL=PROVED
```

No new causal, independence, leading-constant, or perfect-cuboid conclusion is added. Checkpoint 60 waits for fresh Stage17-audit.
