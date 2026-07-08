from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        center = len(nums) // 2
        return TreeNode(
            val=nums[center],
            left=self.sortedArrayToBST(nums[:center]),
            right=self.sortedArrayToBST(nums[center + 1 :]),
        )
