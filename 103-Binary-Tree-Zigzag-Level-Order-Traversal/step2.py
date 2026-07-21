from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse_next_level(
        self, nodes: list[TreeNode], left_first: bool
    ) -> tuple[list[int], list[TreeNode]]:
        next_level_values: list[int] = []
        next_level_nodes: list[TreeNode] = []
        while nodes:
            node = nodes.pop()
            if left_first:
                if node.left is not None:
                    next_level_values.append(node.left.val)
                    next_level_nodes.append(node.left)
                if node.right is not None:
                    next_level_values.append(node.right.val)
                    next_level_nodes.append(node.right)
            else:
                if node.right is not None:
                    next_level_values.append(node.right.val)
                    next_level_nodes.append(node.right)
                if node.left is not None:
                    next_level_values.append(node.left.val)
                    next_level_nodes.append(node.left)

        return next_level_values, next_level_nodes

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        values_by_level: list[list[int]] = [[root.val]]
        nodes: list[TreeNode] = [root]
        left_first = False  # 根の直下は右から見る
        while nodes:
            next_level_values, next_level_nodes = self.traverse_next_level(
                nodes, left_first
            )
            if next_level_values:
                values_by_level.append(next_level_values)
            nodes = next_level_nodes
            left_first = not left_first

        return values_by_level
