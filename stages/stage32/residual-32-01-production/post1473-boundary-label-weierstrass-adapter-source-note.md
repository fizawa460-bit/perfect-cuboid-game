# Stage32 retained-boundary to genus-2 Weierstrass cusp adapter source note

Scope: this note supplies the source/provenance binding requested by hostile audit review 5083453635 for `diagnose_stage32_post1473_boundary_label_weierstrass_adapter.py`. It is an adapter note only; it is not an O=188 exclusion.

## Pinned exact inputs

- Satake 6+6 marking canonical: `69a2a6d3cdf7b0d5c6162424a8102ec41cd09ac7e303469d30577d454363e31d`
- 48 exceptional incidence canonical: `efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143`
- repaired c=0 perfect-matching partition: bound by the companion certificate
- X(8)/V4 cusp quotient canonical: `2869208e7509d7b79378264ea1982299b0f1745b1a54c5856cfbba0754567ce5`

The V4 quotient source lock is Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, arXiv:1303.6495v1, Section 4 Lemma 4.1 and the Section 2 genus statement.

## Theta-ratio normalization

The replay uses the projective modular ratio

`r(z) = theta10(2z) / theta00(2z)`.

The six relevant cusp values are fixed as

- `r(0)=+1`
- `r(2)=-1`
- `r(1)=+i`
- `r(3)=-i`
- `r(infinity)=0`
- `r(1/2)=infinity`.

The normalization is determined by the q-expansion at infinity together with the standard Jacobi theta transformations under `S:z -> -1/z` and translation. The transformation formulas are source-locked to NIST DLMF Chapter 20, especially Section 20.7(viii), equations 20.7.27--20.7.32. The replay uses only the induced projective ratio values, so common nonzero theta multipliers cancel.

For this normalization the exact V4 cusp-orbit replay gives

`{+1:1, -1:6, +i:3, -i:5, 0:2, infinity:4}`.

## Retained-label binding

The Satake marking replay fixes the twelve retained C2 labels as

- first/z: `{34,35,38,39,42,43}`
- second/w: `{33,36,37,40,41,44}`.

Using the exact block/sign equations in `diagnose_stage32_post1473_x8_satake_boundary_marking.py`, the theta-ratio values above, and the V4 cusp-orbit enumeration, the retained-label to quotient-cusp map is

- `33 -> 6`, `34 -> 6`, `35 -> 1`, `36 -> 1`
- `37 -> 5`, `38 -> 3`, `39 -> 5`, `40 -> 3`
- `41 -> 4`, `42 -> 4`, `43 -> 2`, `44 -> 2`.

The three X(2)-block cusp pairs and their outside-V4 inertia labels are

- `Z1: {1,6}`, inertia `T4*u`
- `Z2: {3,5}`, inertia `T4*uv`
- `Z3: {2,4}`, inertia `T4*1`.

The exact 48-node incidence then transports to twelve ordered cusp pairs, each with multiplicity four. The c=0/c!=0 perfect-matching split is inherited from the repaired machine-readable c=0 certificate.

## Firewalls

- This adapter identifies retained boundary labels with the six abstract genus-2 quotient cusps/Weierstrass points.
- It does not identify any hypothetical O=188 defect branch with a retained node.
- It does not prove existence or nonexistence of a degree-93 global correspondence.
- It excludes none of A/B/C by itself.
- O=188 remains OPEN; FULL178 remains inactive.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit is released.
