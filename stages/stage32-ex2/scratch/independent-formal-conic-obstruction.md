# Independent EX2: formal conic neighbourhoods and the global obstruction

Status: SCRATCH / UNAUDITED. This is an independent geometric lemma conditional on the retained five-conic geometry, not an EX2 fixedness decision.
Base PR #1709 head: 2f0bfe9e4c815dd20a1d95c386221d6a8926ecf8.
The mainline currently reconstructs finite-dimensional sections in EX2-04; this note studies formal neighbourhoods instead.

## Input and scope

Source: stages/stage32-ex2/EX2-03/remaining-five-conic-restriction-preflight.json
Canonical digest: 3f8ef39f3bd52804394b704fc2d6c2d810843d9f9f94530796c8c12c75d6f120.

Over Qbar let S be the smooth resolved surface, L=O_S(V6), and let
C_i (labels 21,24,25,30,31) be the five pairwise disjoint smooth rational
curves with C_i^2=-4 and L.C_i=0. Hence L|C_i is trivial.
No new verification of the heavy geometry extraction is claimed.

## Lemma: no obstruction on any finite thickening

For any one C, write nC for the subscheme defined by I_C^n, n>=1.
Then L|nC has a nowhere-vanishing section extending any prescribed
nonzero constant section on C. Compatible choices exist for all n;
in particular the restriction of L to the formal completion along C
is trivial.

Proof. C is an effective Cartier divisor. The extension nC to (n+1)C
has the exact sequence

0 -> L|C tensor O_C(-nC) -> L|(n+1)C -> L|nC -> 0.

The left term is O_P1(4n), since L.C=0 and C^2=-4.
Its H1 vanishes, so every section at order n lifts to order n+1.
Start with a nonzero constant at n=1 and lift inductively.
Each lift is a unit in a local trivialization, because its reduction
modulo the nilpotent ideal is a unit. Thus it trivializes L at every
order, compatibly. This proves the claim without invoking a contraction
or an algebraization theorem.

The only external cohomology input is H1(P1,O(d))=0 for d>=-1:
[Stacks Project, Section 30.8, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS).

The same sequence and H1 vanishing give

h0(nC,L|nC)=sum_{j=0}^{n-1}(4j+1)=2n^2-n,
h1(nC,L|nC)=0.

For Z=sum_i C_i, disjointness gives five independent formal components:
h0(nZ,L|nZ)=5(2n^2-n), h1(nZ,L|nZ)=0.
In particular all five constant values can be prescribed formally.

## What still prevents a global section

The actual obstruction is the connecting map

delta_n: H0(nZ,L|nZ) -> H1(S,L(-nZ))

from 0 -> L(-nZ) -> L -> L|nZ -> 0.
Its kernel is precisely the image of GLOBAL sections on nZ.
Formal lifting does not imply that a chosen formal section lies in
this kernel, nor that it extends to all of S.

At n=1 choose any trivializations on the five disjoint curves and let
delta_1:k^5 -> H1(S,L(-Z)).
Then C_i is nonfixed iff some vector v in ker(delta_1) has v_i != 0.
Equivalently, for the standard coordinate vectors e_i,

C_i is nonfixed iff delta_1(e_i) is in the span of
{delta_1(e_j):j != i}.

Proof: normalize v_i to 1 and rearrange delta_1(v)=0; the converse
constructs such a v. This criterion is invariant under rescaling
the five chosen trivializations.

Thus five connecting classes, rather than a complete basis of H0(L),
would suffice to decide these five fixedness questions. Computing them
requires a global cocycle/evaluation model; their ranks are not provided
by the local conic geometry.

## Research consequence and next bounded unit

The formal-neighbourhood route has a definite answer: arbitrary finite
jets alone supply no obstruction to a nonvanishing section on these
conics. No extra obstruction is exposed merely by increasing n.
This does NOT say global restrictions to higher jets carry no information.

A useful independent continuation is to build the five connecting
classes using an explicit global cover/section presentation, or prove
a dependence among them. Coordinate construction can be consumed from
EX2-04 when available. Do not run unbounded local-jet searches expecting
them alone to settle global fixedness.

No conic is classified fixed or nonfixed here. No integral genus-one
member, complete H0, MAIN/EX credit, authority transition, PR modification,
or merge is produced.
