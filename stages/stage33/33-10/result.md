# Stage33-10 result

Status: `CLOSED_EXACT` subject to the stage-local exact re-verifier on the PR head.

The actual 14x14 proper `Br(Sbar)[2]` Galois matrices admit an explicitly constructed equivariant basis of type

```text
F2^6 + Ind_{G_Q(i)}^{G_Q}(F2)^3 + Ind_{G_Q(sqrt(-2))}^{G_Q}(F2).
```

Therefore continuous Shapiro identifies

```text
H^1(G_Q,Br(Sbar)[2])
 ~= Hom_cont(G_Q,F2)^6
    + Hom_cont(G_Q(i),F2)^3
    + Hom_cont(G_Q(sqrt(-2)),F2).
```

This closes 33-10a/10b/10c through 10e: the finite `V4` receiver of dimension 16 is **not** promoted to the absolute receiver, and the kernel-Galois contribution is retained exactly in the unrestricted character groups. 33-10d is unnecessary after exact 10e closure.

The Stage33-11 interface is now mathematically defined: 26 inherited invariant-factor directions at the order-two localization layer map to the absolute receiver above. No connecting column is computed in this child (`0/26`), so arithmetic localization, arithmetic HS, parent 33-07 closure, Stage33-08 release, theorem credit and endpoint credit all remain false. Stage33 progress stays `6/11`.
