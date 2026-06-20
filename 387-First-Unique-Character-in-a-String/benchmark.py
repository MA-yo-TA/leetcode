import timeit
from collections import Counter
from step1 import Solution as S1
from step2 import Solution as S2

CASES = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
    ("z" * 10000 + "a", 10000),  # 答えが長い文字列の先頭
    ("a" + "z" * 10000, 0),  # 答えが長い文字列の末尾
]

REPEAT = 1000


def bench(fn, s):
    return timeit.timeit(lambda: fn(s), number=REPEAT)


def counter_only(s):
    return Counter(s)


def build_set(s):
    counts = Counter(s)
    unique_character = set()
    for c in counts:
        if counts[c] == 1:
            unique_character.add(c)
    return unique_character


def python_scan(s):
    unique_character = build_set(s)
    for i in range(len(s)):
        if s[i] in unique_character:
            return i
    return -1


def index_scan(s):
    counts = Counter(s)
    for c in counts:
        if counts[c] == 1:
            return s.index(c)
    return -1


def main():
    col = 35
    print(f"{'case':<{col}} {'step1 (ms)':>12} {'step2 (ms)':>12} {'winner':>8}")
    print("-" * (col + 36))
    for s, expected in CASES:
        label = repr(s) if len(s) <= 20 else f"'{s[:15]}…{s[-1]}' (len={len(s)})"
        t1 = bench(S1().firstUniqChar, s) * 1000
        t2 = bench(S2().firstUniqChar, s) * 1000
        winner = "step1" if t1 < t2 else "step2"
        sol1, sol2 = S1().firstUniqChar(s), S2().firstUniqChar(s)
        assert sol1 == expected == sol2, (
            f"answer mismatch: s1={sol1} s2={sol2} expected={expected}"
        )
        print(f"{label:<{col}} {t1:>12.3f} {t2:>12.3f} {winner:>8}")

    # ---- コスト分解 (長い文字列2ケースのみ) ----
    print()
    print(f"-- cost breakdown (REPEAT={REPEAT}) --")
    breakdown_cases = [
        ("z" * 10000 + "a", "unique at end"),
        ("a" + "z" * 10000, "unique at start"),
    ]
    for s, label in breakdown_cases:
        t_counter = bench(counter_only, s) * 1000
        t_set = bench(build_set, s) * 1000
        t_pscan = bench(python_scan, s) * 1000
        t_iscan = bench(index_scan, s) * 1000
        scan_py = t_pscan - t_set  # step1 のベース: Counter + set
        scan_idx = t_iscan - t_counter  # step2 のベース: Counter のみ
        print(f"\n  [{label}]")
        print(f"    Counter only          : {t_counter:>8.3f} ms")
        print(f"    Counter + set (step1) : {t_set:>8.3f} ms")
        print(
            f"    python loop (step1)   : {t_pscan:>8.3f} ms  (scan only: {scan_py:>+.3f} ms)"
        )
        print(
            f"    s.index scan (step2)  : {t_iscan:>8.3f} ms  (scan only: {scan_idx:>+.3f} ms)"
        )
        ratio = scan_py / scan_idx if scan_idx > 0 else float("inf")
        print(f"    scan ratio (py/idx)   : {ratio:>8.2f}x")


if __name__ == "__main__":
    main()
