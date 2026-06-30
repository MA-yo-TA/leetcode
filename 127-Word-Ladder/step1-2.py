from collections import deque


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: list[str]) -> int:
        words_not_used = set(word_list)
        if end_word not in words_not_used:
            return 0

        def are_adjacent(word1: str, word2: str) -> bool:
            diff_count = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diff_count += 1

            return diff_count == 1

        def find_shortest_transformations_length() -> int:
            words_to_see = deque([(begin_word, 1)])
            words_not_used.discard(begin_word)
            while words_to_see:
                word, distance = words_to_see.popleft()
                if word == end_word:
                    return distance

                for w in list(words_not_used):
                    if not are_adjacent(word, w):
                        continue
                    words_not_used.remove(w)
                    words_to_see.append((w, distance + 1))
            return 0

        return find_shortest_transformations_length()
