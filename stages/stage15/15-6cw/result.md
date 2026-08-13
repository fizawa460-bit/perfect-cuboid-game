# Stage15-6cw — EXHAUSTIVE_VIEW_AUDIT of residual S/O channel arithmetic

Base: merged Stage15-6ct-cv, with fresh audit verdict FIX_REQUIRED because the residual-channel gate was parked before a full route inventory.

Keep the exact cross-gcd-cell normal form
\[
m=abM,\quad n=cdN,\quad r=acU,\quad s=bdV,
\qquad H=abcd,
\]
with pairwise-coprime cells, physical cutoff
\[
HMNUV\le B,
\]
and every switched odd channel modulus `q` satisfying `(q,H)=1`.

The four residual channel forms are
\[
F_S^+=a^2b^2M^2+c^2d^2N^2,
\qquad F_S^-=a^2b^2M^2-c^2d^2N^2,
\]
\[
F_O^-=a^2c^2U^2-b^2d^2V^2,
\qquad F_O^+=a^2c^2U^2+b^2d^2V^2.
\]
Thus
\[
G_S=\gcd(F_S^+,F_O^-),\qquad
G_O=\gcd(F_S^-,F_O^+).
\]
For switched divisors `d_S|G_S`, `e_O|G_O`, put `q=d_Se_O`; then `(q,H)=1`.

## Materially distinct attack inventory

### A. Direct congruence / lattice counting — LIVE
For fixed `(d_S,e_O)` and local root orientations, the two coordinate pairs lie on primitive residue lines. This is the cleanest fixed-modulus local engine and preserves the physical measure. Its known weakness is the one-sided dyadic fringe after summing boxes. It remains LIVE, not sufficient by itself.

### B. Gaussian / norm-form reformulation — LIVE, PARTLY EQUIVALENT
The plus forms are norms after multiplication by unit cell coefficients, while the minus forms are split quadratic forms. Over primes away from `H`, the mixed S/O system can be expressed as one norm-type root condition and one split root condition in each coordinate pair. This overlaps the earlier Gaussian-square receiver, but the exact cell-normalized simultaneous S/O formulation has not been exhausted and remains LIVE as a representation layer.

### C. Divisor switching / complementary cofactors — LIVE REFINEMENT, CORE MECHANISM EQUIVALENT
The exact divisor/cofactor involution from 6cf still applies. Merely switching `d_S,e_O` is EQUIVALENT to the existing large-tail receiver. However, switching only after the cell normalization `(q,H)=1`, and then measuring complementary factors in the residual variables `(M,N,U,V)`, is an UNTESTED refinement and is kept LIVE.

### D. Dispersion / large sieve / energy — LIVE, UNTESTED AT THIS NORMAL FORM
Subtract the fixed-modulus main density and average the residue-line discrepancy over moduli and local orientations before summing the physical dyadic fringes. Previous fixed-packet Type-II / spacing inputs do not automatically apply to this moving product-height family, so there is no cross-promotion. A new explicit adapter would be required. This route is materially distinct and LIVE.

### E. Valuation / local-density structure — LIVE
Because `(q,H)=1`, all cell coefficients are units modulo every odd prime dividing `q`. For a prime `p|d_S`, primitivity prevents `M,N` or `U,V` from vanishing simultaneously modulo `p`, and
\[
(abM)^2\equiv-(cdN)^2\pmod p,
\qquad
(acU)^2\equiv(bdV)^2\pmod p.
\]
Hence any odd prime in the S-channel requires a square root of `-1` for the `(M,N)` ratio, while the `(U,V)` ratio is split. For `p|e_O` the roles reverse:
\[
(abM)^2\equiv(cdN)^2,
\qquad
(acU)^2\equiv-(bdV)^2\pmod p.
\]
Thus every odd channel prime lies in the `p=1 mod 4` local class (apart from already-isolated 2-adic conventions), with finitely many root orientations at each prime power. This does not itself give a fixed power saving, but it gives the exact local state space needed by a dispersion or reconstruction argument.

### F. Exact survivor-condition reconstruction — LIVE
Instead of counting ambient congruence states, use the simultaneous root ratios plus the exact space-diagonal-integral/Gaussian-square survivor condition to reconstruct one residual variable or one orientation from the others. This is potentially stronger than fixed-modulus lattice counting because it can remove ambient fringe states. It is LIVE and must be tested before declaring the residual gate external.

### G. Cross-resultant / pair-energy reuse — DOMINATED FOR THE CURRENT SMALL-SUPPORT OBSTRUCTION
The earlier cross-resultant energy controls large shared support and degeneracies. Re-expressing it in the cell variables is legal, but it returns the same pair-overlap information and does not address the surviving one-point/small-support fringe. Retain as a fallback, classify DOMINATED for the present gate.

### H. Linear-factor switching inside the minus forms — UNTESTED
The split forms factor exactly:
\[
F_S^-=(abM-cdN)(abM+cdN),
\]
\[
F_O^-=(acU-bdV)(acU+bdV).
\]
A divisor switch between the two linear factors, while the plus partner remains a norm form, is not identical to the global `G_S,G_O` cofactor switch. This creates a mixed norm/split-factor incidence problem and is materially distinct. Keep UNTESTED.

## Exhaustive-view conclusion

The residual-channel gate is not a single unnamed obstruction. The materially distinct surviving routes are:
- direct root-line counting;
- cell-normalized Gaussian/norm reformulation;
- residual complementary switching;
- discrepancy dispersion / large sieve;
- valuation/local-density analysis;
- exact survivor reconstruction;
- mixed norm / linear-factor switching.

No candidate is discarded merely because it has not yet produced `delta` or `sigma`.

```text
STAGE15_6_SUBSTAGE=6cw
STAGE15_6CW_EXHAUSTIVE_VIEW_AUDIT=true
STAGE15_6CW_RESIDUAL_FORMS_EXPLICIT=true
STAGE15_6CW_DIRECT_LATTICE=LIVE
STAGE15_6CW_GAUSSIAN_NORM=LIVE
STAGE15_6CW_DIVISOR_SWITCH_REFINEMENT=LIVE
STAGE15_6CW_DISPERSION=LIVE_UNTESTED
STAGE15_6CW_LOCAL_DENSITY=LIVE
STAGE15_6CW_EXACT_RECONSTRUCTION=LIVE
STAGE15_6CW_LINEAR_FACTOR_SWITCH=UNTESTED
STAGE15_6CW_PAIR_ENERGY=DOMINATED_CURRENT_GATE
STAGE15_6CW_EXIT=BLIND_REDISCOVERY_READY
```
