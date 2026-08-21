# Stage29-02f — physical-open boundary and Brauer reduction

```text
STAGE=29-02f
ROLE=PHYSICAL_OPEN_BOUNDARY_AND_TRANSCENDENTAL_BRAUER_AUDIT
STATUS=SUBMISSION_PENDING_FRESH_AUDIT
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Physical algebraic open

Write the canonical cuboid surface as

```text
Sbar subset P^6_Q
coordinates=(a1,a2,a3,b1,b2,b3,c)
```

with the four standard cuboid quadrics.  For rational points, the exact nondegeneracy condition is

```text
a1*a2*a3 != 0.
```

Indeed, if all three rational side coordinates are nonzero, then no face diagonal can vanish because a sum of two nonzero rational squares cannot be zero over `Q`; similarly the long diagonal cannot vanish.  Positivity is then a real-chamber condition rather than an additional algebraic deletion.

Define

```text
Ubar = Sbar intersect D_+(a1*a2*a3).
```

Testa--Stoll Lemma 3 shows every point with `a1*a2*a3 != 0` is smooth.  Hence if

```text
b:S -> Sbar
```

is the minimal resolution, then `b` is an isomorphism over `Ubar`.  We identify

```text
U = b^{-1}(Ubar) ~= Ubar.
```

Thus the Brauer object relevant to nondegenerate rational boxes is a concrete smooth quasi-projective surface `U/Q`.

## 2. Exact geometric boundary

Let `D=S\U`.  Over `Qbar`, `D` has exactly the following explicit divisorial components.

### Side hyperplane components

For each `ai=0`, the surface section splits into eight smooth conics.  For example at `a1=0`,

```text
b3 = e3*a2,
b2 = e2*a3,
c  = e1*b1,
a2^2+a3^2=b1^2,
(e1,e2,e3) in {+1,-1}^3.
```

These eight conics are individually defined over `Q`.  The three side hyperplanes therefore contribute

```text
24 Q-defined conics.
```

They are exactly the first 24 conics in the Testa--Stoll / Stoll verification ordering `C1s`.

### Exceptional components

Every singular point of `Sbar` lies outside `Ubar`, because `Ubar` is smooth.  Therefore all 48 exceptional `(-2)`-curves of the minimal resolution are boundary components.  Testa--Stoll's Galois ledger gives

```text
24 exceptional curves defined over Q,
24 exceptional curves strictly over Q(i).
```

Hence

```text
# geometric irreducible boundary components = 24+48 = 72.
```

For `K=Q(i,sqrt(2))` and `G=Gal(K/Q) ~= (Z/2)^2`, the boundary divisor permutation lattice has the explicit form

```text
Div_D(S_Kbar)
  ~= Z^48  + 12 * Z[G/H_i],
```

where `H_i=Gal(K/Q(i))`; the first `Z^48` consists of the 24 rational side conics and 24 rational exceptional curves, while the 12 rank-two permutation summands are the conjugate pairs of non-rational exceptional curves.

This is the exact input missing from the Work-import warning that the proper-surface Brauer theorem does not automatically compute the physical open.

## 3. Proper algebraic Brauer part remains closed

Testa--Stoll Theorem 10 gives

```text
Br_1(S)/im Br(Q) = 0.
```

This statement is retained exactly for the smooth proper surface `S`.  It is not promoted directly to `U`.

## 4. Algebraic Brauer contribution of the open is finite 2-primary data

Over `Qbar`, the standard divisor/unit/Picard exact sequence is

```text
0 -> Qbar^*
  -> O(Ubar)^*
  -> Div_D(Sbar_smooth)
  -> Pic(Sbar_smooth)
  -> Pic(Ubar)
  -> 0,
