from fractions import Fraction

checks=0
for n in range(2,17):
    for k in range(n+1):
        vals=[1 if i<k else 0 for i in range(n)]
        mu=Fraction(sum(vals),n)
        centered=[Fraction(v)-mu for v in vals]
        assert sum(centered)==0
        for v,c in zip(vals,centered):
            assert Fraction(v)==mu+c
        checks += n
print({'principal_centered_checks':checks,'status':'ok'})
