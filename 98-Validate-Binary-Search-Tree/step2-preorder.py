from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node_and_bound: list[tuple[Optional[TreeNode], float, float]] = [
            (root, float("-inf"), float("inf"))
        ]
        while node_and_bound:
            node, lower, upper = node_and_bound.pop()
            if node is None:
                continue
            if not (lower < node.val < upper):
                return False

            node_and_bound.append((node.left, lower, node.val))
            node_and_bound.append((node.right, node.val, upper))

        return True
