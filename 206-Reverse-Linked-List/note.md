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

## step2（整形＆他の人のコードを読む）

破壊的にやる場合、

- previous node
- current node
- next node

の3つだけ持っておいて先頭から順に 前→今 を 前←今 に繋ぎかえていくやり方もある。

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        previous_node = head
        current_node = head.next
        next_node = head.next.next
        head.next = None
        while True:
            current_node.next = previous_node
            if next_node is None:
                break
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next

        return current_node
```

（ 連結リストを逆向きに繋ぎ変えて、と言われたら普通はまず先にこれを思いつく気がしており、<https://1kohei1.com/leetcode/> を見てカテゴリーごとに問題を解いていることで思考が記載されているカテゴリーに引っ張られ過ぎているかもしれないと思った ）

### 他の方のコードを読んで

- <https://github.com/huyfififi/coding-challenges/pull/18/changes>
  - 変数名を深く考えずに previous_node/current_node/next_node にしたけど、確かにもっとわかりやすい命名はあるかもしれない

- <https://github.com/t0hsumi/leetcode/pull/7/changes#diff-f1530fc1072ee1f0b7de99a2e5236992c72355da69982c8ca516fcfba7c57927R47-R48>
  - next_node の初期化をループの前にやらないで1回目のループでやれば、実質の判定を while の条件式にできる（if がいらなくなる）

## step3（10分以内にさっとかける * 3回）
