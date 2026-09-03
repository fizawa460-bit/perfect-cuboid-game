# Stage35 35-06 — Stoll 2019 diagonal genus-5 arithmetic source note

```text
SOURCE_KIND=external_primary_paper
AUTHOR=Michael Stoll
TITLE=Diagonal genus 5 curves, elliptic curves over Q(t), and rational diophantine quintuples
PUBLICATION=Acta Arithmetica 190 (2019), 239-261
DOI=10.4064/aa180416-4-10
ARXIV=1711.00500
SOURCE_URL=https://mathe2.uni-bayreuth.de/stoll/papers/dioph5.pdf
STAGE35_USE=nearest exact structural/arithmetic method for the selected diagonal genus-5 family
```

## Exact structural match

The paper defines a diagonal genus-5 curve as a smooth intersection of three diagonal quadrics in `P4`. This is exactly the structural class of `TS-S-R3-Q1` after 35-03 substitution.

For any such curve over a field `K` of characteristic not 2, eliminating one coordinate gives five genus-one quotient curves `F_j`. Their Jacobians `E_j` have all 2-torsion defined over `K`, and the genus-5 Jacobian is isogenous to the product of the five elliptic curves. The diagonal sign-change subgroup is `(Z/2Z)^4`.

For a fixed curve over `Q`, the paper explains that ordinary Chabauty is usually unavailable because the five elliptic factors tend to contribute positive rank. Its proposed fixed-curve method uses covering collections, 2-descent/Selmer information and elliptic-curve Chabauty on suitable covers/quotients.

## Function-field method

The paper separately studies elliptic curves over `Q(t)` with full rational 2-torsion. It gives a specialization criterion that can prove an injective map

```text
E(Q(t)) -> E_tau(Q)
```

at a chosen good specialization, and uses such an injective specialization together with a known full Mordell-Weil group at the specialization to certify generators of `E(Q(t))`.

In its diophantine-quintuple application the paper then determines the relevant generic function-field groups and proves a classification of `Q(t)`-rational points/sections on that specific family.

## Stage35 hypothesis match

```text
DIAGONAL_GENUS5_STRUCTURE_MATCH=true
FIVE_ELLIPTIC_QUOTIENTS_AVAILABLE=true
ELLIPTIC_QUOTIENT_FULL_2_TORSION_OVER_Q(t)=true
FUNCTION_FIELD_MW_CERTIFICATION_METHOD_STRUCTURALLY_AVAILABLE=true
FIXED_FIBER_COVERING_COLLECTION_METHOD_STRUCTURALLY_AVAILABLE=true
```

## Exact mismatch with T35-R3-PHYS-EMPTY

The Stage35 target is not merely to classify rational sections `C(Q(t))`. It requires

```text
for every tau in Q with tau>1:
    U_tau(Q)=empty.
```

A rational point appearing only after specialization need not arise from a rational section over `Q(t)`. Therefore:

```text
C(Q(t))_CLASSIFICATION_IMPLIES_ALL_SPECIALIZED_C_tau(Q)_CLASSIFICATION=false
INJECTIVITY_OF_E(Q(t))->E_tau(Q)_IMPLIES_SURJECTIVITY=false
SILVERMAN_EVENTUAL_INJECTIVITY_EXCLUDES_NEW_SPECIALIZATION_POINTS=false
FIXED_FIBER_ELLIPTIC_CHABAUTY_UNIFORM_OVER_ALL_tau=false
```

The paper itself describes its `Q(t)` conclusion as a result about the generic extension and treats fixed rational specializations separately. This is precisely the Stage35 uniform-specialization gap.

## Routing consequence

Stoll 2019 supplies the correct local structure and the strongest immediate arithmetic attack vocabulary, but it does not supply the missing uniform theorem `T35-R3-PHYS-EMPTY`.

A Stage35 proof using this route would need an additional theorem that uniformly controls specialization-new rational points in the relevant elliptic quotients/covers, or a different receiver-restricted obstruction valid for every rational `t>1`.
