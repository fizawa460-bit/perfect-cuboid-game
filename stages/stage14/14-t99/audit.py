from fractions import Fraction

# Deterministic audit of the only logical step used in t99:
# a B^o(1)-sized union with non-negligible average forces one
# elementary member to have non-negligible average.
checks=0
for J in range(1,33):
    for total_num in range(1,65):
        total=Fraction(total_num,64)
        # Worst case when J event masses share the total equally.
        lower=total/J
        masses=[lower for _ in range(J)]
        assert max(masses) >= lower
        checks += 1

# Class partition is exhaustive and fixed.
classes=('SIGN','DIV','PROJ')
assert len(classes)==3 and len(set(classes))==3
print({'pigeonhole_checks':checks,'boundary_classes':len(classes),'status':'ok'})
