import sys,os
src_c=open('p16/c_5905_0.sing').read().split('\n')
blk='\n'.join(src_c[59:72])   # lines 60..72: BL .. Z std (critical scheme off base locus and nodes)
tail=blk+'''
if (dim(Z) >= 2) { ideal Zc = std(radical(equidimMax(Z))); "CRITCURVE degree", mult(Zc);
  ideal ZcF = std(Zc + ideal(NN)); "CRITCURVE in this fibre: dim", dim(ZcF);
  def LZ = sat(Z, Zc); ideal Z4; if (typeof(LZ) == "list") { Z4 = LZ[1]; } else { Z4 = LZ; } Z = std(Z4); }
ideal ZF = std(Z + ideal(NN));
int lenF = mult(ZF); if (dim(ZF) <= 0) { lenF = 0; }
ideal ZFr = std(radical(ZF)); int radF = mult(ZFr); if (dim(ZFr) <= 0) { radF = 0; }
"FIBRE critical length", lenF, " distinct", radF, " dim", dim(ZF);
if (lenF == radF) { "FIBRE-CRIT-REDUCED"; } else { "FIBRE-CRIT-NONREDUCED"; }
quit;
'''
names=[]
for f in [l.strip() for l in open('cgk/ll') if l.strip()]:
    if not (os.path.basename(f).startswith('cg_') or os.path.basename(f).startswith('cd_')): continue
    s=open(f).read(); key='ideal B = std(S + ideal(NN));'
    if key not in s: print('nokey',f); continue
    n='z_'+os.path.basename(f)[:-5]
    open('czr/'+n+'.sing','w',newline='\n').write(s[:s.index(key)]+tail); names.append(n)
open('czr/jobs.txt','w',newline='\n').write('\n'.join(names)+'\n'); print(len(names))
