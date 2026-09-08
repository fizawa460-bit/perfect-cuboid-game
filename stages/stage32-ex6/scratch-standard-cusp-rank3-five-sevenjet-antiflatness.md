# Stage32EX6 scratch — standard-cusp rank3 five/seven-jet anti-flatness translation

Status: `SCRATCH_EXACT_BOUNDED_STANDARD_CUSP_RANK3_FIVE_SEVENJET_ANTIFLATNESS_NO_ENDPOINT_CREDIT`

Scratch only. This leaf does not update `MAIN-STATE`, exclude O266, authorize O264 descent, create hostile-audit credit, or advance Stage32 MAIN.

## Source locks

- PR #1715 retained EX6 head used for authority context:
  `5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7`.
- Standard-cusp rank3/theta adapter:
  `scratch-standard-cusp-r3-theta-fourjet-adapter.md`.
- Six-rank3 simultaneous RH budget:
  `scratch-six-rank3-simultaneous-rh-budget.md`.
- Aggregate nonminimal ramification coupling:
  `scratch-rank3-nonminimal-node-ramification-coupling.md`.
- Replay verifier:
  `scratch_verify_standard_cusp_rank3_five_sevenjet.py`.

## 1. Ambient rank3/theta transition through order seven

At the standard modular cusp the exact ambient relation is

`T = u + u*(1-u^8)*x^4 + O(x^8)`.

Write an FSM-minimal branch as

`u(x)=lambda+c1*x+c2*x^2+c3*x^3+c4*x^4+c5*x^5+c6*x^6+c7*x^7+O(x^8)`.

Let

`A(u)=u-u^9`.

Then

`T=u+A(u)x^4+O(x^8)`.

If

`T(x)=lambda+d1*x+d2*x^2+d3*x^3+d4*x^4+d5*x^5+d6*x^6+d7*x^7+O(x^8)`, 

direct expansion gives

- `d1=c1`;
- `d2=c2`;
- `d3=c3`;
- `d4=c4+lambda*(1-lambda^8)`;
- `d5=c5+(1-9*lambda^8)c1`.

Now impose rank3-four-flatness, i.e. `d1=d2=d3=d4=0`. Then exactly

`c1=c2=c3=0`,

`c4=-lambda*(1-lambda^8)`.

Under these relations all lower derivative corrections in `A(u)` vanish through the next three orders, so

`d5=c5`,

and if `d5=0`, then `d6=c6`; if also `d6=0`, then `d7=c7`.

Therefore at the standard cusp:

### rank3-five-flat

is equivalent through order five to

`c1=c2=c3=0`,

`c4=-lambda*(1-lambda^8)`,

`c5=0`.

### rank3-six-flat

adds

`c6=0`.

### rank3-seven-flat

adds

`c7=0`.

The fourth coefficient is the only exceptional correction through order seven; after it is cancelled, orders five through seven agree directly with the AN/resolved normal coefficients.

## 2. Combine with the unconditional six-rank3 RH anti-flatness counts

The aggregate rank3 RH coupling gives, with

`E:=Eta+Rrho`,

- at least `16+E` minimal branches fail rank3-five-flatness;
- at least `45+E` fail rank3-six-flatness;
- at least `65+E` fail rank3-seven-flatness.

Thus, after transporting the standard-cusp ambient formula to a chosen node chart, the hypothetical O266 member cannot satisfy the corresponding jet system on all minimal branches.

At the standard cusp itself, every rank3-five-flat failure means at least one of

`c1`, `c2`, `c3`, `c4+lambda*(1-lambda^8)`, `c5`

is nonzero.

Similarly, the six-flat failure system adds `c6`, and the seven-flat system adds `c7`.

This turns the global RH failure count into an explicit member-jet anti-flatness target rather than a bare local-degree statement.

## 3. Special landing set

If `lambda^8=1`, then the fourth-order correction vanishes and the systems simplify:

rank3-five-flat becomes

`c1=c2=c3=c4=c5=0`,

rank3-six-flat adds `c6=0`, and rank3-seven-flat adds `c7=0`.

No retained theorem forces `lambda^8=1`; the AN local model allows arbitrary nonzero finite landing values. Therefore this simplification is conditional only and is not used as endpoint credit.

## 4. Current mathematical ceiling

The new statement is anti-flatness, not endpoint exclusion. It says a hypothetical O266 carrier must contain a definite population of minimal branches whose fixed global rank3 pencil jets fail the displayed equations.

To obtain a contradiction, one still needs an independent fixed-V6 member theorem forcing those equations on more branches than the RH budget permits. Class-level exceptional degrees and the A1 formal neighborhood do not provide such forcing; previous scratch leaves already source-lock that wall.

## Canonical scratch decisions

- `STANDARD_CUSP_D1_D2_D3_EQUAL_C1_C2_C3 = true`;
- `STANDARD_CUSP_D4 = c4+lambda*(1-lambda^8)`;
- `STANDARD_CUSP_D5 = c5+(1-9lambda^8)c1`;
- `RANK3_FOURFLAT_IMPLIES_C1_C2_C3_ZERO_AND_C4_CORRECTED = true`;
- `UNDER_RANK3_FOURFLAT_D5_EQUALS_C5 = true`;
- `UNDER_RANK3_FIVEFLAT_D6_EQUALS_C6 = true`;
- `UNDER_RANK3_SIXFLAT_D7_EQUALS_C7 = true`;
- `RANK3_FIVEFLAT_JET_SYSTEM = [c1,c2,c3,c4+lambda*(1-lambda^8),c5]=0`;
- `RANK3_FIVEFLAT_FAILURES_GTE = 16+E`;
- `RANK3_SIXFLAT_FAILURES_GTE = 45+E`;
- `RANK3_SEVENFLAT_FAILURES_GTE = 65+E`;
- `LAMBDA8_EQ_1_FOR_V6_MINIMAL_LANDINGS = false_as_current_credit`;
- `INDEPENDENT_MEMBER_JET_FORCING_THEOREM_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- The explicit coefficient formulas are source-locked at the standard modular cusp. No numbered 48-node coefficient table is silently asserted.
- The global RH failure counts are invariant local-degree statements; translating every failure to the displayed raw coefficient tuple at every numbered node would require the corresponding transported cusp coordinate chart.
- No finite landing theorem is inferred from the factor `1-lambda^8`.
- No member equation, hostile audit, retained consolidation, Stage32 MAIN, lower-O, or Perfect Cuboid credit follows.
