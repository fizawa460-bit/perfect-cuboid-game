"""Binary class relations and projection to the coupled local domains."""


class BinarySpan:
    def __init__(self):
        self.rows = {}
        self.pivots = 0

    def reduce(self, vector):
        while vector & self.pivots:
            p = (vector & self.pivots).bit_length() - 1
            vector ^= self.rows[p]
        return vector

    def add(self, vector):
        vector = self.reduce(vector)
        if not vector:
            return False
        p = vector.bit_length() - 1
        self.rows[p] = vector
        self.pivots |= 1 << p
        return True

    def __len__(self):
        return len(self.rows)


def dependencies(vectors):
    """Basis of linear combinations of the inputs with value zero."""
    rows = {}
    result = []
    for i, vector in enumerate(vectors):
        combination = 1 << i
        while vector:
            p = vector.bit_length() - 1
            if p not in rows:
                rows[p] = (vector, combination)
                break
            v, c = rows[p]
            vector ^= v
            combination ^= c
        if not vector:
            result.append(combination)
    return result


def annihilator(values, width):
    """Linear forms vanishing on the given local values."""
    span = BinarySpan()
    for x in values:
        span.add(x)
    for i in range(width):
        if span.pivots >> i & 1:
            continue
        mask = 1 << i
        for p in sorted(span.rows):
            if (mask & span.rows[p]).bit_count() & 1:
                mask |= 1 << p
        yield mask


def coupled_domains(table, starts, n, class_equations, common):
    """All certified constraints are necessary for the actual pair."""
    allowed = {}
    widths = {p: len(row["factors_ascending"]) for p, row in table.items()}
    for p, row in table.items():
        w = widths[p]
        ban = (common >> starts[p]) & ((1 << w) - 1)
        allowed[p] = [a | (b << w) for a, b in row["pairs"] if not (a | b) & ban]
        assert 0 in allowed[p]

    span = BinarySpan()
    for r in class_equations:
        span.add(r)
        span.add(r << n)
    while common:
        bit = common & -common
        common -= bit
        span.add(bit)
        span.add(bit << n)

    affected = set(table)
    while affected:
        for p in sorted(affected):
            w, start = widths[p], starts[p]
            for m in annihilator(allowed[p], 2 * w):
                left, right = m & ((1 << w) - 1), m >> w
                span.add((left << start) | (right << (n + start)))
        affected = set()
        for p in table:
            w, start = widths[p], starts[p]
            if len(allowed[p]) <= 1:
                continue
            vectors = [span.reduce(1 << (start + j + k))
                       for k in (0, n) for j in range(w)]
            conditions = dependencies(vectors)
            keep = [v for v in allowed[p] if not any(
                (v & m).bit_count() & 1 for m in conditions)]
            if keep != allowed[p]:
                assert 0 in keep
                allowed[p] = keep
                affected.add(p)

    return ({p: [[v & ((1 << widths[p]) - 1), v >> widths[p]] for v in ds]
             for p, ds in allowed.items()}, span)


def setup(table, factors, relations):
    starts, labels, offset = {}, [], 0
    for p, (degrees, ramification) in sorted(factors.items()):
        starts[p] = offset
        labels.extend((p, j) for j in range(len(degrees)))
        offset += len(degrees)
    vectors = [sum(1 << (starts[p] + j) for p, j in row) for row in relations]
    # These are the exact relations for the rational principal ideals (p).
    vectors.extend(sum((e & 1) << (starts[p] + j)
                       for j, e in enumerate(ramification))
                   for p, (_, ramification) in sorted(factors.items()))
    return starts, labels, vectors


def generic_reduction(table, starts, labels, vectors, case):
    known = 0
    for p, row in table.items():
        w = len(row["factors_ascending"])
        known |= (((1 << w) - 1) ^ row["possible_nonsplit_masks"][case]) << starts[p]
    span = BinarySpan()
    for r in vectors:
        span.add(r & ~known)
    killed = [list(label) for i, label in enumerate(labels)
              if not (known >> i & 1) and not span.reduce(1 << i)]
    return {"new_split": killed, "formal_rank": len(span)}, span, known