```

where here `Sbar_smooth` means the smooth compactification `S_Qbar`.

All Galois action on the Picard lattice is already known to factor through

```text
G=Gal(Q(i,sqrt(2))/Q),  |G|=4,
```

and the boundary module above is an explicit permutation `G`-lattice.  Therefore the *new algebraic contribution beyond constants* is controlled by finite cohomology of the explicit two-term boundary/Picard lattice complex

```text
[ Div_D(S_Qbar) -> Pic(S_Qbar) ].
```

Because positive-degree cohomology of a finite group is annihilated by the group order, every class produced by this finite `G`-lattice correction is 2-primary (indeed killed by a power dividing the `|G|=4` cohomological bound at the lattice-complex level).

The exact group is not self-declared here, because the rank, saturation and cohomology map of the 72 boundary classes inside the rank-64 Picard lattice must still be executed/audited.  The original receiver `R29-BR0` is therefore reduced to a finite explicit lattice calculation rather than an open-ended purity question.

```text
R29-BR0A=BoundaryDivisorPicardSublatticeRankSaturationAndUnitKernel
R29-BR0B=BoundaryPicardComplexV4Cohomology
ALGEBRAIC_OPEN_NEW_ODD_PRIMARY=ABSENT_CANDIDATE
ALGEBRAIC_OPEN_2_PRIMARY=FINITE_EXACT_RECEIVER
```

## 5. Proper transcendental odd-primary part is killed by an exact Frobenius witness

The proper surface has

```text
b2=78,
rho=64,
disc Pic(S_Qbar)=-2^28,
```

so at every odd prime `ell` the Neron--Severi lattice is `ell`-saturated and the rank-14 transcendental quotient is integral without an odd discriminant defect.

Horie--Yamauchi, together with the audited Stage29-02e global rematch, gives the semisimple rank-14 non-Tate package

```text
3*h16 + h32 + 3*h8.
```

For a good prime `p != ell`, a weight-3 newform piece has Frobenius polynomial

```text
X^2 - a_p X + p^2
```

on `H^2`.  After Tate twist by `(1)`, a fixed vector modulo `ell` forces

```text
2p-a_p == 0 (mod ell).
```

Using the fourteen exact primes already frozen in Stage29-02e, the determinant witness

```text
D_p=(2p-a_p(h16))^3
    *(2p-a_p(h32))
    *(2p-a_p(h8))^3
```

satisfies

```text
gcd_p D_p = 128 = 2^7.
```

Moreover, for every tested odd prime `ell`, removing the `p=ell` row still leaves a power-of-two gcd.  Hence for every odd `ell` there is a good witness prime `p != ell` for which the full rank-14 twisted transcendental Frobenius has no eigenvalue `1 mod ell`.

Consequently

```text
Br(S_Qbar)[ell]^{G_Q}=0
```

for every odd prime `ell`, and therefore the odd-primary part of

```text
Br(S)/Br_1(S)
```

is zero.

Together with Testa--Stoll Theorem 10, any nonconstant proper-surface Brauer class over `Q` is therefore 2-primary.

This is independently reproducible in

```text
stages/stage29/29-02f/odd_brauer_frobenius_witness.py.
```

Fresh audit must verify the Kummer/saturation adapter and the Frobenius convention before promotion.

```text
R29-BR1-PROPER-ODD=PASS_CANDIDATE
PROPER_NONCONSTANT_BRAUER_ODD_PRIMARY=ABSENT_CANDIDATE
```

## 6. What remains for the physical open

The preceding odd-prime argument applies to classes extending across the boundary to the proper surface.  It does **not** show that `Br(U)` has no odd torsion: a nonextendable open Brauer class may have residues along boundary components.

For the geometric open, purity/Gersten reduces those new classes to the explicit residue complex on the 72 boundary curves and their codimension-two intersections.  Since the components are rational curves but intersect nontrivially, the residue compatibility/dual-incidence calculation must be done rather than assumed zero.

Thus the remaining open-surface receivers are

```text
R29-BR0G=BoundaryGerstenResidueAndIntersectionComplexFor72Components
R29-BR2A=PhysicalOpenTwoPrimaryBrauerIntegralLattice
R29-BR2B=PhysicalOpenTwoPrimaryEvaluationMapsOnQvPoints
```

The important narrowing is:

```text
odd-primary class extending from proper S -> impossible;
new algebraic open class -> 2-primary finite V4-lattice calculation;
any remaining odd-primary open class -> must be genuinely boundary-residue/transcendental.
```

## 7. Routing verdict

29-02f converts the Brauer idea from a vague `transcendental Brauer may remain` statement into three explicit finite/integral receivers.  It does not yield a perfect-cuboid existence or nonexistence theorem and does not reopen Stage16--28.

After fresh audit, the independent suffix queue may advance to

```text
29-02g MODULI_M4_8_Q_DESCENT.
```
