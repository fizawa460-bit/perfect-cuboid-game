# SR-STR-021 ChatGPT pre-Work external-search follow-up

Date: 2026-08-19  
Baseline: PR #1147 and the SR-STR-222 Work follow-up recorded in PR #1112.

```text
DIRECT_FULL_TARGET_THEOREM_COUNT=0
CHATGPT_SEARCH_VERDICT=ESCALATE_TO_WORK
ARSENAL_PROMOTION=NO
CARD_STATUS_CHANGE=NO
KEY_NEW_LEAD=Merikoski finite Gaussian character x angular Hecke-character machinery
NARROWED_GAP=single-class-scale short-interval PNT for L(s,xi_k chi) at growing individual modulus
```

## Search result

No published theorem was located that directly gives the full SR-STR-021 target: one fixed invertible ordinary Gaussian residue modulo `d`, a fixed positive-width canonical D4 sector, a fixed-power radial interval, individual-modulus uniformity for `N((d))=X^{o(1)}` beyond the Kai/Mitsui pseudopolynomial range, and exceptional-zero handling at single-class relative scale.

The main improvement over PR #1112 is that the algebraic residue/sector adapter is substantially less mysterious. Merikoski, *On Gaussian primes in sparse sets* (Compositio Math. 161 (2025), arXiv:2302.11331), explicitly combines primary generators, finite Gaussian characters `chi`, and angular Hecke characters `xi_k`; Lemmas 2.12–2.14 provide the relevant zero-free/Landau–Page/log-free zero-density framework and Lemma 6.3 handles ordinary residue plus angular Fourier decomposition in the primary-generator normalization.

Thus the remaining issue is not merely `ray class -> sector`. It is the prime-level **individual short-interval, single-class-scale error term**. Thorner–Zaman 2019 gives the individual ray-class/Chebotarev conductor engine globally, while their later rational AP short-interval work gives the right model of a main term normalized by one residue class. Akbary–Wong has ray-class plus short-interval architecture, but the available absolute error is not normalized by the growing ray-class number strongly enough for the SR-STR-021 one-class target.

Naive endpoint differencing of a global Chebotarev theorem is not sufficient for `H=X^{1-theta_0}` because its global error need not be smaller than the short-interval main term.

## Narrowed missing adapter

```text
SuperKaiAngularFiniteCharacterSingleClassShortIntervalPNTAdapter
```

Required: transfer a Thorner–Zaman-style individual short-interval explicit-formula argument to the family `L(s,xi_k chi)` over `Q(i)` while preserving, after finite-character orthogonality and fixed-sector Fourier decomposition,

```text
error = o(H / phi_Z[i](d))
```

for `N((d))=X^{o(1)}`, with the possible exceptional `k=0` real character retained and still leaving a `X^{-o(1)}` relative lower ratio.

## Focused Work handoff

Do not redo Kai/Mitsui, Thorner–Zaman 2019 Theorem 1.4, Coleman, generic BV/BDH, or generic Chebotarev searches. Treat Merikoski arXiv:2302.11331 Lemmas 2.12–2.14 and 6.3 as fixed known input.

Determine whether a published theorem or a direct published-proof transfer yields, for `K=Q(i)`, `N(q)=X^{o(1)}`, every fixed invertible ordinary residue, fixed smooth D4 sector, and `H=X^{1-theta_0}` for an explicit fixed `theta_0>0`, a class-scale asymptotic/lower bound with all errors `o(H/phi_Z[i](q))`.

Audit every zero-free, zero-density, Deuring–Heilbronn, conductor and short-interval explicit-formula input. If a new uniformity lemma is required, stop at the first precise missing estimate.

## Firewall

No direct theorem was found; no arsenal promotion is justified; SR-STR-021 remains an external gate.