# 63. Unique Paths II

https://leetcode.com/problems/unique-paths-ii/

## step1（まず通す）

考え方は https://leetcode.com/problems/unique-paths/ と同様で、「あるのマスへの行き方はそのマスの左と上への行き方の合計」。ただし、障害物があるところはいけないので 0。

スタート地点に障害物がある場合の扱いは少し迷ったが、左上から右下までの生き方が存在しない = 0 と考えそのようにした。

## step2（整形＆他の人のコードを読む）

## step3（10分以内にさっとかける * 3回）
