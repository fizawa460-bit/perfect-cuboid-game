# Stage27-20-r301m — moduli support is exponent-equivalent to q1 support

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301l
SOURCE_STAGE=Stage20

## 1. Occupied moduli support

Let `Q(B)` be the occupied physical first-coordinate support from r301j and define

\[
J(B):=\{j(x):x\in Q(B)\}.
\]

R301k gives a physical moduli-map fiber of size at most two.  Therefore

\[
\boxed{|J(B)|\le |Q(B)|\le2|J(B)|.}
\]

Consequently `Q(B)` and `J(B)` have exactly the same fixed-power support exponent.  Replacing the slope coordinate by its elliptic moduli point cannot by itself create a strict support saving.

## 2. Squareclass multiplicity remains subpower over one moduli point

For each physical `x`, r301h gives

\[
|D_x(B)|=B^{o(1)}.
\]

Since a fixed physical `j` has at most two corresponding `x`, the union of compatible squareclasses above one moduli point also satisfies

\[
\boxed{|D_j(B)|=B^{o(1)}.}
\]

Thus the squareclass index still costs no fixed positive exponent after passing from `x` to `j`.

## 3. Moduli-fiber progress gate

Define the moduli-twist fiber mass by

\[
W_{j,\delta}(B):=
\sum_{\substack{x\in Q(B)\\j(x)=j}} w_{x,\delta}(B).
\]

Because there are at most two physical `x` above `j`, a uniform bound

\[
W_{j,\delta}(B)\ll B^{\phi+o(1)}
\]

has the same fixed-power exponent as the corresponding uniform `(x,delta)` fiber bound.

If independently

\[
|J(B)|\ll B^{\sigma+o(1)},
\]

then

\[
\boxed{N_2(B)\ll B^{\sigma+\phi+o(1)}.}
\]

The strict-half gate remains exactly

\[
\boxed{\sigma+\phi<\frac12.}
\]

Likewise the second-moment gate remains `sigma+eta<1` after bounded-to-one regrouping.

## 4. Height-only moduli reparametrization does not solve the support problem

For reduced `x=a/b`, the explicit formula is

\[
j(x)=
\frac{256(a^8-a^4b^4+b^8)^3}
{a^8b^8(a^4-b^4)^2}.
\]

Hence the physical height bound `H(x)<=2B` yields only a polynomial moduli-height bound

\[
H(j(x))\ll B^{24}.
\]

Counting rational `j` merely by this height is vastly weaker than the present half-power theorem.  Since the map `x -> j` is bounded-to-one on the physical locus, no support deficit can arise from the reparametrization alone.

The next useful input must exploit arithmetic of the twist family — for example a genuinely uniform/averaged descent, rank, conductor, or off-diagonal theorem — rather than the moduli map by itself.

```text
STAGE27_20_R301M_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
PHYSICAL_Q1_TO_J_MULTIPLICITY_LE_2=true
Q1_AND_J_SUPPORT_EXPONENTS_EQUAL=true
SQUARECLASS_MULTIPLICITY_PER_J_SUBPOWER=true
MODULI_MAX_FIBER_PROGRESS_GATE=sigma+phi<1/2
MODULI_SECOND_MOMENT_PROGRESS_GATE=sigma+eta<1
HEIGHT_ONLY_MODULI_SUPPORT_ROUTE_CLOSED=true
MODULI_REPARAMETRIZATION_FIXED_POWER_SAVING_PROVED=false
UNIFORM_MOVING_FIBER_SUBPOWER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301n
STOP_REASON=UNIFORM_OR_AVERAGED_ARITHMETIC_TWIST_FAMILY_THEOREM_REQUIRED
```
