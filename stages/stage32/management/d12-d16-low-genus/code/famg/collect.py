"""Collect the special members of each 2-Gamma pencil (rep 1: c_, n_; rep 2: r_, n2_, h_) and write member jobs
famg/s1_<tag>_<u>.sing (rep 1, net member F0 - u F1, m16 tail) and famg/s2_<tag>_<u>.sing (rep 2, Y member).
Extension-field factors are listed in famg/ext.json for the length bound."""
import re, glob, os, json
P = 10009
def root(lin):  # 's+2108' / 'u-3415' -> root mod p
    m = re.fullmatch(r'\s*[su]\s*([+-]\s*\d+)?\s*', lin)
    if not m: return None
    c = int(m.group(1).replace(' ', '')) if m.group(1) else 0
    return (-c) % P
meta = json.load(open('famg/meta.json')); R = json.load(open('famg/milp2.json'))
spec = {}; ext = {}
for tag in meta:
    S1, S2 = {}, {}
    def add(d, u, why): d.setdefault(u % P, set()).add(why)
    for rep, fc, fn, d in (('1', f'famg/c_{tag}.out', f'famg/n_{tag}.out', S1), ('2', f'famg/r_{tag}.out', f'famg/n2_{tag}.out', S2)):
        t = open(fc).read().splitlines()
        for i, line in enumerate(t):
            m = re.search(r'fibre factor degree (\d+)\s+critical length (\d+)\s+per fibre (\d+)', line)
            if m and int(m.group(3)) >= 2:
                fac = t[i + 1].split('factor:')[1].strip()
                if int(m.group(1)) == 1: add(d, root(fac), f'crit{m.group(3)}')
                else: ext.setdefault(tag, []).append((rep, 'crit', fac, int(m.group(3))))
            m = re.search(r'EW\[1\]=(.*)', line)
            if m:
                r0 = root(m.group(1).strip())
                if r0 is None: ext.setdefault(tag, []).append((rep, 'critcurve', m.group(1), 0))
                else: add(d, r0, 'critcurve')
        for line in open(fn):
            m = re.search(r'NODEEXC\s+(\d+)\s+oG\s+(\d+)\s+member F0 - u F1 with u =\s*(\S+)', line)
            if m and m.group(3) != 'NONE':
                v = m.group(3)
                if v in ('ALL',): print('NODEEXC ALL', tag, rep, line.strip())
                elif v == 'inf': print('NODEEXC inf', tag, rep)
                else: add(d, int(v), f'exc{m.group(1)}')
            m = re.search(r'NODELEN\s+(\d+)\s+chart\s+(\d+)\s+factor\s+(\S+)\s+deg\s+(\d+)\s+length\s+(\d+)', line)
            if m:
                if m.group(4) == '1': add(d, root(m.group(3)), f'node{m.group(1)}:{m.group(5)}')
                else: ext.setdefault(tag, []).append((rep, f'node{m.group(1)}', m.group(3), int(m.group(5))))
    for line in open(f'famg/h_{tag}.out'):
        m = re.search(r'HIDPT (\d+) (\d+).*singular member: u=(\S+)', line)
        if m:
            v = m.group(3)
            if v in ('inf', '0'): print('HID special', tag, v)
            else: add(S2, int(v), f'hid{m.group(1)}x{m.group(2)}')
        if 'member: ALL' in line: print('HID ALL', tag, line.strip())
    spec[tag] = {'1': {str(k): sorted(v) for k, v in S1.items()}, '2': {str(k): sorted(v) for k, v in S2.items()}}
    print(tag, 'rep1', len(S1), 'rep2', len(S2), 'ext', len(ext.get(tag, [])))
json.dump(spec, open('famg/special.json', 'w'), indent=1); json.dump(ext, open('famg/ext.json', 'w'), indent=1)
