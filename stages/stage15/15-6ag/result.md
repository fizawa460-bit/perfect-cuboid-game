# Stage15-6ag — pair-energy boundary after the genuine cross-resultant

Base: merged Stage15-6af (`PR #838`, merge commit `3a63d6c`). Stage15-6af proved, in one fixed low-core physical outer/core/gcd/orientation fiber, the exact two-point factorization

\[
\Delta_T(z_1,z_2)=-2m^2n^2k\,L_+(z_1,z_2)L_-(z_1,z_2),
\]
with
\[
L_+=a_1a_2+b_1b_2,\qquad L_-=a_1b_2-b_1a_2.
\]

Stage15-6ag counts what this receiver actually controls. It separates the exact degenerate branches, proves a useful large-shared-prime pair-energy bound, and isolates the remaining small-or-zero-overlap obstruction. It does not manufacture a shared prime when none is forced.

## 1. Frozen verdict

Let `Z` be the retained primitive `z=a+ib` points in one fixed charged physical fiber and one dyadic box

```text
A0 <= |a| < 2A0,
B0 <= |b| < 2B0,
W=A0*B0.
```

The exact conclusions are:

1. `L_-=0` and `L_+=0` contribute only `O(#Z)` ordered pairs;
2. for a fixed first point `z_1` and a good rational prime `p` shared by the two transfer values, `z_2` lies on one of two primitive linear root lines modulo `p`;
3. the number of possible good shared primes for fixed `z_1` is `B^o(1)`, because each must divide the fixed polynomially bounded integer `N(T(z_1))`;
4. consequently, for every threshold `P>=2`, pairs sharing at least one good prime `p>=P` satisfy
   \[
   \boxed{
   E_{\ge P}(Z)\ll \#Z\,B^{o(1)}\left(1+\frac{W}{P}\right).
   }
   \]
5. no current identity forces two generic survivors to share any good prime outside the already-charged fixed core. Therefore pairs with only small extra overlap, or with no extra overlap at all, are not bounded by the large-prime energy estimate.

```text
STAGE15_6_SUBSTAGE=6ag
STAGE15_6AG_DEGENERATE_PAIR_COUNT=O(N)
STAGE15_6AG_LARGE_SHARED_PRIME_ENERGY_BOUND=true
STAGE15_6AG_LARGE_SHARED_PRIME_BOUND=N*B^o(1)*(1+W/P)
STAGE15_6AG_EXTRA_GOOD_OVERLAP_FORCED=false
STAGE15_6AG_SMALL_OR_ZERO_OVERLAP_OPEN=true
STAGE15_6AG_GLOBAL_PAIR_ENERGY_SAVING_PROVED=false
STAGE15_6AG_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AG_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AG_EXIT=LARGE_OVERLAP_ENERGY_CONTROLLED_SMALL_OR_ZERO_OVERLAP_OPEN
```

## 2. Degenerate branches are finite-orbit pairs

For primitive integer pairs `z_j=(a_j,b_j)`:

- `L_-=0` means `z_1,z_2` are rationally proportional. Primitivity forces `z_2` to be one of the finite sign copies of `z_1` permitted by the chamber convention.
- `L_+=0` means `z_1,z_2` are orthogonal. Primitivity forces `z_2` to be one of the finite sign copies of `i z_1` permitted by the chamber convention.

Hence each fixed point has `O(1)` degenerate partners, and

