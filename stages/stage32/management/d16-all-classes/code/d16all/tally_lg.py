# tally the fast Lemma G jobs: Sigma g >= (number of distinct removed quartics, genus 1 each, R2 convention) + remainder bound
import glob, re, collections
c = collections.Counter(); low = []
for f in sorted(glob.glob('lg_*.out')):
    s = open(f).read()
    q = len({int(k) for k in re.findall(r'removed known curve (\d+)', s) if int(k) >= 33})
    m = re.findall(r'FASTGENUS(?: lower bound)? (-?\d+)', s)
    if 'LG-ONLY-KNOWN' in s: g = q; tag = 'only-known'
    elif 'LG-REMAINDER-INTEGRAL' in s and m: g = q + max(0, int(m[-1])); tag = 'integral'
    elif 'LG-REMAINDER-REDUCIBLE' in s: g = q; tag = 'remainder-reducible'
    elif 'residual not a curve' in s: g = None; tag = 'not-a-curve'
    elif 'FAST:' in s: g = q; tag = 'fast-gave-up'
    else: g = None; tag = 'incomplete'
    ok = g is not None and g >= 2
    c[(tag, 'closed' if ok else 'open')] += 1
    if not ok: low.append((f[:-4], tag, g))
for k in sorted(c): print(k, c[k])
open('lg_open.txt', 'w').write('\n'.join(f'{a} {b} {c_}' for a, b, c_ in low) + '\n')
print('open', len(low))
