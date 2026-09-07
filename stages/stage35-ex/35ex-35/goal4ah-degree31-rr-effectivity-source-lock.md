# Stage35-EX Goal4AH — degree-31 Riemann–Roch effectivity source lock

## Scope

This note source-locks only the bounded statement that the first Goal4AG survivor at homogeneous degree 31 has a **Q-defined effective residual divisor**. It does **not** materialize a rational function `F_B`, does not prove that the desired degree-31 numerator/denominator pair has been explicitly constructed, and gives no local-evaluation, Brauer–Manin, E1, or Stage35 closure credit.

## Parent exact arithmetic

Parent artifact:

- `stages/stage35-ex/35ex-35/goal4ag-bounded-principalization-degree-exclusion.json`
- canonical SHA256 `9db1f8abc453d50f6849af1236c89e9bf0db5ffbfd26199853ebe43a9f157f45`

Goal4AG fixed-component stripping proves degrees 25 through 30 noneffective. At degree 31, after 325 forced component subtractions, the retained class `D` has

- `H.D = 96`,
- `D^2 = 212`,
- nonnegative intersection with every retained 140 irreducible curve.

The exact Goal4AH local replay is

- head `86f1a13c042357a8a727dce45209294ce3c0cb5d`,
- workflow run `34078793811`,
- job `101610034252`,
- diagnostic `stages/stage35-ex/diagnose_stage35_ex_35_goal4ah_degree31_rr.py`,
- diagnostic git blob `d797ee20d7ee6f81f159249b61c492230d8eb306`.

The replay checks, separately for the two retained Galois generators `cc` and `ct`, that all of the following are invariant:

1. the 69-support formal class-B target;
2. its positive divisor part `P`;
3. its negative divisor part `N`;
4. the complete 325-step forced-component multiplicity vector;
5. the hyperplane class `H`;
6. the positive Picard class `P_c`;
7. the final stripped degree-31 residual class `D`.

Hence both the stripping data and the resulting divisor/line-bundle data descend to Q; this is stronger than checking only geometric Picard-class invariance.

## Surface geometry source lock

Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, arXiv:1009.0388, Lemma 3 and its immediate corollaries state that the canonical model `Sbar` is a geometrically integral complete intersection of multidegree `(2,2,2,2)` in `P^6` with 48 isolated `A_1` singularities; it is Cohen–Macaulay, Gorenstein, normal and projectively normal. For the minimal desingularization `b:S->Sbar`, they state

- `O_S(K_S) ~= b^* O_Sbar(1)`, so the pulled-back hyperplane class is `K_S`;
- `K_S^2 = 16`;
- `chi(O_S) = 8`;
- `p_g(S)=7`, `q(S)=0`;
- the canonical class is big and nef.

The pinned computational geometry remains MichaelStollBayreuth/Verification commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/cuboids.magma`, git blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

## Exact Riemann–Roch deduction

On the smooth surface `S`, Riemann–Roch gives

`chi(O_S(D)) = chi(O_S) + (D.(D-K_S))/2`.

Using the exact retained values

- `chi(O_S)=8`,
- `D^2=212`,
- `K_S.D = H.D = 96`,

we obtain

`chi(O_S(D)) = 8 + (212-96)/2 = 66`.

Also

`H.(K_S-D) = H^2 - H.D = 16-96 = -80`.

Because `H=K_S` is nef, an effective divisor cannot have negative intersection with `H`; therefore `K_S-D` is not effective. By Serre duality,

`h^2(O_S(D)) = h^0(O_S(K_S-D)) = 0`.

Thus

`h^0(O_S(D)) - h^1(O_S(D)) = 66`,

and in particular

`h^0(O_S(D)) >= 66 > 0`.

Since `D` is Q-defined by the exact Galois-invariant divisor data above, this gives a Q-rational nonzero section and hence a Q-defined effective divisor in the class `D`. Re-attaching the Q-defined forced effective components proves that the original degree-31 residual is effective over Q as well.

## Remote Magma diagnostic boundary

The earlier strict-divisor `IsCartier`/`IsPrincipal` route produced blank calculator output. A bounded raw-XML diagnostic fixed the cause exactly:

- head `cad03e972ecdb7e3452ec7149494b0ca1590b105`,
- run `34078576624`, job `101609424024`, SUCCESS,
- response: `The Magma calculator is temporarily disabled due to electrical work in the building.`

Therefore those prior failures are **external infrastructure failures only**. They give no negative mathematical information about Cartierness or principality and are not used in the Riemann–Roch proof above.

## Firewall

The following remain unproved/unmaterialized:

- existence of an explicitly source-locked degree-31 homogeneous numerator/denominator pair realizing the class-B target;
- literal coefficients of `F_B`;
- global non-principality or all-degree exhaustion;
- full algebraic Brauer group of the open receiver;
- local evaluations;
- verticality;
- a Brauer–Manin obstruction;
- E1;
- `R29-PESCH-E1` or `R29-FIB2` closure;
- Stage35 closure;
- any perfect-cuboid existence or nonexistence theorem.

The next legal leaf is therefore degree-31 homogeneous principalization existence / literal section materialization, not local evaluation.