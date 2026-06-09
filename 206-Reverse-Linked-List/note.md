# 206. Reverse Linked List

<https://leetcode.com/problems/reverse-linked-list/description/>

## step1（まず通す）

1. 先頭から見て行って数字を覚えておく
2. 覚えた数字をお尻から取り出しながらノードを繋いでいく

破壊的にやるなら ListNode 自体をリストに入れて後ろから繋いでいけばいい。

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        checking = head
        nodes = []
        while checking is not None:
            nodes.append(checking)
            checking = checking.next

        num_nodes = len(nodes)
        if num_nodes <= 1:
            return head

        for i in range(num_nodes - 1, 0, -1):
            nodes[i].next = nodes[i - 1]
        nodes[0].next = None

        return nodes[-1]
```
