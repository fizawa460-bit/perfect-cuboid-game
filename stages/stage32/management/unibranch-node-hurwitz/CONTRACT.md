# Stage32 UNIBRANCH-NODE-HURWITZ — unibranch node-count Hurwitz filter

Status: `EXTERNAL_BUNDLE_HOSTILE_AUDIT_PASS__REPO_EXACT_HEAD_AUDIT_PENDING__MAIN_AUTHORITY_UNCHANGED`.
Necessary-condition research result. It does not change MAIN authority (V49) and grants no MAIN / FULL178 / effectivity / receiver / theorem / endpoint / Stage32-closure / Perfect-Cuboid / merge credit.

## Notation

- `S`: minimal resolution of the 48 A1 nodes of the cuboid surface; `K_S^2 = 16`.
- `C`: integral non-exceptional curve on `S`; `d = K_S.C`.
- `E_1..E_48`: exceptional curves; `m_i = C.E_i`, `e = sum m_i` (census exceptional mass), `nu = #{i : m_i > 0}` (census support).
- `g`: genus of the normalization `C~`, `g in {0,1}`.
- Unibranch: `C~ -> Cbar` is bijective, where `Cbar` is the image on the singular surface. This is the Freitag--Salvati Manni Theorem 3.1 hypothesis and the R29-LG2 population (`stages/stage29/29-02c-LG2/finite-search-contract.md`).
- `g_1, g_2 : S -> X(4) ~= P1`: the two factor fibrations (N351; `post1648am`/`post1648ao` source notes).

## Proposition

If `C` is unibranch with `g in {0,1}` and is not a component of a fibre of `g_1` or `g_2`, then

`2*nu >= e + d - 4g + 4`, equivalently `d <= 2*nu - e + 4g - 4`.

Corollary: since `nu <= min(48, e)`, `d <= nu + 4g - 4 <= 44 + 4g`. Unibranch rational curves have `d <= 44` and unibranch genus-one curves have `d <= 48`, compared with `d <= 176 + 16g` from FSM Theorem 3.1.

## Proof

Fix `i`. Let `h_i : C~ -> P1` have degree `n_i >= 1`.

1. Riemann--Hurwitz: `R_i = 2g - 2 + 2 n_i`.
2. Special fibres: each of the six special fibres is `F_E = 2E + sum(8 incident exceptional curves)`, where `E` is a boundary elliptic curve.
   - At a singular cusp, the order-two translation acts by `q -> -q`, so the base parameter is `t = q^2 = z` in node coordinates `x=p^2, y=pq, z=q^2`.
   - In the blow-up chart `y = xu, z = xu^2`, the total transform is `z = x*u^2`: the exceptional curve has multiplicity 1 and the boundary elliptic multiplicity 2 (`post1648am-beauville-fibration-picard-source-note.md`).
   - The six 8-sets partition all 48 exceptional curves (independently recomputed by N352's verifier).
   - There are no other special fibres. `Gamma[4]` is torsion-free and does not contain `-I`, so `X(8) -> X(4)` is unramified away from the six cusps, and non-cusp fibres are smooth copies of `X(8)` (genus 5).
3. Local count: at `P in C~` over a special fibre, let `a` be the local intersection with exceptional components and `b` the local intersection with `E`. The local order of `h_i` is `a + 2b`, contributing `a + 2b - 1` to ramification. The bounds `a+2b-1 >= (a-1)+b` (`a>0`) and `2b-1 >= b` (`a=0<b`) give, summed over the six fibres,
   `R_i >= e - B + q_i`,
   with `B = #{P : a_P > 0}` and `q_i` the total boundary-elliptic intersection.
4. Fibre class: `6 n_i = 2 q_i + e` (N351).
5. Unibranch gives `B = nu`: `C.E_j > 0` iff `Cbar` passes through node `j`, and bijectivity gives exactly one point of `C~` above it. N351/N353 weaken this to `B <= e`, which is multibranch-safe and gives `d <= e + 4g - 4`.
6. From 1, 3, 4, 5: `nu >= e/2 + n_i - 2g + 2`. Adding `i = 1, 2` and using `n_1 + n_2 = d` (N352) gives the claim. QED

The same proof gives the stronger `nu >= e/2 + max(n_1, n_2) - 2g + 2`, which needs the individual `n_i`.

For multibranch curves only `2B >= e + d - 4g + 4` holds. Example: two transverse branches through distinct points of one exceptional curve give locally `e = 2, B = 2, nu = 1`.

## Checks (`verify_unibranch_node_hurwitz.py`)

1. **Known curves.** The all-140 intersection matrix is recovered by `hperp_integral_adapter`; the retained payloads are loaded only through their loaders.
   - The 80 curves covered by the proposition all satisfy it with equality: 32 conics `(d,g,e,nu) = (2,0,6,6)` and 48 genus-one G3 curves `(4,1,4,4)`.
   - The 12 boundary elliptic curves `(4,1,8,8)` are fibre components and are not covered.
2. **Audited N354 replay.** The compressed census replays exactly: `[17128, 38560956534397137634780102]`.
3. **Filter.** The N354 loop is rerun with the support requirement raised from `K = ceil((d-16g+16)/4)` to `max(K, ceil((d+e)/2) - 2g + 2)`.
   - Result: `[530, 511353002049]` in 40 rows (genus 0: `d = 8..44`; genus 1: `d = 8..48`).
   - All per-row data must equal `RESULT.json`.

### Count semantics

The counts are **compressed N220 terminals (prefixes)** surviving necessary conditions. The support upper bound `U = S_10 + min(38, e - M_10)` ignores the other lattice conditions. A surviving prefix need not have an integral completion, and the counts are **not** complete Picard classes or curves.

## Audit and promotion

- External hostile audit **PASS** (2026-10-16) on the self-contained review bundle at main `29e1c10`. See `EXTERNAL-AUDIT-RECEIPT.md`.
- Required before any MAIN use:
  1. a hostile audit of this exact repository head;
  2. a separate MAIN V50 authority sync of `MAIN-STATE.json`, `CURRENT.json`, the claim registry and the startup-authority locks.

## Sources

- Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), arXiv:1303.6495, §2--§3.
- Stoll--Testa, *Curves on the surface of cuboids*, arXiv:1009.0388 v3 (2026-09), §1, §5, §7. The best degree bound recorded there for unibranch rational curves is still 176.
- Repository: `post1648ao-special-fibre-hurwitz-budget-source-note.md` (blob `242088ad`), `post1648am-beauville-fibration-picard-source-note.md`, N351 (`377c2c43`), N352 (`60295a86`), N353 audit (`7f1e2a7d`), N354 verifier (`9e67a101`) and audit (`0394b088`), N220 counters (`5855ae08`, `15105339`), `hperp_integral_adapter.py` (`fb1eb380`).
