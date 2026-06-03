# 83. Remove Duplicates from Sorted List

<https://leetcode.com/problems/remove-duplicates-from-sorted-list/>

## step1（まず通す）

ソートされているので、重複するノードは連続してしか出てこない。なので、次のノードの値が今見てるノードの値と同じなら飛ばす（next を繋ぎかえる）、という発想。
連結リストのいいところは、ポインタを繋ぎかえるだけで挿入・削除ができるところ。

## step2（整形＆他の人のコードを読む）

## step3（10分以内にさっとかける * 3回）
