# Stage35 35-05 — bad fiber and exceptional locus

```text
UNIT=35-05_BAD_FIBER_AND_EXCEPTIONAL_LOCUS
VERDICT=PASS
BAD_PARAMETER_DIVISOR=T*U*(T^2-U^2)*(T^2+U^2)*(T^4+U^4)
GEOMETRIC_BAD_FIBERS=10
BAD_PARAMETER_INTERSECTION_WITH_Q_GT_1=EMPTY
ALL_PHYSICAL_PARAMETER_FIBERS_SMOOTH=true
NEW_THEOREM_CREDIT=false
R29_FIB2_CLOSED=false
NEXT=35-06_UNIFORM_ARITHMETIC_ATTACK_BRANCHES
```

For `T^2+U^2 != 0`, normalize the selected diagonal genus-5 fiber by

```text
alpha=((T^2-U^2)/(T^2+U^2))^2,
beta=4*T^2*U^2/(T^2+U^2)^2,
alpha+beta=1.
```

An exact Jacobian multiplier/support exhaustion shows singularity iff `alpha in {-1,0,1}`. Restoring the normalization-failure locus gives the squarefree geometric bad divisor

```text
T*U*(T^2-U^2)*(T^2+U^2)*(T^4+U^4)=0.
```

It has 10 geometric points, exactly matching the Testa--Stoll Section 5 count of ten bad fibers for each rank-3 fibration.

None lies in the physical rational base `t in Q, t>1`: `0,infinity,+/-1` are outside; `T^2+U^2=0` and `T^4+U^4=0` have no rational projective points. The eight singular base-locus points of the original projection are also outside the physical open.

Therefore the 35-04 target needs no exceptional rational-parameter subproblem: every physical parameter `t>1` gives a smooth genus-5 fiber. The remaining wall is entirely the uniform rational-point exclusion on this smooth moving family.
