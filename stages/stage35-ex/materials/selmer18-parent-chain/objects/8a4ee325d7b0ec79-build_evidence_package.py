from pathlib import Path
import json,hashlib,shutil,zipfile
R=Path(__file__).resolve().parent;P=R/'package'
if P.exists():shutil.rmtree(P)
P.mkdir()
def cp(src,dest):
 dest=P/dest;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
for name in['STAGE35EX_R3_07_GLOBAL_RESIDUAL_TWO_DIRECTIONS_20261105.md','README.md','requirements.txt','verify_manifest.py','build_evidence_package.py']:
 cp(R/name,name)
for f in sorted((R/'math').rglob('*')):
 if f.is_file()and'__pycache__'not in f.parts and f.suffix!='.pyc':cp(f,f.relative_to(R))
for name in['search_quadratic_divisors.py','QUADRATIC_DIVISOR_SEARCH.json','search_small_divisors.py','SMALL_DIVISOR_SEARCH.json','search_rational_graphs.py','RATIONAL_GRAPH_SEARCH.json','RATIONAL_POINT_SEARCH.json']:
 cp(R/'exploratory'/name,Path('exploratory')/name)
parents=[('ROW359_ORIGINAL_TRUE_SELMER14_EVIDENCE.zip',R.parent/'r307_next_20261105/STAGE35EX_R3_07_THREE_NEW_UNITS_TRUE_SELMER14_EVIDENCE_20261105.zip'),('ROW361_ORIGINAL_KNOWN7_LOG_FRAME_EVIDENCE.zip',R.parent/'r307_logs_20261105/STAGE35EX_R3_07_KNOWN7_P163_LOG_FRAME_EVIDENCE_20261105.zip')]
expected=['a6022eb5e0e4c89a5f760c326cd72e37b49777efb18565538681cf3b842b2cf6','0bdef991315be807dece4a2ed5630ecd37d8fb71576610ca5ad4b6713b4a86b0']
for(name,f),h in zip(parents,expected):
 if hashlib.sha256(f.read_bytes()).hexdigest()!=h:raise RuntimeError('original parent bytes changed')
 cp(f,Path('parent_evidence')/name)
for name in['build_record_updates.py','verify_writeback.py','writeback-validation.json']:
 cp(R/name,Path('record_updates')/name)
for folder in['sources','updates']:
 for f in sorted((R/folder).glob('*.json')):cp(f,Path('record_updates')/folder/f.name)
manifest={str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest()for f in sorted(P.rglob('*'))if f.is_file()}
(P/'MANIFEST_SHA256.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
dest=R/'STAGE35EX_R3_07_GLOBAL_RESIDUAL_TWO_DIRECTIONS_EVIDENCE_20261105.zip'
with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9)as z:
 for f in sorted(P.rglob('*')):
  if f.is_file():z.write(f,str(f.relative_to(P)))
result={'package_files_in_manifest':len(manifest),'zip_entries':len(manifest)+1,'zip_bytes':dest.stat().st_size,'zip_SHA256':hashlib.sha256(dest.read_bytes()).hexdigest(),'report_SHA256':hashlib.sha256((R/'STAGE35EX_R3_07_GLOBAL_RESIDUAL_TWO_DIRECTIONS_20261105.md').read_bytes()).hexdigest(),'parent_original_SHA256':expected}
(R/'package-validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
