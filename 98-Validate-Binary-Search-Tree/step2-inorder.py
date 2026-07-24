from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node_and_left_done: list[tuple[Optional[TreeNode], bool]] = [(root, False)]
        previous_value = float("-inf")
        while node_and_left_done:
            node, left_done = node_and_left_done.pop()
            if node is None:
                continue

            if not left_done:
                node_and_left_done.append((node, True))
                node_and_left_done.append((node.left, False))
            else:
                if node.val <= previous_value:
                    return False
                node_and_left_done.append((node.right, False))
                previous_value = node.val

        return True
