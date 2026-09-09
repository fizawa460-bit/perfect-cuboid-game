# Stage32EX3 EX3-04h — retained modular graph trace-zero contradiction source note

Status: **RETAINED PROVISIONAL / NOT HOSTILE-AUDITED**

Fixed target only: recovered V6 class `g1-d186`, a hypothetical integral irreducible geometric-genus-1 carrier, `O=210`, `q'=4`, modular factor degrees `(105,81)`, and the retained `Q(T)=602` correspondence shell. This note supplies source locators and the exact adapter used by the retained EX3-04h candidate. It grants no Stage32 MAIN authority.

## External modular source

Primary source: Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, arXiv:1009.0388.

Two separate locators are load-bearing:

- Section 4, “The cuboid surface as a modular surface” (current author-hosted revision p. 8): `X(8)` has
  `u^2=2xy`, `v^2=x^2-y^2`, `w^2=x^2+y^2`; the kernel `G0 ~= (Z/2)^3` acts by signs of `u,v,w`; for `X(8) x X(8)` the diagonal invariants satisfy
  `U=2*b1`, `V=2*b2`, `W=2*b3`, `X=a1+c`, `Y=-a1+c`, `T=a2+i*a3`, `Zc=a2-i*a3`.
- Section 7, “Curves of low degree on Sbar” (current author-hosted revision p. 17, after Corollary 18 / around Lemma 20): images of graphs of automorphisms centralizing `G0` account for the 32 conics, and each such conic passes through six singularities.

## Exact H graph orbit

The retained relative-H marking
`stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-x-relative-h-marked-node-action.json`
gives
`u_H=g7*g9`, `v_H=g7*g8`, `u_H*v_H=g8*g9`.
Under the modular/cuboid identification these act on `(u,v,w)` as

- `1`: `(1,1,1)`;
- `u_H`: `(-1,1,-1)`;
- `v_H`: `(-1,-1,1)`;
- `u_H*v_H`: `(1,-1,-1)`.

The exact C1 group-3 transcription in
`stages/stage33/33-12/diagnose_e3_v91c1v_actual_prime_known140_locator.py`
uses
`a3=0`, `a1+e1*b2=0`, `a2+e2*b1=0`, `b3+e3*c=0`
with nested `e1,e2,e3 in [+1,-1]`.
For `Graph(h)` one gets `(e1,e2,e3)=(-eps_v,-eps_u,-eps_w)`, hence the exact C1 indices in H order are
`[24,21,18,19]`.

## Blow-down intersection adapter

Use the retained exact double-cover/blow-down adapter
`stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-beauville-blowup-picard-adapter-delta-lock.json`.
For a graph-conic `K_h`, its pullback `Ltilde_h`, and carrier pullback `Dtilde`, the resolved intersection is
`Dtilde.Ltilde_h = 2*(C.K_h)`.
At each incident exceptional curve, `Dtilde.Etilde_j=m_j` and `Ltilde_h.Etilde_j=1`; after blow-down,
`D.L_h = 2*(C.K_h) + sum_{j incident K_h} m_j`.
The quotient `P=X(8) x X(8) -> X=P/H_diag` has degree 4, so
`Gamma_P.Graph(h)=4*(D.L_h)`.

The recovered V6 pairings and six-node incidence give, in H order `[1,u_H,v_H,u_H*v_H]`:

- `C.K = [0,0,14,9]`;
- incident node mass `[41,41,24,34]`;
- `D.L = [41,41,52,52]`;
- `Gamma_P.Graph = [164,164,208,208]`.

## Trace contradiction

For bidegree `(105,81)`,
`A_h = 105+81-Gamma_P.Graph(h)`,
hence
`A=[22,22,-22,-22]`.

Averaging over H gives the H-trivial block trace
`Tr_Q(T)=(22+22-22-22)/4=0`
for the downstairs operator `T=(f1)_*(f2)^*` on `J(C0)`.

The retained exact spectrum
`stages/stage32/residual-32-01-production/post1518-o210-q602-residue73-trace-spectrum.json`
is trace-gauge-invariant on the marked survivor orbit `[73,97,235]`, requires
`Tr_Q(T)=4 (mod 8)`,
and has exact allowed traces
`[-68,-60,-52,-44,-36,-28,-20,-12,-4,4,12,20,28,36,44,52,60,68]`.
Zero is absent. Thus the fixed hypothetical O210/q'=4 V6 carrier package is contradictory.

## Population and credit boundary

No finite monodromy or Nielsen sample is used. The contradiction is upstream of any choice of residual monodromy tuple: every hypothetical carrier in the fixed target must carry the same typed common-H correspondence interface and the same fixed V6 divisor/intersection data. Therefore EX3-05 through EX3-08 are dominated by this necessary-condition contradiction; this does **not** claim those enumerations were executed.

This is a retained **PROVISIONAL** terminal gate only. It is not hostile-audited, does not self-promote to Stage32 MAIN, does not globally exclude Q602 outside the fixed O210 target, and does not imply Perfect Cuboid existence or nonexistence. Merge is not authorized.
