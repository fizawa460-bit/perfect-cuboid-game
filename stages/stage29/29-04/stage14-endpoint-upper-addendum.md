# Stage29-04 targeted theorem-surface addendum — Stage14 endpoint upper bound

```text
ADDENDUM_KIND=TARGETED_POST_AUDIT_THEOREM_SURFACE_REPAIR
DISCOVERED_BY=Stage29_GAP_SCAN_B_PR1316
CHANGES_29_04_AUDIT_HISTORY=false
STAGE14_ENDPOINT_COROLLARY=VALID_MISSED_COROLLARY
```

Audited Stage29-04 correctly defined

```text
U(B)={0<a<b<c, gcd(a,b,c)=1, R=sqrt(a^2+b^2+c^2)<=B}
P(B)=#(E3 intersect S),
```

but its theorem-surface provenance listed only finite evidence `P(B)=0` through the certified census cutoff and did not import the following immediate Stage14 consequence.

Stage14 works on the same primitive canonical endpoint objects once `S` holds. Its integral space diagonal is exactly `d=R`, so its cutoff `d<=B` is identical to the Stage29 endpoint cutoff. Stage14 Lemma 3.1, Lemma 3.2 and Proposition 3.6 give

```text
E(B)=N_2(B)+3T(B),
E(B)<<V(B)B^o(1),
V(B)<<B^(1/2+o(1)),
```

hence

```text
P(B)=T(B)<<B^(1/2+o(1)).
```

Epsilon form:

```text
for every epsilon>0,
P(B)=T(B)<<_epsilon B^(1/2+epsilon).
```

This supplements the Stage29-04 theorem surface. It does not change the statement that `P/M3` has no certified asymptotic scale: an upper bound on `P` alone supplies neither a matching lower bound nor an asymptotic for that ratio.

It also does not alter the finite `P=0` evidence and makes no perfect-cuboid existence/nonexistence claim.
