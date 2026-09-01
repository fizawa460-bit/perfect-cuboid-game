# Stage34-02 — sequence classification and theorem funnel

Status: `PREAUDIT_PASS_ROUTE_D_DIRECT_RATIONAL_POINT_COVER_SELECTED`.

## Classification result

The audited EXT-C object is **not** a Lucas/Lehmer sequence and is **not** the standard elliptic divisibility denominator sequence. The load-bearing quantity remains

```text
N_{q,T}(n)=Num(F3(nP_q+T))
```

for rank one and the analogous `N_T(a,b)` on the rank-two lattice.

The theorem funnel therefore rejects automatic use of the classical primitive-divisor machinery:

- Bilu--Hanrot--Voutier: no exact Lucas/Lehmer identification;
- Silverman elliptic Zsigmondy: applies to denominators of `x(nP)`, not the Face-3 numerator;
- Verzobio's shifted elliptic primitive-divisor theorem: still concerns `x(nP+Q)` denominators and, in its stated primitive-divisor theorem, prime-order torsion shifts; Stage34 also has order-4 shifts;
- arithmetic-dynamical primitive-divisor theorems for degree `>=2` iteration do not identify the degree-one translation orbit `Q -> Q+P` with the Face-3 numerator sequence.

Thus routes A/B/C are rejected as direct closure routes, not declared mathematically false.

## Exact route-D reduction

On

```text
E_q: y^2=x(x+1)(x+q^2)
```

the Face-3 value factors exactly as

```text
A_q(x)=x^2+q^2
B_q(x)=(1+q^2)x^2+4q^2x+q^2(1+q^2)

F3(Q)=A_q(x) B_q(x)/(q^2-x^2)^2.
```

Therefore, away from the explicit poles `x=+/-q`, the square obstruction is exactly the rational-point problem on

```text
C_q:
  y^2=x(x+1)(x+q^2)
  z^2=A_q(x)B_q(x).
```

For every Stage34 `q`, the two degree-two covers of the `x`-line have disjoint simple branch loci. Riemann--Hurwitz gives

```text
g(C_q)=5.
```

So the same direct curve handles all fixed-torsion rank-one translates **and** the full rank-two lattice at once. The awkward two-variable notion of a primitive divisor disappears completely on this route.

Exact formulas, branch checks, and the finite squareclass descent are locked in `exact-cover-reduction.json`.

## Finite squareclass descent

Write `q=a/b` in lowest positive terms and `x=X/Z`, `gcd(X,Z)=1`. Then

```text
A_h=b^2 X^2+a^2 Z^2
B_h=b^2(a^2+b^2)X^2+4a^2b^2XZ+a^2(a^2+b^2)Z^2
```

and

```text
B_h-(a^2+b^2)A_h=4a^2b^2XZ.
```

Hence every prime dividing `gcd(A_h,B_h)` divides `2ab`. If `A_h B_h` is a square, the common squareclass is represented by a positive squarefree `d` supported only on primes dividing `2ab`:

```text
A_h=d u^2,
B_h=d v^2.
```

This turns the global square problem into a **finite** 2-cover/squareclass collection before any high-genus computation. The raw upper bounds are only 8 or 16 squareclasses per fiber.

## Selected route

```text
D1: finite squareclass descent + local/Mordell--Weil sieve
    -> if complete, close directly;
    -> otherwise retain only locally viable covers.

D2: genus-5 covering collection + elliptic Chabauty / Mordell--Weil sieve
    -> determine all C_q(Q);
    -> project to E_q(Q);
    -> classify torsion/pole/receiver points exactly.
```

This route is preferred before trying to prove a fresh-prime theorem because it attacks the exact required square condition rather than the stronger intermediate assertion “new prime with odd valuation”.

## Literature species

The selected route is supported by existing proof technology, but no theorem is yet promoted as an automatic Stage34 solver:

- E. González-Jiménez, *Covering Techniques and Rational Points on Some Genus 5 Curves*, Contemporary Mathematics 649 (2015), 89--105, DOI `10.1090/conm/649/13021`: covering collections and elliptic Chabauty for suitable genus-5 curves;
- N. Bruin and M. Stoll, *The Mordell-Weil sieve: proving non-existence of rational points on curves*, LMS J. Comput. Math. 13 (2010), 272--306, DOI `10.1112/S1461157009000187`;
- M. Stoll, *Diagonal genus 5 curves, elliptic curves over Q(t), and rational diophantine quintuples*, arXiv `1711.00500`: concrete genus-5 rational-point methodology and elliptic quotient decompositions.

The next unit must materialize the exact Stage34 cover/quotient maps and verify the hypotheses of whichever covering/Chabauty implementation is actually used.

## Arsenal recheck

No direct formal Arsenal weapon solves the full genus-5/MW-sieve problem. Relevant reusable pieces are narrower:

- `S31-W01`: exact quartic-to-elliptic adapter for the genus-one quotient `D_q: z^2=A_qB_q`;
- `S31-W03`: complete auxiliary point-set pullback, only after an auxiliary point set is genuinely complete;
- `S30-WF02`: immutable layered certificates;
- `S30-WF03`: credit firewall.

## 34-02 exit gate

```text
ONE_ROUTE_SELECTED=true
SELECTED_ROUTE=D_REPLACEMENT_DIRECT_RATIONAL_POINT_COVER
THEOREM_SPECIES_MAPPED=true
REMAINING_HYPOTHESES_EXPLICIT=true
PRIMITIVE_DIVISOR_THEOREM_CREDIT=false
ODD_MULTIPLICITY_CREDIT=false
R29_EXT_CHANG_C_closed=false
```

Because this is a major Class-3 route pivot, the next boundary is a hostile audit of the 34-02 algebraic reduction and route applicability before heavy covering/Chabauty work.
