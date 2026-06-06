class Solution:
    def isValid(self, s: str) -> bool:
        opens = ["(", "[", "{"]
        close_to_open = {")": "(", "]": "[", "}": "{"}
        stack = []
        for parenthesis in s:
            if parenthesis in opens:
                stack.append(parenthesis)
                continue

            if stack and stack[-1] == close_to_open[parenthesis]:
                stack.pop()
                continue

            return False

        if len(stack) != 0:
            return False

        return True
