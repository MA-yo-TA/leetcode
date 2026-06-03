# 83. Remove Duplicates from Sorted List

<https://leetcode.com/problems/remove-duplicates-from-sorted-list/>

## step1（まず通す）

ソートされているので、重複するノードは連続してしか出てこない。なので、次のノードの値が今見てるノードの値と同じなら飛ばす（next を繋ぎかえる）、という発想。
連結リストのいいところは、ポインタを繋ぎかえるだけで挿入・削除ができるところ。

## step2（整形＆他の人のコードを読む）

頭の中では「今見ている値を覚えといて次のノードの値がそれと一緒だったらskip」みたいに考えていたので `current_value` という変数を用意したが、常に current_node.val が入っているし間違ったものを代入してロジックが壊れてもこまる（必要以上に？複雑になっている）のでを考えると変数化しない方がいいかも。

- 入力を破壊している意識はあるか: <https://github.com/shintaro1993/arai60/pull/6/changes#discussion_r1995572104>
  - 「破壊してますかしてませんか」と聞かれたら「してます」と答えられるが、する選択肢としない選択肢を比較してする方を選んだわけではなかった
  - ただし、破壊していいなら繋ぎかえるだけの実装でとても楽なので破壊する方で書きたい
  - 破壊しないでと言われたら、破壊する時と同じように前から見ていって違う数字が出てくるたびに新しいノードを作って繋ぐ、という感じになりそう。たぶん↓みたいな感じ。

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy_head = ListNode()
        non_dup_node = dummy_head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr = curr.next
                continue
            non_dup_node.next = ListNode(val=curr.val)
            non_dup_node = non_dup_node.next
        return dummy_head.next
```

- <https://discord.com/channels/1084280443945353267/1195700948786491403/1196399353116499970>
  - この書き方も参考になる。重複が続いてる間は繋ぎかえを続けるので、一番外の while で回しながら毎回判定をするのでなく、重複が続いてる間ずっと詰めるという二重ループでも書ける

## step3（10分以内にさっとかける * 3回）

`curr` はみんな使ってるし省略形でも悪くなさそう
