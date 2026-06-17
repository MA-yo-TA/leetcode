class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {"(": ")", "[": "]", "{": "}"}
        open_brackets = []
        for character in s:
            if (
                character not in open_to_close.keys()
                and character not in open_to_close.values()
            ):
                continue

            if character in open_to_close.keys():
                open_brackets.append(character)
                continue

            if open_brackets and character == open_to_close[open_brackets[-1]]:
                open_brackets.pop()
                continue

            return False

        return not open_brackets
