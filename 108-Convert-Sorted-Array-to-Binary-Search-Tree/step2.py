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

        root = TreeNode()
        stack: list[tuple[int, int, TreeNode]] = [(0, len(nums), root)]
        while stack:
            head, tail, node = stack.pop()
            center = (tail + head) // 2
            node.val = nums[center]
            if head < center:
                node.left = TreeNode()
                stack.append((head, center, node.left))
            if center + 1 < tail:
                node.right = TreeNode()
                stack.append((center + 1, tail, node.right))

        return root
