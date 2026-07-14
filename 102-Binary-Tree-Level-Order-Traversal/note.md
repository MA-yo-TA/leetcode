# 102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

## step1（まず通す）

幅優先探索をする時に階層ごとにループを回せばいい。

ノード数 n に対して時間計算量 O(n)、空間計算量 O(n)

ノード数の上限は 2000 であり各ノードについて val の取得、子の None 判定とリストへの append などを行う程度なので、計算回数は `2000 * 10 = 2 * 10 ^ 4`くらい、計算時間は 数十 ms くらいか。

## step2（整形＆他の人のコードを読む）



## step3（10分以内にさっとかける \* 3回）
