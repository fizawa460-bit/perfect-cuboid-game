# MB104 — auxiliary branch gate from the retained transverse passport

Batch MB104-DRIVE-20261026-SQUARECLASS-02. Route E. PROVISIONAL / CONDITIONAL EXACT REDUCTION / NO GLOBAL CLOSURE.

## Inputs and result

Use the labelled common-H-cover setup and divisors of E-SQUARECLASS-DIVISOR-01, together with the retained ordinary/transverse normalization branches and balanced eight-value passport. Then:

1. The same-character even half-divisors are disjoint: T_1+ intersect T_2+ is empty, and T_1- intersect T_2- is empty.
2. Put c=a/b. The auxiliary quadratic cover W defined by w^2=c is unramified over E exactly when the full fixed ramification-set candidate is a clump. This includes a possibly disconnected unramified cover; being unramified must not be confused with c being a square.
3. With n=56m and K the number of shared critical points of psi_1,psi_2, the auxiliary branch divisor has degree 224m-2K. A surviving coreless/no-clump candidate therefore requires K<112m and a connected auxiliary cover of genus 1+112m-K >=2.

No argument here forces W to be unramified. The parent route remains OPEN. The result identifies an exact adapter target, rather than supplying its missing input.

## Source locks and scope

- Previous Drive note: MB104-CORELESS-SQUARECLASS-DIVISOR-REDUCTION-20261026.md, ID 1FAzH2yNoKn8cJvI3qOiNkTGMdAn0BrXn.
- STATE.retained_frontier.e2_unique_pair_etale_immersion_orbifold_bmy.etale_immersion: f_i etale, normalization map (f_1,f_2) immersive and birational, distinct normalization branches cannot have equal tangent lines. Its hyperbolic first-jet argument is retained as an input, not independently audited here.
- STATE.retained_frontier.e2_unique_factor_pair_singular_passport.retained_inputs: g(E)=1, p is the degree-four H quotient.
- STATE.retained_frontier.e2_unique_pair_balanced_hurwitz_core_split: n=56m and both exact eight-value cycle passports.
- STATE.retained_frontier.absent_eta_character_line: retained nontrivial eta^2=O_E building-data class. No equation identifying this eta with the auxiliary c is recorded in those inputs.

All 27 retained entries remain unchanged. Their canonical SHA256 is b70a41d328b28cce77e1a73df8b3b97cb0e91185c404c069f6774d50b9ceca17. The companion certificate locks the selected input objects. Historical common-H generator marking still has the previously recorded source gap (factor-line blob 1e121116c1591e3b3d9f748f306151ab0e89b580 not recovered in Drive). The present result is conditional on the current note's labelled, H-equivariant setup. No global novelty or exhaustive historical audit is claimed.

## 1. Same-colour critical points cannot coincide

Let h be the inertia involution for one branch colour. Suppose e lies in T_1h and T_2h. The map p is unramified over every T point. For a lift z of e, both f_i(z) are fixed by h. Hence H-equivariance gives nu(hz)=nu(z) for nu=(f_1,f_2).

At a fixed point of a nontrivial involution on a smooth characteristic-zero curve the derivative is -1. Thus h acts on the product tangent space by -Id and leaves the tangent line of the branch nu(z) invariant. If hz were different from z, nu(z) and nu(hz) would be distinct normalization branches over the same product point with the same tangent. This contradicts the retained first-jet/branch transversality result. Consequently hz=z, contradicting unramifiedness of p at z.

This proof uses the birational normalization and the diagonal labelled H action. It does not follow merely from numerical passport counts. Supported product branches are also transverse in the retained singular passport; the underlying first-jet argument applies to any two product graph germs with both projections etale.

Therefore T_1+ and T_2+ have disjoint support; the same holds for minus. Within each i, T_i+ and T_i- were already disjoint because B+ and B- are disjoint.

## 2. The passport fixes the divisor degrees, not their positions

In the current model B-={+a0,-a0,+b0,-b0} with r^4=4 and B+={+u0,-u0,+v0,-v0} with r^4=-4. Subscripts distinguish branch-value names from multipliers a,b.

