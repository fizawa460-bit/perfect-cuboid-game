def cleared_rhs(d:int, lam:int, T:int)->int:
    return d*(lam*T)**2


def audit_flags():
    return {'ar012_trigger':False,'moving_denominator_T':True}

if __name__=='__main__':
    print(audit_flags())
