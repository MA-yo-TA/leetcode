from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        current_node = head
        current_value = head.val

        while current_node.next is not None:
            if current_node.next.val == current_value:
                # skip next
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                current_value = current_node.val

        return head
