from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectMeetingPoint(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return fast

        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Floyd の循環検出法で fast と slow の出会うポイントを特定する
        meeting_point = self.detectMeetingPoint(head)

        if meeting_point is None:
            return None

        # head から1つずつ進むやつと meeting_point から一つずつ進むやつが最初に出会うところがサイクルの起点
        follower = head
        followed = meeting_point

        while follower is not followed:
            follower = follower.next
            followed = followed.next

        return follower
