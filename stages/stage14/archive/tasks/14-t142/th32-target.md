# Stage14-tH32 immutable target — safe-modulus quarter-scale fixed-residue Gaussian prime short intervals

```text
REQUESTED_OBJECT=SafeMitsuiModulusQuarterScaleFixedGaussianResidueShortIntervalPrimeOccupancy
PARENT_STAGE=Stage14-t142
SOURCE_SNAPSHOT_SHA=744d5b844d9f6b6bcace141497a97fef1945e81b
TARGET_FROZEN=true
```

Audit only the parent snapshot above. Do not use later t-stage conclusions.

## Frozen arithmetic object

Work over `K=Q(i)`. Fix the live fixed-U packet and all t133--t135 local/sector/residue labels. Let

```text
L_B=2*sqrt(B),
d<=exp(c_safe*sqrt(log B)),
q=(d),
N(q)=d^2,
beta_* in (Z[i]/dZ[i])^x.
```

After t140--t142, a whole-exponent-obstructing endpoint packet is localized to one additive-width layer

```text
H_z in (Y,2Y],
Y=B^(lambda+o(1)),
lambda>=1/4-o(1),
```

with prime upper endpoint

```text
y_z=L_B+H_z.
```

The prime variable is the canonical split Gaussian prime element `pi` satisfying

```text
pi == beta_* (mod d),
pi lies in the fixed strict canonical D4 sector,
L_B < N(pi) <= y_z.
```

The principal ordinary-residue comparison count for the same interval is the unrestricted canonical split-prime count divided by

```text
|(Z[i]/dZ[i])^x|.
```

The cofactor set is explicit. It only supplies the moving endpoints `H_z` in one dyadic layer; no opaque arithmetic coefficient is present.

## Required theorem verdict

Determine the sharpest currently proved **unconditional** exponent range for a lower bound of the form

```text
# {pi in fixed sector/residue:
   L_B<N(pi)<=L_B+H}
 >= B^(-o(1))
    / |(Z[i]/dZ[i])^x|
    * # {unrestricted canonical split pi:
         L_B<N(pi)<=L_B+H}
```

uniformly for

```text
d<=exp(c_safe*sqrt(log B)),
H in a fixed dyadic layer (Y,2Y],
Y>=B^(1/4-o(1)).
```

It is enough to rule out a fixed-power depletion; a `(1+o(1))` asymptotic is not required.

The audit must explicitly answer:

```text
1. Does any existing unconditional theorem reach the quarter-scale endpoint Y>=B^(1/4-o(1))?
2. If not, what is the best certified additive-width exponent lambda_known in B-scale for this exact Gaussian sector + ordinary residue problem?
3. Can a possible real Hecke/Siegel zero be retained without destroying the needed B^(-o(1)) lower ratio in the certified short-interval range?
4. Does Kai/Mitsui itself provide a short-interval result after subtraction at this scale, or only the long/cumulative result already used in tH31?
5. Does Stucky/Ricci-type Gaussian short-sector technology accept the growing ordinary residue modulus, or only angular/conductor-one restrictions?
6. Do current Hecke zero-density/Hoheisel results give an individual residue theorem in this pseudopolynomial modulus range?
```

## Mandatory retained conditions

Do not drop or average away:

```text
K=Q(i),
fixed strict broad canonical sector,
fixed ordinary Gaussian residue beta_* mod d,
d<=exp(c_safe*sqrt(log B)),
possible exceptional real Hecke zero,
L_B=2*sqrt(B),
additive interval width H~Y,
Y>=B^(1/4-o(1)),
canonical split-prime convention.
```

Do not use GRH or unproved density hypotheses for a positive verdict.

## Positive/negative output contract

A positive verdict must state a theorem-compatible threshold and prove that it implies

```text
T_endpoint_safe >= B^(-o(1)) M_endpoint_safe
```

on the covered width range.

A negative verdict must identify the precise remaining exponent/modulus obstruction and give the strongest certified threshold found rather than merely saying that short intervals are difficult.

In either case report

```text
DIRECT_THEOREM_APPLICABLE=
QUARTER_SCALE_ENDPOINT_COVERED=
BEST_CERTIFIED_B_WIDTH_EXPONENT=
POSSIBLE_SIEGEL_ZERO_RETAINED=
SAFE_ENDPOINT_FIXED_POWER_DEPLETION_RULED_OUT=
NEXT_H_NEEDED=
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```
