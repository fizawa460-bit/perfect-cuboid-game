# Stage32EX3 EX3-04g — modular graph quotient and trace-zero contradiction source note

## Scope

Fixed target only: recovered V6 class `g1-d186`, hypothetical integral irreducible carrier with geometric normalization genus 1, `O=210`, `q'=4`, product-cover degrees `(105,81)`, and the retained `Q(T)=602` correspondence shell. This is a scratch/provisional argument. It does not grant Stage32 MAIN credit and it does not assert effectivity or existence of the carrier.

## 1. Product modular model and graph quotients

Primary external source: Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, arXiv:1009.0388. Two distinct locators are load-bearing and are kept separate here:

- Section 4, “The cuboid surface as a modular surface” (author-hosted current revision p. 8): the `X(8)` model, the kernel `G0 ~= (Z/2)^3`, its sign action, the diagonal quotient invariants, and the identification `(X(8) x X(8))/G0 ~= Sbar` over `Q(i)`.
- Section 7, “Curves of low degree on Sbar” (author-hosted current revision p. 17, discussion following Corollary 18 / around Lemma 20): images of graphs of automorphisms centralizing `G0` account for the 32 conics; the same discussion states that each such conic passes through six singularities.

Use the following explicit model from Section 4. The genus-5 modular curve `Z=X(8)` is

`u^2=2xy`, `v^2=x^2-y^2`, `w^2=x^2+y^2`.

The kernel `G0` of `PSL(2,Z/8Z) -> PSL(2,Z/4Z)` is `(Z/2)^3` acting by independent signs of `u,v,w`. On `P=Z x Z`, write the diagonal-`G0` invariants

`U=u1*u2`, `V=v1*v2`, `W=w1*w2`, `X=x1*x2`, `Y=y1*y2`, `T=x1*y2`, `Zc=x2*y1`.

The source identifies the quotient with the cuboid surface over `Q(i)` by

`U=2*b1`, `V=2*b2`, `W=2*b3`,

`X=a1+c`, `Y=-a1+c`, `T=a2+i*a3`, `Zc=a2-i*a3`.

Section 7 separately identifies the 32 conics among the images of graphs of automorphisms of `Z` centralizing `G0` and records that these conics pass through six singularities each. Every `h in H` below lies in the abelian group `G0`, hence centralizes `G0`, so its graph is of this type.

The retained Stage32 relative-H marking is source-locked in

`stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-x-relative-h-marked-node-action.json`:

`H=<u_H,v_H> ~= V4`, with

`u_H=g7*g9`, `v_H=g7*g8`, `u_H*v_H=g8*g9`,

where `g7,g8,g9` are the sign changes of `b1,b2,b3`, respectively. Through `U=2b1,V=2b2,W=2b3`, these are exactly the even sign changes of the modular coordinates `(u,v,w)`:

- `1`: `(eps_u,eps_v,eps_w)=(+,+,+)`;
- `u_H`: `(-,+,-)`;
- `v_H`: `(-,-,+)`;
- `u_H*v_H`: `(+,-,-)`.

For a point `(z,hz)` on `Graph(h)`, `x2=x1`, `y2=y1`, while `(u2,v2,w2)=(eps_u*u1,eps_v*v1,eps_w*w1)`. Substitution into the invariant coordinate map gives

`a3=0`, `b1=eps_u*a2`, `b2=eps_v*a1`, `b3=eps_w*c`.

The exact Testa--Stoll C1 group-3 ordering is independently transcribed in

`stages/stage33/33-12/diagnose_e3_v91c1v_actual_prime_known140_locator.py`:

`a3=0`, `a1+e1*b2=0`, `a2+e2*b1=0`, `b3+e3*c=0`,

with nested sign order `e1,e2,e3 in [+1,-1]`. Hence the graph image has

`(e1,e2,e3)=(-eps_v,-eps_u,-eps_w)`.

For the four `H` elements this gives exact global C1 indices

- `Graph(1)` -> C1 index 24 (`e=(-,-,-)`),
- `Graph(u_H)` -> C1 index 21 (`e=(-,+,+)`),
- `Graph(v_H)` -> C1 index 18 (`e=(+,+,-)`),
- `Graph(u_H*v_H)` -> C1 index 19 (`e=(+,-,+)`).

Thus the true four modular graph quotients are the single physical C1 orbit `{18,19,21,24}`. No c=0 block ambiguity remains.

## 2. Resolved-double-cover and blow-down intersection adapter

Use the retained exact adapter

`stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-beauville-blowup-picard-adapter-delta-lock.json`.

Let `Btilde` be the resolved box surface, `Xtilde` the blow-up of the Beauville surface `X` at the 48 fixed points, `pi:Xtilde->Btilde` the finite double cover branched along the 48 exceptional curves, and `beta:Xtilde->X` the blow-down.

