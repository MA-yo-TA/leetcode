# 347. Top K Frequent Elements

<https://leetcode.com/problems/top-k-frequent-elements/>

## step1（まず通す）

値→回数でカウントした後に回数→値の変換が高速にできて回数の大小でトータルオーダーのものが欲しいと思って Frequency を定義したけど冷静に考えると [回数, 値]のリストで良かった（List の順序は辞書順で判定）。

nums の長さを n としたとき、時間計算量は

- カウント部分が O(n)
- ヒープ化が O(n)
- 取り出すところが pop O(log n) をk 回で O(k log n)

なので O(k * log n)

空間計算量は長さ n か k の配列（中身は固定サイズ）をいくつか持っているのとあとは定数だけなので O(n)

## step2（整形＆他の人のコードを読む）

ひとまずリストで書いてみた。

- <https://github.com/potrue/leetcode/pull/9/changes>
  - 自分が欲しかったものとして bidict というやつがあるらしい
    - <https://pypi.org/project/bidict/>
  - 自分の手でアルゴリズムを書かないとしたら Counter が便利
  - 逆引き辞書を `{回数: [その回数出てきた値のリスト]}` で持っておけばバケットソートできて速そう
  - クイックセレクトという、クイックソートの類似のアルゴリズムがあるらしい
  - ヒープじゃなくてソートして先頭k個を取ってくるなら、`{値: 回数}` 辞書のまま value でソートするという方法があるらしい
    - <https://github.com/potrue/leetcode/pull/9/changes#r2083373096>
- heapq.heapify_max() などの max 系は 3.14 から使えるようになった新しい機能
  - <https://docs.python.org/ja/3.14/library/heapq.html>
  - minheap しか使えないなら回数を符号反転で持つことで解決できる

## step3（10分以内にさっとかける * 3回）
