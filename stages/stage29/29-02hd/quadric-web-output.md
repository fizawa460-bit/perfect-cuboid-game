# Exact quadric-web checker output

Command:

```text
python stages/stage29/29-02hd/quadric_web_check.py
```

Expected / independently replayed output:

```text
DISCRIMINANT_FACTORS=7
det ~ t1*t2*t3*t4*(t1+t3+t4)*(t1+t2+t4)*(t2+t3+t4)
DEPENDENT_HYPERPLANE_TRIPLES=0
RANK_LE_4_LOCUS_POSITIVE_DIMENSIONAL=false
RANK_LE_4_PROJECTIVE_POINTS=17
RANK_LE_3_POINTS=6
rank 3 point (0, 0, 1, -1) zero_coefficients B3,B1,A1,A3
rank 3 point (0, 0, 1, 0) zero_coefficients B3,B1,C,A2
rank 3 point (0, 1, 0, -1) zero_coefficients B3,B2,A2,A3
rank 3 point (0, 1, 0, 0) zero_coefficients B3,B2,C,A1
rank 3 point (1, 0, 0, -1) zero_coefficients B1,B2,A1,A2
rank 3 point (1, 0, 0, 0) zero_coefficients B1,B2,C,A3
ADLER_VAN_MOERBEKE_RANK4_CURVE_TRIGGER=false
PASS
```

Interpretation firewall:
- the four-quadric web has an exact reducible discriminant of seven planes in parameter `P3`;
- the rank-<=4 locus is finite, not a rank-4 curve;
- therefore the special Adler–van Moerbeke Abelian-surface trigger screened here is absent;
- the six rank-3 points mirror existing special combinatorics but no new rational-point obstruction is inferred.
