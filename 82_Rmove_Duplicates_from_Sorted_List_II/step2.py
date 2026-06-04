from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(val=float("-inf"), next=head)
        node = dummy_head
        while node:
            if node.next and node.next.next and node.next.val == node.next.next.val:
                duplicate_value = node.next.val
                while node.next and node.next.val == duplicate_value:
                    node.next = node.next.next
            else:
                node = node.next

        return dummy_head.next
