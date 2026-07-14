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

        nodes: list[TreeNode] = [root]
        traversal: list[list[int]] = []
        while nodes:
            values: list[int] = []
            next_layer: list[TreeNode] = []
            for node in nodes:
                values.append(node.val)
                if node.left is not None:
                    next_layer.append(node.left)
                if node.right is not None:
                    next_layer.append(node.right)

            traversal.append(values)
            nodes = next_layer

        return traversal
