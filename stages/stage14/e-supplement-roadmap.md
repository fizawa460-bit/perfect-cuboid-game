# Stage14-e supplement roadmap — post-control-track refinements

## Purpose

Stage14-e1 through Stage14-e5 form a completed control experiment. They are not reopened here. This supplement track sharpens the solved ambient theory without changing the main Stage14 integer-space-diagonal problem.

The literature-first rule remains mandatory: every supplement must refresh primary literature before promoting a constant, secondary term, effective error, or novelty claim.

## 14-e6 — explicit Peyre/Tamagawa constant

Status: [x] Complete.

Stage14-e6 replaces the e4 placeholder

\[
E_q(B)\sim \Lambda_E M_q B(\log B)^5
\]

by the explicit physical-height arithmetic factor

\[
\boxed{
\Lambda_E
=
\frac1{81920}
\prod_{p\ge3}
\left(1-\frac1p\right)^6
\left(1+\frac6p+\frac1{p^2}\right).
}
\]

Locked components:

```text
alpha(Y)=1/2880
beta(Y)=1
archimedean scale relative to e4 M_q = 1/4
odd-prime factor=(1-1/p)^6*(1+6/p+1/p^2)
physical p=2 factor=9/64
```

A deterministic prime product through `10^6` plus a rigorous tail estimate gives

\[
8.60794782429708\times10^{-7}
<\Lambda_E<
8.60811998497517\times10^{-7},
\]

and therefore

\[
1.47953102009666\times10^{-6}
<C_E<
1.47956061101297\times10^{-6}
\]

for

\[
E_2(B)\sim C_EB(\log B)^5.
\]

The e4 thin-set theorem transfers the same coefficient from raw ambient points to the exactly-two population.

Canonical artifacts:

```text
stages/stage14/14-e6/result.md
stages/stage14/14-e6/literature-constant-audit.md
stages/stage14/scripts/14-e6/explicit_peyre_constant_audit.py
stages/stage14/data/14-e6/explicit_peyre_constant_audit.json
```

No secondary term or effective remainder for the counting function is claimed in e6.

## 14-e7 — secondary asymptotics / crossover

Status: [>] Next.

Target the height-zeta Laurent expansion and lower logarithmic terms explaining why the finite census through `B=10^6` mimics `B(log B)^3` despite the proved `B(log B)^5` main order.

Primary targets:

1. identify the full pole-order-six Laurent expansion at `s=1` for the physical height zeta function;
2. convert Laurent coefficients into the polynomial
   \[
   B(c_5\log^5B+c_4\log^4B+c_3\log^3B+\cdots);
   \]
3. determine which lower logarithmic coefficients dominate on the audited finite range;
4. obtain an effective crossover diagnostic without altering the e6 leading constant.

## 14-e8 — quantitative Euler-brick thin-set count

Status: [ ] Pending.

Seek a quantitative saving for the third-face-square subpopulation beyond the e4 qualitative `o(B(log B)^5)` theorem.

## 14-e9 — gcd/lcm and local-statistics decomposition

Status: [ ] Pending.

Resolve the ambient distribution of the common-edge gcd/lcm strata and finite-local statistics as a control object for the main Stage14 arithmetic.

```text
STAGE14_E_CONTROL_TRACK_E1_TO_E5=COMPLETE
STAGE14_E_SUPPLEMENT_TRACK=DEFINED
STAGE14_E6=COMPLETE_EXPLICIT_PEYRE_TAMAGAWA_CONSTANT
GLOBAL_ARITHMETIC_CONSTANT_LAMBDA_E_EVALUATED=true
SECONDARY_ASYMPTOTIC_PROVED=false
NEXT_E_SUPPLEMENT=Stage14-e7 secondary asymptotics / finite crossover
```
