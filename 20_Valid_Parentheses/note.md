# 20. Valid Parentheses

<https://leetcode.com/problems/valid-parentheses/>

## step1（まず通す）

文字列を先頭から見ていって

- 開きカッコ→スタックに積む
- とじカッコ→スタックが空じゃなくて、topが対応する開きカッコならそれをpopする。対応してなかったら即NG

最後にスタックが空になってたらOK

## step2（整形＆他の人のコードを読む）

- opens は文字列で書いてもよかったかも（文字数が少なくてタイプが楽だし見やすそう）
- コメント集： 「"[aiu](eo)" が入力としてきたときに、プログラムの挙動として好ましいのは何だと考えますか?」
  - →カッコに着目して妥当かを判断するプログラムであるのが良いか、あるいは要件によってはカッコ以外が入っていたらエラーを出して止まって欲しい、となるかもしれない。
  - 他の文字を許容して括弧に着目した妥当性を判断する場合は、opens の他に closes も用意して、どちらでもない場合はスルーするようにする、というのが良さそう
    - そうすると、for で回す変数は parenthesis じゃなくて character とかになりそう
- スタックが空になってたら True, そうじゃないなら False → not stack を返すことで見た目がスッキリする
  - <https://github.com/X-XsleepZzz/leetcode/pull/7/changes>
  - 取り組んでいる間にいただいたコメントで教えていただいたスタイルガイドでも、list が空かどうかは "implicit" な boolean で書けと指定されている
    - <https://github.com/MA-yo-TA/leetcode/pull/6#discussion_r3369098265>

## step3（10分以内にさっとかける * 3回）

書いていて気づいたが、step2.py だと括弧の種類が増減した時に opens/closes/close_to_open の3つを書き換えないといけないので、opens/closes を close_to_open.values() close_to_open.keys() にした方がいいかも。ただしその場合でも、読み書きする時に .keys(), .values() だとどっちがどっちか混乱するので、変数に格納しといた方が読みやすそう。

## step4

いただいたコメントに沿って書き直してみる
