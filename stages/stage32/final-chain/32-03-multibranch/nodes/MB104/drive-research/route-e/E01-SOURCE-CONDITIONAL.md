# MB104 Route E — six-hyperplane parity adapter and independent-cover base change

**Batch:** MB104-DRIVE-20261027-E-04  
**Classification:** `EXTEND` of retained `E-BOX-ADAPTER-03` and `E-AUXILIARY-BRANCH-02`; exact *conditional* structural consequences only.  
**Status:** PROVISIONAL / NOT INDEPENDENTLY AUDITED / ROUTE E OPEN / NO MATHEMATICAL CLOSURE CREDIT.

## Scope and source locks

Active `e=2`, balanced `000707000f0f` family, `l=2m`, `m>=1`, and **CORELESS + NO NONEMPTY CLUMP**. Keep the retained labelled common `H=(Z/2)^2` cover `p:Z->E`, genus `g(E)=1`, and the two degree `n=56m` rational quotient pencils `psi_1,psi_2:E->P1`. The two H branch colours have sets `S_+` and `S_-` of degree `112m` each. The even-half critical supports `T_i+`, `T_i-` have degree `56m` each, with no same-colour sharing between i=1,2.

Required sources:
- `MB104-CORELESS-SQUARECLASS-DIVISOR-REDUCTION-20261026.md`, Drive ID `1FAzH2yNoKn8cJvI3qOiNkTGMdAn0BrXn`.
- `MB104-CORELESS-AUXILIARY-BRANCH-GATE-20261026.md`, Drive ID `1DDhhkHvtrRns3tAULT-vKe27k2uUkf_P`.
- `MB104-CORELESS-BOX-SQUARECLASS-ADAPTER-20261026.md`, Drive ID `1jM1vuH-VLAP3IsCEE-ldLcMTNQclxPiM`.
- Historical H quotient model Drive ID `1NlaiF4aLowiIyHr_5sF2M7F_BVTKR0ct`, blob `d2e3056137360a9e15ae7c820088d2977a5eb137`.
- Retained research HEAD `68e9ce5dc1453caa7d4802929b573e5fb3fdb1e0` and unchanged 27-key frontier.

This note neither audits those hypotheses nor assumes an actual normalized carrier has been supplied.

## Result 1: globally evaluable six-hyperplane odd-part test

Put `Q=C+W3`, `D=W1+i W2`, and use `Z1,Z2` for **box** coordinates. Existing exact function-field identity:

    c=a/b=(Z2/Z1)*(Q^2-D^2)/(Q^2+D^2).

Over the complex field, factor both quadratics:

    c = [Z2*(Q-D)*(Q+D)] / [Z1*(Q-iD)*(Q+iD)].       (E4.1)

Therefore the odd valuation of `c` at *every* normalization point `x in E` is determined by the six local orders of pulled-back linear sections

    F = (Z2, Q-D, Q+D, Z1, Q-iD, Q+iD).

For an arbitrary local trivialization of the pulled-back hyperplane bundle, write `v_x(F_j)` for their orders. Then

    ord_x(c) = v_x(Z2)+v_x(Q-D)+v_x(Q+D)
             -v_x(Z1)-v_x(Q-iD)-v_x(Q+iD),        (E4.2)
    branch_W(x) = ord_x(c) mod 2.                  (E4.3)

All six factors are linear in the displayed box coordinates; under a change of local trivialization every order changes by the same integer, and 3 positive + 3 negative terms cancel exactly. Consequently (E4.2) is valid as a valuation formula at points **outside the displayed affine chart**, *provided the six pulled-back sections can be evaluated on the actual normalization*. There is no licence to infer such orders from the ambient coordinates alone. At a point where multiple sections vanish, one must sum all six orders before reducing mod 2; counting set-theoretic hyperplane intersections separately is unsafe.

The cover `W/E` is unramified if and only if the valuation sum (E4.2) is even at **every** point of E; in this retained labelled geometry that is equivalent to the specific fixed ramification-set clump. A single certified odd point would disprove unramifiedness, but is already expected in the surviving coreless/no-clump case; to prove **clump** one needs *complete all-point evenness*, not a bounded sample. This converts the previous abstract missing valuation interface into a concrete six-section input schema; it is not the missing input itself.

For a future carrier normalization `gamma:E->B`, supply a full divisor/zero-order list for the six pulled-back sections, including points over singular boxes and chart boundaries. Check degree of each pulled-back section and local trivialization invariance. From these lists compute

    B = sum_x [ord_x(c) odd],
    K = 112m - B/2.                                (E4.4)

Here `K` is the number of shared critical points of `psi_1,psi_2` (necessarily of opposite colour), by the earlier exact branch formula. An incomplete list is **not** a certificate for `B=0`.

## Result 2: W is independent of the entire common-H cover when the residual is non-clump

From the same retained branch passport, `p:Z->E` has geometric branch divisor `S=S_++S_-`, degree `224m`, inertia order 2 and generic degree 4. The auxiliary `W/E` ramifies at the symmetric difference `T_1 triangle T_2`, of degree `B=224m-2K>0` in the surviving case. Every `T_i` lies outside `S` because `p` is unramified at the half-critical supports.

Let `Y` be the normalization of the fibre product `Z x_E W`. The quadratic extension `k(W)/k(E)` **cannot be contained in** `k(Z)/k(E)`: any subextension of a cover unramified away from `S` would likewise be unramified away from `S`, yet W is ramified at some point outside `S`. As W is quadratic, its intersection with k(Z) is k(E), hence the fibre product is generically connected, and

    Gal(k(Y)/k(E)) = H x (Z/2) = (Z/2)^3, deg(Y/E)=8.  (E4.5)

This is a strictly stronger *negative identification* than merely distinguishing W from the residual simultaneous-sign cover: **no** H-character subcover of p can equal W in the surviving case. It does not identify W with an absent-eta cover of any other construction.

The retained `g(Z)=224m+1` follows from the 224m branch points of p, each contributing 2 to RH for its fourfold H cover. Over Z, the pulled-back W-cover is branched above exactly 4B points, because p is unramified over the W branch set. Therefore

    g(Y)=2g(Z)-1+(4B)/2
        =896m+1-4K,                                (E4.6)

and independently for the degree-8 cover Y->E the degree of the ramification divisor is `4*(224m+B)`, again giving (E4.6). With `K<=112m-1`, this yields `g(Y)>=448m+5`. This is a genus formula **not** a contradiction or uniform degree bound.

## Verification and limits

Companion `verify_mb104_route_e_six_hyperplane_basechange.py` checks six-order parity, cancellation under simultaneous local trivialization changes (including overlapping hyperplanes), the two independent RH computations, and parameter samples for `m=1..100`, including the clump/non-clump boundary. The script uses no heavy computation and makes no claim of verifying any actual carrier or geometric prerequisites. If given no complete six-section divisors it must not produce a PASS for global unramifiedness.

**What remains:** materialize one actual normalized carrier with all six pulled-back divisors and conductor preimages, or prove a genuinely global parity condition on them. Neither follows from the box ambient identity, the passports, linear equivalence, or the disconnected residual algebra. The finite candidate cutoff, e=2 closure, low-energy bulk exclusion, m=1 residual exclusion, MB104 and Stage32 completion all remain **OPEN / NOT ESTABLISHED**. No independent hostile audit, promotion, heavy calculation, or GitHub write is claimed.
