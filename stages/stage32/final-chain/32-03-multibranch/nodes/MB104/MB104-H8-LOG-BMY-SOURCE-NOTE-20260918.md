# Stage32 MB104 — H8 log/orbifold BMY source note — 2026-09-18

Status: **PUBLISHED-SOURCE ADAPTER / NO MB104 CREDIT**

## Imported theorem shape

This note imports only a standard log/orbifold Bogomolov--Miyaoka--Yau inequality for surface pairs.

G. Megyesi, *Generalisation of the Bogomolov--Miyaoka--Yau inequality to singular surfaces*, Proceedings of the London Mathematical Society 78 (1999), 241--282, DOI 10.1112/S0024611599001719, treats normal projective surface pairs `(X,B)` with boundary coefficients `1` or `1-1/m`. For log-canonical pairs with `kappa(X,K_X+B)>=0`, the paper gives the BMY-type consequence

```
(K_X+B)^2 <= 3 e_orb(X,B).
```

The article abstract and bibliographic record are:
https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/abs/generalisation-of-the-bogomolovmiyaokayau-inequality-to-singular-surfaces/5F8649C2AE84F9F0A7B12DFE73921542

Adrian Langer, *Logarithmic orbifold Euler numbers of surfaces with applications*, arXiv:math/0012180, develops orbifold Euler numbers for normal surfaces with Q-divisors and proves a Bogomolov--Miyaoka--Yau type inequality in the log-canonical setting:
https://arxiv.org/abs/math/0012180

No stronger theorem is imported here.

## SNC/orbifold stratification used in H8

For a local normal-crossing pair with boundary coefficient `a` on one smooth branch, the orbifold stratum weight is `1-a`. At a transverse crossing of branches with coefficients `a,b`, the local weight is

```
(1-a)(1-b).
```

Consequently an SNC arrangement may be evaluated by Euler-characteristic stratification with the product of the branch weights on each stratum. H8 uses this only for a formal compatibility witness consisting of ordinary nodes and transverse intersections.

## Scope firewall

- The source theorem is a necessary inequality, not an existence theorem.
- The formal nodal distribution used downstream is not asserted to be realized by an effective MB104 carrier.
- A compatibility witness is used only to show that the retained aggregate packet does not force violation of the log/orbifold BMY inequality.
- No effectivity, irreducibility, finite degree window, receiver, theorem, endpoint, Perfect-Cuboid, or merge credit is imported.
