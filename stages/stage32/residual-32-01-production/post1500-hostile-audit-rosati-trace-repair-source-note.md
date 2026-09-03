# Stage32 post-1500 hostile-audit Rosati-trace repair

Scope: exact recovered V6 class `g1-d186`, `d=186`, `e=266`, `z=(-15,62,-44,26,32)`. This repair responds to hostile-audit FAIL review `5097587880` on PR #1500 at exact head `43a7a46cc7cd3e5ef1f5ae5cb31d17c45b10e9b9`. The exact-head replay `33712731325 / 100515467002` succeeded mechanically, but that does not repair the mathematical defect identified by hostile audit.

## Audit correction

The withdrawn V224 argument used the false implication

`bidegree(Gamma)=(105,81) => Gamma^2=2*105*81=17010`

for a correspondence `Gamma` on `Q=C0 x C0`, where `g(C0)=2`. On a positive-genus product, bidegree does not determine self-intersection: the correspondence/Rosati component contributes. The retained correspondence source lock already states

`sigma(Gamma)=2*d1*d2-Gamma^2`

and identifies `sigma` with the rational Rosati trace pairing.

Therefore the all-overlap deck-cross exclusion certificate and controller V224 are superseded. The earlier O=210 exclusion from #1490 is also reopened because its contradiction used the same zero-Rosati specialization.

## Retained exact class/deck arithmetic

The following data do not use `Gamma^2=17010` and remain retained exact inputs:

- exact V6 resolved class self-intersection `C^2=758`;
- exceptional square mass `sum_j m_j^2=2358`;
- explicit Beauville blow-up/blowdown adapter `D^2=2*758+2358=3874`;
- exact source-locked deck pairings `D.uD=3892`, `D.vD=4020`, `D.uvD=4020`;
- exact deck-translate sum `11932`;
- pair-map degrees `(105,81)` and birationality, using generic degree in `{1,2,4}` together with divisibility by `gcd(105,81)=3`;
- `X -> Q=C0 x C0` finite etale of degree four with deck group V4.

For an actual carrier, `q^*Gamma=D+uD+vD+uvD`. Squaring the finite-etale V4 pullback gives

`Gamma^2 = D^2 + D.uD + D.vD + D.uvD`.

Hence the exact deck data force

`Gamma^2 = 3874+11932 = 15806`.

With `(d1,d2)=(105,81)`, the required Rosati trace is therefore

`sigma(Gamma)=2*105*81-15806=1204`.

The retained principal Rosati normalization uses

`Tr_Q(T^dagger*T)=2*Q(T)`,

so the exact required lattice value is

`Q(T)=602`.

The former gap `13136-11932=1204` is thus not a contradiction. It is precisely the nonzero Rosati trace that the withdrawn argument omitted.

## O=210 normalization arithmetic

For O=210, the retained Beauville odd-branch and modular-factor geometry still gives `g(Y)=106`. The correspondence formula

`sigma(Gamma)=2*d1*d2+2*(d1+d2)-2*p_a(Gamma)+2`

with `sigma=1204` gives `p_a(Gamma)=8090`, hence normalization defect

`delta_Gamma=p_a(Gamma)-g(Y)=7984`.

Equivalently the retained identity `Q(T)=8586-delta_Gamma` gives `602=8586-7984`. Thus the formula `Q=8586-delta` itself remains valid; what fails is the earlier specialization `Gamma^2=17010`, which forced `delta=8586` and `Q=0`.

Any downstream numerical statement that assumed that zero-Rosati specialization, including `Gamma^2=17010`, `delta_Gamma=8586`, the corresponding zero-trace deck-defect specialization, or later simplex values derived from it, is reopened until rederived from corrected inputs.

## Bounded retained-Rosati search at Q=602

The retained principal Rosati lock gives the positive-definite rank-eight integral trace lattice, isometric to `D4 direct-sum D4`, together with the operator constraint `T^dagger*T <= 8505`.

This does not exclude `Q=602`:

1. `602 < 8505`, so the retained automatic implication says the operator inequality is automatic at this trace value.
2. In one D4 factor, norm `602=2*301` is represented. The retained D4 shell formula is
   `a(m)=24*sum_{d|m, d odd} d` for norm `2m`.
   Since `301=7*43`,
   `a(301)=24*(1+7+43+301)=8448>0`.
   Hence the D4 direct-sum D4 trace lattice certainly represents `Q=602`.
3. The retained O=210 Weierstrass collision optimization gives only `delta_Gamma >= 1924`. The corrected required value `delta_Gamma=7984` satisfies this bound, so that constraint is also nonexcluding.

Therefore the bounded existing Rosati/D4/Weierstrass asset search ends in exact nonexclusion. No full Rosati enumeration is authorized or useful here.

## Current exact blocker

The fixed-V6 O=210 carrier is OPEN again. The exact remaining requirement is a genuinely geometric constraint that either

- forces `sigma(Gamma)=0`, or
- independently excludes `sigma(Gamma)=1204` / `Q(T)=602` for a correspondence arising from the common-cover/marked-branch geometry.

Until such an input is source-locked, O=212 and all later overlaps remain blocked behind O=210. Do not infer a contradiction from bidegree alone, do not reuse the zero-Rosati specialization, and do not promote exact CI success to mathematical audit success.

## Firewalls

- O186 and O188 remain closed audited and are not reopened.
- O210 is reopened; O212..266 are not active.
- The V224 all-genus-one fixed-V6 exclusion is withdrawn/superseded.
- No effectivity, FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit follows.
- PR #1500 remains open and must not merge before a new hostile-audit PASS on a repaired claim.
