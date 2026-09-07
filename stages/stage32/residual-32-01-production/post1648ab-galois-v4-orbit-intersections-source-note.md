# Stage32 post1648AB Galois V4 orbit-intersection source note

Scope: the same fixed recovered V6 class `D` used by post1648AA, target `g1-d186`, `(d,e,a,u,v)=(186,266,592,-44,32)`, `O=210`, `q'=4`, `Q=602`. This is a scratch diagnostic leaf and carries no controller, receiver, route, theorem, endpoint, or perfect-cuboid credit.

## Exact Galois action

Reuse the source-locked Stage33-07 Galois adapter. Its `cc` is complex conjugation `i -> -i`; its `ct` is the independent conjugation `sqrt(2) -> -sqrt(2)` with `i` fixed. They are commuting involutions on the same 140 retained divisor classes and are reconstructed as integral Picard64 isometries in the primitive INDLIST basis.

Do not confuse either with the geometric coordinate-sign involution `sigma_c: c -> -c` used for the quotient `S -> K_c`. The older K_c replay is a separate route and already gave `(pi_*C)^2=3266>0`, hence nonexclusion.

## Exact V4 orbit calculation

Transport the exact V6 class through `1, cc, ct, cc*ct`. The four Picard classes are pairwise distinct. Every class has square `758`. The six distinct pairwise intersections are

- `D.ccD = 1116`,
- `D.ctD = 1026`,
- `D.ccctD = 1348`,
- `ccD.ctD = 1348`,
- `ccD.ccctD = 1026`,
- `ctD.ccctD = 1116`.

All are positive, so the simple obstruction "two distinct effective integral curves cannot have negative intersection" does not exclude a carrier.

The retained Satake-factor incidence replay gives bidegrees

- `D` and `ctD`: `(105,81)`,
- `ccD` and `ccctD`: `(81,105)`.

This independently distinguishes the cc-paired factor orientation and is consistent with post1648AA.

## Conditional rational-support reduction

Assume an integral curve `C` exists in the exact class `D`. A `Q`-rational point is fixed by both Galois involutions, hence any `P in C(Q)` lies on all four conjugate curves. In particular

`C(Q) subset C intersection ct(C)`.

Since `[C] != [ct(C)]`, the two integral curves are distinct and the intersection is proper zero-dimensional. Its total scheme-theoretic length is the exact intersection number

`D.ctD = 1026`.

Thus post1648AB improves the post1648AA finite-support envelope from length `1116` to length `1026`. It does not identify that support and does not exclude any rational point in it.

## Firewalls

- Picard-class transport is not effectivity or integral-carrier existence.
- Positive intersection is not rational-point existence.
- A length bound is not a support list.
- No residue-specific commutator is obtained.
- Survivors remain `[73,97,235]`.
- `Q602_excluded=false`, `O210_excluded=false`, and no O212+ advance is authorized.

Next exact route: source-bind the scheme-theoretic support of `C intersection ct(C)`, or obtain an equivalent local `ct`-fixed-point adapter. Pure numerical Galois intersections are exhausted by this V4 replay.
