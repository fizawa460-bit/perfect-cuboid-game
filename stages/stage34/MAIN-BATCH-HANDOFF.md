# Stage34 MAIN batch handoff

```text
STATUS=MAIN_AWAITING_SEPARATE_FIVE_ORBIT_AUDIT
PR=#1482 OPEN
BRANCH=stage34-02b-genus2-rankle1-rationalpoints
AUTHORITATIVE_REMAINING=22
AUTHORITATIVE_SIGN_ORBITS=11
CANDIDATE_EXACT_SIGN_ORBITS=5
CANDIDATE_EXACT_BRANCHES_WITH_SIGN_TRANSFER=10
DO_NOT_MERGE=true
```

Authoritative state is unchanged from the previous hostile-audit promotion: residual `22` branches / `11` audited sign orbits, by-q `{20/99:4,24/7:0,48/55:0,60/11:6,80/39:4,84/13:8}`. Do **not** promote the candidate counts below without a separate hostile audit.

## Current preaudit boundary

Read first:

1. `stages/stage34/34-02/d2-stageA2-five-exact-orbit-preaudit-manifest.json`
2. `stages/stage34/34-02/d2-stageA2-five-exact-orbit-replay-lock.json`
3. only the source evidence named by the manifest if deeper replay is required.

Exactly five direct representatives now have complete exact quotient point sets plus exact parent pullback with zero nondegenerate full-parent lifts:

- q=`60/11`: `06bcc4e821a7d482a435`, `6c6d7f3a758500d6b585`, `70158c7fb753b71bd2dd`;
- q=`84/13`: `54a9782fc24a5475166c`, `8f9ca1a5b214779b0af7`.

The replay lock permanently stores q/delta/model/sextic/scale and all six projective x:z inputs for each candidate. MAIN independently replayed those exact inputs with rational arithmetic: each candidate has six receiver-degenerate quotient points, exactly one full-parent-square point, and zero nondegenerate full-parent lifts. This is preaudit evidence only.

Their five listed sign partners are candidate-only. If and only if hostile audit validates all five direct proofs and the already-audited sign transfer, the prospective residual is `12` branches / `6` sign orbits, by-q `{20/99:4,24/7:0,48/55:0,60/11:0,80/39:4,84/13:4}`.

## Provenance repair performed in this batch

The old compact alternate27 RankBounds certificate did not match immutable artifact `9828202890`; generation-1 six-adapter credit is explicitly revoked in `d2-stageA2-six-rankbound-adapter-generation1-revocation.json`. The diagnostic certificate and six-adapter source lock were rebuilt from the artifact itself, preserving same-model rank evidence. Repaired generation 2 is pinned in `d2-stageA2-six-rankbound-adapter-generation2-certificate.json` with artifact `9828805411`, digest `sha256:e226ab93347c0ee0bfa3f3390f7c1c916d22df206507106482501edb677effab`, internal certificate SHA `sha256:a92ac2b55e2b85990cec170672e5a2c0dac62193503f76b5b86ec4aea15e3cec`, stdout SHA `sha256:363bae2c37e2ad2e0c31928e81a79a094ae2832149c6887aa69d0428e3fd96e5`.

Generation 2 produced two q=`84/13` exact candidates and four computation-incomplete cases. The incomplete cases are **not** mathematical failures and are excluded from the current audit: `169f94dd000a9c5c053f`, `40dc8f63e92a8a3a65e8`, `7a7ef1a67e794fe1651f`, `99448685b81e29427c3f`.

The surviving q=`20/99` representatives `0de8bce4df7652ea803e` and `6c9e0b2ecef523ee0477` have best checked alternate RankBounds upper bound `2`; they are not rank<=1 adapter targets and remain for a harder later leaf.

## Next exact leaf

`D2_STAGEA2_FIVE_EXACT_SIGN_ORBIT_HOSTILE_AUDIT`

Audit must independently check source hashes, same-model rank evidence (no cross-model substitution), quotient normalization, every complete quotient point against all four parent square predicates and receiver degeneracy, and sign transfer only to the five listed partners. Generation-1 six-adapter and all four generation-2 compute-incomplete branches receive no credit.

Keep OPEN: `D2_all_factor_branches_closed`, `direct_cover_rational_points_complete`, `all_multiples_closed`, `R29-EXT-CHANG-C`, and all parent-route/perfect-cuboid claims.
