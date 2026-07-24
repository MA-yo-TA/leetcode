from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _is_valid_bst_sub(
            node: Optional[TreeNode],
        ) -> tuple[bool, int | float, int | float]:
            if node is None:
                return True, float("inf"), float("-inf")
            if node.left is None and node.right is None:
                return True, node.val, node.val

            is_left_valid, left_min, left_max = _is_valid_bst_sub(node.left)

            is_right_valid, right_min, right_max = _is_valid_bst_sub(node.right)

            return (
                is_left_valid and is_right_valid and left_max < node.val < right_min,
                min(left_min, right_min, node.val),
                max(left_max, right_max, node.val),
            )

        is_valid, _, _ = _is_valid_bst_sub(root)
        return is_valid
