# 98. Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

## step1（まず通す）

書きやすそうなのでひとまずは以下の再帰的な定義に従い再帰で書く

- None は valid
- 葉は valid
- 一般に、左右の子が valid かつ左の部分木の最大値 < ノードの値 < 右の部分木の最小値 なら valid

最大値最小値は、ノードが None の時は min max それぞれのの単位元になるようにする（こうすると比較もうまくいく）

ノード数の最大値が `10 ^ 4` なので、再帰呼び出し回数が Python のデフォルトの上限を超えうる。
時間計算量、空間計算量はノード数 N に対して O(N), O(N) である。再帰的な関数呼び出しも考えると、最大で 数十 ms 〜 数百 ms 程度か。

## step2（整形＆他の人のコードを読む）

## step3（10分以内にさっとかける \* 3回）
