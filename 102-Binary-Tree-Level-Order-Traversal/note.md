# 102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

## step1（まず通す）

幅優先探索をする時に階層ごとにループを回せばいい。

ノード数 n に対して時間計算量 O(n)、空間計算量 O(n)

ノード数の上限は 2000 であり各ノードについて val の取得、子の None 判定とリストへの append などを行う程度なので、計算回数は `2000 * 10 = 2 * 10 ^ 4`くらい、計算時間は 数十 ms くらいか。

## step2（整形＆他の人のコードを読む）

- https://github.com/shintaro1993/arai60/pull/30/changes
  - この方もそうだし、問題タイトルや文でも level という語が使われている（し、level のほうがよく聞く気がする）ので layer -> level に変数名を変更
- https://github.com/naoto-iwase/leetcode/pull/30/changes#diff-40c0807c5c71abb50c5c8ebe78ffc21551f9ab6d80ccd6a156c960d1febd1882R19
  - 「キューにはNoneでないことを確かめていれる方が経験で見通しよく書けるので、そうする。」
  - 見通しの他に、None を探索詰めないことで探索回数が半分程度に減るというメリットもありそう。
- https://github.com/naoto-iwase/leetcode/pull/30/changes#diff-40c0807c5c71abb50c5c8ebe78ffc21551f9ab6d80ccd6a156c960d1febd1882R20
  - 「計算量 Time: O(V + E) = O(V), Space: O(width) = O(V)」
    - 自分では全部のノードを見るから O(V)、と雑に考えていたが、実際には高さの回数ループが回り、その中で同じ高さのノードの数だけループが回るという構造であることに気をつける必要がある
- https://github.com/tom4649/Coding/pull/25/changes
  - 変数名 traversal はちょっと変な気がするので、この方が使っている `values_by_level` とか他の方が書いていたような `level_by_level` がいいかもしれない

## step3（10分以内にさっとかける \* 3回）
