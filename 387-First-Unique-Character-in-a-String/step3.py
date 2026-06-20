from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for c in counts:
            if counts[c] == 1:
                return s.index(c)

        return -1
