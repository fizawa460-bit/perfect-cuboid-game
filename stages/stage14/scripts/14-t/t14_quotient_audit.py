from sympy import symbols, factor, simplify

t, r, x = symbols('t r x', nonzero=True)

B = 2*(1-t**2)/(1+t**2) - (1-r**2)**2/(t**2*(1+t**2)*r**2)
D = factor(B**2 - 4)
expected_D = factor((r**2-2*t*r-1)*(r**2+2*t*r-1)*(r**4+(4*t**4-2)*r**2+1)/(r**4*t**4*(1+t**2)**2))
assert simplify(D-expected_D) == 0

minus_B_minus_2 = factor(-B-2)
expected_second = factor((r**2-2*t*r-1)*(r**2+2*t*r-1)/(r**2*t**2*(1+t**2)))
assert simplify(minus_B_minus_2-expected_second) == 0

first_factor_x = factor((x-1)**2 - 4*t**2*x)
second_factor_x = factor(x**2 + (4*t**4-2)*x + 1)
quartic = factor(first_factor_x*second_factor_x)

print('D=', D)
print('-B-2=', minus_B_minus_2)
print('elliptic quotient quartic=', quartic)
print('OK')
