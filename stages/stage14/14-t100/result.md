# Stage14-t100 — stabilizer/mover reduction for one elementary influential boundary

## Status

`COMPLETE_SINGLE_BOUNDARY_STABILIZER_MOVER_REDUCTION`

Stage14-t100 consumes merged Stage14-t99 and does not refine the immutable Stage14-tH27 snapshot.

Fix the single generic split prime selected by t99. Write

```text
varpi^e=A+iB,
gamma_0=u+iv,
gamma_+=gamma_0(A+iB),
gamma_-=gamma_0(A-iB).
```

Let `a` be the frozen norm-`k0` Gaussian factor. Multiplication by `A±iB` acts on the coordinate vector `x=(u,v)^T` through

```text
M_+ = [[A,-B],[ B,A]],
M_- = [[A, B],[-B,A]].
```

Hence

```text
M_+ + M_- = 2A I,
M_+ - M_- = 2B J,
J=[[0,-1],[1,0]].
```

After the fixed multiplication by `a` and any fixed linear reconstruction functional `lambda`, every elementary boundary pair is

```text
L_+(x)=lambda C_a M_+ x,
L_-(x)=lambda C_a M_- x,
```

with `C_a` fixed. Therefore

```text
L_+ + L_- = 2A S(x),
L_+ - L_- = 2B D(x)
```

for fixed integral linear forms `S,D` depending only on the frozen packet and the chosen elementary predicate.

## SIGN branch

For a strict sign XOR, away from the zero boundary,

```text
1_{L_+>0} xor 1_{L_->0}=1
```

implies and is implied by opposite signs, equivalently

```text
L_+ L_- < 0.
```

Using the sum/difference representation,

```text
L_+ L_- = A^2 S(x)^2 - B^2 D(x)^2.
```

Thus the SIGN branch is an explicit indefinite quadratic-cone boundary

```text
|A S(x)| < |B D(x)|
```

up to the exact zero/tie convention of the frozen selector. If the two sign forms induce the same half-space on the packet support, the SIGN influence is identically zero; otherwise the prime is a SIGN mover.

## DIV branch

For one fixed divisor modulus `q|A0*B0`, the elementary event is

```text
1_{q|L_+(x)} xor 1_{q|L_-(x)}.
```

If

```text
L_+ == L_- (mod q)
```

as linear forms, then this event is identically zero. Since

```text
L_+ - L_- = 2B D(x),
```

a sufficient and directly checkable stabilizer condition is

```text
2B*D == 0 (mod q)
```

coefficientwise. More generally the exact DIV stabilizer is the subgroup of the finite residue action modulo `q` preserving the chosen divisibility predicate. A t99 DIV survivor must lie on a nontrivial mover residue action; stabilizer primes contribute zero influence exactly.

## PROJ branch

For the endpoint selector modulo `d=B^o(1)`, the two orientations induce two finite projective residue actions. Let `tau_p` denote the orientation-switch action taking the `+` projective label to the `-` label. For the frozen projective acceptance set `C_d`, define

```text
Stab(C_d)={g : g C_d = C_d}.
```

If

```text
tau_p in Stab(C_d),
```

the PROJ XOR is identically zero. Hence any t99 PROJ survivor must satisfy

```text
tau_p notin Stab(C_d).
```

This is an exact finite-group mover condition and introduces no new analytic variable.

## Consequence

Every square-root-saturating fixed packet surviving t99 is now localized to one **mover** boundary:

```text
SIGN_MOVING_QUADRATIC_CONE
or
DIV_NONTRIVIAL_RESIDUE_MOVER
or
PROJ_NONTRIVIAL_PROJECTIVE_MOVER.
```

All selector-stabilizer cases are removed with exactly zero influence before any analytic estimate.

This is a structural reduction only. It does not prove that mover primes are fixed-power sparse, nor that the resulting cone/residue averages admit a fixed-power saving under the full canonical-LPF and physical masks. Stage14-tH27 remains responsible for that immutable theorem audit.

```text
STAGE14_T100=COMPLETE_SINGLE_BOUNDARY_STABILIZER_MOVER_REDUCTION
T99_SINGLE_BOUNDARY_LOCALIZATION_RETAINED=true
ORIENTATION_SWITCH_MATRIX_IDENTITY_PROVED=true
SIGN_BOUNDARY_QUADRATIC_CONE_REDUCTION_PROVED=true
DIV_STABILIZER_GIVES_ZERO_INFLUENCE_PROVED=true
PROJ_STABILIZER_GIVES_ZERO_INFLUENCE_PROVED=true
SATURATION_REQUIRES_BOUNDARY_MOVER=true
MOVER_PRIME_FIXED_POWER_SPARSITY_PROVED=false
FIXED_U_PACKET_POWER_SAVING_PROVED=false
TH27_TARGET_REOPENED=false
TH27_REFINEMENT_REQUESTED=false
TH28_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFSingleGenericPrimeSingleElementaryMoverBoundaryEnergy
NEXT=Stage14-t101
```
