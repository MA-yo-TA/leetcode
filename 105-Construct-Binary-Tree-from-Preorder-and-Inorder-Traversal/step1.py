from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(val=preorder[0])

        value = preorder[0]

        inorder_index = inorder.index(value)
        left_inorder = inorder[:inorder_index]
        right_inorder = inorder[inorder_index + 1 :]
        left_inorder_set = set(left_inorder)
        right_inorder_set = set(right_inorder)

        left_preorder = []
        right_preorder = []
        for num in preorder:
            if num in left_inorder_set:
                left_preorder.append(num)
            elif num in right_inorder_set:
                right_preorder.append(num)

        return TreeNode(
            val=value,
            left=self.buildTree(preorder=left_preorder, inorder=left_inorder),
            right=self.buildTree(preorder=right_preorder, inorder=right_inorder),
        )
