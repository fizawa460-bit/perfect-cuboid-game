"""Which query profiles a machine may skip in the distributed (9,9) table run (run99.sh).

A pair (f, g) with f in profile P and g in profile Q is found from either side (the table keeps 8 points of every
cover and a hit leaves at most 3 of them unmatched, the query tries all its 5-subsets), so for two different machines
only one of them has to run the other's queries.  The orientation below minimises the largest load
(queries x table slices): me 7.2, part1 6.9, part2 7.1, part3 6.6, part4 3.5 million (all queries everywhere: up to 17.4).
Every machine still runs all queries of its own profiles (pairs inside one machine, other Aut(B) classes).

usage: python3 qskip9.py NAME LOCDIR   -> comma list of tags to skip (empty if NAME is unknown or LOCDIR does not hold
exactly the profiles listed for NAME; then nothing is skipped)."""
import sys, glob, os
G = {'me': '004444 032443 040444 042433 043333 122443 131443 142333 222244 222424 223333',
     'part2': '232324 222433 132334 142342 142324',
     'part3': '222334 133333 132433 123334 042343 032344 121444 042244 031444',
     'part4': '132343 122434 131434'}
G = {k: v.split() for k, v in G.items()}
HERE = os.path.dirname(os.path.abspath(__file__))
ALL = [l.split()[0].replace(',', '') for l in open(f'{HERE}/hurwitz9.txt') if l.strip()]
G['part1'] = [t for t in ALL if t not in sum(G.values(), [])]
RUN = {'me': ['me', 'part1'], 'part1': ['part1', 'part3'], 'part2': ['part2', 'me', 'part1'],
       'part3': ['part3', 'me', 'part2'], 'part4': ['part4', 'me', 'part1', 'part2', 'part3']}
def check():
    import itertools
    assert sorted(sum(G.values(), [])) == sorted(ALL)
    for i, j in itertools.combinations(G, 2): assert (i in RUN[j]) + (j in RUN[i]) == 1, (i, j)
if __name__ == '__main__':
    check(); name, loc = sys.argv[1], sys.argv[2]
    have = sorted(os.path.basename(f)[5:11] for f in glob.glob(f'{loc}/L7_9_*[0-9].pkl'))
    if name not in G or have != sorted(G[name]):
        print(f'qskip9: {name}: local profiles do not match the list, nothing skipped', file=sys.stderr); print(''); sys.exit(0)
    print(','.join(t for k in G if k not in RUN[name] for t in G[k]))
