# Stage29-02 — additional new-foundation lenses

The initial F1--F4 pass uncovered two further materially distinct endpoint descriptions.  They are added to the screening instead of being forced into the original four labels.

## F5 — modular quotient / product-of-curves model

Testa--Stoll, building on Beauville, identify the full cuboid surface geometrically with a quotient of `X(8) x X(8)` by a diagonal `(Z/2)^3` action.  Over `Q(i)` the quotient is explicit; over `Q` the corresponding description uses the Weil restriction.  The same construction gives a quotient quadric `Q`, split over `Q(i)`, hence geometrically `P1 x P1`.

This is materially different from the Stage18 shared-edge toric parametrization: it is a modular/product-of-curves model of the **full endpoint surface**.

Potential Stage29 roles:

- connect endpoint rational points to level-8 elliptic-curve data;
- compare the quotient `P1 x P1` with the Stage18/28 base `Bl_4(P1 x P1)`;
- expose additional involutions/quotients and natural low-genus covers;
- provide a modular-form/cohomological interpretation of local traces.

```text
F5_NEW_FOUNDATION_FOUND=true
F5_KIND=MODULAR_X8_PRODUCT_QUOTIENT
F5_OLD_GATE_REPLAY=false
F5_BACKFLOW_RECOMMENDED=false
```

No claim is made that rational points on the quotient lift to rational points on `X(8) x X(8)` without twists; Faltings on the factors therefore does not solve the perfect-cuboid problem directly.

## F6 — arithmetic cohomology / L-function lens

Horie--Yamauchi, arXiv:2512.22520v3 (2026 revision), compute the `L`-function of the full cuboid surface and explicitly determine its geometric Picard group as a `G_Q`-module.  Their Theorem 1.1 decomposes the degree-two étale cohomology into weight-3 modular-form pieces plus twisted Tate/Dirichlet-character pieces.

This is a new arithmetic foundation for Stage29 because the earlier stages used local square tests and marginal Euler products rather than the étale-cohomological trace of the full endpoint surface.

Potential Stage29 roles:

- exact Frobenius-trace / finite-field point-count diagnostics for the endpoint surface;
- comparison with the F4 cross-character local correlation;
- identification of which local oscillations are algebraic/Picard versus transcendental modular-form contributions;
- a future adapter between the joint-cover local character sum and the known endpoint cohomology.

```text
F6_NEW_FOUNDATION_FOUND=true
F6_KIND=ENDPOINT_L_FUNCTION_AND_GALOIS_PICARD_MODULE
F6_SOURCE=arXiv_2512.22520v3
F6_OLD_GATE_REPLAY=false
F6_BACKFLOW_RECOMMENDED=false
```

Firewall: the existence of an `L`-function factorization or explicit finite-field traces does not imply a global rational-point count or perfect-cuboid existence/nonexistence theorem.

## Updated split queue

```text
29-02a = global endpoint surface geometry / low-degree curve literature lock
29-02b = joint V4 cover geometry preflight
29-02c = low-genus / coverage / fibration reuse screen
29-02d = modular quotient / X(8)xX(8) endpoint adapter screen
29-02e = endpoint L-function / local-trace adapter screen
```

The suffixes are opened only as needed; this file does not require all five child routes to be completed before the parent screening can be audited.
