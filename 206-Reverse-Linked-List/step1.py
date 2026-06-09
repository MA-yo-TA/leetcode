from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        nums = []
        while node is not None:
            nums.append(node.val)
            node = node.next

        dummy_head = ListNode()
        reversed_node = dummy_head
        while nums:
            reversed_node.next = ListNode(val=nums.pop())
            reversed_node = reversed_node.next

        return dummy_head.next
