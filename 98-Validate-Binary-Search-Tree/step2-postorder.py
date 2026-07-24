from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # None の result (base case) は or/min/max の単位元
        node_to_result: dict[Optional[TreeNode], tuple[bool, float, float]] = {
            None: (True, float("inf"), float("-inf"))
        }
        node_and_children_done = [(root, False)]
        while node_and_children_done:
            node, children_done = node_and_children_done.pop()
            if node is None:
                continue
            if not children_done:
                node_and_children_done.append((node, True))
                node_and_children_done.append((node.left, False))
                node_and_children_done.append((node.right, False))
            else:
                is_left_valid, left_min, left_max = node_to_result[node.left]
                is_right_valid, right_min, right_max = node_to_result[node.right]
                is_node_valid = (
                    is_left_valid and is_right_valid and left_max < node.val < right_min
                )

                if not is_node_valid:
                    return False

                node_to_result[node] = (
                    is_node_valid,
                    min(left_min, right_min, node.val),
                    max(left_max, right_max, node.val),
                )

        return node_to_result[root][0]
