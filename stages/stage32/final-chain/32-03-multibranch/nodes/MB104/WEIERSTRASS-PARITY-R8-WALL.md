# Stage32 MB104 — Weierstrass parity is blind to R8 magnitude

Status: **RETAINED ROUTE WALL / MB104 INCOMPLETE / NO CREDIT**

The retained Stage32 O210/Q602 Weierstrass-parity asset proves, for its fixed source-locked carrier, the exact odd-contact identity

```text
n_p = M_p - 2*y_p,
n_p mod 2 = M_p mod 2,
```

and uses the resulting branch-point permutation to identify a nontrivial rank-one symplectic transvection on hyperelliptic `J[2]`.

Source:

`stages/stage32/residual-32-01-production/post1505-o210-q602-weierstrass-parity-transvection-refinement.json`

The asset is highly effective for finite mod-2 residue pruning, but the information it exports at the contact-count layer factors through parity. In particular, replacing any local branch/contact count by

```text
M_p -> M_p + 2k
```

leaves the parity datum unchanged. An FSM-minimal branch has exceptional multiplicity one, so adding two minimal branches at a node can increase `R8` by two without changing this parity layer.

Therefore no argument that uses only the retained Weierstrass parity / transvection datum can upper-bound the magnitude of `R8`. A successful MB104 reuse would need extra non-parity information (integral multiplicity, higher congruence, conductor, jet, or another global inequality), not merely the transvection predicate.

This statement does not generalize the fixed O210 correspondence theorem to every multibranch carrier; it records the narrower structural fact that the retained parity output, even if an appropriate adapter existed, is magnitude-blind modulo additions of two.

No finite degree window, receiver credit, route credit, theorem credit, endpoint credit, or merge authorization is granted.
