# Stage27-19-r5aw — fixed-R physical fiber and exact boundary factorization

```text
TASK_ID=Stage27-19-r5aw
BATCH_ID=Stage27-19-r5
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5at-r5av
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
BASE_MAIN=4045fc9a613e7c9582b586e8151bce5a371d3942
```

The audited r5at-r5av batch removed the varying-modulus `K` entropy after fixing the physical space diagonal `R`, but left two possible successors:

1. count the actual fixed-`R` physical support rather than the raw coefficient host; or
2. factor the boundary congruences more exactly and test whether the accumulated `sqrt(X_R)` term acquires a genuine modulus saving.

StructureRadar has now paused and explicitly returned to Stage27. Its SR-STR-224 search found Ford-type divisor-window theory adjacent but no published theorem that legally removes the exact physical hyperbolic boundary. This route therefore does **not** restart a generic literature search. It resolves the first successor on the physical-object level and rewrites the second successor as an exact divisor/Gaussian-factor receiver.

## 1. Lifecycle and operator-freeze reconciliation

PR #1072 (`Stage27-19-r5at-r5av`) was independently audited `PASS` and merged at

```text
MERGE_COMMIT=a38d6e782718ed01bb813c477f3f021afbf3d47d
AUDITED_CONTENT_COMMIT=34c24f3a61176f652a0f35b84d9c74c351879270
AUDITED_LIFECYCLE_HEAD=02a56737ff56046d1c60523663b2d70c9a7b9d1f
```

The earlier `DO_NOT_START_R5AW` operator freeze was conditional on the StructureRadar / Arsenal census. The current StructureRadar controller has returned to Stage27 with

```text
campaign_state=PAUSED_RETURN_TO_STAGE27
return_targets=Stage27-19,Stage27-20
remaining_external_gates_mandatory_before_stage27=false
```

so the freeze is no longer active.

## 2. Fixed-R physical exactly-two fiber is subpower

Fix a positive integer physical space diagonal `R`. Consider one primitive canonical physical cuboid counted by `N_2` with exactly two integral face diagonals.

The two integral faces share a unique physical edge; call it `e`, and call the other two edges `x,y`. Let

```text
D_x^2=e^2+x^2,
D_y^2=e^2+y^2
```

be the two integral face diagonals. Since the space diagonal is `R`,

```text
R^2=e^2+x^2+y^2=D_x^2+y^2=D_y^2+x^2.       (F1)
```

Therefore every fixed-`R` exactly-two cuboid determines two positive representations of `R^2` as a sum of two squares. To forget all canonical ordering/orientation details safely, retain only which of the three physical edges is the shared edge and the two ordered signed sum-of-two-squares representations. This gives the crude but uniform injection bound

```text
N_{2,R} <= 3 r_2(R^2)^2.                     (F2)
```

Here `r_2(n)` is the classical number of ordered signed representations `u^2+v^2=n`. The standard formula implies

```text
r_2(n) <= 4 tau(n),
```

hence

```text
N_{2,R} <= 48 tau(R^2)^2 = R^o(1).           (F3)
```

Thus the **physical object fiber at fixed `R` is subpower**.

This is stronger than the raw r5av coefficient-cell host as a statement about actual physical cuboids, but it is not a new global exponent theorem. In particular, (F3) controls physical objects, not every Stage19 parameter tuple before the physical quotient/multiplicity normalization.

```text
FIXED_R_PHYSICAL_N2_FIBER_SUBPOWER_PROVED=true
FIXED_R_PHYSICAL_N2_BOUND=3*r2(R^2)^2<=48*tau(R^2)^2=R^o(1)
FIXED_R_OUTER_PARAMETER_SUPPORT_SUBPOWER_PROVED=false
```

## 3. Why fixed-R subpower support alone is globally inert

Summing the fixed-`R` estimate naively over all `R<=B` gives only

```text
sum_{R<=B} N_{2,R} <= B^(1+o(1)).             (F4)
```

This is much weaker than the already proved Stage14 whole-family theorem

```text
N_2(B) << B^(1/2+o(1)).
```

Therefore the fixed-`R` fiber theorem cannot be charged as an independent density saving on top of Stage14. It resolves a local support question but does **not** improve `mu=1/2`.

A useful global continuation now needs at least one of:

- a fixed-power deficit in the set/measure of occupied physical diagonals `R` compatible with the existing Stage14 charged measure; or
- a genuine modulus saving in the r5au/r5av hyperbolic boundary term on the exact physical measure.

```text
FIXED_R_FIBER_ALONE_GIVES_STRICT_SUBSQRT=false
NAIVE_R_SUM_BOUND=B^(1+o(1))
OCCUPIED_R_FIXED_POWER_DEFICIT_PROVED=false
NO_DOUBLE_CHARGE_WITH_STAGE14=true
```

## 4. Exact factorization of the first kappa congruence

The audited r5an receiver gives

```text
kappa | m^2-n^2,
kappa | r^2+s^2,
(kappa,m*n*r*s)=1,
```