For the hypothetical carrier class `C` on `Btilde`, its strict pullback is

`Dtilde=pi^*C`.

Let `K_h` be one of the four strict-transform C1 conics above and let `Ltilde_h=pi^*K_h`. Each physical C1 conic passes exactly six of the 48 nodes, as both externally source-checked above and retained explicitly in `stages/stage33/33-07/exceptional-p1-tangent-coordinates.json`.

Projection formula gives

`Dtilde.Ltilde_h = 2*(C.K_h)`.

At an incident branch exceptional curve `Etilde_j`, the retained A1 adapter gives

`Dtilde.Etilde_j=m_j=C.E_j`.

Because `K_h` meets the corresponding branch exceptional curve once, `Ltilde_h.Etilde_j=1`. Therefore

`beta^*D = Dtilde + sum_j m_j Etilde_j`,

`beta^*L_h = Ltilde_h + sum_{j incident K_h} Etilde_j`.

Using `Etilde_j^2=-1`, the three blow-up correction terms combine to one copy of the incident mass:

`D.L_h = 2*(C.K_h) + sum_{j incident K_h} m_j`.

This explains why the node-mass term is not a double count: `C.K_h` is the resolved `Btilde` intersection, while the additional term is the exact blow-down correction on `X`.

Now let `q:P=Z x Z -> X=P/H_diag` be the degree-4 etale quotient. `Graph(h)` is invariant under `H_diag`; since `H` acts freely on `Z`, the restriction

`Graph(h) -> L_h`

has degree 4. For the connected pullback correspondence divisor `Gamma_P=q^*D`, projection formula gives

`Gamma_P.Graph(h) = 4*(D.L_h)`.

## 3. Exact V6 graph intersections

The recovered V6 all-140 pairings give

- `C.K_24=0`,
- `C.K_21=0`,
- `C.K_18=14`,
- `C.K_19=9`.

The retained six-node incidence plus the V6 exceptional multiplicities give incident masses

- side 24: `41`,
- side 21: `41`,
- side 18: `24`,
- side 19: `34`.

Therefore in actual group order `[1,u_H,v_H,u_H*v_H]`, i.e. sides `[24,21,18,19]`,

`D.L_h = [41,41,52,52]`,

and

`Gamma_P.Graph(h) = [164,164,208,208]`.

## 4. Linear trace and H-trivial block

For a correspondence of bidegree `(105,81)` on `Z x Z`, the standard correspondence trace formula used in the retained post1518 source note is

`Tr_Q(S)=105+81-(Gamma_P,Delta)`.

Replacing `Delta` by `Graph(h)` is the same formula after translating one factor by `h`; it gives the rational trace of the corresponding `h`-twist. Hence define

`A_h = 186-Gamma_P.Graph(h)`.

In actual group order,

`A=[22,22,-22,-22]`.

Averaging over `H` projects to the H-trivial character block. The H-trivial part of `J(Z)` is the pullback of `J(C0)` for `C0=Z/H`, and the common Cartesian cover identifies the induced operator on this block with the retained downstairs correspondence `T=(f1)_*(f2)^*`. Therefore

`Tr_Q(T) = (22+22-22-22)/4 = 0`.

As a normalization cross-check, the nontrivial Fourier block traces are

`chi_u:0`, `chi_v:22`, `chi_uv:0`,

which are compatible with the separately derived Prym degrees `(9,137,9)`; the contradiction below is isolated to the downstairs H-trivial/Q602 block rather than caused by a scale mismatch.

## 5. Q602 contradiction

The retained post1518 exact trace spectrum is source-locked at

`stages/stage32/residual-32-01-production/post1518-o210-q602-residue73-trace-spectrum.json`.

For the hostile-audited marked-gauge survivor orbit `{73,97,235}` with `Q(T)=602`, rational trace is gauge-invariant and necessarily

`Tr_Q(T)=4 (mod 8)`.

Its exact allowed values are

`{-68,-60,-52,-44,-36,-28,-20,-12,-4,4,12,20,28,36,44,52,60,68}`.

The graph geometry forces `Tr_Q(T)=0`, which is not in this spectrum. Hence the fixed hypothetical `O=210`, `q'=4`, V6 carrier configuration cannot satisfy the required Q602 correspondence condition.

## Credit firewall

This note records a scratch/provisional terminal-candidate contradiction only. It is intended to dispose of the entire fixed O210 cover population because every such carrier has the same exact V6 class, same common H-cover geometry, and same mandatory Q602 interface; it is not a finite monodromy sample argument. Nevertheless:

- no hostile-audit credit is assigned here;
- no retained consolidation or claim-DAG synchronization is performed here;
- no Stage32 MAIN authority changes here;
- no merge is authorized;
- no statement about perfect-cuboid existence/nonexistence follows from this scratch note alone.
