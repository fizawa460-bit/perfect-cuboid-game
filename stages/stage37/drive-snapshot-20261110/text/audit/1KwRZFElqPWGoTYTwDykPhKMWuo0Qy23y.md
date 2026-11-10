# Stage37 hostile audit — M3-T11-123
VERDICT=PASS_WITH_EXPLICIT_SCOPE_LIMITS
AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
No global counting credit; full genus2 Selmer set not computed.

1. Normalization: u=a/b reduced, F=b^2Q_u and G=N^3F(X/N), alpha=Ntheta. beta=Nm-nalpha=Nn(z-theta), hence [z-theta]=[Nn beta]. Restoring n is mandatory. No physical root/evaluation conflation.
2. Exact Wolfram computation: disc(F)=16a²N²Delta0³; disc(G)=16a²N⁸Delta0³; Norm(beta)=N³F_h; Norm(alpha(aN-balpha))=-a⁴N⁶(a²+2b²)². All four symbolic comparisons returned True. The sign and all N/b exponents were checked.
3. Independent integer verification: 182 primitive signed u values, 182 discriminant determinants, 1092 beta determinants, 182 gamma determinants and1962 good-prime support checks all PASS. Synthetic algebraic packets are not physical endpoint samples.
4. Good primes: p outside2aNDelta0 misses both discriminant and order index. G modulo p is squarefree and describes O_K locally. For n a unit, beta can occupy at most one degree-one prime abovep. Norm parity then forces even ideal valuation. For p|n, beta is a unit. This does not wrongly use total norm parity when multiple ideal factors might occur.
5. Universal witness: alpha is a unit outsideS. For p|b the second factor aN-balpha is a unit; otherwise its possible prime is unique of residue degreeone. Norm valuation is even. Primes dividing a²+2b² need no added bad support. gamma is nonzero, and lies in the coarse supported norm[-1] fiber without physical data.
6. Coarse fiber versus Selmer: H_u^- nonempty for all retainedu forbids only this coarse empty-fiber screening. No claim that gamma is locally compatible with the full genus2 physical cover, no full Selmer collapse, no norm-kernel triviality and no physical existence theorem.
7. Class-group bound: localized ideal exact sequence retains Cl(O_K,S)[2]; quotient2-rank bounds it byCl(K)[2]. Unit-square rank=r1+r2+|S_K|, at most4+4omega(2aNDelta0). No unjustified principal ideal, trivial class group, GRH or uniform subpower torsion assumption.
8. Height/measure: |2aNDelta0|<=100H5; order discriminant bound64,000,000H24 is only an upperbound. Original exact R<=B measure retained. No small-H assumption and no conversion from ambientu counts.
9. Counting: finite labels per fixedu cannot improve audited036 or control movingu. Different fields have different squareclass spaces. No independent probability, fixed-power gain or closure follows.
10. Dependencies remain scoped:105 physical norm,106 physical z and109 S4 complement;106/107 local selector firewalls,120 withdrawal,122 phi no-go and TI parked state retained. The current attack moves to the already-authorized theta backup; global S4 realization gate remains open.

REPLAY_FILES=verify_m3_t11_123.py; M3-T11-123-verification.json; M3-T11-123-symbolic-check.wl; M3-T11-123-symbolic-result.txt
REOPEN_ONLY=Normalization/ideal argument failure or genuinely new realized non-norm local-compatible cross-u information.
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false

