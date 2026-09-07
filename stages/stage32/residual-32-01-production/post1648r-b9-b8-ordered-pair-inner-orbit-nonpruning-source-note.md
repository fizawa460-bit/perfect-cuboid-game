# Stage32 post1648R scratch source note — named B9/B8 ordered pair still nonpruning

This leaf is scratch-only and grants no MAIN or arithmetic credit.

A stronger named pair is available in the retained/external source chain. Koziarz–Rito–Roulleau, Section 4 Proposition 7(b), write an order-3 Bolza automorphism

`x -> ((1+i)x-(1+i))/((1-i)x+(1-i)) = i*(x-1)/(x+1)`,

which is the same x-map as Cecotti Appendix B.8. Together with Cecotti B.9

`(x,y) -> (i*x, exp(i*pi/4)*y)`

this gives a named B9/B8 generating pair on the Bolza Jacobian.

## Representation convention repair

post1648J records matrices on holomorphic differentials, whereas post1648N and the retained `G12` matrices act on the homology/torus lattice. These are contragredient conventions. For a 2x2 pullback matrix with trace `t` and determinant `d`, the inverse has trace `t/d`.

Therefore B9 changes from pullback trace `+r` with determinant `-1` to homology/torus trace `-r`. B8 has determinant `1`, so trace `1` is unchanged. The initial scratch R attempt incorrectly compared B9 pullback trace `+r` directly with N's homology images; its failing run was a convention mismatch, not a mathematical counterexample.

In the corrected homology/torus convention the source pair `(A,B)` satisfies

- `A^4=-I`, `tr(A)=-r`, `det(A)=-1`;
- `B^3=-I`, `tr(B)=1`, `det(B)=1`;
- `(AB)^2=I`, `tr(AB)=0`, `det(AB)=-1`.

Modulo the hyperelliptic center this is the `(4,3,2)` generating signature.

The verifier enumerates the retained `G12=<S=b4,T=-b3>` exactly. There are six possible B9 images with the corrected full A-invariants, and these six are exactly the six images independently materialized in post1648N. There are eight possible B8 images. Exactly 24 ordered pairs satisfy all source pair invariants, every pair generates the full order-48 group, and the pairs form the expected inner-conjugacy orbit. Their B9 fixed Richelot lines occur

`L1:8, L2:8, L3:8`.

Thus even the named B9+B8 generating pair selects only an inner-conjugacy orbit, not an absolute retained marking. A distinguished inner conjugating element, marked theta divisor/half-period, or equivalent source datum is still required.
