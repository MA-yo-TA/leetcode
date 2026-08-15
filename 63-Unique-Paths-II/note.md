# 63. Unique Paths II

https://leetcode.com/problems/unique-paths-ii/

## step1（まず通す）

考え方は https://leetcode.com/problems/unique-paths/ と同様で、「あるのマスへの行き方はそのマスの左と上への行き方の合計」。ただし、障害物があるところはいけないので 0。

スタート地点に障害物がある場合の扱いは少し迷ったが、左上から右下までの生き方が存在しない = 0 と考えそのようにした。

## step2（整形＆他の人のコードを読む）

https://github.com/h-masder/Arai60/pull/37

- ループの中でそのマスの左隣・下のインデックスが範囲内かをいちいち確認するとちょっと煩雑に見える可能性がある
  - num_paths の 外側 1行1列を 0 埋めする
  - 範囲チェックと後続処理をまとめて関数にする

などが議論されている

外側ゼロ埋めをやってみる。

## step3（10分以内にさっとかける * 3回）

- キャメルケースをやめ obstacle_grid に
- 1 は OBSTACLE という定数でおいて意味がわかりやすいように
