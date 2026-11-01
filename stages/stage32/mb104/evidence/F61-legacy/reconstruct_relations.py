#!/usr/bin/env python3
"""CRT is only a discovery step: all reconstructed relations must be
checked against characteristic-zero entries before being used as proof.
"""
from pathlib import Path
from fractions import Fraction
from math import isqrt
import subprocess,json
from array import array

ROOT=Path(__file__).resolve().parent
def rational_reconstruct(a,m):
    a%=m
    if a==0:return Fraction(0)
    bound=isqrt(m//2);r0,r1=m,a;t0,t1=0,1
    while abs(r1)>bound:
        q=r0//r1;r0,r1=r1,r0-q*r1;t0,t1=t1,t0-q*t1
    if t1 and abs(t1)<=bound and (r1-a*t1)%m==0:
        return Fraction(r1,t1)
    raise ValueError('insufficient modulus')
def main():
    state=ROOT/'crtstate.json'
    if state.exists():
        old=json.loads(state.read_text());modulus=old['modulus'];values=old['values'];expected_pivots=old['pivots'];done=old['primes']
    else:
        modulus=1;values=[0]*(4*896*2);expected_pivots=None;done=[]
    for p in (41,73,89,97,113,137,193,233,241,257,281,313,337,353,401,409,433,449,457,521,569,577,593,601,617,641,673):
        if p in done:continue
        ii=next(x for x in range(p) if x*x%p==p-1)
        arrays=[]
        for i in (ii,p-ii):
            dest=ROOT/f'crt_p{p}_i{i}'
            subprocess.run(['python',str(ROOT/'build_prime_matrix.py'),str(p),str(i),str(dest)],check=True,capture_output=True)
            subprocess.run([str(ROOT/'left_prime'),str(dest),str(p)],check=True,capture_output=True)
            lines=(dest/'canonical_left.txt').read_text().splitlines()
            rank=int(lines[0]);pivots=[int(x) for x in lines[1].split()]
            if rank!=892 or (expected_pivots is not None and pivots!=expected_pivots):
                raise RuntimeError(f'bad reduction: p={p}, rank={rank}, pivots={pivots}')
            expected_pivots=pivots
            decoded=array('H');decoded.frombytes((dest/'canonical_left.bin').read_bytes());arrays.append(decoded)
        residues=[]
        for x,y in zip(*arrays):
            residues.extend(((x+y)*pow(2,-1,p)%p,(x-y)*pow(2*ii,-1,p)%p))
        for k,residue in enumerate(residues):values[k]+=modulus*((residue-values[k])*pow(modulus,-1,p)%p)
        modulus*=p
        done.append(p);state.write_text(json.dumps({'modulus':modulus,'values':values,'pivots':expected_pivots,'primes':done}))
        success=True;reconstruction=[]
        for value in values:
            try:reconstruction.append(str(rational_reconstruct(value,modulus)))
            except ValueError:success=False;break
        print(json.dumps({'prime':p,'modulus_bits':modulus.bit_length(),'all_reconstructed':success,'first_unreconstructed':None if success else len(reconstruction)}),flush=True)
        if success:
            data={'field':'Q(i)','basis':['1','i'],'pivots':expected_pivots,'modulus':modulus,'coefficients':reconstruction}
            (ROOT/f'relations_candidate_{modulus.bit_length()}.json').write_text(json.dumps(data,indent=2)+'\n')
            break
    print('Discovery finished; exact verification required.')
if __name__=='__main__':main()
