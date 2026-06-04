# 82. Remove Duplicates from Sorted List II

<https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/>

## step1（まず通す）

「次とその次を見て、値が重複していたらその値を覚えておき、ちがう値が出てくるまで次を繋ぎ替え続ける。重複してなかったら一つ進む」という考え方。スタートから重複する可能性もあるのでhead の前にダミーヘッドを用意してheadから重複判定を開始する必要がある。

## step2（整形＆他の人のコードを読む）

## step3（10分以内にさっとかける * 3回）
