# Stage29-04 — population host, predicate masks, and condition-cost matrix

```text
TASK_ID=Stage29-04
ROLE=POPULATION_HOST_PREDICATE_AND_CONDITION_COST_MATRIX
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ROADMAP_REVISION=R2_POST_29_02_FOUNDATION_SCREEN_AUDITED
OLD_STAGE_REENTRY_REQUIRED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Exact common physical host

Let

\[
\mathcal U(B)=\{(a,b,c)\in\mathbf Z_{>0}^3:0<a<b<c,\ \gcd(a,b,c)=1,\ R=\sqrt{a^2+b^2+c^2}\le B\}.
\]

Define four Boolean predicates on every object of `U(B)`:

```text
F_ab = [a^2+b^2 is a square]
F_ac = [a^2+c^2 is a square]
F_bc = [b^2+c^2 is a square]
S    = [R is an integer]
```

For `epsilon_ab,epsilon_ac,epsilon_bc,sigma in {0,1}`, define the cell

\[
C_{\epsilon_{ab}\epsilon_{ac}\epsilon_{bc};\sigma}(B)
\]

to be the objects of `U(B)` with exactly those four truth values.

Then the sixteen cells are pairwise disjoint and their union is exactly `U(B)`:

\[
\boxed{\mathcal U(B)=\bigsqcup_{\epsilon_{ab},\epsilon_{ac},\epsilon_{bc},\sigma\in\{0,1\}} C_{\epsilon_{ab}\epsilon_{ac}\epsilon_{bc};\sigma}(B).}
\]

This is an elementary exact partition, not an asymptotic statement.

```text
PHYSICAL_BOOLEAN_PREDICATES=4
PHYSICAL_BOOLEAN_CELLS=16
BOOLEAN_PARTITION_EXHAUSTIVE=true
BOOLEAN_PARTITION_DISJOINT=true
```

## 2. Stage16–20 populations inside the sixteen-cell partition

Let `f=F_ab+F_ac+F_bc` be the number of integral face diagonals. Define

```text
E_k = {f=k}                       # space predicate unrestricted
E_k^S = {f=k and S=1}
```

Then, object-for-object under the common primitive/canonical `R<=B` convention,

```text
E_1   = M1       (Stage16)
E_1^S = N1       (Stage17)
E_2   = M2       (Stage18)
E_2^S = N2       (Stage19)
E_3   = M3       (Stage20)
E_3^S = P        (perfect-cuboid endpoint)
```

Thus

\[
M_1=(E_1\cap\{S=0\})\sqcup N_1,
\]
\[
M_2=(E_2\cap\{S=0\})\sqcup N_2,
\]
\[
M_3=(E_3\cap\{S=0\})\sqcup P.
\]

The last identity is load-bearing: Stage20 imposes no space-diagonal condition, so a hypothetical perfect cuboid is included in `M3`. No use of the finite `P(B)=0` census is made in this set identity.

The two face-zero cells `E_0 cap {S=0}` and `E_0 cap {S=1}` are part of the exhaustive host but are not Stage16–20 target populations.

## 3. The legal nested face-condition ladder

The exact-face populations `M1`, `M2`, `M3` are disjoint, so they are not a literal subset chain. The correct nested physical hosts are

\[
H_{\ge1}=E_1\sqcup E_2\sqcup E_3=M_1+M_2+M_3,
\]
\[
H_{\ge2}=E_2\sqcup E_3=M_2+M_3,
\]
\[
H_{\ge3}=E_3=M_3.
\]

Hence

\[
\boxed{H_{\ge3}\subset H_{\ge2}\subset H_{\ge1}\subset U.}
\]

This is the exact objectwise ladder for the statements

```text
at least one face succeeds
at least two faces succeed
all three faces succeed
```

and is the correct host if one wants literal YES/NO survival semantics for adding further face conditions.

The corresponding space intersections are

\[
S\cap H_{\ge1}=N_1\sqcup N_2\sqcup P,
\]
\[
S\cap H_{\ge2}=N_2\sqcup P,
\]
\[
S\cap H_{\ge3}=P.
\]

No global dominance of `N2` over `P` is assumed in `S cap H_{>=2}`.

## 4. Legal versus illegal survival ratios

### Literal survival ratios

The following are genuine subset ratios under one fixed physical host:

```text
N1/M1                 # add S inside exactly-one-face host
N2/M2                 # add S inside exactly-two-face host
P/M3                  # add S inside exactly-three-face host
H_ge1/U               # require at least one face
H_ge2/H_ge1           # require at least two faces after at least one
H_ge3/H_ge2           # require all three faces after at least two
```

### Not literal survival ratios

The following compare disjoint or differently masked exact strata and must not be called objectwise survival probabilities:

```text
M2/M1
M3/M2
N2/N1
M3/N2
```

They remain meaningful matched population-size ratios when their common physical conventions are locked, but require a common host to obtain literal conditional-event semantics.

This reproduces and unifies the Stage22, Stage26 and Stage28 firewalls.

## 5. Current certified population surface on the exact host

The strongest Stage29-entry theorem surface used here is the audited Stage28/Stage29 synthesis:

\[
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2),
\]

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\qquad
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3,
\]

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

and

\[
\liminf_{B\to\infty}\frac{M_3(B)}{B^{1/3}}\ge\frac{27}{40\pi^2}>0,
\]

while for every fixed `0<eta<1/46`,

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

For the endpoint,

```text
P(B)=0 for every B<=10^9       # exact finite census
P(B)=0 for all B globally      # NOT PROVED
```

No finite zero is promoted to a global asymptotic or nonexistence theorem.

## 6. Condition-cost matrix

### 6.1 First face, interpreted on the nested at-least host

Since `M2=o(M1)` and `M3=o(M2)`,

\[
H_{\ge1}(B)\sim M_1(B).
\]

Therefore

\[
\frac{H_{\ge1}}{U}
\sim
\frac{27\zeta(3)}{\pi^3}\frac{\log B}{B}.
\]

So requiring at least one integral face has literal-host cost

```text
POLYNOMIAL_COST=B^-1
LOG_FACTOR=log B
```

relative to the unrestricted primitive/canonical cuboid host.

### 6.2 Second face, interpreted on the nested at-least host

Stage26 gives `H_ge2=M2+M3~M2`, while `H_ge1~M1`. Hence

\[
\frac{H_{\ge2}}{H_{\ge1}}
\sim
\frac{M_2}{M_1}
\sim
\frac{4\pi^2C_{M_2}}3\frac{(\log B)^4}{B}.
\]

Thus the legal nested second-face completion has

```text
POLYNOMIAL_COST=B^-1
LOG_COMPENSATION=(log B)^4
```

The equality with the adjacent-stratum ratio is asymptotic because the omitted higher-face strata are lower order; `M2` is not literally a subset of `M1`.

### 6.3 Third face, interpreted on `H_ge2`

Let

\[
\Phi(B)=\frac{M_3(B)}{M_2(B)+M_3(B)}.
\]

Stage26 proves `Phi(B)->0` and, for fixed `epsilon>0` and fixed `0<delta<1/46`,

\[
B^{-2/3-\varepsilon}(\log B)^{-5}\ll_\varepsilon\Phi(B)=o((\log B)^{-\delta}).
\]

The true cost is not identified. This is a literal host survival observable, unlike the bare exact-stratum statement `M3/M2`.

### 6.4 Space diagonal after exactly one face

`N1 subset M1` is literal and Stage21 gives

\[
\boxed{
\frac{N_1}{M_1}
\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
}
\]

So after exactly one face, the integral-space predicate has

```text
POLYNOMIAL_COST=B^-1
INTERACTION_ENHANCEMENT=(log B)^2
```

relative to the ambient `B^-1` space-diagonal scale certified in Stage21.

### 6.5 Space diagonal after exactly two faces

`N2 subset M2` is literal. Current bounds imply

\[
\frac{N_2}{M_2}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5},
\]

while the Stage28 lower construction gives the lower corridor

\[
\frac{N_2}{M_2}\gg
B^{-3/4}(\log B)^{-5}
\]

up to the fixed-constant interpretation of the imported `N2 >> B^{1/4}` lower theorem.

Independently, Stage19 proves

\[
\boxed{N_2/M_2\to0}
\]

by its same-measure split-prime parity sieve. The true exponent remains unknown and the local-sieve saving is not multiplied with the half-power upper theorem.

### 6.6 Space diagonal after all three faces

`P subset M3` is the exact perfect-cuboid survival question:

\[
\frac{P(B)}{M_3(B)}.
\]

No global upper forcing this ratio to zero, no positive lower, and no nonexistence theorem is known. The exact finite census gives zero through `B=10^9` only.

```text
ENDPOINT_LITERAL_SURVIVAL_HOST=M3
ENDPOINT_LITERAL_SURVIVAL_TARGET=P
GLOBAL_ENDPOINT_SURVIVAL_COST=UNKNOWN
```

## 7. What the sixteen cells do and do not prove

The physical YES/NO classification is exhaustive:

```text
FACE_ab yes/no
FACE_ac yes/no
FACE_bc yes/no
SPACE yes/no
=> 2^4 = 16 exact physical Boolean cells
```

Therefore every primitive canonical cuboid under the cutoff belongs to exactly one physical condition cell.

This is **not** the same `64` as the degree-64 sign/Kummer cover found in 29-02ha.

The `16` records whether four arithmetic integrality predicates succeed. The `64` records geometric sign/square-root sheets of the full endpoint cover after passing to the seven-line square-root model and quotienting global sign.

```text
BOOLEAN_16_EQUALS_SIGN_COVER_64=false
BOOLEAN_TO_SIGN_TOWER_EXACT_ADAPTER_PROVED=false
```

`R29-KUM4` is now sharpened to the following 29-07 receiver:

```text
R29-KUM4 = PhysicalBooleanPredicateCellsToSignSubcoverLatticeExactAdapter
INPUT_HOST=U(B) plus exact face/space predicate masks
MUST_PROVE=common geometric host + map direction + rational-lift semantics + physical height + primitivity + canonical multiplicity
MAY_RETURN=FULL_EXACT_TOWER_BRIDGE | PARTIAL_PREDICATE_BRIDGE | GEOMETRIC_ONLY_BRIDGE_NO_POPULATION_TRANSFER | NO_CLEAN_BRIDGE
```

No outcome is prejudged here.

## 8. Backflow verdict

29-04 does not find a contradiction in the frozen Stage16–28 contracts. It clarifies their exact-mask semantics and supplies a new Stage29 host ledger.

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
R29_KUM4_CONDITIONAL_BACKFLOW_WATCH=true
OLD_STAGE_CONTRACT_REPAIR_PROVED_NECESSARY=false
```

If 29-07 later proves that a frozen old-stage contract itself must be extended or corrected, the conditional KUM4 backflow watch may activate. Merely proving a new crosswalk does not reopen an old stage.

## 9. Handoff to 29-05

29-05 should use this exact host/mask vocabulary to assign canonical route ownership and prevent double-charging the same arithmetic condition under multiple names.

Priority duplicate checks include:

```text
exact face predicate vs Pythagorean parametrization language
space predicate vs squareclass/Gaussian-norm language
third-face predicate vs K3 double-cover/local-blocker language
joint two-completion predicate vs V4/cross-character language
full endpoint predicate vs seven-line common-squareclass lifting language
```

```text
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM=29-05_DEPENDENCY_EQUIVALENCE_ROUTE_OWNERSHIP_AND_DOUBLE_CHARGE_LEDGER
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
