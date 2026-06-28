# 695. Max Area of Island

<https://leetcode.com/problems/max-area-of-island/>

## step1（まず通す）

直前に解いた <https://leetcode.com/problems/number-of-islands/> とほぼ同じ。数える対象が違うだけ。

<https://leetcode.com/problems/number-of-islands/> では str の "0" or "1", こっちは int の 0 or 1 で海と陸が表現されているが、ゲームのマップとか地図データの処理とかそういうのを考えるといろんな地形をわかりやすい形で表現したいので [enum](https://docs.python.org/ja/3/library/enum.html) で管理したい。

(row, column) も、大規模なコードベースなら tuple[int,int] に Position とか名前をつけておきたいかも。

## step2（整形＆他の人のコードを読む）

- <https://github.com/shintaro1993/arai60/pull/22/changes>
  - やはり 0/1 だとわかりづらいので、この方は `WATER = 0` のように定数としておいている
- <https://github.com/naoto-iwase/leetcode/pull/18#discussion_r2424179923>
  - area のインクリメントをキューへの追加時にするのか取り出し時にするのか
  - 今回の自分のコードは、同じマスを2回キューに詰めないようにキューへ詰めたタイミングで seen への追加を行っており、area のインクリメントも同じところにまとめている

- <https://github.com/naoto-iwase/leetcode/pull/18#discussion_r2425068670>
  - itertools.product を使うと単純なn重ループのネストを浅くできる

enum を使う場合、int として比較したいので [IntEnum](https://docs.python.org/ja/3/library/enum.html#enum.IntEnum) を使う。そうすると、作成する maxAreaOfIsland の引数 grid の型も `list[list[NodeType]]` が良さそう。

## step3（10分以内にさっとかける * 3回）

- <https://github.com/MA-yo-TA/leetcode/pull/18#discussion_r3487683841>
  - やってる最中に一つ前の問題のレビューをいただいたので反映させた
