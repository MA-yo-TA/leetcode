# 103. Binary Tree Zigzag Level Order Traversal

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

## step1（まず通す）

node を取り出す時に値をチェックすると反転の扱いが面倒そうと考えて、詰める時にチェックするようにした。

フラグを用意して切り替えることも考えたが、2階層セットで書けば同じことの繰り返しなのでコードの重複部分が増える代わりに考えることが減ると思って書いた。

## step2（整形＆他の人のコードを読む）

実際書いてみると、奇数階層と偶数階層で異なるのは右の子を先に見るか左の子を先に見るかだけなのでここをフラグ化して関数に切り出してみる。

フラグによる切り替え部分は以下のようにも書ける。ちょっとパズル的で読みづらいかもしれない。

```python
            if left_first:
                if node.left is not None:
                    next_level_values.append(node.left.val)
                    next_level_nodes.append(node.left)

            if node.right is not None:
                next_level_values.append(node.right.val)
                next_level_nodes.append(node.right)

            if not left_first:
                if node.left is not None:
                    next_level_values.append(node.left.val)
                    next_level_nodes.append(node.left)
```

### 他の方のコード

- https://github.com/naoto-iwase/leetcode/pull/31/changes#diff-18873955c02f8e2268cf8385696e9d0aa7cce7bd5e4d5059818cb2903515da83R15
  - 「levelごとのvaluesは、level内では常にleft to rightで一旦貯めていき、複数レベルのリストに格納する直前に反転するかどうか決めたらいい。」
  - この単純な事実に気づいていなかった。「node を取り出す時に値をチェックすると反転の扱いが面倒そう」と思い込んでいたが実際にはそうではなかった。
  - ただしリストのコピーは発生する。
  - とはいっても、Python で高速化してもしょうがない面はあるので読みやすさ的にこれがよさそう。

## step3（10分以内にさっとかける \* 3回）
