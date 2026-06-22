from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_node = head
        visited_nodes = set()

        while current_node is not None:
            visited_nodes.add(current_node)
            current_node = current_node.next

            if current_node in visited_nodes:
                return True

        return False
