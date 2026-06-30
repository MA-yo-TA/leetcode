from collections import deque


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: list[str]) -> int:
        all_letters = "abcdefghijklmnopqrstuvwxyz"
        word_set = set(word_list)
        word_list_and_begin = word_list + [begin_word]

        def get_adjacent_words(word: str) -> list[str]:
            adjacenct_words = []
            for i in range(len(word)):
                for letter in all_letters:
                    if word[i] == letter:
                        continue
                    candidate = word[:i] + letter + word[i + 1 :]
                    if candidate in word_set:
                        adjacenct_words.append(str(candidate))

            return adjacenct_words

        def construct_adjacency_list() -> dict[str, list[str]]:
            adjacency_list = dict()
            for word in word_list_and_begin:
                adjacency_list[word] = get_adjacent_words(word)

            return adjacency_list

        def find_shortest_transformations_length(
            adjacency_list: dict[str, list[str]],
        ) -> int:
            words_to_see = deque([(begin_word, 1)])
            seen_words = set([begin_word])
            while words_to_see:
                word, distance = words_to_see.popleft()
                if word == end_word:
                    return distance

                for adjacent in adjacency_list[word]:
                    if adjacent in seen_words:
                        continue
                    seen_words.add(adjacent)
                    words_to_see.append((adjacent, distance + 1))

            return 0

        adjacency_list = construct_adjacency_list()
        num_min_step = find_shortest_transformations_length(adjacency_list)
        return num_min_step
