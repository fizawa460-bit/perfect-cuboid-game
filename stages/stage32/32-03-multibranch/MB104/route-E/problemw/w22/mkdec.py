import re,sys
P=sys.argv[1]; s=open(f'slack0C_{P}.sing').read()
s='LIB "primdec.lib";\n'+s
out=[]
for l in s.split('\n'):
    m=re.search(r'Dx(\d+)\[',l)
    if m:
        l=re.sub(r'if \(dim\(Jc\)>0\) \{ ne\+\+; "NONEMPTY[^;]*;',
                 'if (dim(Jc)>0) { ne++; list PQ=minAssGTZ(Jc); for (int z=1;z<=size(PQ);z++) { ideal Qz=std(PQ[z]); "PRIME '+m.group(1)+'", mult(Qz), " ", string(Qz); kill Qz; } kill PQ;',l)
    out.append(l)
open(f'slack0C_dec_{P}.sing','w').write('\n'.join(out))
