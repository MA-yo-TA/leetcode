# 703. Kth Largest Element in a Stream

<https://leetcode.com/problems/kth-largest-element-in-a-stream/>

## step1（まず通す）

ヒープを書くのに自信がなかったので、最初にソートしてあとは2分探索で挿入してくコードを書いた。
ヒープは書こうとしてとしてめちゃくちゃ時間をかけてしまった。非常に混乱しながら書いているのでとても効率の悪いコードになっている。時間がもったいないのでもっと早く他の人のコードを読みにいくべきだった。

## step2（整形＆他の人のコードを読む）

- そもそも insert している時点で挿入部分の時間計算量が配列の長さnに対して O(n) あるので2分探索じゃなくていっそ線形に探索した方が楽だった
- heapq というライブラリがあるのでそれを使えば話が早そうではある
  - <https://docs.python.org/ja/3.13/library/heapq.html>
- みなさん、max ヒープを作って k 回 pop するんじゃなくて、k 要素の min ヒープを作っていらっしゃる
  - <https://github.com/shining-ai/leetcode/pull/8> など
  - 「k番目に大きい＝大きい方からk要素だけの中で最小」なので、こうすると判定が早い
- 簡単にセルフ実装してみた。最初 push を↓のように書いていて時間計算量がO(配列長さ) だなあと思っていたところ CPython では 末尾を pop してから先頭をその値で上書きしていた。なるほどいいやり方だ。
  - <https://github.com/python/cpython/blob/3.13/Lib/heapq.py#L137>
- 親の位置をビット演算で計算しているのも勉強になる
  - <https://github.com/python/cpython/blob/06dce35b5a63ea653d6101d36a8afc0e922255c6/Lib/heapq.py#L212>
- 最初書いた時はクラスのメンバ変数として Minheap.heap を持たせたために self.heap を直接いじるメソッドと引数として受け取るメソッドが混在していたので改善した
  - CPython の heapq は関数を集めた名前空間

```python
    def pop(self) -> int:
        head = self.heap[0]
        # 配列をスライスしているので O(k) かかるがそれで良いのかと思ったが
        self.heap = self.heapify(self.heap[1:])
        return head
```

## step3（10分以内にさっとかける * 3回）
