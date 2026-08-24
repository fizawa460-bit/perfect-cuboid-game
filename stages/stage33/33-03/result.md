# Stage33-03 — BR0B absolute-Galois UPic/Gersten production result

```text
STAGE33_UNIT=33-03
PR=1361
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0B=DISCHARGED
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
OPEN_ALGEBRAIC_Q_DEFINED_CLASS_INVENTORY_COMPLETE=true
KERNELS_COKERNELS_TORSION_EXACT=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PENDING_REAUDIT_AFTER_EXTENSION_CLASS_FIX
FILTRATION_EXTENSION_SPLIT_CLAIMED=false
FILTRATION_EXTENSION_CLASS_EXACT=true
NEXT_EXPECTED_COMMAND=Stage33-audit
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Scope

This production pass resumes exactly at the hostile-audit residual

```text
R33-BR0B-ABSOLUTE-HYPERCOHOMOLOGY-EXTENSION-CLASS
L33-03-COMPUTE-ABSOLUTE-H2-UPIC-EXTENSION-CLASS-AND-PRIMARY-ORDERS
```

left by the previous Stage33-audit.  The previously accepted exact prefix is retained; only the hidden absolute hypercohomology extension and the primary orders of its lifts are new here.

## Previously audited exact prefix

Let

```text
X_Q = Hom_cont(G_Q,Q/Z).
```

The prior hostile audit accepted:

```text
U_D = Z^14 with trivial absolute G_Q action,
Pic(Ubar) = Z^6 direct-sum (Z/2)^2,
H^3(G_Q,U_D)=0,
H^1(G_Q,Pic(Ubar)) = Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5,
H^2(V4,UPic) = (Z/2)^33,
H^1(V4,UPic) = 0,
(rank d2_01, rank d2_11) = (2,2),
```

and the exact filtration

```text
0
-> X_Q^14/<KAPPA_1,KAPPA_2>
-> H^2(G_Q,UPic(Ubar))
-> Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5
-> 0.
```

The audit correctly rejected the previous attempt to promote this filtration alone to a complete all-primary inventory, because the middle extension class had not yet been determined.

## Exact hidden extension

Write

```text
A = X_Q^14/<KAPPA_1,KAPPA_2>.
```

The exact `d2_01` materialization identifies the two torsion Postnikov classes as

```text
lambda_1 = v_1 * chi_-1,
lambda_2 = v_2 * chi_-1,
```

with independent unit-coordinate vectors

```text
v_1 = [1,0,1,0,0,0,0,0,1,1,1,1,0,0]
v_2 = [0,0,0,1,0,0,1,1,1,0,1,1,0,0].
```

For a right-filtration quadratic pair

```text
alpha=(alpha_1,alpha_2) in Hom_cont(G_Q,(Z/2)^2),
```

the hidden extension is now represented exactly by the doubling map

```text
delta(alpha_1,alpha_2)
  = [v_1*alpha_1 + v_2*alpha_2]
  in A/2A.
```

Equivalently a normalized lift `s(alpha)` satisfies

```text
2*s(alpha) = v_1*alpha_1 + v_2*alpha_2 in A.
```

This computes the extension class itself.  It does **not** assert that the filtration splits.

## Primary orders

For the quadratic-family part, the minimal order of a lift is exactly

```text
2  if delta(alpha_1,alpha_2)=0,
4  if delta(alpha_1,alpha_2)!=0.
```

No right-filtration quadratic class requires minimal lift order above four.
Because `v_1,v_2` are F2-independent,

```text
delta(alpha_1,alpha_2)=0
```

is equivalent to the two independent conditions

```text
[alpha_j] in span_F2([chi_-1]) inside X_Q/2X_Q,  j=1,2.
```

For `alpha_j=chi_d`, the Serre cyclic-quartic adapter gives the equivalent criterion that `(d,-1)` is either `0` or `(-1,-1)` in `Br(Q)[2]`; equivalently at least one of `d` and `-d` is a norm from `Q(i)`.

The five finite classes `PICU-FREE-H1-1` through `PICU-FREE-H1-5` have order-two absolute lifts.  The exact V4 bar check shows that the two torsion Postnikov generators already account for the full finite `rank(d2_11)=2`; hence `d2_11` vanishes on the five free `H^1(V4,F)` classes, whose lifts lie in the exponent-two group `H^2(V4,UPic)=(Z/2)^33` and inflate absolutely.

## Exact all-primary inventory

The final inventory therefore keeps the exact filtration

```text
0
-> A
-> Br_a(U)=H^2(G_Q,UPic(Ubar))
-> Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5
-> 0
```

together with its exact extension class `delta` above.

The left odd-primary part remains

```text
X_Q,odd^14,
```

and the left two-primary part is

```text
X_Q[2^infinity]^14/<KAPPA_1,KAPPA_2>.
```

Thus all primary families and the primary orders/group law of the right-filtration lifts are accounted parametrically without making a split claim.

## Exact computation and source locks

Functional head audited by the new CI pass:

```text
a5264ad5e4001a54e6e61729db0aada5ca6b2b4a
```

Workflow:

```text
run=32706986905
run_number=57
conclusion=success
artifact_id=9512907728
artifact_zip_sha256=bf84653fce4a22b733ef36dcb571b3f06b9485d2afb7a27494c84eb769872f33
```

New exact certificate hashes:

```text
absolute-h2-extension-class.json
  canonical_sha256=8016e883ad7dbaca6abf77de0ae9e504532f6b71e2c5e99853767143a39185fc

br0b-all-primary-inventory.json
  canonical_sha256=b29957e51f34c73c12279460e48dc95b3a37f371e5fb35099c024dcea0df4743

handoff-preaudit.json
  canonical_sha256=7b6f7c432ed07ca102cbd710c7f3708214396dee577039caafa90f22f99e310f
```

External theorem locators used in the absolute adapter are:

```text
J. S. Milne, Arithmetic Duality Theorems, Chapter I section 4 Corollary 4.17
  H^r(G_K,Z)=0 for odd r; used for H^3(G_Q,Z)=0.

J.-P. Serre, Topics in Galois Theory, Chapter 1 section 1.2,
Theorem 1.2.4 and the following cohomological proof, printed pp. 4-5
  Bockstein x -> x cup x and (epsilon,epsilon)=(-1,epsilon);
  used for the cyclic-quartic/sum-of-two-squares adapter.
```

## Handoff boundary

Stage33-03 now claims all ten non-audit closure conditions.  By the Stage33 unit contract it remains

```text
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
STAGE33_PROGRESS=2/11
STAGE33_06_RELEASED=false
```

until a fresh hostile audit accepts the new extension-class certificate.
