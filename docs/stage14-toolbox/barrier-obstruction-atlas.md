# Stage14 barrier and obstruction atlas

This atlas records the current Stage14 main/s barrier, the routes already audited as insufficient, the genuinely live theorem targets, and the support-route gates that may feed them.

It does not create a new theorem. Every mathematical status below is imported from merged repository results.

## 0. Atlas status vocabulary

```text
CURRENT_CHECKPOINT
  current proved whole-family theorem or current critical geometry

HISTORICAL_ARCHITECTURE
  once-current global architecture that is globally superseded but still contains reusable proved receivers

CLOSED_POSITIVE
  a former obstruction has been rigorously removed

CLOSED_NEGATIVE
  a proposed route was rigorously shown not to improve the current barrier with the stated ingredients

LIVE_PRIMARY
  a theorem that would directly produce a new main/s saving if proved with the recorded quantifiers

LIVE_BRIDGE
  a theorem on another exact receiver that may feed a LIVE_PRIMARY target only after an explicit operator/quantifier bridge

SUPPORT_TRIGGERED
  support-track work is explicitly required by a merged source

FORBIDDEN
  an invalid, circular, or quantifier-skipping shortcut
```

These are atlas labels, not replacements for canonical card `STATUS` values.

## 1. Current whole-family checkpoint

Merged Stage14-s7-13 proves

```text
V(B) << B^(7/8+o(1)).
```

The terminal current ledger is therefore

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
CURRENT_REMAINING_GAP_TO_SQRT=3/8
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=17/168
```

The exponent-critical common-refinement geometry is

```text
P,Q  ~ B^(1/2)
a,b  ~ B^(3/8)
x,y  ~ B^(1/16)
xi=ab~ B^(3/4).
```

Merged Stage14-4cb and Stage14-s7-14 independently compress this equality block to the shared squarefree label `xi`.

## 2. Barrier atlas

### A. Historical square-sieve barrier at 13/14

Status: `HISTORICAL_ARCHITECTURE`.

Merged s7-10 / 4by proves the adjacent two-cell receiver

```text
N_2cell(A,B) << (A*B)^(2/3) B^o(1),
```

and merged 4bz proves that the then-current square-root square-sieve architecture had exact minimax barrier `13/14`.

The global `13/14` checkpoint is superseded by s7-13, but the two-cell theorem remains a current reusable receiver.

### B. Shared-label support plus one selected two-cell receiver

Status: `CLOSED_NEGATIVE` as an improvement route; `CURRENT_CHECKPOINT` as the 7/8 barrier certificate.

On `xi~B^gamma`, merged 4cb / s7-14 gives

```text
E_support(gamma) = 1/2 + gamma/2,
E_2cell(gamma)   = 1 - gamma/6,
E(gamma)         = min(E_support,E_2cell).
```

The exact crossing is

```text
gamma=3/4,
E=7/8.
```

Therefore

```text
LARGE_XI_SUPPORT_ALONE_BEATS_7_8=false
SHARED_LABEL_SUPPORT_PLUS_ONE_TWO_CELL_ARCHITECTURE_BARRIER=7/8.
```

Further dyadic refinement of only `alpha,beta,x,y` cannot beat the critical block while using only these same two ingredients.

### C. Existing one-cell/two-cell cell geometry

Status: `CLOSED_NEGATIVE` as a standalone route below 7/8.

The critical exponent pattern

```text
(r,s,t,j)=(1/4,1/8,1/8,1/4)
```

gives

```text
a=b=c=d=3/8,
xi=3/4.
```

The proved one-cell and adjacent two-cell receivers both return exactly `7/8` on this pattern. Merged s7-11 / 4bz also rules out naive higher-cell enlargement of the same square detector as a source of a new independent saving.

### D. Realized shared-label sparsity

Status: `LIVE_PRIMARY`.

Merged 4cb proves the following sufficient contract. If, near the critical label range,

```text
#{physically realized xi~B^gamma}
  << B^((1-delta)*gamma+o(1))
```

for some fixed `delta>0`, then

```text
E_delta = 1 - 1/(8-12*delta) < 7/8
```

while the crossing remains in range. Example:

```text
delta=1/12 -> E_delta=6/7.
```

No positive `delta` is currently proved.

### E. Stronger transverse coefficient saving

Status: `LIVE_PRIMARY`.

If a genuinely transverse theorem improves the selected coefficient saving from

```text
C^(-1/3)
```

to

```text
C^(-1/3-eta), eta>0,
```

then merged 4cb gives

```text
E_eta=(7+3*eta)/(8+6*eta) < 7/8.
```

This cannot be obtained by multiplying the already-correlated `a` and `b` two-cell estimates.

### F. Off-diagonal `(xi,k)` collision energy

Status: `LIVE_PRIMARY`, direct s-route target.

Merged s7-14 defines

```text
xi = ker(PQ),
k  = ker(Q^2-P^2),
gcd(xi,k)=1,
```

and

```text
r_B(xi,k)
 = #{P/Q in the canonical Stage14 window with these two labels}.
```

A physical pair requires the same `xi` and the same `k`. Hence the direct collision receiver is

```text
E_off(B)
 = sum_xi sum_k r_B(xi,k)*(r_B(xi,k)-1).
