# 387. First Unique Character in a String

<https://leetcode.com/problems/first-unique-character-in-a-string/>

## step1（まず通す）

- 複数回出現するかをみるためには先頭から頭まで全部の要素を見る必要がある
- 重複していないもののうち一番前にあるやつを出力するのでもう一度文字列を見る必要がありそう？

以下のようなことをして一度の操作でできないか考えたけど、全部の要素を見ないと重複しているかが確定しないので難しそう

- まずリスト線形に走査して出現回数を数えて、1 回のものを探すためにもう一度先頭から見ていく
- リストの末尾から見ていって、暫定的に重複していない最後（後ろから見ていくのでリストの先頭側）の文字の index を覚えておく。それを更新していく。

## step2（整形＆他の人のコードを読む）

unique_character を作る必要はなくて、単に Counter の値が1かを見ればよかった。

Counter は dict のサブクラスで、dict と同様 3.7 以降は挿入順を維持することが言語仕様で決まったので Counter のキーを順番に見ていって value が 1 ならインデックスを探して即リターンできる。

- <https://docs.python.org/ja/3.13/library/stdtypes.html#dicthttps://docs.python.org/ja/3.13/library/stdtypes.html#dict>
- <https://docs.python.org/ja/3.13/library/collections.html#collections.Counter>

str.index()の挙動は以下なので、該当するインデックスを探す処理が step1 のような python でループを書くより速そう

- unicode_index_impl
  - <https://github.com/python/cpython/blob/main/Objects/unicodeobject.c#L11698>
- ↑の実体である any_find_slice
  - <https://github.com/python/cpython/blob/main/Objects/unicodeobject.c#L9522>
  - any_find_slice では index() の引数の長さが 1 のとき、findchar を呼ぶ
    - <https://github.com/python/cpython/blob/main/Objects/unicodeobject.c#L9544>
- findchar は 文字種（何倍と文字か）ごとに処理を分けている
  - <https://github.com/python/cpython/blob/main/Objects/unicodeobject.c#L1004>
- 最終的に memchr/wmemchr という c の標準ライブラリに行き着く

例えば、`"aaaaaaa...aaaab"` みたいな、文字種数は少ないが答えが出てくるのが最後の方というケースではかなり速くなるはず。

### 実験してみた（benchmark.py）

こう見ると、

- unique_character を得るための set 化は文字列が長い時はほぼ誤差なくらい小さい（英小文字で 26 種と、文字の種類が少ないから）
- インデックスを探す部分が step1 の python のループに比べて str.index() がめちゃくちゃ速い（C で動くから）

注意：

- 表示されている時間はすべて REPEAT 回分の合計
- 実際の1回の呼び出しはインタープリタのオーバーヘッドがあるのでもっとかかる & 実験で見えている差は薄まる

```txt
> python benchmark.py
case                                  step1 (ms)   step2 (ms)   winner
-----------------------------------------------------------------------
'leetcode'                                 0.740        0.519    step2
'loveleetcode'                             0.811        0.600    step2
'aabb'                                     0.474        0.441    step2
'zzzzzzzzzzzzzzz…a' (len=10001)          271.670      155.136    step2
'azzzzzzzzzzzzzz…z' (len=10001)          158.467      156.757    step2

-- cost breakdown (REPEAT=1000) --

  [unique at end]
    Counter only          :  156.362 ms
    Counter + set (step1) :  155.801 ms
    python loop (step1)   :  269.456 ms  (scan only: +113.656 ms)
    s.index scan (step2)  :  156.773 ms  (scan only: +0.411 ms)
    scan ratio (py/idx)   :   276.79x

  [unique at start]
    Counter only          :  154.897 ms
    Counter + set (step1) :  156.597 ms
    python loop (step1)   :  157.018 ms  (scan only: +0.421 ms)
    s.index scan (step2)  :  156.023 ms  (scan only: +1.125 ms)
    scan ratio (py/idx)   :     0.37x
```

### 他の人のコードを読む

- <https://github.com/naoto-iwase/leetcode/pull/15/changes>
  - インデックスも記録しておけばさがしにいかなくていい、というやり方
- <https://github.com/t0hsumi/leetcode/pull/15#discussion_r1930362913>
  - 「1度しか出てこない」を「find （左から探索した時に最初に見つかる index） と rfind （右から〃）が一致する」と言い換えたコード
    - 計算量としては2乗になるが、find, rfind が c で実装されているので文字列の長さがそれなりに短ければ結構速そう（index が速いのと同じような理由）

これも書いてみる

## step3（10分以内にさっとかける * 3回）
