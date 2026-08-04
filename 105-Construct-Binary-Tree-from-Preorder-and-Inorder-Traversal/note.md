# 105. Construct Binary Tree from Preorder and Inorder Traversal

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

## step1（まず通す）

再帰で書くなら、

- preorder の先頭を取り出して、inorder の同じ数字を探す
- inorder の中で今見ているものより左にあるものは、左部分木、右にあるものは右の部分木
- preorder は順番を保ったまま左右に振り分け

単純にそのまま書いたが、配列のコピーや set にする処理が多く時間計算量で O(n^2) かかるので遅い。せめて添字で持つべき。

## step2（整形＆他の人のコードを読む）

- https://github.com/shintaro1993/arai60/pull/33/changes#diff-a286a96e11af3976f76d77e55be1edb9b540b1e2f1aabed1da12171208a553bcR24
  - 右の子を計算する時に node_index を node_index + split_index + 1 にすれば良い、というのに気づいていなかった

## step3（10分以内にさっとかける \* 3回）

stack でも書ける
