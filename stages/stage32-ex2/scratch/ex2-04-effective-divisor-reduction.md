# EX2-04 scratch: global nefness and reduction to the known effective divisor

Status: SCRATCH / PROVISIONAL / UNAUDITED. Base retained PR #1709 head is `2f0bfe9e4c815dd20a1d95c386221d6a8926ecf8`. This note does not modify that PR and grants no fixedness, member, Stage32 MAIN, theorem, endpoint, or Perfect Cuboid credit.

Let `S` be the smooth minimal desingularization over `Qbar`, `D=V6`, `L=O_S(D)`, and let

`E = sum_j m_j C_j`

be the exact retained effective known-140 divisor with `[E]=D` in `Pic(S)`, with all `m_j >= 0` and 61 nonzero terms.

## 1. Global nefness of V6

The retained all-140 scan gives `D.C_j >= 0` for every known curve `C_j`.

Take any irreducible curve `Gamma` on `S`.

- If `Gamma` is a component of `E`, then it is one of the retained known-140 curves, hence `D.Gamma >= 0` by the exact scan.
- If `Gamma` is not a component of `E`, then `E` and `Gamma` have no common irreducible component. On the smooth surface, intersection multiplicities of distinct effective irreducible curves are nonnegative, so

  `E.Gamma = sum_j m_j (C_j.Gamma) >= 0`.

Since `E` and `D` are linearly equivalent, `D.Gamma=E.Gamma>=0`. Hence `V6` is globally nef over `Qbar`, not merely nonnegative on the retained known-140 population.

Because `D^2=758>0`, `D` is also big. This does not classify the null locus: an unknown curve disjoint from the support of `E` could still have `D.Gamma=0`.

## 2. Complete H0 reduction to the one-dimensional divisor E

The surface source lock gives `q(S)=h^1(O_S)=0`, and `S` is connected projective integral, so `H^0(O_S)=Qbar`.

The canonical section `s_E` of `O_S(E)=L` gives

`0 -> O_S -> L -> L|E -> 0`.

Taking cohomology and using `H^1(O_S)=0` gives the exact isomorphism

`H^0(S,L) / <s_E>  ~=  H^0(E,L|E)`.

Thus reconstructing the full section space is equivalent to reconstructing sections on the explicit nonreduced known-curve divisor `E`, plus the one canonical line `<s_E>`.

For each unresolved conic `C_i` with label in `[21,24,25,30,31]`, the retained divisor `E` contains `C_i` with positive multiplicity. Therefore `s_E|C_i=0`. It follows that the image of

`H^0(S,L) -> H^0(C_i,L|C_i)`

is exactly the image of

`H^0(E,L|E) -> H^0(C_i,L|C_i)`.

Since `L|C_i ~= O_P1`, the divisorial fixedness of `C_i` can therefore be decided entirely on `E`: `C_i` is nonfixed iff some section of `L|E` restricts to a nonzero constant on `C_i`.

## 3. Relation to the formal-conic scratch lemma

The independent formal-neighbourhood lemma already proves that `L` is trivial on every finite thickening of each target conic. Therefore the unresolved obstruction is not local transverse jet lifting. After the reduction above, the missing object is the scheme-theoretic gluing/restriction map on the finite one-dimensional divisor `E`.

A useful EX2-04 implementation target is now:

1. construct a source-bound scheme/gluing model of the 61-component nonreduced divisor `E` (including exceptional components and multiplicities), or an equivalent exact complex;
2. compute only the five restriction coordinates to labels `[21,24,25,30,31]`;
3. classify each conic by the resulting rank/evaluation test.

An ambient presentation of the entire `H^0(S,L)` is no longer logically required for these five fixedness questions.

## Firewalls

Global nefness of `V6` does not imply `H^1(L-C_i)=0`, because the previously tested adjoint divisors remain a separate condition. It also does not prove semiampleness of `L`, classify the full null locus, classify the fixed part, or produce an integral irreducible genus-one member.
