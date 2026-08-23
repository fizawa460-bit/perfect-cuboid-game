#!/usr/bin/env python3
from __future__ import annotations
import json, pathlib, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
CORE = json.loads((ROOT / 'picard-core.json').read_text())
MAGMA_URL = 'https://magma.maths.usyd.edu.au/xml/calculator.xml'
REFERER = 'https://magma.maths.usyd.edu.au/calc/'


def mm(M):
    return f"Matrix(Integers(),{len(M)},{len(M[0])},[" + ','.join(str(int(x)) for r in M for x in r) + '])'


def vv(v):
    return '[' + ','.join(str(int(x)) for x in v) + ']'


G = CORE['basis_gram']
H = CORE['hyperplane']
I = CORE['raw_cross_pairings_with_basis']
hf = [sum(H[i] * G[i][j] for i in range(64)) for j in range(64)]
ef = [sum(I[k][j] for k in range(92, 140)) for j in range(64)]
# Deterministic half of the 92 known nonexceptional curves.  Fixing its total
# lowers the CloseVectors dimension by one while preserving an exact partition.
gf = [sum(I[k][j] for k in range(46)) for j in range(64)]


def parse_rows(lines):
    rows = []
    for line in lines:
        if line.startswith('STAGE32_ADAPT a='):
            vals = {q.split('=')[0]: int(q.split('=')[1]) for q in line.split()[1:]}
            rows.append(vals)
    return rows


def post_range(d, g, e, lo, hi):
    lower = -d - 2 + 2 * g
    imgs = ', '.join(f'Z3![{hf[j]},{ef[j]},{gf[j]}]' for j in range(64))
    code = f'''
SetColumns(0);
G:={mm(G)}; Pic:=RSpace(Integers(),64,G); H:=Pic!{vv(H)}; I:={mm(I)};
Z64:=RSpace(Integers(),64); Z3:=RSpace(Integers(),3);
phi:=hom<Z64 -> Z3 | [{imgs}]>;
K:=Kernel(phi); B:=BasisMatrix(K); Q:=-B*G*Transpose(B); assert IsPositiveDefinite(Q);
KM:=RSpace(Integers(),Dimension(K)); inc:=hom<KM -> Pic | [Pic!Eltseq(b): b in Basis(K)]>;
QQ:=ChangeRing(Q,Rationals()); L:=LatticeWithGram(Q);
for aa in [{lo}..{hi}] do
  tar:=Z3![{d},{e},aa]; raw:=0; kept:=0; feas:=0;
  if tar in Image(phi) then
    feas:=1; c0z:=tar @@ phi; C0:=Pic!Eltseq(c0z);
    b:=Vector(Rationals(),[(C0,inc(KM.j)): j in [1..Dimension(K)]]);
    center:=Solution(QQ,b); radius:=-{lower}+(C0,C0)+(center*QQ,center);
    if radius ge 0 then
      clv:=CloseVectors(L,center,radius); raw:=#clv;
      for cv in clv do
        z:=KM!Eltseq(cv[1]); C:=C0+inc(z);
        exmass:=&+[&+[I[k,j]*C[j] : j in [1..64]] : k in [93..140]];
        amass:=&+[&+[I[k,j]*C[j] : j in [1..64]] : k in [1..46]];
        if (C,H) eq {d} and exmass eq {e} and amass eq aa and (C,C) ge {lower}
           and forall{{k : k in [1..140] | &+[I[k,j]*C[j] : j in [1..64]] ge 0}} then kept +:= 1; end if;
      end for;
    end if;
  end if;
  printf "STAGE32_ADAPT a=%o feasible=%o raw=%o kept=%o\\n",aa,feas,raw,kept;
end for;
printf "STAGE32_ADAPT_END lo={lo} hi={hi}\\n";
'''
    data = urllib.parse.urlencode({'input': code}).encode()
    req = urllib.request.Request(
        MAGMA_URL, data=data,
        headers={'Content-Type': 'application/x-www-form-urlencoded', 'Referer': REFERER,
                 'User-Agent': 'perfect-cuboid-stage32/2.0'}, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=72) as resp:
            rawxml = resp.read().decode('utf-8', 'replace')
        root = ET.fromstring(rawxml)
        lines = [''.join(line.itertext()) for result in root.findall('.//results') for line in result.findall('.//line')]
        out = '\n'.join(lines)
        rows = parse_rows(lines)
        complete = (f'STAGE32_ADAPT_END lo={lo} hi={hi}' in out
                    and len(rows) == hi - lo + 1
                    and not any(x in out for x in ('Runtime error', 'User error', 'Internal error')))
        return {'lo': lo, 'hi': hi, 'ok': complete, 'seconds': round(time.time() - t0, 3),
                'rows': rows, 'stdout': out}
    except Exception as exc:
        return {'lo': lo, 'hi': hi, 'ok': False, 'seconds': round(time.time() - t0, 3),
                'rows': [], 'error': repr(exc)}


