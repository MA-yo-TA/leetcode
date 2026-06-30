from collections import defaultdict, deque


class Solution:
    def construct_adjacency_list(
        self, begin_word: str, word_list: list[str]
    ) -> dict[str, list[str]]:
        patterns_to_words = defaultdict(list)
        for word in word_list:
            for i in range(len(word)):
                patterns_to_words[(word[:i], word[i + 1 :])].append(word)

        adjacency_list = defaultdict(list)
        for word in word_list + [begin_word]:
            for i in range(len(word)):
                adjacency_list[word] += patterns_to_words[(word[:i], word[i + 1 :])]

        return adjacency_list

    def find_shortest_transformation_length(
        self, adjacency_list: dict[str, list[str]], begin_word: str, end_word: str
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
                words_to_see.append((adjacent, distance + 1))
                seen_words.add(adjacent)

        return 0

    def ladderLength(self, begin_word: str, end_word: str, word_list: list[str]) -> int:
        adjacency_list = self.construct_adjacency_list(begin_word, word_list)
        return self.find_shortest_transformation_length(
            adjacency_list, begin_word, end_word
        )
