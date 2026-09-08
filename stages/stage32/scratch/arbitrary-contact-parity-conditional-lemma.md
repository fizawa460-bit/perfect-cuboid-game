# Conditional arbitrary-contact parity lemma — MAIN scratch

Status: SCRATCH_ONLY / UNAUDITED_CONDITIONAL_LEMMA.
This does not import the O210 three-residue conclusion into EX1.

## Locked reading context

Snapshot: f2a89e613cdf91191a0aada9e90c9fc93373a6c6.
Sources:
- stages/stage32-ex1/ex1-05f-h4-local-cusp-projection-ramification-adapter.md
- stages/stage32/residual-32-01-production/post1505-o210-q602-weierstrass-parity-transvection-refinement-source-note.md

The former supplies the local normalized-base-change formula k_i=m+2*ell_i.
The latter supplies the O210 marked-pair parity argument and its limitations.
No independent hostile audit of those sources is claimed.

## Hypotheses

Work over C on smooth normalized curves with the common double-cover
involution tau and two finite maps f_i to the same genus-two hyperelliptic
curve, equivariant for its involution iota. At every relevant node branch
assume the local formula k_i=m+2*ell_i, m>0, ell_i>=0, with the same marked
ordered Weierstrass pair as in the retained geometry.

For the GLOBAL application additionally require:
all tau-fixed points contributing to these Weierstrass pullbacks are
accounted for by these branches; their marked pair masses equal the
retained masses; and the same Jacobian/marking/orientation adapters apply.
These extra hypotheses are obligations, not conclusions of this note.

## Local calculation for arbitrary multiplicity

At a node branch put u=t^k*unit and normalize v^2=u. Over C the unit has
a local analytic square root.

If k is odd, write t=s^2; then v=s^k*unit. There is one tau-fixed point,
and the local degree to the hyperelliptic curve is k. Thus the multiplicity
in f_2^*P_b is k_2=m+2*ell_2, an odd integer whenever m is odd. It need
not equal one.

If k is even, normalization has two branches exchanged by tau. The two
points have equal pullback multiplicities. Their pushforwards under f_1
form a multiple of Q+iota(Q), a hyperelliptic fiber, including when Q is
itself Weierstrass.

For odd m=2a+1, k_2=1+2(a+ell_2). Consequently the fixed point contributes
one copy of its marked first-factor Weierstrass point modulo multiples
of the hyperelliptic fiber class F, since 2P_a is linearly equivalent to F.
This argument does not require f_1 to be unramified and does not restrict
m to 1 or 2.

## Parity of a fixed marked-pair mass

For any positive-integer branch partition M_p=sum_j m_j, let n_p be the
number of odd m_j. Then

M_p-n_p = sum_j (m_j-(m_j mod 2))

is even. Hence n_p == M_p (mod 2) for arbitrary branch multiplicities.
The O210 expression M_p=n_p+2*y_p is one special case of this identity.

## From divisors to J[2]: conditional scope

Modulo multiples of F, (f_1)_*(f_2)^*P_b has the parity-weighted marked
Weierstrass coefficients just described. When the resulting parity matrix
is the retained permutation matrix B, each column has a single odd entry.
Since all these divisors have the same degree, their remaining multiples
of F have the same coefficient. They cancel in the differences for
P_b-P_c. Thus the retained transposition action follows under the GLOBAL
hypotheses above, even with higher contact multiplicities.

Do not regard an arbitrary even divisor as zero in J[2]; the argument uses
specifically 2P_a~F and cancellation in equal-degree divisor differences.

## Exact progress and next check

Higher multiplicity and local projection ramification alone do not break
the parity step. This removes one prospective obstruction to extending
the proof, conditionally; it does not establish a uniform transvection
adapter for all 29 EX1 states.

Next check: establish exhaustive marked-pair incidence and the equality
of the grouped masses for the same h=4 pullback across the 29 states,
including absence/accounting of additional fixed-point contributions.
Then replay the retained-coordinate predicate on the EX1 input set;
do not assume the intermediate 16-residue filter is uniform.

No new O state or residue is excluded. MAIN authority, [73,97,235],
EX1 states, claim DAG and audit credit are unchanged.
