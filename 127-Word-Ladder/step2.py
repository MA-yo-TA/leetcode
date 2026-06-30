from collections import defaultdict, deque


class Solution:
    def get_patterns_map(
        self, word_list: list[str]
    ) -> dict[tuple[str, str], list[str]]:
        patterns_to_words = defaultdict(list)
        for word in word_list:
            for i in range(len(word)):
                patterns_to_words[(word[:i], word[i + 1 :])].append(word)

        return patterns_to_words

    def get_adjacent_words(
        self, patterns_to_words: dict[tuple[str, str], list[str]], word: str
    ) -> list[str]:
        adjacenct_words = []
        for i in range(len(word)):
            adjacenct_words += patterns_to_words[(word[:i], word[i + 1 :])]
        return adjacenct_words

    def construct_adjacency_list(
        self, word_list: list[str], begin_word: str
    ) -> dict[str, list[str]]:
        adjacency_list = dict()
        patterns_to_words = self.get_patterns_map(word_list)
        adjacency_list[begin_word] = self.get_adjacent_words(
            patterns_to_words, begin_word
        )
        for word in word_list:
            adjacency_list[word] = self.get_adjacent_words(patterns_to_words, word)

        return adjacency_list

    def find_shortest_transformations_length(
        self, begin_word: str, end_word: str, adjacency_list: dict[str, list[str]]
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

    def ladderLength(self, begin_word: str, end_word: str, word_list: list[str]) -> int:
        adjacency_list = self.construct_adjacency_list(word_list, begin_word)
        num_min_step = self.find_shortest_transformations_length(
            begin_word, end_word, adjacency_list
        )
        return num_min_step
