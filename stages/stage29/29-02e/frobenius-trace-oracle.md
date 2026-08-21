# Stage29-02e — exact good-prime endpoint Frobenius oracle

```text
ROLE=ENDPOINT_FINITE_FIELD_TRACE_ORACLE
STATUS=DERIVED_SUBMISSION_PENDING_FRESH_AUDIT
```

Let `p` be a good odd prime and `ell != p`. Write `a_p(hN)` for the `p`-th Fourier coefficient / Frobenius trace of the rational weight-3 newform of level `N in {8,16,32}` and

```text
chi_-1(p)=chi_{Q(i)}(p),
chi_-2(p)=chi_{Q(sqrt(-2))}(p),
chi_2(p)=chi_{Q(sqrt(2))}(p).
```

Horie--Yamauchi Theorem 1.1 gives the semisimple `H2(Sbar)` factorization

```text
h16^3 + h32 + h8^3
+ 10 Tate-trivial characters
+ 2 chi_-1 Tate characters
+ 1 chi_-2 Tate character
+ 3 chi_2 Tate characters.
```

Therefore

```text
T_Sbar(p)
 = 3 a_p(h16) + a_p(h32) + 3 a_p(h8)
   + p*(10 + 2 chi_-1(p) + chi_-2(p) + 3 chi_2(p)).
```

Since `H1=H3=0` in the relevant proper model convention,

```text
#Sbar(F_p)=1+p^2+T_Sbar(p).
```

For the smooth resolution, the 48 exceptional curves are represented in Theorem 1.1 by 24 trivial Tate characters and 24 `chi_-1` Tate characters, so

```text
T_S(p)=T_Sbar(p)+24p*(1+chi_-1(p)),
#S(F_p)=#Sbar(F_p)+24p*(1+chi_-1(p)).
```

This is an exact local regression oracle at good primes. It is not a count of rational perfect cuboids over `Q` and is not multiplied into a physical-height Euler product.

```text
ENDPOINT_GOOD_PRIME_TRACE_ORACLE=PASS_CANDIDATE
BAD_PRIME_ADAPTER_REQUIRED=true
PHYSICAL_OPEN_BOUNDARY_ADAPTER_REQUIRED=true
GLOBAL_Q_POINT_CONCLUSION=NONE
```
