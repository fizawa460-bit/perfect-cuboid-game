Stage35EX C35-08 — independent Coleman p=3 trace certificate

Contains 3 independent Python scripts and the exact rational Mumford representatives
E26=26D2, F8=8D2+T0 (previously confirmed by exact Cantor arithmetic).
No Magma/PARI and no GitHub access. Requires Python 3 only.

Execute:
 python c35_08_independent_disk.py

Independently computes and checks:
 log(D2)/3 modulo 729 = [56,164,310]
 Lambda(R1)/3 modulo 729 = [503,268,626]
 normalized annihilator polynomials A and B modulo 243, with root residues 106 and 187.
Each local trace is computed in a quadratic algebra WITHOUT the original script's
sigma, conjugate sqrt(-1) selection, or its chabauty helpers.
Exact Mumford U|V^2-ft verified in each script.

Parameter stability matrix (all 12 pass):
 PADIC_PREC in {14,17,19,24}; SERIES_K in {16,24,32}
Default: PADIC_PREC=19, SERIES_K=32
Strong error bound uses 3^19 input modulus; divisions by 3^k consume at
most 8 digits in unramified quadratic evaluation, at most 6 digits in
ramified evaluation, leaving >7 digits for the required absolute p^7.
For all omitted Taylor terms after degree 16: infinity e>=17, Q9 pair n>=17
v_3>=n+1-v_3(n+1); Weierstrass y^2 in 3*order and n>=17
v_3>=n-v_3(2n+1). All exceed 7.
For A/B normalized tail coefficients m>=7, v3 >=m-1-v3(m) >=5.

This is an independently checked *p-adic arithmetic/analytic* certificate
conditional on the exact Jacobian divisor identities and rank J3(Q)=1;
full C35-03 p2 Kummer completeness and source adapter remain HOLD.
