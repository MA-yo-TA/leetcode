class Solution:
    def isValid(self, s: str) -> bool:
        opens = "([{"
        closes = ")]}"
        close_to_open = {")": "(", "]": "[", "}": "{"}
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
