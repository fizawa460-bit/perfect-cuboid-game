// Independent integer-polynomial checker for the row381 scalar chain.
#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using Poly = std::vector<int>;
using Divisor = std::pair<Poly, Poly>;
constexpr int p = 31, modulus = 961, genus = 52, generators = 9;

void require(bool ok, const char* message) {
    if (!ok) throw std::runtime_error(message);
}

int reduced(long long a, int m) {
    int b = static_cast<int>(a % m);
    return b < 0 ? b + m : b;
}

void trim(Poly& a) { while (!a.empty() && a.back() == 0) a.pop_back(); }
int deg(const Poly& a) { return static_cast<int>(a.size()) - 1; }
int coefficient(const Poly& a, size_t j) { return j < a.size() ? a[j] : 0; }

Poly scale(Poly a, int c, int m) {
    for (int& x : a) x = reduced(1LL * c * x, m);
    trim(a);
    return a;
}

Poly subtract(Poly a, const Poly& b, int m) {
    a.resize(std::max(a.size(), b.size()), 0);
    for (size_t j = 0; j < b.size(); ++j) a[j] = reduced(a[j] - b[j], m);
    trim(a);
    return a;
}

Poly multiply(const Poly& a, const Poly& b, int m) {
    if (a.empty() || b.empty()) return {};
    std::vector<long long> c(a.size() + b.size() - 1, 0);
    for (size_t i = 0; i < a.size(); ++i)
        for (size_t j = 0; j < b.size(); ++j)
            c[i + j] += 1LL * a[i] * b[j];
    Poly out(c.size());
    std::transform(c.begin(), c.end(), out.begin(), [m](long long t) { return reduced(t, m); });
    trim(out);
    return out;
}

int inverse(int a, int m) {
    a = reduced(a, m);
    int r = m, s = a, u = 0, v = 1;
    while (s) {
        int q = r / s;
        std::tie(r, s) = std::make_pair(s, r - q * s);
        std::tie(u, v) = std::make_pair(v, u - q * v);
    }
    require(r == 1, "nonunit inverse");
    return reduced(u, m);
}

std::pair<Poly, Poly> divide(Poly a, const Poly& b, int m) {
    require(!b.empty(), "polynomial division by zero");
    Poly q(std::max(0, deg(a) - deg(b) + 1), 0);
    const int inv = inverse(b.back(), m);
    while (a.size() >= b.size()) {
        const size_t d = a.size() - b.size();
        const int c = reduced(1LL * a.back() * inv, m);
        q[d] = c;
        for (size_t j = 0; j < b.size(); ++j) a[d + j] = reduced(a[d + j] - 1LL * c * b[j], m);
        trim(a);
    }
    trim(q);
    return {q, a};
}

Poly mod(const Poly& a, const Poly& b, int m) { return divide(a, b, m).second; }
Poly exact_div(const Poly& a, const Poly& b, int m) {
    auto [q, r] = divide(a, b, m);
    require(r.empty(), "polynomial division is not exact");
    return q;
}

Poly over_p(Poly a) { return scale(std::move(a), 1, p); }
Poly derivative(const Poly& a) {
    if (a.empty()) return {};
    Poly out(a.size() - 1);
    for (size_t i = 1; i < a.size(); ++i) out[i - 1] = reduced(1LL * i * a[i], p);
    trim(out);
    return out;
}

bool coprime(Poly a, Poly b) {
    a = over_p(std::move(a)); b = over_p(std::move(b));
    while (!b.empty()) {
        Poly r = mod(a, b, p);
        a = std::move(b);
        b = std::move(r);
    }
    return deg(a) == 0;
}

Poly polynomial_inverse(const Poly& a, const Poly& u) {
    Poly r = u, s = mod(a, u, p), v, w{1};
    while (!s.empty()) {
        auto [q, t] = divide(r, s, p);
        Poly z = mod(subtract(v, multiply(q, w, p), p), u, p);
        r = std::move(s); s = std::move(t); v = std::move(w); w = std::move(z);
    }
    require(deg(r) == 0, "no inverse modulo the anchor");
    return scale(v, inverse(r[0], p), p);
}

Poly read_poly(std::istream& in) {
    int n = -1;
    in >> n;
    require(bool(in) && n >= 0 && n <= 210, "bad polynomial length");
    Poly out(n);
    for (int& a : out) {
        in >> a;
        require(bool(in) && a >= 0 && a < modulus, "bad polynomial coefficient");
    }
    require(out.empty() || out.back() != 0, "noncanonical polynomial");
    return out;
}

Divisor read_divisor(std::istream& in) { return {read_poly(in), read_poly(in)}; }

