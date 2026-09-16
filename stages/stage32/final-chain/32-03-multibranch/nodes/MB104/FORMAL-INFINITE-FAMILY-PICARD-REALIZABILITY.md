# Stage32 MB104 — formal infinite families survive integral Picard-class realizability

Status: **RETAINED PICARD-REALIZABILITY DEFORMATION / MB104 INCOMPLETE / NO CREDIT**

## Purpose

The retained `FORMAL-INFINITE-FAMILY-FEASIBILITY` leaf showed that the currently source-locked MB104 packet constraints do not force finiteness in the three hard support sectors. That first packet deliberately tested the numerical/local constraints and used `Delta_total=0`; it did **not** assert a Picard class.

This continuation asks the next prioritized question: can the same unbounded degree/contact/support skeleton be realized by honest **integral divisor classes in `Pic(S)`**?

The answer is **yes on infinite arithmetic subsequences**, after allowing the exact MB102 adjunction identity to determine the required strict-transform genus defect `Delta_total`. Thus the obstruction does not occur at the level of integrality of the Picard class. The unresolved wall moves to effectivity, irreducibility, and existence of an actual curve in the class with normalization genus `0` or `1` and the prescribed node profile.

This is still a formal construction. No effective divisor or actual carrier is produced.

## Source-locked Picard interface

Let `S` be the minimal resolution, `H=K_S` the hyperplane/canonical class, and `E_i` the 48 exceptional curves. The retained MB101/MB102/Hodge interface gives

```text
H^2=16,
H.E_i=0,
E_i.E_j=0  (i!=j),
E_i^2=-2,
d=H.D.
```

`H` and every `E_i` are integral divisor classes. Hence any integer combination

```text
a H - sum_i b_i E_i
```

is an integral Picard class.

For a 14-node support `S14`, put

```text
D(a,k;S14) = a H - k sum_{i in S14} E_i.
```

Then exactly

```text
H.D = 16a,
E_i.D = 2k  for i in S14,
E_i.D = 0   otherwise,
D^2 = 16a^2 - 28k^2.
```

Thus the retained formal skeleton `M_i=2k` on 14 nodes is Picard-realizable whenever the desired degree is divisible by `16`.

## F0-P6 Picard subsequence

Keep the retained full-span 14-node support and the formal degree skeleton

```text
g=0,
d=28k-4,
M_i=2k on the 14 supported nodes.
```

Choose

```text
k=4*l+3,  l>=0.
```

Then

```text
d=112*l+80,
a=d/16=7*l+5=(7k-1)/4,
```

so the integral class

```text
D0_l = (7*l+5) H - (4*l+3) sum_{i in S_P6} E_i
```

has exactly the desired degree and exceptional intersections.

Its square is

```text
D0_l^2 = 21k^2-14k+1
         = 336*l^2+448*l+148.
```

MB102 adjunction for normalization genus zero requires

```text
D^2+d = -2+2*Delta_total,
```

hence

```text
Delta_total = (21k^2+14k-1)/2
            = 168*l^2+280*l+115.
```

This is a nonnegative integer for every `l>=0`. Since the retained branch packet uses distinct exceptional landing keys, this defect need not be placed on the exceptional intersections; MB102 explicitly permits `Delta_off>0`. Therefore the Picard class and genus arithmetic are numerically compatible, but no actual singular curve realizing that defect is asserted.

The six exact rank-3 fiber nef tests also remain nonnegative. For the retained P6 block node counts `[3,3,2,2,2,2]`,

```text
D.F_Q = 11k-2  on a 3-node block,
D.F_Q = 12k-2  on a 2-node block.
```

## F1-P5 Picard subsequence

Keep the retained hyperplane-spanning 14-node support `S_P5` and

```text
g=1,
d=28k,
M_i=2k.
```

Choose

```text
k=4*l,  l>=1.
```

Then

```text
a=d/16=7*l,
D1_P5,l = 7*l H - 4*l sum_{i in S_P5} E_i.
```

This is an integral Picard class with the desired pairings. Its square is

```text
D^2=21k^2=336*l^2,
```

and MB102 adjunction for normalization genus one requires

```text
Delta_total=(D^2+d)/2
           =(21k^2+28k)/2
           =168*l^2+56*l.
```

For the retained rank-3 block counts `[0,0,0,5,5,4]`, the six fiber intersections are respectively

```text
14k,14k,14k,9k,9k,10k,
```

all nonnegative.

## F1-P6 Picard subsequence

Use the same progression `k=4*l`, `l>=1`, but the retained full-span support `S_P6`:

```text
D1_P6,l = 7*l H - 4*l sum_{i in S_P6} E_i.
```

Again

```text
H.D=28k,
E_i.D=2k on S_P6,
D^2=21k^2,
Delta_total=(21k^2+28k)/2.
```

The rank-3 intersections are `11k` on each 3-node block and `12k` on each 2-node block.

## Compatibility with the retained global walls

For all three subsequences the contact skeleton remains

```text
N=14,
R=R8=M=r_odd=28k.
```

Therefore the previously retained non-Picard constraints remain compatible:

- BTVA support/span: by the same fixed supports;
- Beauville: equality, `r_odd=d+4` for `F0-P6` and `r_odd=d` for genus one;
- GFU: `-d+M+4g-4=0` identically;
- rank-3 nef: explicit nonnegative formulas above;
- Hodge: the displayed Picard class makes the intersection calculation exact rather than merely satisfying the earlier upper bound;
- local A1/FSM data: unchanged at the contact skeleton level.

The earlier `Delta_total=0` field was a feature of the first packet-feasibility test and is **not** retained in this Picard deformation. Once the divisor class is fixed, MB102 adjunction determines the positive `Delta_total` written above.

## Consequence for the reprioritized MB104 search

This eliminates one candidate obstruction:

```text
"the degree/ex\-ceptional-contact skeleton cannot even occur in Pic(S)"
```

is false for infinite arithmetic subsequences of all three hard-sector formal families.

The next genuinely load-bearing questions are therefore global:

1. is `D_l` effective for infinitely many `l`?
2. if effective, can an irreducible component have the prescribed full/hyperplane node support and normalization genus `0` or `1`?
3. can the required `Delta_off = Theta(k^2)` coexist with the cuboid equations and low normalization genus?
4. do the remaining Picard cone, nef/effective cone, fibration, or incidence constraints exclude these rays?

These are classification/effectivity questions, not another direct `R8<d/4` calculation.

## Firewalls

- `integral_picard_class_realizability=true` only for the displayed arithmetic subsequences and displayed classes.
- `effectivity_proved=false`.
- `irreducible_curve_proved=false`.
- `normalization_genus_realized=false`.
- no population-wide finite degree window is proved.
- MB104 remains incomplete; MB105 is not released.
- no receiver/effectivity/final-milestone/theorem/endpoint/Perfect-Cuboid credit.
- no merge authorization.
