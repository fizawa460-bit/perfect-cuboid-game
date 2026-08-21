# Stage29-02f — source lock

## Testa--Stoll / cuboid surface

Primary source:

- Michael Stoll, Damiano Testa, *The surface parametrizing cuboids*, arXiv:1009.0388v2, revised 24 February 2025; accepted/published successor title *Curves on the surface of cuboids*, Math. Comp., DOI `10.1090/mcom/4238`.

Load-bearing source interfaces used here:

```text
Lemma 3:
Sbar is a (2,2,2,2) complete intersection with 48 isolated A1 nodes;
points with a1*a2*a3 != 0 are smooth.

Definition 6 / Picard ledger:
32 conics in a1=0,a2=0,a3=0,c=0;
24 of these side-hyperplane conics are Q-defined;
48 exceptional curves, 24 over Q and 24 strictly over Q(i).

Theorem 8 / Picard theorem:
Pic(S_Qbar) free rank 64;
discriminant -2^28;
explicit Galois module generated over Q(i,sqrt(2)).

Theorem 10:
Br_1(S)/im Br(Q)=0
for the smooth proper surface S.
```

The source itself explicitly says the transcendental quotient is left to investigate; 29-02f does not attribute any transcendental Brauer computation to Testa--Stoll.

## Horie--Yamauchi / transcendental Frobenius package

Primary source:

- Madoka Horie, Takuya Yamauchi, *The L-function of the surface parametrizing cuboids*, arXiv:2512.22520v3 (2026 revision).

The audited Stage29-02e interface used here is only

```text
T_nonT(S) = 3*h16 + h32 + 3*h8
```

at the semisimple l-adic level, plus the exact Frobenius/newform conventions already source-locked there.

No claim is made that rational semisimplified l-adic data alone computes 2-primary integral Brauer groups or local evaluation maps.

## Stoll verification source

Immutable executable source already locked in 29-02c-LG2:

```text
repo=MichaelStollBayreuth/Verification
commit=51233ed5ef2bf228fac9416c66db9adc0ebcaadd
file=Cuboids/cuboids.magma
blob=0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

Relevant live objects constructed by the script include

```text
Pic, PicL, pmPic,
C1s, pts,
ccPic, ctPic,
permcc, permct.
```

They are sufficient to extract the exact physical-boundary sublattice and its `V4` action without re-enumerating cuboid curves.

## Scope firewall

```text
PROPER_ALGEBRAIC_BRAUER_SOURCE_LOCKED=true
PHYSICAL_OPEN_BRAUER_SOURCE_LOCKED_AS_COMPUTATION=false
ODD_PROPER_TRANSCENDENTAL_CONCLUSION=DERIVED_IN_29_02F_PENDING_AUDIT
TWO_PRIMARY_BRAUER_COMPUTED=false
BRAUER_EVALUATION_MAPS_COMPUTED=false
PERFECT_CUBOID_CONCLUSION=NONE
```
