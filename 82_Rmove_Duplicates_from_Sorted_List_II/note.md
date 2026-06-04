# 82. Remove Duplicates from Sorted List II

<https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/>

## step1（まず通す）

「次とその次を見て、値が重複していたらその値を覚えておき、ちがう値が出てくるまで次を繋ぎ替え続ける。重複してなかったら一つ進む」という考え方。スタートから重複する可能性もあるのでhead の前にダミーヘッドを用意してheadから重複判定を開始する必要がある。ダミーヘッドは本当の head と値が重複しないように `-100 <= Node.val <= 100` の外である必要がある。

## step2（整形＆他の人のコードを読む）

`does_duplicate_start` は条件分岐があってかつ return が False, True, False と並ぶのは認知不可高そう。`is None` だと長くなるが、単に `node` とか書けば短いので True になる条件一つ vs. その他は False の方がいいかも。

本体の方で、while のあとに if が来て処理が長い→else は短い処理なので、if の判定を入れ替えた方がいいかも。↑のコメントも T と F が入れ替わる形で。

変数名に略語を使うかどうかは流派によるだろうが、今回は関数名にも duplicate があるのでdup_val でもわかりそうと思いつつ、エディタが補完してくれるので略さずに書けというのもわかる。

いつ仕様が変わるかわからないのでマジックナンバー避けるべしというのも納得: <https://github.com/goto-untrapped/Arai60/pull/43#discussion_r1695376875>

if else で書くか if の中で continue して else の方は外で書くかだが、今回はネストが深くない方がいいので continue かな。

と思ったが、そもそも is_unique を関数化する意味が薄い気がして来た。関数の中身が一つの if else だけなので。そうなると、条件に否定がない方が見やすいと思うので結局元と同じ順番に戻った。

-1000 がマジックナンバーになっておりよくないので、 float("-inf") にしてみた。マイナスなのは、一応ソートされてて欲しいので。一応 int vs. float の型の違いはあるが int の最大みたいなのはないので一旦これで。

## step3（10分以内にさっとかける * 3回）
