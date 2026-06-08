class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "]": "[", "}": "{"}
        closes = close_to_open.keys()
        opens = close_to_open.values()
        stack = []
        for character in s:
            if character in opens:
                stack.append(character)
                continue

            if character in closes:
                if stack and stack[-1] == close_to_open[character]:
                    stack.pop()
                else:
                    return False

        return not stack
