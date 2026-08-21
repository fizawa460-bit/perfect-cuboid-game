# Stage29-02g — exact Q-moduli adapter

```text
ROLE=EXACT_CONJUGATE_SELF_8_TORSION_LEVEL4_ADAPTER
STATUS=PASS_CANDIDATE_PENDING_FRESH_AUDIT
```

Let `K=Q(i)` and let `sigma` be complex conjugation.

Testa--Stoll Section 4 gives the exact arithmetic interpretation of a rational point of the endpoint surface:

```text
P in Sbar(Q)
=>
E/K elliptic,
(P1,P2) a basis of E[4],
psi:E[8] -> E^sigma[8],
psi(P1)=P1^sigma,
psi(P2)=-P2^sigma.
```

The level structures on `X(8)` are symplectic, so the induced 8-torsion correspondence is the symplectic congruence inherited from the diagonal quotient.

The signs in the level-4 condition are not cosmetic. If the basis is normalized so that the Weil pairing of `(P1,P2)` is `i`, conjugation sends that value to `-i`; changing `P2^sigma` to `-P2^sigma` restores the pairing. Thus the displayed sign pattern is exactly compatible with the symplectic level structure.

This yields the exact Stage29 modular receiver

```text
R29-MOD1=ConjugateSelf8CongruenceWithLevel4QDescent
```

and splits it into bounded subreceivers

```text
R29-MOD1A=ExactConjugateSelfLevel4ModuliAdapter
R29-MOD1B=EightTorsionConjugationDefectStratification
R29-MOD1C=ArithmeticAnalysisOfTheFourDefectOrbits
R29-MOD1D=CuspStabilizerAndPhysicalOpenRemoval
```

`R29-MOD1A` is the structural statement recorded here. The arithmetic point analysis is not solved.

## Important non-equivalences

The following implications are forbidden:

```text
ordinary 8-congruence => endpoint point                 FALSE
E[8] ~= E^sigma[8] without level4 signs => endpoint    NOT PROVED
psi^sigma psi = 1 => E descends to Q                    FALSE IN GENERAL
```

The last firewall matters because `psi` is an isomorphism of 8-torsion group schemes/Galois modules, not an isomorphism of elliptic curves.

```text
R29_MOD1A=PASS_CANDIDATE
ELLIPTIC_CURVE_Q_DESCENT_INFERRED=false
ENDPOINT_RATIONAL_POINT_DECIDED=false
```