\[
\boxed{E_{\rm deg}(Z)\ll \#Z.}
\]

These pairs can be removed before any generic energy argument.

## 3. A shared good prime gives two linear lines modulo p

Fix a nondegenerate first point `z_1=(a_1,b_1)` and a good prime

\[
p\nmid 2mnkh_\alpha(a_1^2+b_1^2).
\]

If a Gaussian prime of rational norm `p` is shared by the two transfer values, Stage15-6af gives

\[
p\mid L_+L_-.
\]

Thus `z_2=(a_2,b_2)` satisfies one of

\[
a_1a_2+b_1b_2\equiv0\pmod p,
\]
\[
a_1b_2-b_1a_2\equiv0\pmod p.
\]

Because `z_1` is a unit vector modulo `p`, each is one nonzero linear residue line. In a dyadic rectangle of area scale `W=A_0B_0`, each line contains

\[
\ll 1+\frac{W}{p}
\]

integer points, and the primitive/physical filters only delete points. Therefore a fixed good shared prime costs

\[
\boxed{\ll1+W/p}
\]

possible second points.

This is an elementary linear-lattice use of the same spacing principle underlying AR-009; it does not reactivate the low-core one-point modulus.

## 4. Fixed z1 has only B^o(1) possible shared good primes

For fixed charged outer data and fixed `z_1`, the transfer value `T(z_1)` is a nonzero Gaussian integer with norm polynomially bounded in the physical height. Every good rational prime shared with another transfer value must divide `N(T(z_1))`.

Hence

\[
\#\{p:\ p\text{ can be a good shared norm prime for fixed }z_1\}
\le \omega(N(T(z_1)))=B^{o(1)}.
\]

This is AR-016 finite/divisor accounting. It is not a saving by itself.

## 5. Large-shared-prime energy bound

Let `E_{>=P}(Z)` count ordered nondegenerate pairs `(z_1,z_2)` for which the transfer values share at least one good rational norm prime `p>=P`.

For fixed `z_1`, union over its `B^o(1)` eligible primes and the two resultant lines gives

\[
\#\{z_2:(z_1,z_2)\in E_{\ge P}\}
\ll B^{o(1)}\left(1+\frac{W}{P}\right).
\]

Summing `z_1` gives

\[
\boxed{
E_{\ge P}(Z)
\ll \#Z\,B^{o(1)}\left(1+\frac{W}{P}\right).
}
\]

Thus whenever `P` is a fixed-power fraction of the box area scale, genuine shared large-prime mass has a real pair-energy saving.

## 6. Why this does not bound all generic pairs

The transfer target has the fixed form

\[
T(z)=mn h_\beta K_\beta w^2.
\]

The primes of the fixed core `K_beta` are shared by construction, but they are exactly the already-charged squareclass/orientation data from Stage15-6aa--6ac. AR-028 forbids charging them again as new pair energy.

Outside that fixed core, the square factor `w^2` may have private prime support. The exact receiver currently gives no theorem that two distinct retained points must share an additional good prime.

Therefore the pair population splits into

```text
degenerate orbit pairs
  -> O(N)

generic pairs with a shared good p >= P
  -> N*B^o(1)*(1+W/P)

generic pairs whose extra common good support is < P
  -> open

generic pairs with no extra common good support
  -> open
```

The last two classes cannot be deleted merely because a cross-resultant exists.

## 7. Arsenal comparison

The relevant Arsenal lesson is exactly the distinction encoded by AR-017 and AR-028:

```text
AR-017=Genuine shared primes transfer to cross-resultants.
AR-028=The same fixed core/private root data cannot be charged twice.
```

Targeted comparison with the Stage14 t68/t69 buried-gold sequence gives the same boundary: private canonical primes did not transfer, genuine noncanonical common support did transfer, but same squareclass did not force nontrivial additional overlap. This is negative guidance only; no Stage14 exponent is imported into the Stage15 physical measure.

```text
STAGE14_T68_T69_DIRECT_REUSE=false
STAGE14_T68_T69_BOUNDARY_ANALOGY=SHARED_SUPPORT_TRANSFERS_BUT_EXTRA_OVERLAP_NOT_FORCED
```

AR-009 is used only as an abstract linear-spacing lemma after a genuinely shared `p` is fixed. It is not a second one-point low-core modulus. AR-010 remains consumed; AR-012/013 remain untriggered; AR-014 remains unnecessary.

## 8. Counting boundary

Stage15-6ag proves a quantitative energy theorem for the portion of the pair set carrying a large shared good prime. It does not prove an unweighted energy saving for every pair because no positive extra overlap is presently forced.

Hence the next stage must address exactly one question:

> in the original physical low-core fiber, can the `small-or-zero extra overlap` population be reconstructed/count-controlled directly, or can one prove that a sufficiently large extra shared prime occurs on the part that matters?

No generic large-sieve, genus-one, or character theorem should be opened before that support question is normalized.

## 9. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ag
STAGE15_6AG_STARTING_GATE=COUNT_GENUINE_TWO_POINT_CROSS_RESULTANT
STAGE15_6AG_PARALLEL_BRANCH=O(N)
STAGE15_6AG_ORTHOGONAL_BRANCH=O(N)
STAGE15_6AG_GENERIC_SHARED_PRIME_TWO_LINES=true
STAGE15_6AG_FIXED_FIRST_POINT_SHARED_PRIME_CHOICES=B^o(1)
STAGE15_6AG_LARGE_SHARED_PRIME_ENERGY_BOUND=true
STAGE15_6AG_LARGE_SHARED_PRIME_BOUND=N*B^o(1)*(1+W/P)
STAGE15_6AG_AR017_ENERGY_ADAPTER=PARTIAL_QUANTITATIVE_LARGE_OVERLAP
STAGE15_6AG_AR028_NO_DOUBLE_CHARGE_PASS=true
STAGE15_6AG_EXTRA_GOOD_OVERLAP_FORCED=false
STAGE15_6AG_SMALL_OR_ZERO_OVERLAP_OPEN=true
STAGE15_6AG_GLOBAL_PAIR_ENERGY_SAVING_PROVED=false
STAGE15_6AG_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AG_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AG_EXIT=LARGE_OVERLAP_ENERGY_CONTROLLED_SMALL_OR_ZERO_OVERLAP_OPEN
```

Stage15-6ag stops here.