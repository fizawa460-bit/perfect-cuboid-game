# 36-09CI source lock — Hasse bound for elliptic curves over finite fields

External source used only for the finite-field existence step in 36-09CI:

- MIT 18.783 Elliptic Curves, Lecture Notes 7, Hasse's theorem.
- Source URL: https://math.mit.edu/classes/18.783/2013/LectureNotes7.pdf
- Locked statement: for an elliptic curve E over F_q,
  |#E(F_q) - (q+1)| <= 2*sqrt(q).

Stage36 application:

For every odd prime q dividing Q=a^2+b^2, consider

    E_q: z^2 = y(1-y^2).

The cubic y(1-y^2)=y(1-y)(1+y) has the three distinct roots 0,+1,-1 in odd characteristic, so this is a nonsingular elliptic curve. If chi is the quadratic character of F_q and

    C_q = sum_{y in F_q} chi(y(1-y^2)),

then the standard point-count identity gives

    #E_q(F_q) = q + 1 + C_q.

Therefore Hasse gives

    |C_q| <= 2*sqrt(q).

No stronger elliptic-curve theorem, rank statement, BSD converse, or global arithmetic conclusion is imported from this source. The bound is used only to prove positivity of one finite-field residue-pattern count in 36-09CI.
