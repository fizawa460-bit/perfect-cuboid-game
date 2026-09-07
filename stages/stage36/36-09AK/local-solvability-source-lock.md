# Stage36 36-09AK source lock: local lifting and everywhere-local genus-one coverings

Accessed: 2026-09-07

This leaf needs only three standard local facts. It does not import any global Mordell-Weil or Tate-Shafarevich computation.

## A. Finite-field point on a smooth genus-one reduction

David Roberts, *Explicit Descent On Elliptic Curves Over Function Fields*, §2.5, Theorem 4:
https://johncremona.github.io/theses/roberts.pdf

For a projective genus-one curve over `F_q`,

```text
|#C(F_q)-(q+1)| <= 2*sqrt(q).
```

Roberts records the corollary that a genus-one curve over a finite field always has a rational point. For the Stage36 two-quadric intersection, when an odd prime `p` does not divide `2*A*B*C*D`, the exact pencil determinant from audited 36-09AH remains squarefree modulo `p`; hence the reduction is smooth genus one and every `F_p` point is nonsingular.

## B. Multivariate Hensel lifting

Joshua A. Grochow, *A note on multivariate Hensel lifting* (2024), Theorem 1:
https://home.cs.colorado.edu/~jgrochow/hensel-notes.pdf

For a system of integer polynomials, lifts of a solution modulo `p^k` are governed by the Jacobian linear system. In particular, if the Jacobian has full row rank modulo `p`, the linear system is surjective and a lift exists; iterating gives a `Z_p` solution. Stage36 uses this only for two equations in an affine chart, with directly certified rank `2` modulo each bad odd prime.

## C. Squares in Q_2

Fernando Q. Gouvea, *p-adic Numbers: An Introduction*, 3rd ed., Springer Universitext (2020), Problem 124 / standard square criterion:
https://link.springer.com/book/10.1007/978-3-030-47295-5

An odd `2`-adic unit is a square in `Q_2` iff it is congruent to `1 mod 8`. Stage36 applies this criterion only to the explicit units `31/7` and `-21/11`.

## D. Descent interpretation firewall

Roberts, Chapter 3 introduction and Chapter 6, distinguishes homogeneous spaces that are everywhere locally solvable from those having a global point; an everywhere-locally-soluble homogeneous space may represent a nontrivial order-2 Tate-Shafarevich class. Thus establishing ELS gives the usual 2-Selmer/local condition for the already-identified full-2 class, but does not place the class in the Mordell-Weil Kummer image.

## Scope firewall

The local arguments below prove one explicit Stage36 full-2 homogeneous space is everywhere locally soluble. They do not prove a rational point on it, do not decide whether its Selmer class is Mordell-Weil or Sha[2], and do not produce a receiver point or receiver emptiness theorem.
