from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        nodes = [root]
        next_layer = []
        depth = 1
        while nodes:
            for node in nodes:
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    next_layer.append(node.left)
                if node.right is not None:
                    next_layer.append(node.right)
            nodes = next_layer
            next_layer = []
            depth += 1

        raise RuntimeError("unreachable")
