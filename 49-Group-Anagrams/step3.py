class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped_anagrams: dict[str, list[str]] = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in grouped_anagrams:
                grouped_anagrams[sorted_s].append(s)
            else:
                grouped_anagrams[sorted_s] = [s]
        return list(grouped_anagrams.values())
