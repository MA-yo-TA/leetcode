from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node_l1 = l1
        node_l2 = l2
        dummy_head = ListNode()
        node = dummy_head
        carry = 0
        while node_l1 or node_l2:
            if node_l1:
                value_l1 = node_l1.val
                node_l1 = node_l1.next
            else:
                value_l1 = 0

            if node_l2:
                value_l2 = node_l2.val
                node_l2 = node_l2.next
            else:
                value_l2 = 0

            sum = value_l1 + value_l2 + carry
            digit = sum % 10
            carry = sum // 10
            node.next = ListNode(val=digit)
            node = node.next

        if carry:
            node.next = ListNode(val=carry)

        return dummy_head.next
