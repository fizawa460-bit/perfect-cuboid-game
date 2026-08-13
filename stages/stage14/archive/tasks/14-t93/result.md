# Stage14-t93 — conjugation antipodal pairing on the generic orientation cube

## Status

`COMPLETE_ORIENTATION_CUBE_CONJUGATION_EVEN_ODD_SPLIT`

Consumes merged t92 and merged frozen tH26. No H target is reopened.

Let the generic split-prime orientation cube be `epsilon in {+1,-1}^r`. Simultaneous reversal `epsilon -> -epsilon` is Gaussian conjugation of every generic split-prime factor, up to the already-fixed exceptional/unit conventions.

For the physical Boolean coefficient `C_U(epsilon)` define

```text
C_even(epsilon)=(C_U(epsilon)+C_U(-epsilon))/2,
C_odd(epsilon) =(C_U(epsilon)-C_U(-epsilon))/2.
```

Then exactly

```text
C_U=C_even+C_odd,
C_even(-epsilon)=C_even(epsilon),
C_odd(-epsilon)=-C_odd(epsilon).
```

In the Walsh basis `chi_S(epsilon)=prod_{p in S} epsilon_p`, antipodal reversal acts by `(-1)^|S|`. Hence the spectrum separates exactly:

```text
C_even : |S| even only,
C_odd  : |S| odd only.
```

The t92 cube mean

```text
mu_U=2^(-r) sum_epsilon C_U(epsilon)
```

is the empty-set Walsh coefficient and therefore belongs to the even sector. Conjugation alone does **not** force `mu_U=0`. This is essential because the physical principal occupancy is nonnegative and may be conjugation invariant.

The odd sector has exact antipodal cancellation:

```text
sum_epsilon C_odd(epsilon)=0.
```

Thus only the centered odd spectrum is automatically removed by conjugation pairing. The centered even nonconstant spectrum and the principal mean survive.

The merged 4dj principal-density localization is compatible with this conclusion: any fixed-power deficit in principal occupancy is already strict sub-square-root, but no legal t-route cross-promotion is claimed here. Square-root saturation can still only occur in near-maximal principal occupancy cells.

Frozen boundary:

```text
STAGE14_T93=COMPLETE_ORIENTATION_CUBE_CONJUGATION_EVEN_ODD_SPLIT
CONJUGATION_IS_GLOBAL_ORIENTATION_ANTIPODE=true
WALSH_PARITY_SPLIT_EXACT=true
ODD_WALSH_SECTOR_ANTIPODALLY_CENTERED=true
PRINCIPAL_CUBE_MEAN_KILLED_BY_CONJUGATION=false
CENTERED_EVEN_SPECTRUM_ELIMINATED=false
TH26_COMPLETE_CONSUMED=true
TH27_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-t94
```

Current receiver:

`SharedUCanonicalLPFPrincipalEvenOccupancyPlusCenteredEvenOrientationCorrelation`.
