# Stage33-10 result

Status: `CLOSED_EXACT` subject to the stage-local exact re-verifier on the PR head.

The source-locked proper `K=Br(Sbar)[2]` matrices do **not** split as the earlier provisional `F2^6 + four index-two blocks` model. Exact image/intersection data force one non-semisimple three-dimensional quotient-regular block. The certified decomposition is

```text
K ~= F2^5
     + Ind_{G_Q(i)}^{G_Q}(F2)^3
     + Q_L,

Q_L = Ind_{G_L}^{G_Q}(F2)/F2_diag,
L = Q(i,sqrt(2)).
```

The explicit equivariant basis is constructed in the original 14 coordinates. On `Q_L`, `cc(top)=top+u` and `ct(top)=top+v` with `u,v` independent joint-fixed vectors. The other three nontrivial blocks are exact `Q(i)` permutation modules. This recovers the retained finite result `dim_F2 H^1(V4,K)=16` without identifying it with absolute H1.

Continuous Shapiro plus the long exact sequence of `0 -> F2 -> Ind_{G_L}^{G_Q}(F2) -> Q_L -> 0` gives the absolute receiver

```text
H^1(G_Q,K) ~= X_Q^5 + X_Q(i)^3 + E_L,
X_F = Hom_cont(G_F,F2),
E_L = H^1(G_Q,Q_L),
```

with exact filtration

```text
0 -> coker(res^1: X_Q -> X_L)
  -> E_L
  -> ker(res^2: H^2(G_Q,F2) -> H^2(G_L,F2))
  -> 0.
```

No splitting of `E_L` is claimed. This closes 33-10a/10b/10c through 10e: the finite shortcut is explicitly replaced and the kernel-Galois contribution is accounted for rather than killed. 33-10d is unnecessary after exact 10e closure.

The Stage33-11 interface is therefore well-defined: 26 inherited invariant-factor directions at the order-two localization layer map into this absolute receiver. No connecting column is computed here (`0/26`); arithmetic localization, arithmetic HS, parent 33-07 closure, Stage33-08 release, theorem credit and endpoint credit remain false. Stage33 progress stays `6/11`.
