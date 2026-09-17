#!/usr/bin/env python3
from __future__ import annotations

import importlib.util, json, tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
DIRECT=HERE/"run_full_hist_row.py"; BCHUNK=HERE/"run_full_hist_bchunk.py"; ASSEMBLER=HERE/"assemble_full_hist_row_from_bchunks.py"

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path); req(spec is not None and spec.loader is not None,"cannot load "+name); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    direct=load(DIRECT,"hpadj21_direct_eq"); bc=load(BCHUNK,"hpadj21_bchunk_eq"); asm=load(ASSEMBLER,"hpadj21_asm_eq")
    row_index=0; expected=direct.compute_row(row_index); h=int(expected["row"]["d"])//2
    with tempfile.TemporaryDirectory() as td:
        root=Path(td); paths=[]
        for start in range(0,h+1,2):
            stop=min(h,start+1); d=bc.compute_chunk(row_index,start,stop); p=root/f"hpadj21-bchunk-{row_index}-{start}-{stop}.json"; p.write_text(json.dumps(d,sort_keys=True,separators=(",",":"))+"\n"); paths.append(p)
        got=asm.assemble(row_index,paths)
    req(got==expected,"assembled b-chunks differ from direct row certificate")
    print(json.dumps({"schema":"STAGE32EX5_HPADJ21_BCHUNK_EQUIVALENCE_V1","status":"EXACT_BOUNDED_EQUIVALENCE_PASS","row_index":row_index,"chunk_count":len(paths),"canonical":got["canonical_sha256_without_this_field"],"credit":{"stage32_main_credit":False,"full178_completion_credit":False,"merge_authorized":False}},sort_keys=True,separators=(",",":")))

if __name__=="__main__": main()
