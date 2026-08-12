def endpoint_cells(kxp,kxq,kyp,kyq,X,Y,P,Q):
    ksw=kxq*kyp; kag=kxp*kyq
    A=kxp*X*P; B=kyq*Y*Q; C=kxq*X*Q; D=kyp*Y*P
    return {
      'E1':ksw*(A*A-B*B), 'E3':ksw*(A*A+B*B),
      'E2':kag*(C*C+D*D), 'E4':kag*(D*D-C*C),
      'A':A,'B':B,'C':C,'D':D
    }
