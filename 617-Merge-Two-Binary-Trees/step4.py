from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None

        merged_root = TreeNode()
        stack = [(root1, root2, merged_root)]
        while stack:
            node1, node2, merged_node = stack.pop()
            if node1 is None:
                node1 = TreeNode(0)
            if node2 is None:
                node2 = TreeNode(0)

            merged_node.val = node1.val + node2.val
            if not (node1.left is None and node2.left is None):
                merged_node.left = TreeNode()
                stack.append((node1.left, node2.left, merged_node.left))
            if not (node1.right is None and node2.right is None):
                merged_node.right = TreeNode()
                stack.append((node1.right, node2.right, merged_node.right))

        return merged_root
