import itertools, numpy as np
exec(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'t01_mirror.py')).read().split("Os=[[z")[0])
Os=[[z for z,_ in m[2]] for m in maps]
# maps 0..3: critical values {0,inf,1,-1}; parameter k = roots of 27k^4-54k^3+36k^2-6k-1
N=mob3(Bg[0],Bg[1],Bg[2]); z=ap(N,Bg[3]); print("z =",np.round(z,8))
H=np.polysub(np.polymul([1,0],np.polymul([3,-2],np.polymul([3,-2],[3,-2]))),z*np.array([2,-1]))
ks=np.roots(H); print("k:",np.round(ks,6))
print("same class as map 0:",[setequiv(Os[0],Os[i]) for i in range(4)])
s3=3**0.5
# candidate exact roots over Q(sqrt3, i)
print("(3+s3)/6 =",(3+s3)/6,"(3-s3)/6 =",(3-s3)/6, " sum of real pair/2 =",sum(k.real for k in ks if abs(k.imag)<1e-9)/2)
print("product real pair",np.prod([k.real for k in ks if abs(k.imag)<1e-9])," product complex pair",np.prod([k for k in ks if abs(k.imag)>1e-9]))
