from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        nodes = [root]
        values_by_level = []
        while nodes:
            values = []
            next_layer = []
            for node in nodes:
                values.append(node.val)
                if node.left is not None:
                    next_layer.append(node.left)
                if node.right is not None:
                    next_layer.append(node.right)

            values_by_level.append(values)
            nodes = next_layer

        return values_by_level
