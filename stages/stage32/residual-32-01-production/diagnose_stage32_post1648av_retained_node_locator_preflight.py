#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ST33 = ROOT / "stages" / "stage33" / "33-07"
MATCH = re.compile(r"node|sing|exception|label|curve|coord|equat|name|point", re.I)
TEXT_MATCH = re.compile(r"node|singular|exceptional|curve|label", re.I)


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def describe(v):
    if isinstance(v, dict):
        return {"type":"dict","len":len(v),"keys":sorted(map(str,v.keys()))[:80]}
    if isinstance(v, (list,tuple)):
        out={"type":type(v).__name__,"len":len(v)}
        if len(v)<=16 and all(isinstance(x,(str,int,float,bool,type(None))) for x in v):
            out["value"]=list(v)
        return out
    if isinstance(v, (str,int,float,bool,type(None))):
        s=v if not isinstance(v,str) or len(v)<=240 else v[:240]+"..."
        return {"type":type(v).__name__,"value":s}
    return {"type":type(v).__name__}


def walk(obj, path="", depth=0, out=None):
    if out is None: out=[]
    if depth>3 or len(out)>=120: return out
    if isinstance(obj,dict):
        for k,v in obj.items():
            p=f"{path}.{k}" if path else str(k)
            if MATCH.search(str(k)):
                out.append({"path":p,"summary":describe(v)})
                if len(out)>=120: break
            if depth<3 and isinstance(v,dict):
                walk(v,p,depth+1,out)
    return out


def bounded_text_hits(text: str):
    hits=[]
    for i,line in enumerate(text.splitlines(),1):
        if TEXT_MATCH.search(line):
            hits.append({"line":i,"text":line[:300]})
            if len(hits)>=40: break
    return {"line_count":len(text.splitlines()),"matching_line_count_bounded":len(hits),"hits":hits}


def main():
    marking=load_retained(ST33/"stage32_picard_marking_retained.py","s32_av_marking")
    bundle=load_retained(ST33/"picard_base_rows_retained.py","s32_av_bundle")
    out={
      "mode":"SCRATCH_POST1648AV_RETAINED_NODE_LOCATOR_PREFLIGHT_V2",
      "marking_top":describe(marking),
      "bundle_top":describe(bundle),
      "marking_matching_paths":walk(marking),
      "bundle_matching_paths":walk(bundle),
      "hperp_semantic_locator_scan":bounded_text_hits(str(marking.get("hperp_text",""))),
      "firewalls":{"retained_payload_emitted":False,"scratch_only":True}
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__": main()
