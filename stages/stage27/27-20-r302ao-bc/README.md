# Stage27-20-r302ao-bc batch

This batch resumes from merged PR #1250 and advances checkpoint40 from `r302ao` through `r302bc`.

The first task is a successor repair: PR #1250's `r302v-an` chain promoted a fixed-additive-frequency primitive Gauss magnitude statement to a frequency-flat **full gcd-stratum** kernel. SR-GATE-35A/36A does not justify that promotion because the sum over all `a` with `(a,q)=d` remains inside the physical stratum kernel. This batch does not rewrite main history; it records the correction prospectively and stops using the old A/B/C package.

The corrected chain then:

1. recombines one `(a,q)=d` stratum exactly as a Ramanujan multiplier `c_{q/d}(f^2-C)/q`;
2. recombines all strata exactly to the original root projector `1_{f^2=C mod q}`;
3. proves the local root projector has generic `L2` operator norm one when roots exist, so arbitrary-coefficient power contraction is not the canonical target;
4. derives the actual-`W` root-energy receiver;
5. bounds root multiplicity by `B^o(1)s_q(C)` with explicit singular square-root factor `s_q(C)`;
6. replaces pointwise effective support by the normalized fourth-moment collision index;
7. reduces the entire sufficient fixed-power input to the same-`H_phys^MAIN` weighted theorem

```text
Z(W,C)=s_q(C)^3
       * sum_f |W(f)|^4 /(sum_f |W(f)|^2)^2,

sum_packet H_phys^MAIN(packet) Z(W,C)
 <= B^{-gamma+o(1)} sum_packet H_phys^MAIN(packet).
```

The same quantity splits exactly into a structural zero mode `s_q(C)^3/q` and a nonzero Fourier-energy term for `|W|^2`.

StructureRadar/Arsenal use:
- SR-STR-019: generalized CRT algebra only;
- SR-STR-169: finite Fourier/Gauss and same-measure architecture;
- SR-STR-173: moment-to-support / same-measure firewall;
- AR-012: optional peak-multiplicity adapter only, not a density saving.

No fixed-power theorem is proved in this batch. Checkpoint remains 40 and `mu=1/2` remains unchanged.

```text
BATCH_ID=Stage27-20-r302ao-bc
BASE_MAIN=e27bc3134d8f1c8ce385ce614e5e9f9bc1437ecb
PARENT_MERGE_PR=1250
PARENT_AUDIT_RECORD_PRESENT=false
ROUTES=r302ao,r302ap,r302aq,r302ar,r302as,r302at,r302au,r302av,r302aw,r302ax,r302ay,r302az,r302ba,r302bb,r302bc
NEXT_DERIVED_ROUTE=27-20-r302bd
NEXT_EXPECTED_COMMAND=Stage27-20-r302-audit
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
```