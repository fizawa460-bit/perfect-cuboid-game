# Stage33-10 — ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER

Authoritative scope: `ROADMAP-33-07-REPAIR-BAND.md`, not the pre-amendment Stage33 numbering. The old Stage33-10 local-evaluation objective is now Stage33-41.

This child identifies the exact absolute receiver needed by Stage33-11. It does **not** compute any of the 26 arithmetic localization columns.

## Exact route

The retained proper geometric two-torsion module is

`K = Br(Sbar)[2]`, `dim_F2 K = 14`, with `G_Q` action factoring through `L=Q(i,sqrt(2))` and `V4=<cc,ct>`.

`certify_stage33_10_absolute_receiver.py` works from the actual source-locked 14x14 `cc`/`ct` matrices. It constructs and verifies an invertible equivariant basis with

```text
K ~= F2^6
     direct_sum Ind_{G_Q(i)}^{G_Q}(F2)^3
     direct_sum Ind_{G_Q(sqrt(-2))}^{G_Q}(F2).
```

The three `Q(i)` blocks have `cc` swapping and `ct` fixed; the `Q(sqrt(-2))` block has both `cc` and `ct` swapping. This also recovers finite `H^1(V4,K)` dimension `6*2+3+1=16`.

Continuous Shapiro (Neukirch--Schmidt--Wingberg, *Cohomology of Number Fields*, Proposition 1.6.3) then gives the exact absolute receiver

```text
H^1(G_Q,K)
 ~= Hom_cont(G_Q,F2)^6
    direct_sum Hom_cont(G_Q(i),F2)^3
    direct_sum Hom_cont(G_Q(sqrt(-2)),F2).
```

Thus the finite-V4 shortcut is explicitly replaced rather than silently promoted. The unrestricted character groups account for the kernel-Galois contribution directly; no assertion that the `G_L` contribution vanishes is made.

## Exit

```text
ABSOLUTE_H1_RECEIVER_EXACT=true
FINITE_V4_SHORTCUT_STATUS=EXPLICITLY_REPLACED
KERNEL_GALOIS_RELEVANT_CONTRIBUTION_ACCOUNTED=true
STAGE33_11_DOMAIN_AND_CODOMAIN_WELL_DEFINED=true
```

Stage33-11 inherits 26 invariant-factor source directions from `(Z/2)^23 direct_sum (Z/4)^3`. Their actual absolute localization cocycles remain `0/26` materialized here. Parent Stage33-07 remains open, Stage33-08 remains blocked, and Stage33 progress remains `6/11`.
