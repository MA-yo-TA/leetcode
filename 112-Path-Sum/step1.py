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

        frontiers = [(root, 0)]
        while frontiers:
            node, sum_so_far = frontiers.pop()
            sum_so_far += node.val
            if node.left is None and node.right is None and sum_so_far == target_sum:
                return True

            if node.left is not None:
                frontiers.append((node.left, sum_so_far))
            if node.right is not None:
                frontiers.append((node.right, sum_so_far))

        return False
