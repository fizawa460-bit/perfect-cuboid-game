# Exact Campedelli-kernel enumeration checkpoint

```text
SCRIPT=stages/stage29/29-02hb/campedelli_kernel_check.py
ARITHMETIC=EXACT_F2
STATUS=PASS_ALL_ASSERTIONS_AFTER_ADVERSARIAL_AUDIT
```

Audited output:

```text
raw_admissible_labelings=1680
GL3_F2_order=168
distinct_rank3_kernels=10
geometric_arrangement_aut_order=24
geometric_Qi_kernel_orbit_sizes=8,2
certified_Q_liftable_base_aut_order=6
certified_Q_kernel_orbit_sizes=6,2,2
exact_Q_isomorphism_class_count_not_claimed=true
```

The ten kernels are labelings modulo target `GL(3,F2)`, hence ten distinct rank-3 subgroups of the six-dimensional sign deck group. The checker also verifies for every admissible labeling that the three inertia labels at every triple point are linearly independent; equivalently the kernel meets the local triple inertia trivially.

Each kernel is represented upstairs in `F2^7` by a rank-four nullspace containing the all-ones projective-sign relation; quotienting by that relation gives rank three in `Gamma`.

The original `8+2` count remains exact, but only as a geometric / `Q(i)` statement. Stage29-02ha already proves that the full arrangement `S4` lifts over `Q(i)` while only its coordinate-permutation `S3` subgroup lifts over `Q`. Under that certified Q-defined subgroup, the ten kernels split as

```text
6 + 2 + 2.
```

Thus no arithmetic reduction from ten kernels to two representatives is allowed. Three Q-symmetry representatives are certified sufficient; whether some of those are nevertheless Q-isomorphic by maps not lifting to the endpoint is left open.
