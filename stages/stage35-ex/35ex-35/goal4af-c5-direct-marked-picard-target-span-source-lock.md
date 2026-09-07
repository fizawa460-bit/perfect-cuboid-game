# Stage35-EX Goal4AF source lock — direct C5 marked Picard adapter and target-span test

Scope: continue only the Goal4AC/Goal4AE class-B `Q(i)/Q` cyclic principalization route. Goal4AF computes the missing marked Picard classes of the four antipodal C5 residual pairs and tests the fixed Goal4AA 69-support divisor target against the old complete-linear-section span augmented by marked representatives of those C5 pair classes. This leaf does not identify a marked representative with the literal C5 support divisor, does not construct `F_B`, and grants no Brauer–Manin or E1 credit.

## Exact parent and source locks

- parent live V68 head before Goal4AF promotion: `00d4c9bf9bb37781c81954fb41f22e97d721995b`;
- immutable V68 snapshot: `stages/stage35-ex/snapshots/MAIN-STATE-V68-00d4c9bf9bb3.json`, snapshot creation commit `bf16d58cc1d85a930073184a2ac6309e5ff4d095`;
- pinned upstream source: `MichaelStollBayreuth/Verification`, commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/cuboids.magma`, git blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`;
- Stage33 primitive Picard certifier: `stages/stage33/33-07/certify_two_coordinate_swap_picard_rows.py`, blob `296e2005f822ae89c1aa085161553fe9ef76d077`;
- Goal4AB verifier: `stages/stage35-ex/verify_stage35_ex_35_goal4ab.py`, blob `347cc43a60f7772d6c8b3f4145839cf9978b4114`;
- C5 receiver diagnostic: `stages/stage35-ex/diagnose_stage35_ex_35_goal4af_c5_branch_conic_receiver_v4.py`, blob `cd80f7533dd865eb68ad75e0f25454d542ebf4e7`;
- target-span diagnostic: `stages/stage35-ex/diagnose_stage35_ex_35_goal4af_c5_target_span.py`, blob `3a5045f7f3c48a2f93a8116090beca1422bafac3`.

## Exact marked-Picard receiver solve

The retained sign/Galois constraints determine a C5 pair class up to one final Picard direction: rank 63, nullity 1. The remaining direction is detected exactly by retained C1 curves 25 through 32. For the seed pair `(e1,e2,e3)=(1,1,1)`, source C1 #25 is

`c=0, i*a1+b1=0, i*a2+b2=0, i*a3+b3=0`.

On C1 #25, either `e4=±1` C5 curve restricts to the line `a1+a2+a3=0`. This line cuts the conic `a1^2+a2^2+a3^2=0` in two distinct points; after `a1=1`, the equation is `2(r^2+r+1)=0`, with discriminant `-3`. The exact retained 48-node model shows neither intersection point is singular, so there is no blow-up subtraction. Hence each seed C5 has intersection 2 with C1 #25 and the pair has intersection 4.

Adding only this source-computed receiver raises the exact system from rank 63 to rank 64. Exact run:

- head `5b395e62f83337959297794e93ca1e6facb0828d`;
- workflow `34071239834`;
- job `101588889887`;
- conclusion `SUCCESS`;
- marker `GOAL4AF_BRANCH_CONIC_RECEIVER_G10_BOUNDARY=PASS`.

The solve materializes all eight C5 pair classes and the four Goal4AC antipodal residual-pair classes. The four residual pairs use exactly two distinct primitive INDLIST64 classes, each twice. For these residual rows the strict and total-pullback marked classes coincide; the contracted-exceptional correction is zero.

The observed pair square is 8 and the observed antipodal total-pair relation is `D_t + D_{-t}=2H`. Neither observation is used as a solver constraint.

## Exact target-span test

Goal4AB had 43 exact complete degree-16 linear-section divisor columns in the retained 140-divisor packet, with Q-span rank 31. The fixed class-B formal target has support count 69 and is outside that rank-31 span.

A primitive INDLIST64 row is embedded as a marked representative in the retained 140-divisor packet by placing its 64 coefficients on the corresponding 64 primitive INDLIST basis curves. The diagnostic verifies the embedding by mapping it back through the retained Picard marking. This is a marked representative only; it is not asserted to equal the literal geometric C5 support divisor.

Adjoining the four Goal4AC residual-pair marked representatives contributes two independent columns and raises the span rank from 31 to 33. The fixed 69-support target remains outside the resulting Q-span.

Exact run:

- head `00d4c9bf9bb37781c81954fb41f22e97d721995b`;
- workflow `34071619263`;
- job `101589927928`;
- conclusion `SUCCESS`;
- result: `augmented_column_count=47`, `augmented_span_rank=33`, `formal_target_in_Q_span_after_adjoining_c5_marked_representatives=false`;
- marker `GOAL4AF_TARGET_SPAN_G12_BOUNDARY=PASS`.

## Consequence and firewall

Goal4AF therefore acquires the previously missing C5 pair marked-Picard adapter and completes the requested marked-representative target-span test. The result is bounded negative: the Goal4AA 69-support target is not synthesized by the old rank-31 complete-linear-section span even after adding the two new C5 marked-Picard directions.

This does **not** prove the target divisor nonprincipal and does **not** prove global nonexistence of `F_B`. It blocks only this retained marked-representative augmentation. The general graded-coordinate-ring / Riemann–Roch principal-function synthesis remains open and is the next legal leaf.

Still uncomputed/unproved:

- literal actual C5 support vectors in the retained 140-divisor packet identified with these marked representatives;
- an explicit rational function `F_B` or a proof that no such function exists;
- full algebraic Brauer group on the open receiver;
- local evaluations, verticality, or Brauer–Manin obstruction;
- E1, R29-PESCH-E1, R29-FIB2, Stage35 closure, or any perfect-cuboid theorem.
