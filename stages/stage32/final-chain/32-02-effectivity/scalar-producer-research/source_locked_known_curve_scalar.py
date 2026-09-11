#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,json,math,sys
from pathlib import Path
from sympy import Matrix
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
RES=ROOT/"stages/stage32/residual-32-01-production"
S33=ROOT/"stages/stage33/33-07"
sys.path.insert(0,str(RES))
import hperp_integral_adapter as hp
from pairing_prefix_engine import INDLIST
BUNDLE=S33/"picard_base_rows_retained.py"
MARKING=S33/"stage32_picard_marking_retained.py"
LOCKS={RES/"hperp_integral_adapter.py":"fb1eb380ca786e42a6b00c5ef454b0e79fdba771",RES/"pairing_prefix_engine.py":"c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",BUNDLE:"82e4d450a1d852e34f6615440fb88a029c6e54eb",MARKING:"5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"}
def blob(p):
 raw=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def load_py_data(path,name):
 spec=importlib.util.spec_from_file_location(name,path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
 for key in ("DATA","RESULT","PAYLOAD","CERTIFICATE"):
  if hasattr(mod,key): return getattr(mod,key)
 raise ValueError("retained data export not found: "+str(path))
def load():
 for p,h in LOCKS.items():
  if blob(p)!=h: raise ValueError("source-lock drift: "+str(p.relative_to(ROOT)))
 bundle=load_py_data(BUNDLE,"s32_scalar_bundle"); marking=load_py_data(MARKING,"s32_scalar_marking")
 adapter=hp.HperpIntegralPairingAdapter.from_retained(marking,bundle)
 P=Matrix(adapter.pairing_matrix); G=Matrix(bundle["picard_gram_64x64"])
 Psel=P.extract([int(i)-1 for i in INDLIST],list(range(64)))
 q,degree,linear,caps,meta=hp._parse_hperp(marking["hperp_text"])
 return adapter,Psel,G,degree,meta
def produce_known_curve(label):
 adapter,Psel,G,degree,meta=load(); i=int(label)-1
 c=Matrix(adapter.class_coordinates_in_retained_basis).row(i).T
 y=Psel*c; d=int(degree[i]); C2=int((c.T*G*c)[0]); m=16//math.gcd(d,16)
 num=m*m*d*d-16*m*m*C2
 if num%16 or num<0: raise ValueError("known curve Hperp norm invalid")
 return {"schema":"STAGE32_32_02_SOURCE_LOCKED_KNOWN_CURVE_SCALAR_V1","known_curve_label":label,"row_id":"known-curve-regression","d":d,"m":m,"C2":C2,"negative_hperp_square_N":num//16,"selected64_pairings":[int(v) for v in y],"picard64_coordinates":[int(v) for v in c],"hperp_text_sha256":meta["hperp_text_sha256"],"source_blobs":{str(p.relative_to(ROOT)):h for p,h in LOCKS.items()},"credit":{"regression_only":True,"main":False,"full178":False,"effectivity_final":False,"merge":False}}
