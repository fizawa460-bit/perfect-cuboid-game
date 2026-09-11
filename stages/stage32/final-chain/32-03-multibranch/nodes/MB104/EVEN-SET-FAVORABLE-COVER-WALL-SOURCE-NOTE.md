# Stage32 MB104 — even-set favorable-cover wall

Status: **RETAINED CUBOID-SPECIFIC COVER-AMPLIFICATION NONCLOSURE / NO FINITE DEGREE WINDOW**.

This note tests the remaining idea from `TWO-FACTOR-SAME-BEAUVILLE-COVER-WALL.json`: replace the two projections of the same Beauville cover by a genuinely different double cover of the resolved cuboid surface, branched over another even subset of the 48 exceptional curves.

## 1. Source geometry

Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, Section 4, source-locks the Beauville manifold

`X=(H/Gamma[8] x H/Gamma[8])/Gamma'[4]`

as a smooth two-fold cover of the singular box variety, unramified away from the 48 nodes. After blowing up the 48 inverse images, one obtains `Xtilde -> S` ramified along the full exceptional divisor. Equivalently, the sum of all 48 exceptional curves is divisible by two in `Pic(S)`.

Their modular description also gives quotient genus `2` in each factor. Hence

`q(X)=2+2=4`, so `b1(X)=8`.

For an even full node set, the standard Beauville/code relation for nodal double covers gives

`dim_F2 C_even = b1(X)+1 = 9`.

A convenient published instance of this relation is Catanese--Tonoli, JEMS 9 (2007), Lemma 1.9, which invokes Beauville's Lemma 2 / Jaffe--Ruberman Theorem 4.5 in the form `dim K=b1(cover)+1`.

No claim below reconstructs all 512 words of the actual even-set code. Only its exact dimension, Aut(S)-stability, the known all-48 word, and necessary parity constraints are used.

## 2. Necessary parity supercode from the 92 known nonexceptional curves

Let `E_1,...,E_48` be the exceptional curves and let `J` be an actual even subset:

`sum_{j in J} E_j = 2L` in `Pic(S)`.

For every known nonexceptional curve `C`,

`#(J intersect nodes(C)) = C.sum_{j in J}E_j = 2(C.L)`

is even. Thus the characteristic vector of every actual even subset lies in the binary kernel of the 92x48 node-incidence matrix formed by the 32 conics, 12 boundary elliptics and 48 remaining known elliptics.

The verifier reconstructs the 48 nodes and all 92 incidence rows directly from the exact equations in

`MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd:Cuboids/cuboids.magma`

(blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`). It obtains the expected row weights `6,8,4` and binary incidence rank `25`. Hence the necessary parity supercode has dimension

`48-25=23`.

This 23-dimensional kernel is only a necessary supercode; it is not identified with the 9-dimensional actual even-set code.

## 3. Weight-4 orbit obstruction

Inside the necessary parity supercode there are exactly 12 weight-4 words.

Using the exact nine Aut(S) node permutations retained by MB103, these 12 words form one Aut(S)-orbit. Their F2-linear span has dimension exactly `12`.

The actual even-set code is Aut(S)-stable and has dimension `9`. Therefore it cannot contain a weight-4 word: if it contained one, it would contain the full 12-word orbit and therefore its 12-dimensional span.

The full 48-node set is an actual even set. Consequently a hypothetical weight-44 actual even set would have symmetric difference with the full set equal to a weight-4 actual even set. Hence:

- no actual even set has weight `4`;
- no actual even set has weight `44`.

## 4. Why this kills the distinct favorable-Chern cover route

Let an actual even subset have weight `w`, and let `Ytilde -> S` be the corresponding double cover. Blowing down the `w` ramification `(-1)`-curves gives a smooth surface `Y`.

Because `K_S.E_i=0` and `E_i^2=-2`, the standard double-cover formulas give

`K_Y^2=32`,

`c2(Y)=160-3w`.

Also

`chi(O_Y)=16-w/4`,

so integrality forces `w` to be divisible by `4`.

For the favorable Miyaoka regime one needs

`K_Y^2 > c2(Y)`, i.e.

`32 > 160-3w`, hence `w>128/3`.

With `0<=w<=48` and `4|w`, this leaves only

`w=44` or `w=48`.

Weight `44` is excluded above. Weight `48` is precisely the already retained Beauville cover. Therefore there is **no genuinely distinct even-subset double cover with `K^2>c2`** available for an independent favorable-Chern ramification ledger.

## 5. What is and is not closed

This closes only the specific amplification route

`find another even subset -> build another K^2>c2 cover -> charge ramification independently`.

It does **not** prove that the full even-set code has no other weights, and it does not exclude even subsets of weight at most `40`. Such covers have `K^2<=c2` and therefore do not supply the favorable Miyaoka 2008 mechanism used in `BEAUVILLE-MIYAOKA-COVER-WALL.json`.

No finite degree window follows. The active MB104 problem remains a cuboid-specific bound on ordinary self-singularities / globalization, a global jet-interpolation obstruction, or another member-level theorem.

## Firewalls

- the 23-dimensional incidence kernel is a necessary parity supercode, not the actual even-set code;
- only `dim C_even=9`, Aut(S)-stability and the all-48 word are imported for the actual code;
- no weight-8/12/16/etc. necessary-parity word is promoted to an actual even set;
- no new cover is asserted to exist;
- finite degree window remains open;
- finite Picard enumeration remains unreleased;
- no `R29-LG2-MB`, receiver, theorem, endpoint or Perfect-Cuboid credit;
- merge remains unauthorized.
