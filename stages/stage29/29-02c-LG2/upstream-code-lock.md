# Stage29-02c-LG2 — upstream computation source lock

The published Testa--Stoll low-degree classifications are accompanied by public Magma verification code.

```text
UPSTREAM_REPO=https://github.com/MichaelStollBayreuth/Verification
UPSTREAM_COMMIT=51233ed5ef2bf228fac9416c66db9adc0ebcaadd
UPSTREAM_FILE=Cuboids/cuboids.magma
UPSTREAM_BLOB=0422b69847f2afb97cb7b3ed02ebef91279f61b1
UPSTREAM_LICENSE=GPL-3.0
SOURCE_LOCK_AUDIT=PASS
```

This Stage29 suffix does not vendor or modify the upstream file. It records the immutable source locators and the exact pieces relevant to the new receiver.

## Source-attribution precision

The Magma file constructs the known-curve intersection lattice, verifies rank `64`, and materializes the corresponding `PicL` lattice and intersection form. In the source itself this construction is introduced under the working assumption that the known curves generate the Picard group. The fact that this known rank-64 lattice is the **full geometric Picard group** is supplied by the Testa--Stoll theorem package already audited in Stage29-02a, not by the rank assertion alone.

Accordingly the reusable interface is:

```text
CODE_CONSTRUCTS_KNOWN_CURVE_RANK64_LATTICE=true
TESTA_STOLL_THEOREM_IDENTIFIES_FULL_PICARD_GROUP=true
CODE_ALONE_PROVES_FULL_PICARD_GROUP=false
FULL_PICARD_LATTICE_AVAILABLE_AFTER_THEOREM_PLUS_CODE=true
```

## Relevant published-code objects

The source constructs the cuboid surface and its 48 nodes, then builds the intersection matrix for the known curve configuration and exceptional divisors. It asserts rank `64` and constructs `PicL`, the lattice with its symmetric intersection form.

The canonical/projective hyperplane class is stored as `HinPicL`. The script also constructs the linear automorphism action on Picard classes and the Galois action.

For low degree the script uses negative-definite orthogonal-complement enumeration:

- degree 2: `8*C-H` lies in `H^perp`; `CloseVectors` enumerates the relevant coset;
- degree 4: `4*C-H` lies in `H^perp`; another `CloseVectors` search is performed;
- degree 6: the proof passes through the long-diagonal-sign K3 quotient, enumerates candidate K3 classes and then checks lifts back to `S`.

The degree-6 lifting helper `liftcands_pr(v)` computes a rank-44 negative-definite kernel and uses `CloseVectorsProcess`. The script explicitly prints an expected close-vector count of the form

```text
LkertrcE_vol * bound^(Dimension(LkertrcE)/2)
```

with `Dimension(LkertrcE)=44`; hence the lift-stage volume model has exponent `22`.

## What is reused

```text
REUSE_FULL_PICARD_LATTICE_AFTER_THEOREM_LOCK=true
REUSE_HYPERPLANE_CLASS=true
REUSE_AUTOMORPHISM_ACTION=true
REUSE_KNOWN_CURVE_INTERSECTION_FILTERS=true
REUSE_CLOSE_VECTOR_METHOD_AS_TEMPLATE=true
```

## What is not inferred

```text
UPSTREAM_CODE_ALREADY_ENUMERATES_D176_D192=false
DEGREE6_K3_REDUCTION_AUTOMATICALLY_GENERALIZES_TO_ALL_DEGREES=false
NONNEGATIVE_INTERSECTION_WITH_KNOWN_CURVES_IMPLIES_EFFECTIVE=false
FINITE_SEARCH_IMPLIES_PRACTICALLY_SMALL_SEARCH=false
```

Any production 176/192 enumeration must be a new computation with its own completeness and effectivity audit.
