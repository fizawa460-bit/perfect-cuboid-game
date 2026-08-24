# Stage33-05 — K3 Br[2] Q(i)/Q descent production state

```text
STAGE33_UNIT=33-05
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
K3_GEOMETRIC_BR2_DIM=2
LCE_DIMENSION=5
XALPHA_IMAGE_DIMENSION=3
COMMON_NORMALIZATION_EXACT=true
ASSOCIATED_GRADED_CC_ACTION_EXACT=true
FULL_LCE_CC_ACTION_EXACT=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
QI_OVER_Q_ACTION_MATRIX_EXACT=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Exact ruled-branch and Creutz--Viray dimension skeleton

The source-locked model satisfies

```text
F=(X+iY)(X-iY) over Q(i),
B+,B- smooth of bidegree (2,2),
complex conjugation swaps B+ and B-,
B+ intersect B- in 8 transverse nodes.
```

Relative to the first ruling, both normalized components have common quadratic function field

```text
z^2 = q(t) = t^4 - 6*t^2 + 1.
```

After the mandatory nodal-fiber correction, the exact Creutz--Viray dimensions are

```text
Jac(B)[2] dimension          = 4
dual graph b1                = 7
special even-e fibers        = 8
K-squareclass kernel dim     = 1
raw generator dimension      = 12
kernel to K*L^2 dimension    = 7
L_E = L_{c,E} dimension      = 5
im(x-alpha) dimension        = 3
Br(K_c_Qbar)[2] dimension    = 2.
```

The superseded `L_{c,E}=9` pilot remains invalid.

## 2. Explicit common normalization and node-level conjugation

Run `32689168245` materializes the common normalization maps

```text
B+ : s =  i*(1-t^2+z)/(2*t)
B- : s = -i*(1-t^2+z)/(2*t)
z^2 = t^4 - 6*t^2 + 1.
```

Complex conjugation swaps `B+` and `B-`, fixes the abstract functions `t,z`, and conjugates constants.  All eight intersection edges are individually stable as geometric dual-graph edges.

Therefore the associated-graded Creutz--Viray pieces have exact conjugation action:

```text
Jac(B)[2] = Jac(B+)[2] + Jac(B-)[2]
  dimension 4
  cc swaps the two 2-dimensional summands
  fixed dimension = 2

H1(Gamma,F2)
  dimension 7
  cc action = identity
  fixed dimension = 7

G1/G2
  dimension 1
  cc action = identity
  fixed dimension = 1.
```

Hence the raw 12-dimensional associated-graded candidate space has

```text
ASSOCIATED_GRADED_CC_FIXED_DIMENSION = 10.
```

A compatible two-function skeleton for the 2-torsion on each common normalization is also explicit via ratios `(t-r_i)/(t-r_j)` at the four roots of `q(t)`.

Evidence:

```text
workflow_run = 32689168245
workflow_conclusion = success
normalization_galois_certificate_sha256 = 7eb25f097b0d84d92aa8b6fe9dbf049992261cd7545c7103a3b193553845ccd8
artifact_id = 9506667861
artifact_zip_sha256 = b363f15a31602b9b2a1d67be12c7d4f960f8da73869de747859d59d390ca918c
cv_dimension_sha256 = 2f56fb20b25af27f68639e0154713ba1b4995113715f516a014c0a605b2fc976
```

## 3. Firewall: associated graded does not determine Q survival

The value

```text
raw associated-graded fixed dimension = 10
```

does not determine the action on the actual five-dimensional `L_{c,E}` quotient.  The seven-dimensional `K*L^2` relation space can mix the graded pieces, and the rank-three `x-alpha` image must then be quotiented before the two-dimensional geometric Brauer group is obtained.

Thus none of the following is claimed:

```text
EXPLICIT_LCE_BASIS_MATERIALIZED=false
EXPLICIT_XALPHA_MATRIX_MATERIALIZED=false
FULL_LCE_CC_ACTION_EXACT=false
BRAUER_QUOTIENT_CC_ACTION_EXACT=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
GEOMETRIC_BR2_DIM2_IMPLIES_Q_SURVIVAL=false
```

## 4. Next exact leaf

```text
LEAF_ID=L33-05-CV-FUNCTION-SYNTHESIS-ON-z2=q-AND-XALPHA
CLASS=2
NEW_THEOREM_REQUIRED=false
INPUT_COMMON_NORMALIZATION=z^2-(t^4-6*t^2+1)
INPUT_LCE_DIMENSION=5
REQUIRED_XALPHA_IMAGE_RANK=3
REQUIRED_BRAUER_QUOTIENT_DIM=2
```

Remaining bounded work is now concrete:

```text
1. synthesize five compatible explicit functions representing a basis of L_{c,E};
2. transport a certified NS(K_c) generating set to the ruled model/generic fiber;
3. compute the exact rank-three x-alpha relation matrix;
4. choose two explicit quotient symbol representatives;
5. compute complex-conjugation on that quotient;
6. certify Q(i)/Q descended survivors or exact zero survival.
```

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
