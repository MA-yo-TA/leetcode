from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # リストを先頭から一つずつ歩いていくやつと1つ飛ばし（2倍速）で歩いていくやつがいて
        # 速いやつが遅いやつに追いついたらループしてる
        # どこかで None が出てきたらループしてない（そこが終端）

        slow = head
        fast = head

        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
