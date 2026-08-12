def rank_one_from_endpoints(e1,e2,e3,e4):
    xp=(e3+e1)//2; yq=(e3-e1)//2
    yp=(e2+e4)//2; xq=(e2-e4)//2
    return xp*yq-xq*yp

def equal_norm_defect(e1,e2,e3,e4):
    return e1*e1+e2*e2-e3*e3-e4*e4
