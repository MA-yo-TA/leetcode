# 111. Minimum Depth of Binary Tree

https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

## step1（まず通す）

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/ とほぼ同じ。

違う点は、一番深いところは全ノード見ないとがわからないが、一番浅いところは同じ高さごとに見ていって、最初に見つかった葉のところなのでそれ以降を見なくて済む。

再帰で自然に書くと全部見ることになる。

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```

例えば、

```txt
   0
 /  \
1    2
     /\
     ...（めっちゃ深い）
```

みたいな時にはだいぶ計算量が違う。

逆に、root から唯一の葉まで一本道みたいなときは見るノード数が同じになる。

## step2（整形＆他の人のコードを読む）

2点知りたいことがある

- [昨日のやつにいただいたコメント](https://github.com/MA-yo-TA/leetcode/pull/21#discussion_r3506905860) に関連して、next_layer の初期化は while の冒頭と nodes とセットでやるのとみなさんどちらで書いているのか
  - https://github.com/shintaro1993/arai60/pull/26/changes
    - この方は while の冒頭
    - ついでに depth の更新は while の最後
      - 自分としては「nodes があるなら一段加算」という気がするので while の判定の直後に書きたい気がしているが変な気もする
- while ループを return 以外で抜けることはないが、それを型チェッカーに示す方法としては何がいいのか。
  - 関数の末尾でエラーを出す？
  - raise RuntimeError("unreachable") しているもの
    - https://github.com/tom4649/Coding/pull/20/changes#diff-974436ac64380be2414ffa842d4dc5dd641279483233dca84985f0deee4311e2R24
    -

- https://github.com/tom4649/Coding/pull/20/changes#r2939305873
  - min_depth の初期値を float("inf") としていて、「ここの初期値はどんな感じで決められましたか？」「intのinfがないので、floatのinfで代用しました（質問の意図に合っているか分かりませんが）」とあるが、「（int からキャストできる float における）min() の単位元だから」というのが意図に沿った回答だろうか？
    - 単位元 `e` は、（Python 風にいうと）同じ型のオブジェクト `x` とその型の引数を二つ取る関数・メソッド・演算子 `f` に対して常に（どんな `x` でも） `f(e, x) = x` となるもの
    - counter を += で増やしていくなら 0
    - min なら float("inf")（か、絶対越えられない適当なデカい値）
    - max なら float("-inf") か 0（対象が自然数の場合）
  - メリットは初回の操作がおかしくならないので初回と2回目以降を同じように扱えること
  - 自分にも「ある変数を2項演算によって更新していくとき、初期値はその演算の単位元であるのが好ましい」という感覚がある
  - ただし、操作が行われなかったときに初期値をそのまま返すような場合は気をつけた方がいい。期待されている出力が異なることがあるので。
- https://github.com/garunitule/coding_practice/blob/main/Tree/111/memo.md
  - ここにも初期値をどうするかの議論がある
  - 2 << 30 や 1 << 30 が「絶対越えられない適当なデカい数」として上がっている

## step3（10分以内にさっとかける \* 3回）

結局ループでは最初から次のレイヤーを探しに行きたい気がして諸々の更新処理は全部最後にした。仕事の引き継ぎだとすると、朝来て「細かいところは昨日のやつ全部やっといてくれよ」と思いそう。
あとループの前に登場人物が全員見えてた方が落ち着く。
