from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # まず fast と slow が出会う点を見つける
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                break

        else:
            return None

        # fast と slow が合流したなら、片方をスタート地点に戻して同じ速さで再度歩かせると次に合流する点がサイクルの始まりの点
        slow = head

        while 1:
            if fast is slow:
                return fast

            fast = fast.next
            slow = slow.next
