from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        values_by_level: list[list[int]] = [[root.val]]
        nodes: list[TreeNode] = [root]
        # 2階層ごとに同じことを繰り返すので、2階層セットでループを回す
        while nodes:
            # まず次のレベルを右から左へ見る
            next_level_values: list[int] = []
            next_level_nodes: list[TreeNode] = []
            while nodes:
                node = nodes.pop()
                if node.right is not None:
                    next_level_values.append(node.right.val)
                    next_level_nodes.append(node.right)
                if node.left is not None:
                    next_level_values.append(node.left.val)
                    next_level_nodes.append(node.left)

            if next_level_values:
                values_by_level.append(next_level_values)
            nodes = next_level_nodes

            # 次に、左から右へ
            next_level_values = []
            next_level_nodes = []
            while nodes:
                node = nodes.pop()
                if node.left is not None:
                    next_level_values.append(node.left.val)
                    next_level_nodes.append(node.left)
                if node.right is not None:
                    next_level_values.append(node.right.val)
                    next_level_nodes.append(node.right)

            if next_level_values:
                values_by_level.append(next_level_values)
            nodes = next_level_nodes

        return values_by_level
