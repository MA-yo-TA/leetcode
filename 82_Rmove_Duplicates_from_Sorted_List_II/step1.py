from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def does_duplicate_start(self, node: Optional[ListNode]) -> bool:
        if node is None or node.next is None:
            return False
        if node.val == node.next.val:
            return True
        return False

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(val=-1000, next=head)
        node = dummy_head
        while node is not None:
            if self.does_duplicate_start(node.next):
                dup_val = node.next.val
                while node.next and node.next.val == dup_val:
                    node.next = node.next.next
            else:
                node = node.next

        return dummy_head.next
