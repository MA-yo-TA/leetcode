from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        unique_character = set()
        for c in counts:
            if counts[c] == 1:
                unique_character.add(c)

        if not unique_character:
            return -1

        for i in range(len(s)):
            if s[i] in unique_character:
                return i

        return -1