```

On the critical `xi~B^(3/4)` shell, any fixed `delta>0` in

```text
E_off,critical(B) << B^(7/8-delta+o(1))
```

is sufficient for a strict improvement after the standard slack split.

This is the most direct current obstruction statement.

### G. Fixed `(xi,k)` genus-one multiplicity

Status: `CLOSED_NEGATIVE` as a collision-saving theorem.

The fixed-fiber bounded-height theorem gives only

```text
r_B(xi,k) <= B^o(1).
```

Merged s7-14 proves that pointwise subpolynomial multiplicity alone does not imply power saving in

```text
sum r(r-1).
```

The missing information is average recurrence of the map

```text
P/Q -> (xi,k),
```

not a stronger fixed-fiber point bound.

### H. External auxiliary bad-prime aggregate

Status: `CLOSED_POSITIVE`.

Merged t50 proves

```text
R_bad << H*P^2*B^o(1)
```

at the t49 amplifier scale. Bad auxiliary primes are therefore no longer the live two-modulus obstruction.

### I. Selector-sensitive two-modulus Gaussian second moment

Status: `LIVE_BRIDGE` for main/s; direct live t/tH receiver.

Merged t50 isolates the exact missing t-side theorem

```text
sum_{p!=q} |sum_R S_R(p,q)|^2
 << P^2 * (sum_R ||w_R||_2^2) * B^o(1),
```

with all of the following retained:

```text
signed common-refinement aggregation,
shared U/V modulus group,
divisor-coupled hyperbola,
canonical/physical selector,
two distinct split auxiliary primes p,q.
```

The t50 good Frobenius kernel is exactly the tH8 physical Route-B kernel.

However merged s7-14 does not prove that this t/tH operator is already the same operator as the main/s `(xi,k)` collision energy. Therefore the two-modulus theorem is not automatically a main/s 7/8 improvement. An exact bridge is required before transfer.

### J. Complete finite-field angular cancellation -> sparse physical selector

Status: `FORBIDDEN`.

Merged t50 proves

```text
T32_COMPLETE_ANGULAR_BOUND_DIRECTLY_CONTROLS_SPARSE_PHYSICAL_SELECTOR=false.
```

The complete t32 cancellation cannot simply be restricted to the sparse selected physical set.

### K. Pair collapse before physical/norm-index cancellation

Status: `FORBIDDEN`.

Merged t49/t50 records that collapsing ordered physical state pairs to cross-kernel coefficient energy before the signed physical/norm-index cancellation reimports the unresolved fourth energy and becomes circular.

Required order:

```text
signed physical state sum
 -> angular completion
 -> common-refinement / divisor-coupled aggregation
 -> only then product-kernel / Frobenius bookkeeping.
```

### L. tH14 support route

Status: `SUPPORT_TRIGGERED`.

Merged t50 explicitly records

```text
TH11_MULTI_MODULUS_REOPEN_TRIGGER_HIT=true
TH14_NEEDED=true.
```

The required support task is a selector-sensitive two-auxiliary Gaussian second-moment receiver/certificate preserving the t50 selector and aggregation contract. It should reuse t32 angular completion, tH4 weighted transfer, and tH5 exact-pair energy without pair-collapse circularity.

## 3. Current next-receiver ordering

For direct main/s progress below `7/8`, the atlas priority is:

```text
P1  off-diagonal (xi,k) collision power saving
P2  realized xi sparsity with any fixed delta>0
P3  genuinely transverse coefficient gain eta>0
P4  exact bridge from the selector-sensitive two-modulus theorem to P1/P3
```

P1 is the most direct s-route contract. P2 and P3 are the exact main-route sufficient contracts from 4cb. P4 is a support/bridge route and cannot be promoted without the operator identification.

## 4. Do-not-reopen list at the current checkpoint

Do not spend a new stage merely on:

```text
more xi-only support counting,
more alpha/beta/x/y dyadic splitting with the same two bounds,
threshold retuning of the old 13/14 architecture,
naive three-/four-cell enlargement of the same square detector,
stronger fixed-(xi,k) pointwise multiplicity alone,
complete finite-field cancellation with the physical selector silently removed,
pair collapse before signed physical/norm-index cancellation.
```

Each item has already been closed or forbidden by a merged source.

## 5. Current boundary

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
CURRENT_CRITICAL_SHARED_LABEL_EXPONENT=3/4
CURRENT_CRITICAL_SELECTED_COEFFICIENT_EXPONENT=3/8
CURRENT_CRITICAL_SQUAREPART_ROOT_EXPONENT=1/16
CURRENT_REMAINING_GAP_TO_SQRT=3/8
PRIMARY_DIRECT_OBSTRUCTION=off-diagonal-(xi,k)-collision-energy
REALIZED_XI_SPARSITY_POWER_SAVING_PROVED=false
TRANSVERSE_COEFFICIENT_GAIN_PROVED=false
OFF_DIAGONAL_XI_K_COLLISION_POWER_SAVING_PROVED=false
SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_PROVED=false
EXTERNAL_BAD_AUXILIARY_AGGREGATE_BOUND_PROVED=true
TH14_NEEDED=true
SQRT_B_UPPER_BOUND_PROVED=false
```
