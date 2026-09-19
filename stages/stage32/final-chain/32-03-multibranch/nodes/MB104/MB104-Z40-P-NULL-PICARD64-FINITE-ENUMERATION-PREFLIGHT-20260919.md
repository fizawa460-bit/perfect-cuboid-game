# MB104 Z40 — P-null Picard64 finite enumeration preflight — 2026-09-19

Status: **PRE-AUDIT EXACT 17-SHELL EXECUTABLE PREFLIGHT / ENUMERATION NOT YET CREDITED**

## Input from Z39

Every nonexceptional integral `P`-null curve has

```text
e=H.R in {4,8,12,16,20}.
```

For fixed degree `e`, adjunction gives

```text
R^2=2p_a(R)-2-e.
```

The Z39 Hodge bound

```text
R^2 <= -3e^2/64
```

leaves exactly 17 degree/genus/self-intersection shells:

```text
e   p_a   R^2    N=16e^2-256R^2
4    0     -6      1792
4    1     -4      1280
4    2     -2       768

8    0    -10      3584
8    1     -8      3072
8    2     -6      2560
8    3     -4      2048

12   0    -14      5888
12   1    -12      5376
12   2    -10      4864
12   3     -8      4352

16   0    -18      8704
16   1    -16      8192
16   2    -14      7680
16   3    -12      7168

20   0    -22     12032
20   1    -20     11520
```

No other arithmetic genus is compatible with the exact Z39 bound.

## Exact H-perp close-vector formulation

The retained Stoll--Testa Picard construction has

```text
Pic(S) rank 64,
H^perp rank 63,
-H^perp pairing positive definite.
```

Choose one retained degree-four genus-one known curve `Q0`. For each allowed degree put

```text
B_e=(e/4)Q0.
```

Then `H.B_e=e`.

For any class `R` of degree e define

```text
v_R=16R-eH in H^perp.
```

Its positive H-perp norm is

```text
N=-v_R^2=16e^2-256R^2.
```

If

```text
b_e=16B_e-eH,
x=16(B_e-R) in 16H^perp,
```

then

```text
x-b_e=eH-16R=-v_R.
```

Thus every candidate in one of the 17 shells is recovered by the same exact Stoll-style
close-vector call

```text
CloseVectors(16*LHp, b_e, N, N)
```

followed by

```text
R=B_e-(x/16).
```

This is the direct degree-e analogue of the pinned Stoll low-degree enumeration; no rational
relaxation is introduced.

## Support-specific P construction

The three remaining balanced canonical supports are

```text
0000770000ff   orbit 48
00007b0000ff   orbit 48
000707000f0f   orbit 768.
```

The compact 48-node generator and Stoll's pinned Magma source both give exact projective points over
`Q(i)`. The correct adapter is therefore:

1. generate the 48 compact node coordinates in their current index order;
2. inside the pinned Magma model, match each coordinate projectively to the actual element of
   `pts=Points(SingularSubscheme(S))`;
3. require a bijection of all 48 points;
4. only then construct
   `P=7H-4 sum E_i`
   for each support mask.

No equality between the two index orderings is assumed.

## Candidate filter

For each reconstructed integral class R:

```text
H.R=e                         exact by shell construction,
P.R=0                         required,
p_a(R)=(R^2+e)/2+1           required,
R^2                           shell-locked.
```

Known classes are retained separately. A class not equal to one of the 140 retained known classes
must have nonnegative intersection with every retained known irreducible curve before it is kept as
a numerical-effectivity candidate.

Survival of that filter is **not** a proof of effectivity.

## Executable source surface

Current main contains the exact nonexpiring Stage33 retained interface:

```text
stages/stage33/33-07/stage32_picard_marking_retained.py
blob 5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7

stages/stage33/33-07/stoll_cuboid_source.py
blob 010db3767b8f932c71ac5722b50ccb64a8c79f9d
```

The helper pins Stoll--Testa

```text
repository MichaelStollBayreuth/Verification
commit     51233ed5ef2bf228fac9416c66db9adc0ebcaadd
blob       0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

and exposes the same Magma `CloseVectors` surface already used in the published verification.

Therefore Z40 is an executable finite computation. The result itself is not asserted by this
preflight.

## Next execution

```text
MB104-Z40-P-NULL-PICARD64-FINITE-ENUMERATION
```

Run the 17 shells for each of the three canonical supports, quotient duplicate classes, and emit the
complete candidate list with degree, arithmetic genus, self-intersection, known/unknown status, and
all P-pairings.

## Firewalls

```text
shell_count=17
enumeration_executed=false
complete_null_locus_classified=false
unknown_candidate_effectivity_proved=false
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
