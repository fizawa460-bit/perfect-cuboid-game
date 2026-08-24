# Stage33-07 — BR2A full relevant class inventory — audited CLOSED

Hostile audit verdict:

```text
PASS_AFTER_J2_PROPER_TRANSCENDENTAL_ENDPOINT_SURVIVAL_AND_EXACT_BR0B_BR0G_GLOBAL_INTEGRATION
```

```text
STAGE33_UNIT=33-07
UNIT_STATUS=CLOSED
UNIT_CLOSED=true
DOWNSTREAM_RELEASED=true
BR2A=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
CLOSURE_CRITERIA_TOTAL=14
CLOSURE_CRITERIA_SATISFIED=14
HOSTILE_AUDIT=PASS
STAGE33_PROGRESS=7/11
STAGE33_08_RELEASED=true
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```

## Audited exact integrated inventory

The frozen Stage33 relevant Q-defined Brauer scope is accounted for without double-counting BR0B.

```text
odd-primary constant-character block:
  Hom_cont(G_Q,Q/Z)_odd^48
    direct_sum
  Hom_cont(G_Q(i),Q/Z)_odd^12

two-primary constant-character block:
  Hom_cont(G_Q,Q_2/Z_2)^48
    direct_sum
  Hom_cont(G_Q(i),Q_2/Z_2)^12

finite nonconstant two-primary block:
  (Z/2)^50 direct_sum (Z/4)^12

seven-line endpoint block:
  0
```

The finite block is the exact BR0G ramified module

```text
(Z/2)^49 direct_sum (Z/4)^12
```

plus the independent proper K3 class `J2 ~= Z/2`.

BR0B is counted exactly once as its injective image inside the boundary constant-character block. Its audited Stage33-03 nonsplit filtration is preserved; no splitting is claimed.

## J2 endpoint survival is exact and locally nonconstant

Stage33-05 left one Q-relevant K3 class, `J2`. Stage33-07 now certifies all of the following:

```text
J2_Q_DEFINED=true
J2_EXACT_ORDER=2
J2_ENDPOINT_PULLBACK_NONZERO=true
J2_PROPER_UNRAMIFIED=true
J2_PROPER_TRANSCENDENTAL=true
J2_Q2_EVALUATION_NONCONSTANT=true
```

At the genuine endpoint `Q_2` lift `(t,s)=(2,3)`, the specialized corestriction has invariant `1/2`. A seven-point scan on the endpoint `Q_2` locus realizes both `0` and `1/2`; in particular, the pulled-back class is not constant modulo `Br(Q)`.

The proper-extension argument uses the proper K3 target at every codimension-one DVR of the regular cuboid surface, followed by Brauer purity. Testa--Stoll Theorem 10 was independently source-checked: the algebraic Brauer group of the proper cuboid surface is exactly the image of `Br(Q)`, with the proof computing `H^1(Q,Pic(Sbar))=0`. Therefore the nonconstant proper pullback of `J2` is transcendental.

## BR0B / BR0G integration

The compactification exact segment together with `H^1(Q,Pic(Sbar))=0` makes the full BR0B boundary map injective, including the Stage33-03 right filtration. Hence the BR0B/BR0G constant-character overlap is exactly the injected BR0B image.

The finite BR0G presentation has

```text
unit-symbol rank F2 = 44
graph-residual rank F2 = 17
combined exponent-two rank F2 = 61
order-four generators = 12
order-four double projection to R17 rank = 3
order-four double intersection with U44 rank = 9
```

and Smith form

```text
1^12, 2^49, 4^12,
```

giving `(Z/2)^49 direct_sum (Z/4)^12` exactly.

Finite-coefficient Gersten/Faddeev exactness and Kummer supply exponent-preserving lifts of exact order 2 and 4. Adding the independent order-two `J2` gives the audited augmented Smith counts

```text
1^12, 2^50, 4^12,
```

hence `(Z/2)^50 direct_sum (Z/4)^12`. The 74x120 mixed-modulus relation/symbol compatibility is exact. No hidden order-8 extension is promoted.

NF-PHYS2/CAMP4 remain hypothesis-gated and are not invoked for closure.

## Evidence

Audited functional head and current-head run:

```text
audited_functional_head=5f469907c125cdabd96c9084fd107fc79d57b6ad
workflow_run=32730159528
workflow_run_number=22
workflow_conclusion=success
artifact_id=9521076746
artifact_zip_sha256=c9de08cff9ce04b0bfe1fd216e176996437d44fa7c841673f037400ad8e47dca
```

All JSON certificates in the downloaded artifact were independently canonical-rehashed and matched:

```text
j2_endpoint_q2_pullback=90a697b703b7928e47572f33eac228c539239a78b83898631c2064deb8e3a495
j2_q2_variation=580837c7b986ba9a26821eee8a8379fff1122a5ce1add5d65cb28207b9885e69
integration_prefix=0725953e32305ff864284fe082d6bc8e81afc308ab8ccb0704ab6673b2f19c49
br0b_boundary_residue_map=44f03877c524a817e41036d89cf20ea971cc95c3d52adf53c2af6317a83d2324
br0g_finite_ramified=5725302099557d0770d032e901a3cb6429107f108afc673ba61ea0e555d836cf
full_br0b_boundary_injection=8f00de8408589c05baad22e1136a900bf3edfdbdb005c028a2b8138afc2a4469
global_two_primary=2335f1376ab190d47985d48702f24defb89107512ddee8f29fe828c8286cdc13
```

## Firewall

This closes the Stage33 class-inventory integration, not the Brauer--Manin problem.

The obstruction chain now has a genuine exact partial success for `J2`:

```text
A. nontrivial Q-defined endpoint class   DONE
B. nonconstant local evaluation at Q2   DONE
C. global reciprocity kills every
   physical adelic candidate             NOT DONE
```

Therefore:

```text
BRAUER_MANIN_SET_EMPTY_NOT_PROVED=true
ENDPOINT_EMPTY_NOT_PROVED=true
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Stage33-08 is released to materialize explicit evaluable representatives for the complete audited inventory.
