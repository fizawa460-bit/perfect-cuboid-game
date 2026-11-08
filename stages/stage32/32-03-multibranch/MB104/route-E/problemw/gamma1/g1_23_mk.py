# 32R-94 s5: k = 8, gamma = 1, bidegree (2,3): W = sum c_ij X1^i X0^(3-i) Y1^j Y0^(2-j) (x = X1/X0 cubic, y quadratic),
# exact over Q(i).  Case A (s2 = 0): J = {be} x B_e + {bb} x B_b + {ba} x B_a, other three x-fibres ramified, every
# y-fibre over B has a double root.  Case B (s2 = 1): node at (b0x, b0) with b0x in B_chi(b0), x' = other point of
# B_chi(b0): (x', b0), (x', b0'), blocks {b1} x B_chi1, {b2} x B_chi2; two remaining x-fibres ramified, y-fibres over
# the five b != b0 have a double root.  Emptiness of the projective solution set is printed per case.
import itertools
B = {'e': ['0', 'inf'], 'b': ['1', '-1'], 'a': ['I', '-I']}
ALL = [p for c in 'eba' for p in B[c]]
LAB = {p: c for c in 'eba' for p in B[c]}
def hom(p):   # homogeneous coordinates (Z0, Z1) with z = Z1/Z0
    return ('0', '1') if p == 'inf' else ('1', p if p != '0' else '0')
MON = [(i, j) for i in range(4) for j in range(3)]
W = '+'.join(f'c{i}{j}*X1^{i}*X0^{3-i}*Y1^{j}*Y0^{2-j}' for i, j in MON)
hdr = ['ring R = (0,I),(' + ','.join(f'c{i}{j}' for i, j in MON) + ',X0,X1,Y0,Y1),dp; minpoly = I^2+1;',
       'LIB "elim.lib";', f'poly W = {W};',
       'proc at(poly f, string px0, string px1, string py0, string py1) { execute("poly g = subst(subst(subst(subst(f,X0,(" + px0 + ")),X1,(" + px1 + ")),Y0,(" + py0 + ")),Y1,(" + py1 + "));"); return(g); }',
       'proc dq(poly q) { poly A = diff(diff(q,Y1),Y1)/2; poly Bq = diff(diff(q,Y0),Y1); poly C = diff(diff(q,Y0),Y0)/2; return(subst(subst(Bq^2-4*A*C,Y0,1),Y1,1)); }',
       'proc dc(poly q) { poly a3 = diff(diff(diff(q,X1),X1),X1)/6; poly a0 = diff(diff(diff(q,X0),X0),X0)/6; poly a2 = diff(diff(diff(q,X1),X1),X0)/2; poly a1 = diff(diff(diff(q,X1),X0),X0)/2; poly D = a2^2*a1^2-4*a3*a1^3-4*a2^3*a0-27*a3^2*a0^2+18*a3*a2*a1*a0; return(subst(subst(D,X0,1),X1,1)); }',
       'ring L = (0,I),(' + ','.join(f'c{i}{j}' for i, j in MON) + '),dp; minpoly = I^2+1; setring R;']
def pt(px, py):
    (a0, a1), (b0, b1) = hom(px), hom(py)
    return f'at(W,"{a0}","{a1}","{b0}","{b1}")'
def xfib(px):  # quadratic in Y over x = px
    a0, a1 = hom(px); return f'dq(subst(subst(W,X0,({a0})),X1,({a1})))'
def yfib(py):
    b0, b1 = hom(py); return f'dc(subst(subst(W,Y0,({b0})),Y1,({b1})))'
def node(px, py):
    (a0, a1), (b0, b1) = hom(px), hom(py)
    return ','.join(f'at(diff(W,{v}),"{a0}","{a1}","{b0}","{b1}")' for v in ('X0', 'X1', 'Y0', 'Y1'))
out = list(hdr); n = 0
def case(tag, eqs):
    global n; n += 1
    out.append(f'ideal E{n} = {",".join(eqs)}; setring L; ideal F = imap(R, E{n}); F = std(F); "{tag} : dim", dim(F), " (0 = empty projectively)"; kill F; setring R;')
# Case A
for be, bb, ba in itertools.product(B['e'], B['b'], B['a']):
    J = [(be, y) for y in B['e']] + [(bb, y) for y in B['b']] + [(ba, y) for y in B['a']]
    eqs = [pt(*p) for p in J] + [xfib(x) for x in ALL if x not in (be, bb, ba)] + [yfib(y) for y in ALL]
    case(f'A {be} {bb} {ba}', eqs)
# Case B
for c0 in 'eba':
    c1, c2 = [c for c in 'eba' if c != c0]
    for b0, b0x in itertools.product(B[c0], B[c0]):
        b0p = [y for y in B[c0] if y != b0][0]; xp = [x for x in B[c0] if x != b0x][0]
        for b1, b2 in itertools.product(B[c1], B[c2]):
            J = [(xp, b0), (xp, b0p)] + [(b1, y) for y in B[c1]] + [(b2, y) for y in B[c2]]
            eqs = [pt(b0x, b0), node(b0x, b0)] + [pt(*p) for p in J] + [xfib(x) for x in ALL if x not in (b0x, xp, b1, b2)] + [yfib(y) for y in ALL if y != b0]
            case(f'B node ({b0x},{b0}) x\'={xp} blocks {b1},{b2}', eqs)
out.append('quit;')
open('g1_23.sing', 'w', newline='\n').write('\n'.join(out)); print('cases', n)
