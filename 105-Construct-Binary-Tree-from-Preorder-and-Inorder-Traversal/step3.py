from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        value_to_inorder_index = {value: index for index, value in enumerate(inorder)}

        root = TreeNode()
        # stack: [(node, preorder_index, inorder_begin, inorder_end)]
        stack = [(root, 0, 0, len(inorder))]
        while stack:
            node, preorder_index, inorder_begin, inorder_end = stack.pop()
            node.val = preorder[preorder_index]
            inorder_pivot = value_to_inorder_index[node.val]
            if inorder_begin < inorder_pivot:
                node.left = TreeNode()
                stack.append(
                    (
                        node.left,
                        preorder_index + 1,
                        inorder_begin,
                        inorder_pivot,
                    )
                )
            if inorder_pivot + 1 < inorder_end:
                node.right = TreeNode()
                stack.append(
                    (
                        node.right,
                        preorder_index + (inorder_pivot - inorder_begin) + 1,
                        inorder_pivot + 1,
                        inorder_end,
                    )
                )

        return root
