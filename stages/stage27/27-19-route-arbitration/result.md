# Stage27-19 route arbitration after r402 freeze

```text
TASK_ID=Stage27-19-route-arbitration
OWNER_STAGE=Stage27
TRIGGER_CHECKPOINT=40
CURRENT_UPPER_EXPONENT=1/2
CURRENT_LOWER_EXPONENT=1/4
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## 1. Current audited state

The r6 family is frozen.  Its useful output r6d discharged fixed-`(p,q,g)` representation multiplicity:

\[
\#\{(m,n,r,s)\}\le4\tau(pg)^2=B^{o(1)}.
\]

The reactivated r402 route then proved that the remaining polynomial mass is exactly the support of realized coupled pairs

\[
A=s^2(m^2+n^2),\qquad D=n^2(r^2-s^2),
\]

up to subpower factors, with `(tau,g)` merely the gcd decomposition `(A,D)=(pg,qg)`.  Fresh audit passed with route freeze: no further elementary gcd/core/divisor decomposition can legally be charged as a new power saving.

The lower r401 route is also bounded.  Its audited calibration gives the one-parameter progress criterion

\[
2d_x+2d_y-g<8,
\]

or alternatively a polynomially thicker moving family.  No such new curve/cancellation/thick family is presently available in the repository.

Thus neither lane should be mechanically extended.

## 2. Priority decision

Upper remains the preferred first reopen because r6d produced genuine new compression: fixed-core representation entropy has already been removed.  A single same-measure support theorem can now act directly on the physical counting dimension.

The exact upper receiver is:

> Prove, uniformly for every dyadic `T<=2B^2`, that the number of physically realized pairs `(A,D)` with
>
> `A=s^2(m^2+n^2)`, `D=n^2(r^2-s^2)`, `A,D<2B^2`,
>
> reduced direction height `T<=H(A/g,D/g)<2T`, `g=gcd(A,D)`,
>
> and all primitive/canonical/exactly-two Stage19 masks retained,
>
> satisfies
>
> `#P_T(B) << B^(1/2-delta+o(1))`
>
> for some fixed `delta>0`.

Any theorem proving this, or a weighted energy estimate strong enough to imply it through the frozen r402f hybrid inequality, yields

\[
N_2(B)\ll B^{1/2-\delta+o(1)}.
\]

## 3. Admissible theorem species

A useful external/new theorem must genuinely couple the two forms.  Admissible species include:

1. a same-measure determinant-method / rational-point bound for the realized `(A,D)` image with a fixed-power deficit;
2. a bilinear/incidence theorem controlling simultaneous representations by `s^2(m^2+n^2)` and `n^2(r^2-s^2)`;
3. a sieve theorem imposing a new non-duplicate local/global restriction on the coupled pair and preserving the physical measure;
4. a weighted second-moment theorem for the same realized support that yields the r402f band contract.

Not admissible as new savings:

- reusing the Stage15 squareclass parity condition;
- counting possible `g`, `tau`, divisors, or Gaussian factor allocations separately after the proved bijections;
- unweighted exceptional-set cardinality without a physical-weight transfer theorem;
- a theorem on a larger host with no same-measure adapter.

## 4. Lower fallback receiver

If no upper theorem of the preceding species exists, the next legal lower reopen requires at least one of:

- a new physical rational curve with `h_alg=2d_x+2d_y-g<8`;
- a provable stronger polynomial cancellation reducing physical height below 8;
- a polynomially thicker moving family whose parameter-count exponent raises the lower bound above `B^(1/4-o(1))`.

Blind continuation of affine/constant-u ansatz searches is not authorized; r401 already closed those shortcuts.

## 5. Route policy

```text
UPPER_CURRENT_WALL=COUPLED_FORM_REALIZED_AD_SUPPORT_THEOREM
LOWER_CURRENT_WALL=NEW_H_LT_8_CURVE_OR_STRONGER_CANCELLATION_OR_THICK_FAMILY
PREFERRED_REOPEN=UPPER_IF_NEW_THEOREM_INPUT_EXISTS
FALLBACK_REOPEN=LOWER_IF_NEW_CONSTRUCTION_INPUT_EXISTS
MECHANICAL_NEW_SUBROUTE_WITHOUT_NEW_INPUT=FORBIDDEN
CURRENT_MU=1/2
CURRENT_LOWER_EXPONENT=1/4
ADVANCE_TO_CHECKPOINT50=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_EXPECTED_COMMAND=Stage27-19-route-audit
```
