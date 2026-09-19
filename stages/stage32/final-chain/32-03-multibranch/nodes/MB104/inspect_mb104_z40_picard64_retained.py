#!/usr/bin/env python3
"""Bounded structural introspection for the retained Stage32 Picard64 payload.

Prints keys, scalar metadata, and array dimensions only. Never prints retained
matrix/vector payload entries.
"""
from __future__ import annotations
import hashlib, importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[6]
MARKING=ROOT/"stages/stage33/33-07/stage32_picard_marking_retained.py"
HELPER=ROOT/"stages/stage33/33-07/stoll_cuboid_source.py"
EXPECTED_MARKING_BLOB="5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"
EXPECTED_HELPER_BLOB="010db3767b8f932c71ac5722b50ccb64a8c79f9d"

def git_blob_sha(path: Path) -> str:
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def shape_only(x, depth=0):
    if isinstance(x, dict):
        if depth >= 2:
            return {"type":"dict","keys":sorted(map(str,x.keys())),"len":len(x)}
        return {"type":"dict","keys":sorted(map(str,x.keys())),
                "children":{str(k):shape_only(v,depth+1) for k,v in x.items()}}
    if isinstance(x, (list,tuple)):
        out={"type":type(x).__name__,"len":len(x)}
        if x and all(isinstance(r,(list,tuple)) for r in x):
            lens={len(r) for r in x}
            if len(lens)==1:
                out["matrix_shape"]=[len(x),next(iter(lens))]
        if depth < 2 and x:
            # Structural description of the first element only; never values.
            out["element_structure"]=shape_only(x[0],depth+1)
        return out
    return {"type":type(x).__name__}

def main():
    assert git_blob_sha(MARKING)==EXPECTED_MARKING_BLOB, "marking blob lock mismatch"
    assert git_blob_sha(HELPER)==EXPECTED_HELPER_BLOB, "helper blob lock mismatch"
    spec=importlib.util.spec_from_file_location("stage32_picard_marking_retained",MARKING)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    data=mod.load()
    out={
      "success":True,
      "marking_blob":EXPECTED_MARKING_BLOB,
      "helper_blob":EXPECTED_HELPER_BLOB,
      "top_level_keys":sorted(data.keys()),
      "structure":shape_only(data),
    }
    print(json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
