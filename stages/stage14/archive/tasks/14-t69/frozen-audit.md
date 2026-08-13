# Stage14-t69 frozen common-support profile

The deterministic audit on the inherited frozen family gives:

```text
reciprocal states                         560
invisible states                          419
mutually Cayley-private pairs               5
angular factorization checks              419
full Cayley largest-prime checks          419
common-support orientation checks           5

J values:                      5, 17, 65, 65, 75
J = H*gcd(D_i,D_j):                         1 pair
J > H*gcd(D_i,D_j):                         4 pairs
J = 1:                                      0 pairs
max J:                                     75
max extra common support:                  65
max observed noncanonical prime / ell:  47/229
```

Thus the tiny frozen sample contains extra noncanonical overlap in four of its five clean private pairs, while one pair has only the forced radial base.  This is diagnostic only.  It does **not** prove an asymptotic lower bound for `J`.

The synthetic square-scale guard in the frozen JSON has `J=1`, so the exact squareclass/private-largest-prime algebra by itself cannot justify assuming nontrivial overlap.  Any Stage14-t70 large/small-`J` argument must obtain its lower bound or counting gain from the physical height/reconstruction conditions, not from squareclass equality alone.
