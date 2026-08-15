# Stage25-60 R504 residual — hostile re-audit repair

STATUS=REPAIR_SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504

## Audited original-base theorem retained

For
\[
E_F/\mathbf Q(k):\quad Y^2=X^3-4(k^4+1)^2X,
\]
the hostile-audited original-base result is `rank E_F(Q(k))=1`; the first nondegenerate fixed section is `3P` and
\[
N_{R504,3P}(B)=\Theta(B^{1/10}).
\]
No global Stage25 exponent changes.

```text
R504_ORIGINAL_BASE_STATUS=AUDITED_CLOSED_NO_GLOBAL_UPGRADE
R504_GENERIC_QK_RANK=1
R504_SECOND_INDEPENDENT_QK_SECTION_EXISTS=false
R504_3P_EXACT_FAMILY_GROWTH=Theta(B^(1/10))
```

## Correct Q-form / twisted product-Kummer statement

Put `E0: v^2=u^3-4u` and `C:s^2=k^4+1`. The audited birational identification `C ~= E0` sends the deck involution to
\[
Q\mapsto T-Q,\qquad T=(0,0),
\]
not to `Q -> -Q`. The earlier R504 audit also proved that `T` is not twice a Q-rational point. Therefore no Q-rational translation conjugates this action to standard negation. Over an extension containing a half of `T` it becomes the usual product-Kummer involution, but over Q the safe classification is only a Q-form/twist of that product Kummer.

```text
R504_STANDARD_Q_KUMMER_IDENTIFICATION=false
R504_SAFE_KUMMER_CLASS=Q_FORM_OR_TWIST_OF_PRODUCT_KUMMER
R504_KUMMER_MODEL_EXACT_OVER_Q=false
```

This correction does not affect BC1/BC2, which were checked directly on their pullback covers.

## Rational base change / multisection mechanism

A rational finite base change `phi:P1_u -> P1_k` plus a new section gives a rational multisection on the original surface; normalizing a rational multisection gives the converse pullback picture. Thus the unresolved positive-power rational-base-change and rational-multisection searches are the same mechanism.

```text
R504_RATIONAL_BASE_CHANGE_EQUIVALENT_TO_RATIONAL_MULTISECTION=true
```

The natural twist-killing cover has genus one and introduces no rational one-parameter base. The two concrete degree-two candidates already accepted by hostile re-audit are:

```text
R504_BC1=k=u^2
R504_BC1_COVER=y^2=u^8+1
R504_BC1_JACOBIAN_FACTORS_J=1728,8000,8000
R504_BC1_PULLBACK_MW_RANK=1
R504_BC1_STATUS=CLOSED_NO_RANK_JUMP
R504_BC2=k=(u^2-1)/(2u)
R504_BC2_EXTRA_QUOTIENT_J=10976,10976
R504_BC2_PULLBACK_MW_RANK=1
R504_BC2_STATUS=CLOSED_NO_RANK_JUMP
```

For a general degree-two `phi`, a rank jump still requires an additional `E0`-isogeny factor in `J(C_phi)` beyond the inherited factor. BC1/BC2 do not classify all `phi`.

```text
R504_DEGREE2_GENERAL_GATE=EXTRA_E0_FACTOR_IN_JACOBIAN_OF_C_phi
R504_NEW_EXCEPTIONAL_phi_REQUIRED=true
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_EXPLICIT_CURVE_SEARCH
R504_RESIDUAL_DEEP_STOP_CLASS=LIVE_NOT_EXTERNAL_THEOREM_GATE
```

This residual is deliberately kept LIVE under the unchanged normative continuation policy. No self-relaxation of the stop rule is asserted.

## Growing multiples — real-component parity lemma