For psi_1, the transposition counts per +/- pair are: a0:12m each, b0:16m each, u0:0 each, v0:28m each. For psi_2 they are: a0:0 each, b0:28m each, u0:16m each, v0:12m each.

Thus deg(T_i+)=deg(T_i-)=56m; deg(T_i)=112m for T_i=T_i++T_i-. For each colour the common simple part S has degree112m, consistent with deg(D_i colour)=4n=224m. Riemann-Hurwitz for E->P1 gives deg(R_psi_i)=2n=112m, exactly deg(T_i), so these are all its critical points and there are no additional ones away from the eight values.

Equal degrees alone do not identify T_1 and T_2. Same-colour disjointness rules out equality of either individual coloured half-divisor, since their degrees are positive. Full equality T_1=T_2 can occur only by opposite-colour pairing: T_1+=T_2- and T_1-=T_2+.

## 3. The auxiliary quadratic cover measures the remaining mismatch

The previous exact divisor relation gives

div(c)=T_1+ - T_2+ - T_1- + T_2-, c=a/b.

The polar divisors I_i cancel. At a critical point occurring in only one pencil, ord(c) is +1 or -1. At a shared critical point, same-colour pairing is excluded by section 1, so the colours are opposite and ord(c) is +2 or -2. At the common S points and away from these critical divisors, ord(c)=0.

The reduced odd-valuation divisor of c is therefore exactly the symmetric difference of the two critical sets:

Br(W/E)=supp(T_1) symmetric_difference supp(T_2).

Hence W/E is unramified iff T_1=T_2. By the preceding note, this is iff

f_1^{-1}(Ram(pi))=f_2^{-1}(Ram(pi)),

which is a nonempty clump. No other possible clump is classified by this equivalence.

Since deg(T_1)=deg(T_2)=112m and both are reduced, writing K=deg(T_1 intersect T_2) gives deg Br(W/E)=224m-2K. If the no-clump condition holds this degree is positive; W is then connected, and Riemann-Hurwitz over the elliptic E gives g(W)=1+(224m-2K)/2=1+112m-K. This is not a uniform genus bound and does not contradict existence by itself.

## 4. Adapter test against the retained absent eta

The retained eta class is unramified. Identifying W with its quadratic cover would force Br(W/E)=empty and therefore produce the desired clump contradiction. But that identification is not implied by eta^2=O_E, M_1^2=M_2^2, equal degrees, or the fact that div(c) is principal. A principal divisor may have odd coefficients. On an elliptic curve an everywhere-even principal divisor may also represent a nontrivial unramified square class, so evenness and triviality remain distinct.

No retained input inspected here gives an actual marked equation w^2=a/b for the eta cover. Calling c the absent-eta character without such an equation would assume precisely the missing unramifiedness. The class-only-to-eta identification shortcut is therefore unavailable; this is not a NO-GO for the full common-cover route.

## Next task and parking boundary

The concrete next gate is to seek a source-complete marked lift identifying the auxiliary square class [a/b], or otherwise proving every valuation of a/b even, from the actual larger common-cover/support data. A positive result would close the particular no-clump residual by sections 1–3. Recover the historical labelled factor-line/cover source before promoting application to the actual retained surface. Merely constructing some unramified eta or repeating the odd-part/square-class equations does not meet this gate.

Until that adapter exists, this auxiliary-cover subroute is PARKED / MARKED-LIFT ADAPTER MISSING. No further executable proof or computation is identified in the unchanged Drive inputs. A subsequent batch must not simply rerun this parity/passport gate. The broader coreless/no-clump branch and e=2 remain OPEN. No new finite cutoff, actual carrier, global clump, core, receiver/effectivity/theorem/endpoint credit, heavy run, or GitHub action is authorized or claimed.

## Verification boundary

The standard-library verifier locks the 27-entry frontier, checks the retained hypotheses and exact two passports, exhausts the nine admissible local colour patterns, and checks the parity and Riemann-Hurwitz coefficient formulas. It does not discover actual critical points or prove the geometric input hypotheses. The arguments above are conditional proofs; finite enumeration is not a global hostile audit.
