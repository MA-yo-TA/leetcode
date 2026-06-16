class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_to_originals: dict[str, list[str]] = {}
        for string in strs:
            sorted_string = str(sorted(string))
            if sorted_string in sorted_to_originals:
                sorted_to_originals[sorted_string].append(string)
            else:
                sorted_to_originals[sorted_string] = [string]

        return list(sorted_to_originals.values())
