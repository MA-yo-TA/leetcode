class Solution:
    def firstUniqChar(self, s: str) -> int:
        first_indices = dict()
        for i, letter in enumerate(s):
            if letter not in first_indices:
                first_indices[letter] = i
            else:
                # 参考にしたコードでは index が 0 以上かを見ているが、キーの有無で既出かどうかはわかるのですでに -1 （3回目以降）でも単に代入
                first_indices[letter] = -1

        for letter in first_indices:
            if first_indices[letter] != -1:
                return first_indices[letter]

        return -1