where `kappa` is odd and squarefree, and every prime divisor of `kappa` is `1 mod 4`.

Because

```text
m^2-n^2=(m-n)(m+n)
```

and

```text
gcd(m-n,m+n) | 2,
```

no odd prime `p|kappa` can divide both factors. Define

```text
kappa_- = gcd(kappa, |m-n|),
kappa_+ = kappa/kappa_-.
```

Then exactly

```text
gcd(kappa_-,kappa_+)=1,
kappa_- | (m-n),
kappa_+ | (m+n),
kappa=kappa_-*kappa_+.
```

With the signed integer

```text
A=(m-n)/kappa_-
```

and positive integer

```text
B=(m+n)/kappa_+,
```

one reconstructs

```text
m=(kappa_-*A+kappa_+*B)/2,
n=(kappa_+*B-kappa_-*A)/2.                   (F5)
```

Thus the `m/n = +/-1 mod p` root choice has an exact global divisor-factor interpretation: it is the choice of a coprime factorization `kappa=kappa_- kappa_+` assigning each prime to `m-n` or `m+n`. The number of such assignments is at most

```text
2^omega(kappa)=kappa^o(1).
```

No `K`-power saving follows from this entropy statement alone.

## 5. Exact Gaussian factorization of the second kappa congruence

For every prime `p|kappa`, `p=1 mod 4`, so in `Z[i]`

```text
p=pi_p * conjugate(pi_p).
```

The congruence `p | r^2+s^2=N(r+i s)` means one of the two Gaussian primes above `p` divides `r+i s`. They cannot both divide `r+i s`, because then their product `p` would divide both `r` and `s`, contradicting `(r,s)=1`.

Choose for each `p|kappa` the unique conjugate side dividing `r+i s`, and put

```text
lambda = product_{p|kappa} pi_p.
```

Up to a Gaussian unit,

```text
lambda | (r+i s),
N(lambda)=kappa,
r+i s=lambda*eta,
N(eta)=(r^2+s^2)/kappa.                      (F6)
```

Again the choice count is at most `2^omega(kappa)=kappa^o(1)` (up to four units). The `r/s = +/- i_p mod p` root choice has therefore been replaced by an exact norm-factor allocation.

Combining (F5) and (F6), the modular root-choice packet from r5an/r5aq is now an exact divisor/Gaussian-factor packet with only subpower allocation entropy at fixed `R` because `kappa|R`.

```text
EXACT_DIFFERENCE_FACTOR_SPLIT_PROVED=true
EXACT_GAUSSIAN_NORM_FACTOR_SPLIT_PROVED=true
KAPPA_ROOT_ALLOCATION_ENTROPY_AT_FIXED_R=R^o(1)
BOUNDARY_MODULUS_SAVING_PROVED=false
```

## 6. Exact witness check

The existing Stage19 witness

```text
(m,n,r,s)=(21,16,27,14),
kappa=185=5*37,
R=7585
```

makes both exact factorizations visible.

For the difference side,

```text
m-n=5,
m+n=37,
kappa_-=5,
kappa_+=37,
A=B=1,
```

and (F5) gives back `(m,n)=(21,16)`.

For the Gaussian side,

```text
lambda=11-8i=(2-i)(6-i),
N(lambda)=185,
eta=1+2i,
(11-8i)(1+2i)=27+14i.
```

The same witness has physical data

```text
(e,x,y)=(6048,1665,4264),
(D_x,D_y)=(6273,7400),
R=7585,
```

and indeed

```text
6273^2+4264^2=7585^2,
7400^2+1665^2=7585^2.
```

So both the fixed-`R` physical-fiber receiver and the exact boundary factorization attach to an actual Stage19 survivor, not merely to an ambient congruence model.

## 7. StructureRadar applicability verdict and next attack

StructureRadar SR-STR-224 already searched the adjacent divisor-window literature. Ford-type divisor-in-an-interval estimates are useful ambient context, but no theorem was found that transfers with the exact fixed-`R` physical masks and yields the needed boundary saving. The anti-loop rule therefore forbids restarting the same generic search under a renamed receiver.

The next admissible calculation is concrete rather than nominal:

1. substitute the exact `kappa_- / kappa_+` and Gaussian `lambda` factorization into the r5au dyadic boundary cells;
2. test whether the boundary count acquires any genuine negative power of `K` after preserving the physical product budget and coefficient weights;
3. if no `K`-power survives, freeze this r5 upper lane rather than minting another equivalent missing-theorem name, and return to the other Stage27 attack surface.

No such `K`-power is claimed in r5aw itself.

```text
STRUCTURE_RADAR_SR_STR_224_REUSED=true
GENERIC_DIVISOR_WINDOW_RESEARCH_RESTARTED=false
FACTORIZED_BOUNDARY_K_POWER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-19-r5ax
NEXT_TARGET=APPLY_EXACT_FACTOR_PACKET_TO_R5AU_BOUNDARY_AND_TEST_K_POWER_OR_FREEZE
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage27-19-r5-audit
```
