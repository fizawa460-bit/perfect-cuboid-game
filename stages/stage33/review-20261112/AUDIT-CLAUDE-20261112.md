# Audit of STRATEGY-REVIEW.md (Claude, 2026-11-12, main 3e210ee7)

Status: reading audit. Proposal only. No STATE, ledger or credit change.

## Verdict

- Lemma 0: **PASS**. The script reruns to PASS. P0 = (3,4,0;4,3,5;5) is a smooth Q-point of the
  four quadrics, and U = Sbar ∩ D+(a1 a2 a3) (29-02f/audit.md) excludes it.
- Theorem 1, for a **finite** subgroup B ⊂ Br(U): **PASS**, with one fix (F1).
- Corollary "EMPTY cannot occur, whatever the class list": **FAIL** as stated for the frozen
  Stage33 scope (F2). The scope is not finite.
- Recommendation D (do not reopen 33-13): **agreed**, for a stronger reason (F2).

## F1 (should-fix): cite the formal lemma in its density form; drop the perturbation step

Harpaz–Wittenberg (arXiv:1409.0993, §3 intro) state it as follows. Let X⁰ be a dense open in a
smooth variety X over a number field, and B ⊂ Br(X⁰) finite. Then X⁰(A_k)^B is dense in
X(A_k)^{B ∩ Br X}. Sources: Harari 1994 Cor. 2.6.1; CT–Skorobogatov 2000 Prop. 1.1; CT 2003 Thm 1.4.

With X = S proper, the constant adele (P0)_v lies in X(A)^{Br X}, by reciprocity. Density then
gives a point of U(A)^B (restricted product, integral at almost all v) arbitrarily close to it.
This argument does not need step 1 (P_v ∈ U(Q_v) near P0 at every v). Step 1 is also not
literally an adele of U, because P0 reduces into the boundary at every p.

For the real chamber, replace P0 by a coordinate permutation so that the nearby box is ordered.
At ∞ take Q_ε, and at finite places take P0. This adele is still orthogonal to B ∩ Br(S),
because evaluation is locally constant.

## F2 (blocking for the corollary): the frozen scope contains infinitely many unit–character classes

33-03/result.md gives U_D ≅ Z^14 (units, trivial Galois action) and retains
H^2(G_Q, UPic)_odd ≅ X_Q,odd^14 parametrically. So the scope contains (χ, u) for every character χ
of G_Q and every unit u. Theorem 1 does not apply to an infinite B.

Worse, for this infinite part the Brauer–Manin condition becomes the rational-point condition
itself:

- Orthogonality of an adele (M_v) to (χ, u) for all χ means that the idele (u(M_v))_v lies in
  the kernel of the global Artin map, which is Q*·R_{>0}. So u(M_p) = q_u ∈ Q* for every p.
- The functions a2/a1, a3/a1, (b1−a2)/a3, (b2−a1)/a3, (b3−a1)/a2 and (c−b3)/a3 are Q-units on U.
  Each has zeros and poles only on {a1 a2 a3 = 0}; for example, b1² − a2² = a3².
  Their values fix all seven coordinates.
- Hence every adele orthogonal to all these classes is the diagonal image of one point of U(Q).

So, with the full scope, "BM set empty" is equivalent to "no physical rational point". The method
is circular: it is exactly the perfect cuboid problem. With any finite truncation, Theorem 1 gives
NONEMPTY.

**Either way, Stage33's local–global computation cannot decide anything new.**

F2 is my own argument, so it needs an independent check. The weakest point is whether these
specific functions are units on the resolved S minus the full 72-component boundary. They are units
on U, which is all the argument needs.

## Net

- Stage33 should be frozen.
- 33-13 (e3 column) should not be reopened. Its 1/10 (V34) stays as retained evidence.
- Suggested freeze note: Theorem 1 (finite B) + F2 (circularity of the infinite unit–character part).
