from fractions import Fraction

checks = 0
for n in range(1, 65):
    for k in range(n + 1):
        rho = Fraction(k, n)
        vals = [Fraction(1,1)-rho]*k + [-rho]*(n-k)
        assert sum(vals, Fraction(0,1)) == 0
        e2 = sum(v*v for v in vals) / n
        assert e2 == rho*(1-rho)
        checks += 1
print({'principal_centered_checks': checks, 'status': 'ok'})
