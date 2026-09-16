# Stage32 MB104 source note: exact `Aut(S)` action on box nodes

Status: **IMMUTABLE EXTERNAL SOURCE LOCK / NODE-ACTION ADAPTER ONLY / NO CREDIT**

This note records the exact external formulas used by the span-five hyperplane orbit classifier.

## Immutable source

Repository: `MichaelStollBayreuth/Verification`

Commit: `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`

Path: `Cuboids/cuboids.magma`

Git blob SHA-1: `0422b69847f2afb97cb7b3ed02ebef91279f61b1`

The source constructs the 48 singular points of the perfect-cuboid surface, gives nine coordinate substitutions generating the automorphism action, computes the induced permutations on singular points and known curves, descends the action to `Pic(S)`, and verifies `#Aut(S)=1536`.

## Exact coordinate substitutions

Coordinates are ordered

```text
[a1,a2,a3,b1,b2,b3,c].
```

The nine substitutions are

```text
1. [a2, a1, a3, b2, b1, b3, c]
2. [a3, a2, a1, b3, b2, b1, c]
3. [i*c, a2, a3, b1, i*b3, -i*b2, -i*a1]
4. [-a1, a2, a3, b1, b2, b3, c]
5. [a1, -a2, a3, b1, b2, b3, c]
6. [a1, a2, -a3, b1, b2, b3, c]
7. [a1, a2, a3, -b1, b2, b3, c]
8. [a1, a2, a3, b1, -b2, b3, c]
9. [a1, a2, a3, b1, b2, -b3, c]
```

The current verifier applies these monomial linear transformations to its own exact `Q(i)` 48-node model and matches projective images back to that same model. Using the forward substitutions rather than Magma's scheme-side inverse convention does not change the generated subgroup, because replacing generators by their inverses generates the same group.

The verifier then explicitly checks that the generated permutation group on the 48 nodes has order `1536`, matching the immutable source.

## Scope firewall

This note supplies only the exact node action needed for orbit classification. It does not by itself prove any span-five carrier is effective or irreducible, does not close MB104, and grants no receiver/theorem/endpoint credit.
