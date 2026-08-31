# Stage33-05 — K3 Br[2] Q-action and arithmetic descent

```text
STAGE33_UNIT=33-05
UNIT_STATUS=CLOSED
UNIT_CLOSED=true
DOWNSTREAM_RELEASED=true
STAGE33_PROGRESS=6/11
HOSTILE_AUDIT=PASS
```

Stage33-05 is reclosed through the **exact-zero-survival** alternative in the original unit closure contract. This does not restore the revoked historical `ell_J2` and does not prove that corrected `J2` descends to Q.

## Geometric invariant receiver

The exact geometric invariant two-primary Brauer receiver is

```text
Br(Kc_bar)[2]^G_Q = span_F2{J2,q1}
dimension = 2
```

with corrected geometric

```text
J2=(f2,1),
marked J2=[1,0],
T(X_J2)=<8> direct_sum <16>.
```

The historical Q-defined `ell_J2` / `ell_Q` witness remains revoked because its full geometric Creutz--Viray class is zero.

## Arithmetic HS classification

The previously isolated q1 route remains valid independently of the revoked J2 producer:

```text
d2(q1)|_<ct> != 0.
```

The corrected J2 surface calculation now gives

```text
cc Pic/2 defect = 0,
ct Pic/2 defect = [0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,0],
Z_J2=(B+ct(B))/2
    =[0,0,0,0,0,0,0,1,1,1,-1,0,0,0,2,1,0,0,0,0],
d2(J2)|_<ct> != 0.
```

The two restricted classes are not equal. Using two ct-fixed marked Picard tests, `CsK[2]` and `CsK[5]`, their mod-2 pairing signatures are

```text
             CsK[2]  CsK[5]
J2              1       1
q1              1       0
```

so the signature matrix has determinant `1` over F2. Equivalently, all three nonzero elements `J2`, `q1`, and `J2+q1` have nonzero restricted HS d2. Hence

```text
rank_F2(d2|_<ct> on span{J2,q1}) = 2,
ker(d2|_<ct>) = 0,
ker(global d2 on Br(Kc_bar)[2]^G_Q) = 0,
Q_RELEVANT_SURVIVING_DIM = 0.
```

Primary certificates:

```text
stage33-05-br2-zero-q-survival-after-j2-nogo.json
canonical_sha256=a48386c523e8c98b1d2b22a7dc3d789e4cea1bfa4557e658fb150e3c6b85a585

stage33-05-br2-zero-q-survival-hostile-replay.json
canonical_sha256=4e9f20c1f753bb63134207422b097c1985ce3edd6be87f7f41ba8afa316e7dc9
status=PASS_HOSTILE_REPLAY_EXACT_ZERO_K3_BR2_Q_SURVIVAL
```

## Closure interpretation

The Stage33-05 closure contract explicitly allows

```text
ALL_SURVIVING_K3_CLASSES_HAVE_EXPLICIT_ARITHMETIC_REPRESENTATIVES=true
OR EXACT_ZERO_SURVIVAL_CERTIFICATE=true.
```

The second branch is now exact and hostile-replayed. Therefore Stage33-05 closes even though corrected J2 itself has nonzero HS d2 and no Q-defined Brauer preimage.

```text
K3_GEOMETRIC_BR2_DIM=2
QI_OVER_Q_ACTION_MATRIX_EXACT=true
INVARIANT_DESCENDED_SUBSPACE_EXACT=true
DESCENT_OBSTRUCTION_ACCOUNTED=true
Q_RELEVANT_SURVIVING_DIM_EXACT=true
Q_RELEVANT_SURVIVING_DIM=0
EXACT_ZERO_SURVIVAL_CERTIFICATE=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
UNIT_STATUS=CLOSED
```

## Dependency rebuild

The old J2-repair-specific successful-exit gate

```text
corrected J2 d2=0 -> Q-defined J2 preimage
```

is no longer a valid prerequisite for downstream Stage33. The downstream adapter must instead consume the complete arithmetic classification of the K3 Br[2] invariant block, allowing exact zero survival. In the current case that input is the empty K3 Br[2] Q-survivor list.

Next exact leaf:

```text
REBUILD_STAGE33_12_EXIT_ADAPTER_TO_CONSUME_ZERO_K3_BR2_Q_SURVIVAL_WITHOUT_J2_Q_PREIMAGE
```

Stage33-07 and Stage33-12 are not closed by this result alone; the independent BR0B/BR0G/global inventory obligations remain governed by their own repair contracts.

## Firewalls

```text
CORRECTED_J2_Q_DEFINED_BRAUER_PREIMAGE=false
R5_FULL_SUCCESSFUL_J2_DESCENT_EXIT=false
STAGE33_05_RECLOSED=true
STAGE33_07_CLOSED=false
STAGE33_12_CLOSED_EXACT=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
