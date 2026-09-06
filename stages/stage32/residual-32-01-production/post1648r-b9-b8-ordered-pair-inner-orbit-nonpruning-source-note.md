# Stage32 post1648R scratch source note — named B9/B8 ordered pair still nonpruning

This leaf is scratch-only and grants no MAIN or arithmetic credit.

A stronger named pair is available in the retained/external source chain. Koziarz–Rito–Roulleau, Section 4 Proposition 7(b), write an order-3 Bolza automorphism

`x -> ((1+i)x-(1+i))/((1-i)x+(1-i)) = i*(x-1)/(x+1)`,

which is the same x-map as Cecotti Appendix B.8. Together with Cecotti B.9

`(x,y) -> (i*x, exp(i*pi/4)*y)`

this gives a named order-8/order-6 pair on the Bolza Jacobian.

Using the exact B.8 differential matrix already locked in post1648J and the direct B.9 differential action in the basis `(dx/y, x dx/y)`, the source pair `(A,B)` satisfies

- `A^4=-I`, `tr(A)=r`, `det(A)=-1`;
- `B^3=-I`, `tr(B)=1`, `det(B)=1`;
- `(AB)^2=I`, `tr(AB)=0`, `det(AB)=-1`.

Modulo the hyperelliptic center this is the `(4,3,2)` generating signature.

The verifier enumerates the retained `G12=<S=b4,T=-b3>` exactly. There are six possible B9 images with the full A-invariants and eight possible B8 images with the full B-invariants. Exactly 24 ordered pairs satisfy all source pair invariants, every one generates the full order-48 group, and they form the expected inner-conjugacy orbit. Their B9 fixed Richelot lines occur

`L1:8, L2:8, L3:8`.

Thus even the named B9+B8 generating pair selects only an inner-conjugacy orbit, not an absolute retained marking. A distinguished inner conjugating element, marked theta divisor/half-period, or equivalent source datum is still required.