void check_chart(const Divisor& d, const Poly& f) {
    const auto& [u, v] = d;
    require(!u.empty() && u.back() == 1 && deg(v) < deg(u) && deg(u) <= genus, "invalid chart degrees");
    require(mod(subtract(f, multiply(v, v, modulus), modulus), u, modulus).empty(), "chart off the curve");
}

void check_composition(const Divisor& left, const Divisor& right,
                       const Divisor& raw, const Poly& f) {
    const auto& [u, v] = left;
    const auto& [w, z] = right;
    const auto& [U, V] = raw;
    require(U == multiply(u, w, modulus) && deg(V) < deg(U), "wrong composed support");
    require(mod(V, u, modulus) == v && mod(V, w, modulus) == z, "wrong composed interpolation");
    require(mod(subtract(f, multiply(V, V, modulus), modulus), U, modulus).empty(),
            "wrong composed square relation");
    if (left == right) require(coprime(u, v), "doubling through a Weierstrass point");
    else require(coprime(u, w), "non-disjoint addition supports");
}

Divisor iterative_reduce(Divisor d, const Poly& f, int& steps) {
    auto& [u, v] = d;
    while (deg(u) > genus) {
        require(2 * deg(v) < deg(f) || v.back() % p, "nonunit pole at infinity");
        Poly q = exact_div(subtract(f, multiply(v, v, modulus), modulus), u, modulus);
        require(!q.empty() && deg(q) < deg(u) && q.back() % p, "illegal residual pole");
        q = scale(q, inverse(q.back(), modulus), modulus);
        v = mod(scale(v, -1, modulus), q, modulus);
        u = std::move(q);
        ++steps;
    }
    return d;
}

void check_function_reduction(const Divisor& raw, const Divisor& out,
                              const Poly& a, const Poly& b, const Poly& f) {
    const auto& [u, v] = raw;
    const auto& [q, w] = out;
    Poly uq = multiply(u, q, modulus);
    require(coprime(b, uq), "nonunit denominator on residual support");
    require(mod(subtract(a, multiply(b, v, modulus), modulus), u, modulus).empty(), "function misses input");
    require(mod(subtract(a, scale(multiply(b, w, modulus), -1, modulus), modulus),
                q, modulus).empty(), "function misses residual");
    Poly norm = subtract(multiply(a, a, modulus), multiply(f, multiply(b, b, modulus), modulus), modulus);
    require(!norm.empty() && norm.back() % p && deg(norm) == deg(uq), "wrong function norm pole");
    int a_pole = a.empty() ? -1 : 2 * deg(a);
    int b_pole = b.empty() ? -1 : deg(f) + 2 * deg(b);
    require(std::max(a_pole, b_pole) == deg(norm), "hidden nilpotent pole in function");
    require(norm == scale(uq, norm.back(), modulus), "wrong function norm factorization");
}

std::vector<int> first_digit(const Divisor& anchor, const Divisor& result, int scalar_mod31) {
    const auto& [u, v] = anchor;
    const auto& [U, V] = result;
    Poly q = over_p(u), b = over_p(v);
    require(over_p(U) == q && over_p(V) == b, "endpoint is not in the anchor chart");
    require(deg(q) == genus && coprime(q, derivative(q)) && coprime(q, b),
            "anchor cannot be used for differential evaluation");
    Poly d(genus);
    for (int i = 0; i < genus; ++i) {
        int delta = coefficient(U, i) - coefficient(u, i);
        require(delta % p == 0, "invalid tangent difference");
        d[i] = reduced(-delta / p, p);
    }
    trim(d);
    Poly z = mod(multiply(d, polynomial_inverse(scale(b, 2, p), q), p), q, p);
    const int ni = inverse(scalar_mod31, p);
    std::vector<int> answer;
    for (int j = 0; j < genus; ++j) {
        answer.push_back(reduced(1LL * ni * coefficient(z, genus - 1), p));
        z.insert(z.begin(), 0);
        trim(z);
        z = mod(z, q, p);
    }
    return answer;
}

int determinant(std::vector<std::vector<int>> m) {
    int result = 1;
    for (size_t i = 0; i < m.size(); ++i) {
        size_t j = i;
        while (j < m.size() && m[j][i] == 0) ++j;
        if (j == m.size()) return 0;
        if (i != j) {
            std::swap(m[i], m[j]);
            result = reduced(-result, p);
        }
        const int inv = inverse(m[i][i], p);
        result = reduced(1LL * result * m[i][i], p);
        for (j = i + 1; j < m.size(); ++j) {
            int x = reduced(1LL * m[j][i] * inv, p);
            for (size_t k = i; k < m.size(); ++k) m[j][k] = reduced(m[j][k] - 1LL * x * m[i][k], p);
        }
    }
    return result;
}

