import sympy as s
m,n,r,t=s.symbols('m n r t')
raw=(4*m*n*r*t)**2+(2*r*t*(m*m-n*n))**2+(2*m*n*(r*r-t*t))**2
assert s.factor(raw)==4*(m*m*r*r+n*n*t*t)*(m*m*t*t+n*n*r*r)
