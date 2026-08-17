# Stage27-20-r301y — existing q1 projections are exponent-neutral on critical support

STATUS=AUDITED_PASS_MERGED
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301x
SOURCE_STAGE=Stage20

## 1. Two available projections

The current r301 package has two explicit ways to re-express occupied first-coordinate support.

First, r301t gives the degree-one Möbius equivalence

\[
q_0=\frac{q_1-1}{q_1+1},\qquad
q_1=\frac{1+q_0}{1-q_0}.
\]

Thus passing from critical `q1` support to the corresponding Stage14 rational-circle coordinate is birational and preserves cardinality exactly.

Second, r301m defines the elliptic moduli support

\[
J(B)=\{j(q_1):q_1\in Q(B)\}
\]

and proves on the physical locus

\[
|J(B)|\le |Q(B)|\le2|J(B)|.
\]

Restricting to the critical subset preserves the same bounded-fiber inequality. Hence `q1` support and its available `j`-projection have the same fixed-power exponent.

## 2. Consequence for a thin-projection attack

Neither existing projection supplies the missing fixed-power deficit:

- `q1 -> q0` is degree one, so there is no algebraic thinness created by the map;
- `q1 -> j` is bounded-to-one on the physical locus, so its support exponent is equivalent to the original one. Calling the moduli image thin does not by itself improve its quantitative count under the physical cutoff.

The height-only `j` route was already closed in r301m: the available polynomial height transfer is far too weak to beat the current half-power support theorem.

## 3. Exact next theorem contract

A genuinely new thin-projection receiver must therefore provide more than a coordinate change. One sufficient form is a new non-birational arithmetic correspondence

\[
\pi:Q_{\rm crit}\dashrightarrow Z
\]

with all of the following audited at the physical cutoff:

1. the occupied critical set maps into a quantitatively sparse rational image;
2. the image count has a fixed-power deficit;
3. the physical fibers are bounded or `B^{o(1)}`;
4. the height/cutoff transfer is polynomial and uniform over the critical packets;
5. no Stage14 host saving is charged a second time.

No current `q0` or `j` adapter satisfies this stronger quantitative contract.

## 4. Outcome and final r301-letter target

The three legal internal-looking weapons named at r301v have now been separated from their circular/reused forms:

- existing local/root factors: already charged in the Stage14 complete host (r301w);
- natural slope collisions: zero off-diagonal because the Möbius adapter is injective (r301x);
- existing projections: cardinality/exponent neutral (this route).

Therefore `r301z` should be reserved for a receiver-synthesis step: identify or derive one genuinely new critical-support theorem satisfying one of the surviving contracts, rather than another reparametrization of the same half-power host.

```text
STAGE27_20_R301Y_STATUS=AUDITED_PASS_MERGED
Q1_TO_Q0_PROJECTION_BIRATIONAL=true
Q1_TO_Q0_SUPPORT_CARDINALITY_PRESERVED=true
Q1_TO_J_PHYSICAL_MULTIPLICITY_BOUNDED=true
Q1_AND_J_CRITICAL_SUPPORT_EXPONENTS_EQUAL=true
EXISTING_PROJECTIONS_FIXED_POWER_SAVING_PROVED=false
NEW_HEIGHT_CONTROLLED_NONBIRATIONAL_PROJECTION_PROVED=false
CRITICAL_Q1_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301z
STOP_REASON=GENUINELY_NEW_CRITICAL_SUPPORT_RECEIVER_THEOREM_REQUIRED
```