int main(int argc, char** argv) {
    try {
        require(argc == 3, "usage: verify_rank_tape trace.txt rational_inputs.txt");
        std::ifstream trace(argv[1]), inputs(argv[2]);
        require(trace.is_open() && inputs.is_open(), "could not open certificate");
        std::string version;
        trace >> version;
        require(version == "ROW382-31-CHAIN-1", "unrecognized certificate version");
        const Poly f = read_poly(trace);
        require(f == read_poly(inputs) && deg(f) == 105 && f.back() == 1 && coprime(f, derivative(f)),
                "wrong curve or bad reduction");
        std::string N;
        int n = 0, scalar_mod31 = 0;
        trace >> N >> n;
        require(!N.empty(), "missing scalar");
        for (char c : N) {
            require(c >= '0' && c <= '9', "invalid scalar digit");
            scalar_mod31 = (10 * scalar_mod31 + c - '0') % p;
        }
        require(scalar_mod31 == 13 && n == 8, "invalid scalar or run count");
        std::vector<std::vector<int>> coordinates;
        int additions = 0, negations = 0, function_steps = 0, iterative_steps = 0;
        for (int run = 0; run < n; ++run) {
            std::string name, expected_name;
            int seed;
            trace >> name >> seed;
            inputs >> expected_name;
            require(name == expected_name, "divisor name mismatch");
            const Divisor rational = read_divisor(inputs);
            std::vector<Divisor> points;
            for (int j = 0; j < generators; ++j) {
                auto d = read_divisor(trace);
                check_chart(d, f);
                if (j == 0) require(d == rational, "rational divisor mismatch");
                points.push_back(std::move(d));
            }
            int m = 0;
            trace >> m;
            require(m > 0 && m < 10000, "invalid chain length");
            auto check_index = [&points](int i) {
                require(i >= 0 && i < static_cast<int>(points.size()), "invalid operand");
            };
            for (int step = 0; step < m; ++step) {
                char op;
                int i;
                trace >> op >> i;
                require(bool(trace), "truncated chain");
                check_index(i);
                if (op == 'N') {
                    const auto& [u, v] = points[i];
                    Divisor d{u, scale(v, -1, modulus)};
                    points.push_back(std::move(d));
                        ++negations;
                    continue;
                }
                require(op == 'A', "unknown chain operation");
                int j, mode;
                trace >> j >> mode;
                check_index(j);
                require(mode >= 0 && mode <= 2, "invalid reduction mode");
                Divisor out = read_divisor(trace);
                check_chart(out, f);
                Divisor raw = mode ? read_divisor(trace) : out;
                check_composition(points[i], points[j], raw, f);
                if (mode == 1) require(iterative_reduce(raw, f, iterative_steps) == out, "wrong iterative endpoint");
                if (mode == 2) {
                    auto a = read_poly(trace), b = read_poly(trace);
                    check_function_reduction(raw, out, a, b, f);
                    ++function_steps;
                }
                points.push_back(std::move(out));
                ++additions;
            }
            int a, q;
            trace >> a >> q;
            check_index(q);
            require(a > 0 && a < generators, "invalid terminal anchor");
            coordinates.push_back(first_digit(points[a], points[q], scalar_mod31));
        }
        std::string extra;
        require(!(trace >> extra) && !(inputs >> extra), "trailing certificate data");
        require(additions == 4473, "incomplete addition chain");
        std::vector<std::vector<int>> minor;
        for (auto& v : coordinates) minor.emplace_back(v.begin(), v.begin() + 10);
        minor.push_back(std::vector<int>(10, 0)); minor.back()[0] = 1;
        minor.push_back(std::vector<int>(10, 0)); minor.back()[1] = 1;
        const int det = determinant(minor);
        require(det == 6, "wrong rank minor");
        std::cout << "{\"additions\":" << additions << ",\"negations\":" << negations
                  << ",\"iterative_steps_on_successful_paths\":" << iterative_steps
                  << ",\"function_reductions\":" << function_steps
                  << ",\"determinant_mod31\":" << det << ",\"log_coordinates\":[";
        for (size_t j = 0; j < coordinates.size(); ++j) {
            std::cout << (j ? ",[" : "[");
            for (size_t k = 0; k < coordinates[j].size(); ++k) {
                if (k) std::cout << ',';
                std::cout << coordinates[j][k];
            }
            std::cout << ']';
        }
        std::cout << "]}\n";
    } catch (const std::exception& e) {
        std::cerr << e.what() << '\n';
        return 1;
    }
}
