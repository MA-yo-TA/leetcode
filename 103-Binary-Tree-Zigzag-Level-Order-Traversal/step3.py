from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        values_by_level = []
        nodes = [root]
        is_left_to_right = True
        while nodes:
            values = []
            next_level = []
            for node in nodes:
                values.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            if not is_left_to_right:
                values.reverse()
            values_by_level.append(values)

            nodes = next_level
            is_left_to_right = not is_left_to_right

        return values_by_level
