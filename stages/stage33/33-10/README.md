# Stage33-10 — ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER

Authoritative scope: `ROADMAP-33-07-REPAIR-BAND.md`. The pre-amendment Stage33-10 local-evaluation objective is now Stage33-41.

This repair child identifies the exact absolute receiver needed by Stage33-11. It does **not** compute any of the 26 arithmetic-localization columns.

## Exact module structure

The retained proper geometric two-torsion module is `K=Br(Sbar)[2]`, `dim_F2 K=14`, with `G_Q` action factoring through `L=Q(i,sqrt(2))`, `Gal(L/Q)=V4=<cc,ct>`.

The exact source-locked matrices have

```text
dim K^cc = 10
dim K^ct = 13
dim K^V4 = 10
rank(cc-1) = 4
rank(ct-1) = 1
rank(Im(cc-1)+Im(ct-1)) = 5
(cc-1)(ct-1) = (ct-1)(cc-1) = 0.
```

In particular `Im(ct-1)` is not contained in `Im(cc-1)`. Therefore the earlier tempting decomposition into four index-two permutation blocks is false. The certifier instead constructs an explicit invertible equivariant basis proving

```text
K ~= F2^5
     direct_sum Ind_{G_Q(i)}^{G_Q}(F2)^3
     direct_sum Q_L,

Q_L = Ind_{G_L}^{G_Q}(F2) / F2_diag,
dim_F2 Q_L = 3.
```

On the last block one may choose `top,u,v` with `u,v` jointly fixed and independent such that

```text
cc(top)=top+u,
ct(top)=top+v.
```

This decomposition independently recovers `dim_F2 H^1(V4,K)=5*2+3+3=16`, agreeing with the retained finite calculation while preserving the firewall that finite `V4` H1 is not automatically absolute H1.

## Absolute receiver

Continuous Shapiro (Neukirch--Schmidt--Wingberg, *Cohomology of Number Fields*, Proposition 1.6.3) and the long exact sequence of

```text
0 -> F2_diag -> Ind_{G_L}^{G_Q}(F2) -> Q_L -> 0
```

give

```text
H^1(G_Q,K)
 ~= X_Q^5 direct_sum X_Q(i)^3 direct_sum E_L,

X_F = Hom_cont(G_F,F2),
E_L = H^1(G_Q,Q_L),
```

with the exact, not-assumed-split filtration

```text
0 -> coker(res^1: X_Q -> X_L)
  -> E_L
  -> ker(res^2: H^2(G_Q,F2) -> H^2(G_L,F2))
  -> 0.
```

Thus the finite-V4 shortcut is explicitly replaced and the kernel-Galois contribution is retained rather than set to zero.

## Exit and firewalls

```text
ABSOLUTE_H1_RECEIVER_EXACT=true
FINITE_V4_SHORTCUT_STATUS=EXPLICITLY_REPLACED
KERNEL_GALOIS_RELEVANT_CONTRIBUTION_ACCOUNTED=true
STAGE33_11_DOMAIN_AND_CODOMAIN_WELL_DEFINED=true
```

Stage33-11 inherits 26 invariant-factor source directions from `(Z/2)^23 direct_sum (Z/4)^3`; actual connecting columns remain `0/26`. Arithmetic localization, arithmetic HS, parent Stage33-07 closure, Stage33-08 release, theorem credit and endpoint credit remain false. Stage33 progress remains `6/11`.
