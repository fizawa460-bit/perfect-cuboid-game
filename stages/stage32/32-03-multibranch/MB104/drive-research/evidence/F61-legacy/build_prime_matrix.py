#!/usr/bin/env python3
import argparse
from pathlib import Path
import build_f61_matrix as b

p=argparse.ArgumentParser();p.add_argument('prime',type=int);p.add_argument('imaginary_root',type=int);p.add_argument('destination',type=Path)
a=p.parse_args();a.destination.mkdir(parents=True,exist_ok=True)
b.P=a.prime;b.II=a.imaginary_root;b.SQRT2=next(x for x in range(a.prime) if x*x%a.prime==2);b.ROOT=a.destination
b.main()
