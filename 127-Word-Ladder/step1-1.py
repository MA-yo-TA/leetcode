from collections import defaultdict, deque


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: list[str]) -> int:
        def are_adjacent(word1: str, word2: str) -> bool:
            diff_count = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diff_count += 1

            return diff_count == 1

        def construct_adjacency_list() -> dict[str, list[str]]:
            word_to_adjacency_list = defaultdict(list)
            for i in range(len(word_list)):
                for j in range(i):
                    word1 = word_list[i]
                    word2 = word_list[j]
                    if are_adjacent(word1, word2):
                        word_to_adjacency_list[word1].append(word2)
                        word_to_adjacency_list[word2].append(word1)

            return word_to_adjacency_list

        def find_shortest_transformations_length(
            word_to_adjacency_list: dict[str, list[str]],
        ) -> int:
            words_to_see = deque([(begin_word, 1)])
            seen_words = set([begin_word])
            while words_to_see:
                word, distance = words_to_see.popleft()
                if word == end_word:
                    return distance

                for adjacent in word_to_adjacency_list[word]:
                    if adjacent in seen_words:
                        continue
                    seen_words.add(adjacent)
                    words_to_see.append((adjacent, distance + 1))

            return 0

        if end_word not in word_list:
            return 0

        word_list.append(begin_word)
        word_to_adjacency_list = construct_adjacency_list()
        return find_shortest_transformations_length(word_to_adjacency_list)
