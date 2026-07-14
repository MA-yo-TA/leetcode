from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if root is None:
            return False

        frontiers = [(root, target_sum)]
        while frontiers:
            node, rest = frontiers.pop()
            rest -= node.val
            if node.left is None and node.right is None:
                if rest == 0:
                    return True
                else:
                    continue

            if node.left is not None:
                frontiers.append((node.left, rest))
            if node.right is not None:
                frontiers.append((node.right, rest))

        return False
