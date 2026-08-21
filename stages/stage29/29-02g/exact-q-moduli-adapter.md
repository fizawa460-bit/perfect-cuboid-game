# Stage29-02g — audited exact Q-moduli adapter

```text
ROLE=EXACT_CONJUGATE_SELF_8_TORSION_LEVEL4_ADAPTER
STATUS=AUDITED_PASS_ON_NONCUSP_FINE_MODULI_LOCUS
```

Let `K=Q(i)` and let `sigma` be the nontrivial automorphism of `K/Q`.

Testa--Stoll Section 4 gives the exact arithmetic interpretation of a Q-rational endpoint point on the noncuspidal modular locus:

```text
P in Sbar(Q)
=>
E/K elliptic,
(P1,P2) a basis of E[4],
psi:E[8] -> E^sigma[8],
psi(P1)=P1^sigma,
psi(P2)=-P2^sigma.
```

The `X(8)` level structures are symplectic, so the induced 8-torsion correspondence is symplectic. The minus sign is load-bearing: if the level-4 basis has Weil pairing `i`, conjugation changes it to `-i`, and the sign on `P2^sigma` restores the symplectic pairing convention.

Thus

```text
R29-MOD1=ConjugateSelf8CongruenceWithLevel4QDescent
R29-MOD1A=ExactConjugateSelfLevel4ModuliAdapter
R29_MOD1A=DISCHARGED_GENERIC_MODULI_LOCUS
```

The source statement is exact for the modular datum, but cusp and extra-automorphism/stabilizer loci are intentionally kept separate in

```text
R29-MOD1D=CuspStabilizerAndPhysicalOpenRemoval.
```

The remaining defect receiver is interpreted with the audit repair from `torsion-descent-defect.md`:

```text
R29-MOD1B=AbstractK8ConjugacyClassification
R29-MOD1C=TwistedSigmaDescentActionAndArithmeticAnalysisOfK8Classes
```

## Important non-equivalences

```text
ordinary 8-congruence => endpoint point                 FALSE
E[8] ~= E^sigma[8] without level4 signs => endpoint    NOT PROVED
psi^sigma psi = 1 => E descends to Q                    FALSE IN GENERAL
four abstract K8 classes => four arithmetic strata      NOT YET PROVED
```

`psi` is an isomorphism of 8-torsion group schemes/Galois modules, not an elliptic-curve isomorphism `E -> E^sigma`.

```text
ELLIPTIC_CURVE_Q_DESCENT_INFERRED=false
ENDPOINT_RATIONAL_POINT_DECIDED=false
PERFECT_CUBOID_CONCLUSION=NONE
```
