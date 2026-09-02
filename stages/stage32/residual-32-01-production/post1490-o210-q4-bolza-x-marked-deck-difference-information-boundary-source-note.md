# Stage32 post1490 O210: X-side marked deck-difference information boundary

## Purpose

This leaf records an exact information boundary. It does **not** assign the three nonidentity deck elements to the retained marked exceptional support.

The current retained projected payload contains 48 marked exceptional nodes, grouped into 12 realized boundary pairs (four nodes per pair), together with the 12 pair masses totaling 266. The marked-node records contain only the exceptional label and the two projected boundary labels. The pair-mass records contain only the two projected boundary labels, exceptional mass, and `m2_capacity`.

The retained V4 cusp quotient separately gives the six abstract quotient cusp orbits, but its firewall explicitly says that these abstract cusp orbits have **not** been identified with the retained boundary labels. Therefore the serialized retained data do not contain a relative `H_diag` lift / `G_diag/H_diag` deck-difference label.

## Exact non-identifiability witness

Take the retained ordered pair masses

`[5,5,21,25,24,18,19,35,28,34,32,20]`.

Annotating the same 12 visible records cyclically by `(g1,g2,g1+g2)` gives grouped visible masses `(83,96,87)`. Annotating the same records in three blocks of four gives `(56,96,114)`. Both annotations use each nonidentity label four times, and deleting the annotation recovers exactly the same visible retained records.

This is an information witness only; it is **not** a claim that either annotation is geometrically realized. Its role is narrower: no ordered deck split can be source-locked from the serialized projected records alone without an additional X-side lift/deck-difference datum.

## Consequence

Keep the exact retained identity

`delta_D + c_g1 + c_g2 + c_g1_plus_g2 = 8586`, with `c_t=D.t(D)/2`.

The visible exceptional mass 266 is not any `c_t`, and the annotation witness must not be promoted to geometry. The next exact leaf is to source-lock, for each relevant marked local branch/node, its lift to `X=P/H_diag` or an equivalent relative `G_diag/H_diag` deck-difference label, together with the local intersection multiplicity needed to accumulate `D.t(D)`.

No O210 exclusion, receiver/route/theorem/endpoint credit, FULL178 authorization, or perfect-cuboid claim is made.
