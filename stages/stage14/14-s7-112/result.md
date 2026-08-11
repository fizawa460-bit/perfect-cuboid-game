# Stage14-s7-112 — split the bundled physical Boolean into reconstructed prefilter and existential completion support

## Status

`COMPLETE_PRECOMPLETION_DETERMINISTIC_FILTER_VERSUS_EXISTENTIAL_REVERSE_COMPLETION_SPLIT`

Consumes batch-local `Stage14-s7-111`, merged `Stage14-4fk`, merged `Stage14-s7-97`, merged `Stage14-4gb`, and merged `Stage14-Work-byX37`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Split predicates by quantifier type, not by presumed density

For one exact reconstructed candidate `chi`, define

```text
C_pre(chi) in {0,1}
```

as the conjunction of every still-live predicate whose truth is already determined by `chi` and the frozen packet data, without introducing any new completion variable.

This class includes only predicates that provenance really makes decidable on the reconstructed tuple; examples may include primitive/gcd bookkeeping already carried by the candidate, parity/two-primary data, root-origin/sign data, allocation consistency, chart/orientation tests, and canonical tests that use no not-yet-reconstructed completion variable.

Any canonical predicate that still depends on an extension variable is **not** moved into `C_pre` merely because it is called canonical.

Define the extension-witness set

```text
R(chi)
```

as the set of reverse/post-column completions, together with any still-unreconstructed extension variables, that satisfy all remaining physical conditions. Then set

```text
C_ext(chi) := 1_{R(chi) is nonempty}.
```

By construction,

```text
C_phys(chi)=C_pre(chi)*C_ext(chi).                 (1)
```

Equation (1) is an exact conjunction split by quantifier location. It asserts no independence and no multiplicativity.

```text
PRECOMPLETION_FILTER_DEFINED_BY_PROVEN_VARIABLE_DEPENDENCE=true
EXISTENTIAL_REVERSE_POSTCOLUMN_COMPLETION_BOOLEAN_DEFINED=true
PHYSICAL_BOOLEAN_SPLIT_USES_INDEPENDENCE=false
CANONICAL_EXTENSION_DEPENDENT_PREDICATES_FORCED_INTO_PRE=false
```

## 2. The prefilter is deterministic but not automatically dense

Because `chi` fixes the full normalized pre-completion tuple from s7-111, `C_pre(chi)` is a deterministic Boolean on the already-charged candidate support.

This only means that no additional polynomial multiplicity is hidden inside the evaluation of `C_pre`. It does **not** prove

```text
C_pre=1,
#supp(C_pre)=B^(ambient exponent+o(1)),
```

or any fixed-power deficit.

Thus a future saving may still come from a sparse deterministic prefilter, but such sparsity must be proved on the actual Stage14 candidate family rather than inferred from the names of its predicates.

```text
PRECOMPLETION_FILTER_EVALUATION_MULTIPLICITY=1
PRECOMPLETION_FILTER_FULL_DENSITY_PROVED=false
PRECOMPLETION_FILTER_FIXED_POWER_DEFICIT_PROVED=false
```

## 3. Existing reverse-completion fiber bounds control multiplicity only

Merged s7-97, using merged fixed-radial/reverse reconstruction results, records that for fixed exact normalized candidate data the number of successful full physical reverse completions is at most

```text
B^o(1).
```

Therefore on every current branch

```text
#R(chi) <= B^o(1).                                (2)
```

Equation (2) forbids polynomial entropy in the extension witness. It does not imply `R(chi)` is nonempty and therefore gives no lower bound for `C_ext`.

Consequently the correct extension object is support of existence,

```text
C_ext(chi)=1_{#R(chi)>=1},
```

not the raw witness count.

```text
REVERSE_POSTCOLUMN_WITNESS_MULTIPLICITY=Bo1
REVERSE_POSTCOLUMN_EXISTENCE_AUTOMATIC=false
REVERSE_COMPLETION_MULTIPLICITY_RECHARGE_ALLOWED=false
EXISTENTIAL_SUPPORT_NOT_WITNESS_COUNT_IS_RECEIVER=true
```

## 4. Exact nested supports

On any one of the four s realizations let

```text
S_amb   = {chi : chi lies in the already-charged ambient candidate cell},
S_pre   = {chi in S_amb : C_pre(chi)=1},
S_phys  = {chi in S_pre : C_ext(chi)=1}.
```

Then exactly

```text
S_phys subseteq S_pre subseteq S_amb.             (3)
```

No relative-density comparison between these sets is assumed.

This is the first exact opening of the completion-only receiver after Work-byX37: ambient multiplicative capacity has been exhausted, and the residual physical loss has two logically distinct locations, deterministic pre-completion filtering and existential reverse/post-column completion.

## 5. Receiver and H decision

The split (3) is substantive but the exponent receiver is not frozen until the headroom ledger is written uniformly across all four branches. The next stage defines the two conditional deficits and the exact heavy-survival inequality.

No new sH is opened yet because `R(chi)` has not been expressed by a stable arithmetic equation family and `C_pre` may still carry coupled canonical conditions.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_112_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-113
```

## Boundary

```text
STAGE14_S7_112=COMPLETE_PRECOMPLETION_DETERMINISTIC_FILTER_VERSUS_EXISTENTIAL_REVERSE_COMPLETION_SPLIT
PRECOMPLETION_FILTER_DEFINED_BY_PROVEN_VARIABLE_DEPENDENCE=true
EXISTENTIAL_REVERSE_POSTCOLUMN_COMPLETION_BOOLEAN_DEFINED=true
REVERSE_POSTCOLUMN_WITNESS_MULTIPLICITY=Bo1
REVERSE_POSTCOLUMN_EXISTENCE_AUTOMATIC=false
EXISTENTIAL_SUPPORT_NOT_WITNESS_COUNT_IS_RECEIVER=true
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_112_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-113
```