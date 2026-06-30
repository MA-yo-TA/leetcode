import importlib.util
import itertools
import random
import timeit
from pathlib import Path


BASE_DIR = Path(__file__).parent
SOLUTION_FILES = ("step1-1.py", "step1-2.py", "step1-3.py")
REPEAT = 5


def load_solution(filename: str):
    path = BASE_DIR / filename
    module_name = filename.removesuffix(".py").replace("-", "_")
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution()


def random_words(count: int, word_length: int, seed: int) -> list[str]:
    rng = random.Random(seed)
    words = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while len(words) < count:
        words.add("".join(rng.choice(alphabet) for _ in range(word_length)))
    return list(words)


def sparse_with_short_chain(count: int) -> tuple[str, str, list[str]]:
    chain = ["aaaaa", "aaaab", "aaabb", "aabbb", "abbbb", "bbbbb"]
    extras = [
        word
        for word in random_words(count + 20, word_length=5, seed=count)
        if word not in chain
    ]
    word_list = chain[1:] + extras[: max(0, count - len(chain) + 1)]
    return chain[0], chain[-1], word_list


def are_adjacent(word1: str, word2: str) -> bool:
    return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1


def long_induced_chain(count: int, word_length: int = 10) -> tuple[str, str, list[str]]:
    rng = random.Random(count)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chain = ["a" * word_length]
    used = set(chain)

    while len(chain) < count:
        current = chain[-1]
        candidates = []
        for i in range(word_length):
            for letter in alphabet:
                if current[i] == letter:
                    continue
                candidate = current[:i] + letter + current[i + 1 :]
                if candidate in used:
                    continue
                if any(are_adjacent(candidate, word) for word in chain[:-1]):
                    continue
                candidates.append(candidate)

        if not candidates:
            raise RuntimeError(f"failed to generate long chain: count={count}")

        next_word = rng.choice(candidates)
        chain.append(next_word)
        used.add(next_word)

    return chain[0], chain[-1], chain[1:]


def connected_grid(count: int) -> tuple[str, str, list[str]]:
    words = ["".join(chars) for chars in itertools.product("abcde", repeat=5)]
    selected = words[:count]
    begin_word = selected[0]
    end_word = selected[-1]
    word_list = [word for word in selected if word != begin_word]
    return begin_word, end_word, word_list


def bench(solution, begin_word: str, end_word: str, word_list: list[str]) -> float:
    def run():
        # step1-1.py appends begin_word, so pass a fresh copy every run.
        return solution.ladderLength(begin_word, end_word, word_list.copy())

    return timeit.timeit(run, number=REPEAT)


def main() -> None:
    cases = [
        ("classic", "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
    ]
    for count in (200, 800, 1600):
        begin_word, end_word, word_list = sparse_with_short_chain(count)
        cases.append((f"sparse-chain-{count}", begin_word, end_word, word_list, 6))
    for count in (100, 200, 400):
        begin_word, end_word, word_list = long_induced_chain(count)
        cases.append((f"long-chain-{count}", begin_word, end_word, word_list, count))
    for count in (125, 625, 1500):
        begin_word, end_word, word_list = connected_grid(count)
        cases.append((f"connected-grid-{count}", begin_word, end_word, word_list, None))

    solutions = {filename: load_solution(filename) for filename in SOLUTION_FILES}

    print(f"REPEAT={REPEAT}")
    print(
        f"{'case':<22} {'expected':>8} {'step1-1 (ms)':>14} "
        f"{'step1-2 (ms)':>14} {'step1-3 (ms)':>14} {'winner':>8}"
    )
    print("-" * 86)
    for name, begin_word, end_word, word_list, expected in cases:
        results = {}
        durations = {}
        for filename, solution in solutions.items():
            result = solution.ladderLength(begin_word, end_word, word_list.copy())
            if expected is not None:
                assert result == expected, (
                    f"{filename}: got {result}, expected {expected} in {name}"
                )
            results[filename] = result
            durations[filename] = bench(solution, begin_word, end_word, word_list) * 1000

        if expected is None:
            result_values = set(results.values())
            assert len(result_values) == 1, f"answer mismatch in {name}: {results}"
            expected = result_values.pop()

        winner = min(durations, key=durations.get)
        print(
            f"{name:<22} {expected:>8} "
            f"{durations['step1-1.py']:>14.3f} "
            f"{durations['step1-2.py']:>14.3f} "
            f"{durations['step1-3.py']:>14.3f} "
            f"{winner.removesuffix('.py'):>8}"
        )


if __name__ == "__main__":
    main()