def seed_rows(d, g, e):
    rows = {}
    # Consume any partial all-in-one batch first (notably d6/g1/e0 a=0..42).
    for name in (
        f'numeric-magma-curvegroup-batch-d{d}-g{g}-e{e}.json',
        f'numeric-magma-curvegroup-adaptive-d{d}-g{g}-e{e}.json',
    ):
        p = ROOT / name
        if not p.exists():
            continue
        try:
            data = json.loads(p.read_text())
        except Exception:
            continue
        for r in data.get('rows', []):
            if {'a', 'feasible', 'raw', 'kept'} <= set(r):
                rows[int(r['a'])] = {k: int(r[k]) for k in ('a', 'feasible', 'raw', 'kept')}
    # Also consume the older per-a refinement format when present.
    p = ROOT / f'numeric-magma-curvegroup-d{d}-g{g}-e{e}.json'
    if p.exists():
        try:
            data = json.loads(p.read_text())
            for r in data.get('results', []):
                if not r.get('ok'):
                    continue
                for rr in parse_rows(r.get('stdout', '').splitlines()):
                    rows[int(rr['a'])] = rr
        except Exception:
            pass
    return rows


def save(d, g, e, total, rows, attempts, unresolved):
    payload = {
        'schema': 'STAGE32_CURVEGROUP_ADAPTIVE_V1',
        'degree': d,
        'genus': g,
        'exceptional_mass': e,
        'curve_mass_total': total,
        'expected_row_count': total + 1,
        'completed_row_count': len(rows),
        'all_completed': len(rows) == total + 1 and not unresolved,
        'raw_total': sum(r['raw'] for r in rows.values()),
        'kept_total': sum(r['kept'] for r in rows.values()),
        'rows': [rows[a] for a in sorted(rows)],
        'attempts': attempts,
        'unresolved': unresolved,
    }
    (ROOT / f'numeric-magma-curvegroup-adaptive-d{d}-g{g}-e{e}.json').write_text(
        json.dumps(payload, indent=2, sort_keys=True) + '\n')
    return payload


def contiguous_chunks(values, chunk):
    values = sorted(values)
    if not values:
        return []
    runs = []
    start = prev = values[0]
    for v in values[1:]:
        if v != prev + 1:
            runs.append((start, prev)); start = v
        prev = v
    runs.append((start, prev))
    out = []
    for lo, hi in runs:
        x = lo
        while x <= hi:
            y = min(hi, x + chunk - 1)
            out.append((x, y)); x = y + 1
    return out


def run(d, g, e, chunk=12):
    total = 19 * d - 5 * e
    if total < 0:
        raise SystemExit('negative curve mass')
    rows = seed_rows(d, g, e)
    attempts = []
    unresolved = []
    queue = contiguous_chunks(set(range(total + 1)) - set(rows), chunk)
    while queue:
        lo, hi = queue.pop(0)
        missing = [a for a in range(lo, hi + 1) if a not in rows]
        if not missing:
            continue
        lo, hi = missing[0], missing[-1]
        r = post_range(d, g, e, lo, hi)
        attempts.append({k: r[k] for k in r if k != 'stdout'})
        for rr in r.get('rows', []):
            rows[int(rr['a'])] = {k: int(rr[k]) for k in ('a', 'feasible', 'raw', 'kept')}
        still = [a for a in range(lo, hi + 1) if a not in rows]
        print(json.dumps({'d': d, 'g': g, 'e': e, 'lo': lo, 'hi': hi, 'ok': r['ok'],
                          'seconds': r['seconds'], 'new_rows': len(r.get('rows', [])),
                          'completed': len(rows), 'expected': total + 1}, sort_keys=True), flush=True)
        save(d, g, e, total, rows, attempts, unresolved)
        if still:
            if len(still) == 1:
                unresolved.append(still[0])
            else:
                mid = len(still) // 2
                left, right = still[:mid], still[mid:]
                if left: queue.insert(0, (left[0], left[-1]))
                if right: queue.insert(1 if left else 0, (right[0], right[-1]))
        time.sleep(0.25)
    payload = save(d, g, e, total, rows, attempts, sorted(set(unresolved) - set(rows)))
    print(json.dumps({'degree': d, 'genus': g, 'e': e,
                      'all_completed': payload['all_completed'],
                      'rows': payload['completed_row_count'],
                      'raw_total': payload['raw_total'], 'kept_total': payload['kept_total'],
                      'unresolved': payload['unresolved']}, sort_keys=True))
    if not payload['all_completed']:
        raise SystemExit('adaptive curve-group enumeration still has unresolved singleton shards')


if __name__ == '__main__':
    if len(sys.argv) < 4:
        raise SystemExit('usage: degree genus exceptional_mass [initial_chunk]')
    run(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else 12)
