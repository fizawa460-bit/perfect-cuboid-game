# StructureRadar audit — SR-BATCH-STAGE16_25_CURRENT-03-R01

AUDIT_VERDICT=PASS_WITH_MINOR_PROVENANCE_NOTES
PR=1083
AUDITED_HEAD=a1815038e6b801f90d100f3e96dfb21ac69a095d
SOURCES_REVIEWED=60
STRUCTURES_ADDED=4
STRUCTURES_UPDATED=3

## Mathematical audit

- `SR-STR-148`: PASS. Stage21 proves `N1/M1 ~ (kappa*pi/18)(log B)^2/B`, while the ambient space baseline is `N_S^all/U ~ [9*zeta(3)/(8*pi*G)]/B`; their quotient is `[4*kappa*pi^2*G/(81*zeta(3))](log B)^2`, so the intrinsic polynomial space cost remains `B^-1` and one-face conditioning contributes a positive `(log B)^2` enhancement. Fine pole/local-factor allocation remains explicitly open.
- `SR-STR-149`: PASS. The audited post-Stage25 geometric receiver gives `b(M1)=2`, `b(N1)=4`, `b(M2)=6`, hence `6-2=4` and the geometric decomposition `(6-2)=(4-2)+(6-4)=2+2`. No four-factor independence or four independent Dirichlet poles are claimed.
- `SR-STR-150`: PASS. The selected slice is `w^2=(t^2+1)(t^2+2t+2)`. With `s=2t+1`, `W=4w`, one has the exact identity `W^2=s^4+6s^2+25`. For every integral `t`, exactly one of `t,t+1` is odd, so one factor is `2 mod 8` and the other is odd; the product is always `2 mod 8`, impossible for an integer square. This excludes the entire selected slice and no global Stage19 upper improvement is inferred.
- `SR-STR-151`: PASS. The source-level Q06 execution proves the exact physical-height identity `H_M=d`, bounded orientation multiplicity, and the fixed-squareclass Jacobi lift `y^2=(t^2+s)(1+s*t^2)`. The unresolved requirement is a uniform moving-transverse-family count/dispersion theorem; the fixed-curve exponent `<=1/2` cannot be summed into a strict global sub-half bound.

## Provenance notes

- `SR-STR-150`'s primary checkpoint40 source contains the global mod-8 proof. Its checkpoint30 audit provenance should be read only as prior audited acceptance of the genus-one receiver, not as the source of the later mod-8 exclusion.
- `SR-STR-151`'s `q06-source-execution.md` is the controlling source. The earlier `deep-execution-q03-q06.md` records the pre-source-opening boundary and is superseded on the question of whether the concrete receiver/height package is materialized.
- These notes do not change either normalized mathematical statement because the controlling primary sources are present and correct.

## Corpus / lifecycle audit

- all 60 queued source IDs have an explicit `STRUCTURES_RECORDED` or `DUPLICATE_SOURCE` decision;
- batch accounting is `structures_added=4`, `structures_updated=3`, `structures_deduped=38`, `structure_carrier_sources=22`, with 60 source decisions total;
- helper reports and temporary workflows were removed before handoff;
- branch was `behind_by=0` versus main at the audited head;
- exact-head `StructureRadar controller` was SUCCESS before this audit-record commit;
- this audit closes only the submitted batch and does not authorize automatic merge.

MERGE_ALLOWED=true
AUDIT_REQUIRED=false
NEXT_EXPECTED_COMMAND=merge PR #1083; then StructureRadar-main-batch