Let `F=k^4+1>0`. The quartic-to-elliptic map has x-coordinate
\[
X(t)=-\frac{4Ft^2}{t^4+1}.
\]
For real `t`, AM-GM gives `0 <= 2t^2/(t^4+1) <= 1`, hence
\[
-2F\le X(t)\le0.
\]
Thus every real quartic image lies on the bounded/non-identity real component of
\[
E_F(\mathbf R):\quad y^2=x(x-2F)(x+2F).
\]
The audited generator `P` is a quartic image, so its component class is the nonzero element of
\[
E_F(\mathbf R)/E_F(\mathbf R)^0\cong\mathbf Z/2.
\]
The component map is a group homomorphism. Therefore `[n]P` is on the bounded component exactly when `n` is odd; every even multiple lies on the identity component, whose real x-coordinates satisfy `x>=2F`, and so cannot be a real quartic image. Consequently every nondegenerate physical quartic multiple is odd. Since `P` itself is the degenerate/nonphysical first class in this lane, the first possible nondegenerate physical multiple is `n=3`.

```text
R504_QUARTIC_REAL_X_RANGE=[-2F,0]
R504_REAL_COMPONENT_GROUP=Z/2
R504_GENERATOR_COMPONENT=NONIDENTITY
R504_EVEN_MULTIPLES_COMPONENT=IDENTITY
R504_EVEN_MULTIPLES_ARE_QUARTIC_IMAGES=false
R504_ALL_PHYSICAL_MULTIPLES_ODD_LEMMA_MATERIALIZED=true
R504_FIRST_NONDEGENERATE_PHYSICAL_MULTIPLE_INDEX=3
```

## Growing-multiple count

For an odd physical multiple `[n]P`, the induced Lattes map on the quartic parameter has degree `n^2`. For a primitive physical box of space height at most `B`, exact face identities give
\[
(t/k)^2=(H_X-X)/(H_X+X),\qquad (kt)^2=(H_Y+Y)/(H_Y-Y),
\]
so
\[
h(t)\le\tfrac12\log(2B).
\]
Canonical quotient height satisfies `h_L(t_n(k))=n^2 h_L(k)` and `h_L=h+O(1)`, uniformly in `n`. Hence fixed odd `n` contributes `O(B^(1/n^2))` rational base parameters. Degree-<=2 Northcott on lifts to `E0` gives `|n|=O(sqrt(log B))` outside a finite torsion/preperiodic set. The parity lemma forces every nondegenerate physical term to have `n>=3`, therefore
\[
N_{R504,\mathrm{all\ multiples}}(B)
\ll B^{1/9}\sqrt{\log B}=o(B^{1/4}).
\]
The exactly-two/canonical filters only decrease this count.

```text
R504_GROWING_MULTIPLE_LATTES_DEGREE=n^2
R504_PHYSICAL_BOX_IMPLIES_h_t<=0.5log(2B)
R504_ALL_MULTIPLES_COUNT_UPPER=O(B^(1/9)*sqrt(log B))
R504_GROWING_MULTIPLE_QUARTER_UPGRADE=false
R504_GROWING_MULTIPLE_ROUTE=CLOSED_NO_QUARTER_UPGRADE_WITH_HEIGHT_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
```

## Current R504 classification submitted

```text
R504_BC1_STATUS=CLOSED_NO_RANK_JUMP
R504_BC2_STATUS=CLOSED_NO_RANK_JUMP
R504_GROWING_MULTIPLE_ROUTE=CLOSED_NO_QUARTER_UPGRADE_WITH_HEIGHT_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_EXPLICIT_CURVE_SEARCH
R504_RESIDUAL_STATUS=LIVE_UNDER_NORMATIVE_STOP_RULE
R504_GLOBAL_LOWER_CHANGED=false
FINITE_DATA_USED_AS_PROOF=false
```

Fresh audit may accept the growing-multiple closure, but it may not use this artifact to deep-stop checkpoint60: the exceptional rational base-change/multisection search remains LIVE unless separately closed or reduced to the pre-existing normative `EXTERNAL_THEOREM_GATE` class.