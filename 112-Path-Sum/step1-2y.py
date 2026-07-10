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

        if root.left is None and root.right is None and root.val == target_sum:
            return True

        children_target_sum = target_sum - root.val
        return self.hasPathSum(root.left, children_target_sum) or self.hasPathSum(
            root.right, children_target_sum
        )
