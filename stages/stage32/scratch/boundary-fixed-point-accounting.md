# Boundary fixed-point accounting — conditional scratch follow-up

Status: SCRATCH_ONLY, UNAUDITED. Continuation of arbitrary-contact-parity-conditional-lemma.md.
Snapshot: f2a89e613cdf91191a0aada9e90c9fc93373a6c6.

## Sources checked

- stages/stage32/residual-32-01-production/post1484-v6-modular-factor-bidegree-source-note.md
  Blob lock recorded by EX1-05F: deeecac5599f3b542b445cd87c2070dae488bc85.
- stages/stage32-ex1/ex1-05f-h4-local-cusp-projection-ramification-adapter.json
- stages/stage32-ex1/ex1-05f-h4-local-cusp-projection-ramification-adapter.md

The resolved cusp fiber is exactly 2L + sum E_j, with eight incident exceptional curves per L.
This source statement is for the fixed V6 class, not only its O210 slice.

## Conditional exhaustion of fixed-point locations

Assume the common degree-two cover of the normalized original carrier N
is the normalization of the pullback of C2->X(4), branched only at its
six special cusps. Work over C. Assume N's image is not a fiber component;
the positive factor degrees 105 and 81 exclude constant factor maps here.

At any point t of N over a cusp, write the pulled-back parameter as
u=t^k times a unit. Normalization of v^2=u is ramified exactly when k
is odd. Thus:

1. Away from the six cusp fibers, the base cover is etale and remains
   etale after pullback. No fixed point of the double-cover involution
   appears there, even if the original image curve was singular: the
   base is N, its smooth normalization.
2. At a smooth boundary point outside exceptional curves,
   k=2*I_t(N,L) is even for every positive tangency order. Consequently
   higher boundary tangency creates no extra fixed point.
3. At an exceptional contact, k=I_t(N,E_j)+2*I_t(N,L).
   Odd k is equivalent to odd exceptional contact. This remains true
   at L intersect E_j and when distinct normalized branches meet the
   same resolved point.

The exceptional curves over distinct surface nodes are disjoint.
Hence all ramification of this specified pullback is accounted for by
odd exceptional contacts. Boundary tangencies introduce no additional
fixed-point parity contribution. This is a consequence of the complete
fiber divisor and the specified double-cover model; it does not identify
an arbitrary double cover with this pullback.

## What remains before importing the transvection predicate

Location completeness is now reduced to the existing common-cover
identification and complete cusp-fiber source, not a new requirement
to construct an actual member.

Still check the exact node-to-ordered-Weierstrass-pair map and the grouped
mass table used by post1505 across the h=4 family. In particular verify
that individual node classes are grouped with the same ordered marking,
and that the retained Jacobian coordinate/plane adapter is available.
Then replay the transvection predicate against EX1's 28 residues rather
than silently importing the O210 intermediate 16-residue filter.

No claim here establishes all those adapters, eliminates an O state,
changes MAIN routing, or grants audit/receiver/theorem credit.
