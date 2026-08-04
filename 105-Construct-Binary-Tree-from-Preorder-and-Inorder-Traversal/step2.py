from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        value_to_inorder_index = {value: index for index, value in enumerate(inorder)}

        def build_tree_with_indices(
            inorder_begin: int,
            inorder_end: int,
            preorder_index: int,
        ) -> Optional[TreeNode]:
            if inorder_begin >= inorder_end:
                return None

            value = preorder[preorder_index]
            inorder_pivot = value_to_inorder_index[value]
            return TreeNode(
                val=value,
                left=build_tree_with_indices(
                    inorder_begin,
                    inorder_pivot,
                    preorder_index + 1,
                ),
                right=build_tree_with_indices(
                    inorder_pivot + 1,
                    inorder_end,
                    preorder_index + (inorder_pivot - inorder_begin) + 1,
                ),
            )

        return build_tree_with_indices(0, len(inorder), 0)
