import json
from pathlib import Path

BATCH_ID='SR-BATCH-STAGE14_15_DEEP_CORPUS-23-R01'
TASK_ID='SR-CENSUS-STAGE14_15_DEEP_CORPUS-01'
MAPPING={
'SRC-737BE4A23BE5':['SR-STR-199'],'SRC-23FF9ED6569C':['SR-STR-199'],'SRC-0DEBB4C4B005':['SR-STR-197'],'SRC-0ADDCEBC41B1':['SR-STR-200'],'SRC-FCE6C067FBF4':['SR-STR-200'],'SRC-0D20629504E7':['SR-STR-200'],'SRC-F7A5755105C3':['SR-STR-035'],'SRC-37929EF5409F':[],'SRC-FA21C4C7D284':['SR-STR-181'],'SRC-CFDA6E7234BD':['SR-STR-010'],'SRC-554EDA3C715F':['SR-STR-010'],'SRC-C670DF0B62A0':['SR-STR-143'],'SRC-4891593F405E':['SR-STR-005'],'SRC-060DB95FD085':['SR-STR-149'],'SRC-E001EA09C399':[],'SRC-F0722438261D':['SR-STR-216'],'SRC-648501F7E828':['SR-STR-216'],'SRC-EF084EC25611':['SR-STR-003'],'SRC-CE90E41ABAF4':['SR-STR-010','SR-STR-181'],'SRC-0532FBA4BB15':['SR-STR-014'],'SRC-FAA4CD0C773E':['SR-STR-014'],'SRC-88BE6A73D6E6':['SR-STR-034'],'SRC-2106A87EA273':['SR-STR-034'],'SRC-64383F0CADDC':['SR-STR-034'],'SRC-34CE15B4D50D':['SR-STR-014'],'SRC-87621FF80FD0':['SR-STR-014'],'SRC-951BED9A0173':['SR-STR-035'],'SRC-D76B4ACF27B7':['SR-STR-035'],'SRC-310CF52B97A1':['SR-STR-035'],'SRC-ECD2752AE235':['SR-STR-034'],'SRC-39A36B43CA9A':['SR-STR-034'],'SRC-164B414B8E31':['SR-STR-034'],'SRC-22BC734BDBC9':['SR-STR-034'],'SRC-D20B0DF64536':['SR-STR-014'],'SRC-BB53DF6DD02C':['SR-STR-014'],'SRC-E49D6C0BAE66':['SR-STR-014'],'SRC-3D41F32286B1':['SR-STR-014'],'SRC-0893915C5035':[],'SRC-2B0829FC4ACE':[],'SRC-739EC5F3B337':['SR-STR-014'],'SRC-CD4034944FA7':['SR-STR-014','SR-STR-035'],'SRC-D46DEEFC43F3':['SR-STR-014','SR-STR-035'],'SRC-502566BB20E8':['SR-STR-014'],'SRC-EFE64D3828F0':['SR-STR-114'],'SRC-AA449020EE85':['SR-STR-114'],'SRC-70876F522523':['SR-STR-162'],'SRC-82DE51BE6F99':['SR-STR-114','SR-STR-162'],'SRC-8C89359FB2ED':['SR-STR-217'],'SRC-3E1FDACA4EC9':['SR-STR-217'],'SRC-341B061118F5':['SR-STR-162'],'SRC-54D56C8DA497':['SR-STR-223'],'SRC-6C195F4F66B5':['SR-STR-223'],'SRC-E4330B493812':['SR-STR-223'],'SRC-B1FDB20A881C':['SR-STR-163'],'SRC-122B785F295E':['SR-STR-163'],'SRC-26A5598291B2':['SR-STR-163'],'SRC-6E9076751401':['SR-STR-032'],'SRC-84FA913400FE':['SR-STR-038','SR-STR-164'],'SRC-DC3C94CCBE18':['SR-STR-164','SR-STR-219'],'SRC-1E0222343ED3':['SR-STR-219']}
assert len(MAPPING)==60
SOURCE_IDS=list(MAPPING)
UNIQUE=sorted({x for ids in MAPPING.values() for x in ids})
assert len(UNIQUE)==22
assert sum(bool(ids) for ids in MAPPING.values())==56

sources=[]
for p in sorted(Path('docs/structure-radar/source-manifest').glob('part-*.json')):
    sources += json.loads(p.read_text()).get('sources',[])
source_map={s['source_id']:s for s in sources}
assert all(sid in source_map for sid in SOURCE_IDS)

progress_path=Path('docs/structure-radar/progress.json')
progress=json.loads(progress_path.read_text())
for sid,ids in MAPPING.items():
    s=source_map[sid]
    rec={'fingerprint':s['fingerprint'],'status':'STRUCTURES_RECORDED' if ids else 'NO_DISTINCT_STRUCTURE','batch_id':BATCH_ID}
    if ids: rec['structure_ids']=ids
    progress['source_reviews'][sid]=rec
progress['audit_batches']=[b for b in progress.get('audit_batches',[]) if b.get('batch_id')!=BATCH_ID]
progress['audit_batches'].append({'batch_id':BATCH_ID,'task_id':TASK_ID,'status':'SUBMITTED_FOR_AUDIT','source_ids':SOURCE_IDS,'sources_reviewed':60,'structures_added':0,'structures_updated':22,'structure_carrier_sources':56,'structures_deduped':4,'searches_completed':0,'arsenal_decisions':0,'audit_required':True,'duplicate_source':0,'no_distinct_structure':4})
progress_path.write_text(json.dumps(progress,indent=2,ensure_ascii=False)+'\n')

registry_path=Path('docs/structure-radar/structure-registry.json')
registry=json.loads(registry_path.read_text())
cards={c['structure_id']:c for c in registry['structures']}
assert all(cid in cards for cid in UNIQUE)
changed=set()
for sid,ids in MAPPING.items():
    if not ids: continue
    s=source_map[sid]
    prov={'source_id':sid,'path':s['path'],'locator':'StructureRadar batch23 source carrier','fingerprint':s['fingerprint']}
    for cid in ids:
        lst=cards[cid]['repo_provenance']
        if not any(x.get('source_id')==sid for x in lst):
            lst.append(prov.copy()); changed.add(cid)
assert changed==set(UNIQUE), (len(changed),sorted(changed))
registry['status']='BATCH_SUBMITTED_FOR_AUDIT'
registry_path.write_text(json.dumps(registry,indent=2,ensure_ascii=False)+'\n')

canonical="""name: StructureRadar controller

on:
  pull_request:
    paths:
      - 'docs/structure-radar/**'
      - 'scripts/structure_radar.py'
      - '.github/workflows/structure-radar.yml'
  workflow_dispatch:

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Verify repository-wide StructureRadar corpus and queue
        run: python scripts/structure_radar.py verify
"""
Path('.github/workflows/structure-radar.yml').write_text(canonical)
for name in ['.github/workflows/structure-radar-batch23-analyze.yml','.github/workflows/structure-radar-batch22-audit-repair-direct.yml','docs/structure-radar/.batch23-analysis-trigger','docs/structure-radar/.batch23-analysis.json','docs/structure-radar/.batch23-compact.tsv','docs/structure-radar/.batch23-unresolved.tsv','docs/structure-radar/.batch23-card-index.tsv','scripts/.structure_radar_batch23_finalize.py']:
    p=Path(name)
    if p.exists(): p.unlink()
