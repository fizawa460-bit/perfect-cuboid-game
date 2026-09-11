#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,json,math,sys,types
from pathlib import Path
from sympy import Matrix
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
RES=ROOT/"stages/stage32/residual-32-01-production"
S33=ROOT/"stages/stage33/33-07"
BUNDLE=S33/"picard_base_rows_retained.py"
MARKING=S33/"stage32_picard_marking_retained.py"
LOCKS={RES/"hperp_integral_adapter.py":"fb1eb380ca786e42a6b00c5ef454b0e79fdba771",RES/"pairing_prefix_engine.py":"c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",BUNDLE:"82e4d450a1d852e34f6615440fb88a029c6e54eb",MARKING:"5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"}
def blob(p):
 raw=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def load_py_data(mod):
 if hasattr(mod,"load"):
  return mod.load()
 for key in ("DATA","RESULT","CERTIFICATE"):
  if hasattr(mod,key): return getattr(mod,key)
 raise ValueError("retained data export not found")
def load():
 # Snapshot and validate EVERY repository dependency before executing any of it.
 # Execute the verified bytes, never a cached module or a second file read.
 sources={p:p.read_bytes() for p in LOCKS}
 for p,h in LOCKS.items():
  raw=sources[p]
  if hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()!=h:
   raise ValueError("source-lock drift: "+str(p))
 names=[("pairing_prefix_engine",RES/"pairing_prefix_engine.py"),
        ("hperp_integral_adapter",RES/"hperp_integral_adapter.py"),
        ("s32_scalar_bundle",BUNDLE),("s32_scalar_marking",MARKING)]
 saved={name:sys.modules.get(name) for name,_ in names}; loaded={}
 try:
  for name,p in names:
   mod=types.ModuleType(name); mod.__file__=str(p)
   sys.modules[name]=mod; loaded[name]=mod
   exec(compile(sources[p],str(p),"exec"),mod.__dict__)
 finally:
  for name,old in saved.items():
   if old is None: sys.modules.pop(name,None)
   else: sys.modules[name]=old
 hp=loaded["hperp_integral_adapter"]; INDLIST=loaded["pairing_prefix_engine"].INDLIST
 bundle=load_py_data(loaded["s32_scalar_bundle"]); marking=load_py_data(loaded["s32_scalar_marking"])
 adapter=hp.HperpIntegralPairingAdapter.from_retained(marking,bundle)
 P=Matrix(adapter.pairing_matrix); G=Matrix(bundle["picard_gram_64x64"])
 Psel=P.extract([int(i)-1 for i in INDLIST],list(range(64)))
 q,degree,linear,caps,meta=hp._parse_hperp(marking["hperp_text"])
 return adapter,Psel,G,degree,meta
def produce_known_curve(label):
 from picard_pairing_scalar_producer import produce
 if type(label) is not int or not 1<=label<=140: raise ValueError("known curve label must be 1..140")
 adapter,Psel,G,degree,meta=load(); i=int(label)-1
 c=Matrix(adapter.class_coordinates_in_retained_basis).row(i).T
 y=Psel*c; d=int(degree[i]); C2=int((c.T*G*c)[0]); m=16//math.gcd(d,16)
 num=m*m*d*d-16*m*m*C2
 if num%16 or num<0: raise ValueError("known curve Hperp norm invalid")
 locks={str(p.relative_to(ROOT)):h for p,h in LOCKS.items()}
 plain=lambda A:[[int(v) for v in row] for row in A.tolist()]
 record=produce("known-curve-regression",d,"known-curve:"+str(label),[int(v) for v in y],plain(Psel),plain(G),locks)
 record.update(known_curve_label=label,hperp_text_sha256=meta["hperp_text_sha256"],source_blobs=locks)
 record["credit"]={"regression_only":True,"main":False,"full178":False,"effectivity_final":False,"merge":False}
 return record
