class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_to_originals: dict[str, list[str]] = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in sorted_to_originals:
                sorted_to_originals[sorted_s].append(s)
            else:
                sorted_to_originals[sorted_s] = [s]

        return list(sorted_to_originals.values())
