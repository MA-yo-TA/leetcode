# 349. Intersection of Two Arrays

<https://leetcode.com/problems/intersection-of-two-arrays/>

## step1（まず通す）

set にして intersection をとってlist に戻す。

## step2（整形＆他の人のコードを読む）

intersection は `&` でも `set.intersection()` でも取れる。

### 違いは何？

<https://docs.python.org/3.14/library/stdtypes.html> によると

> Note, the non-operator versions of union(), intersection(), difference(), symmetric_difference(), issubset(), and issuperset() methods will accept any iterable as an argument. In contrast, their operator based counterparts require their arguments to be sets. This precludes error-prone constructions like set('abc') & 'cbs' in favor of the more readable set('abc').intersection('cbs').

つまりメソッドの方を使うと以下のように書ける。

```python
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_set = set(nums1)
        return list(nums1_set.intersection(nums2))
```

個人的には、可換な演算子というか、対等な2つを並べる時にメソッドで書くのそんなに好きじゃないかもしれない。`2.add(1)` みたいな感じに見える。

ただし、 `&` より `intersection` のほうがインターセクションだとわかりやすい（ `&&` とか `and` とかと混乱しない）という点ではメソッドの方が好ましいかもしれない。

また、メソッドは複数の引数を取れるので 3 つ以上の集合をまとめて処理したいときは見やすいかもしれない。

#### 自分になかった観点

「set 化はリストの全要素をハッシュ化してハッシュテーブルに挿入する(リサイズの可能性も含む)ので結構重い処理」

- <https://github.com/naoto-iwase/leetcode/pull/13#discussion_r2415407889>
  - メソッドの場合、CPython は内部的には引数が set の場合とそうでない場合を分けて処理している。
    - <https://github.com/python/cpython/blob/e7e3d1d4a8dece01b1bbd0253684d5b46b2409d7/Objects/setobject.c#L1409>
  - 引数が set でない場合、set にせずに「引数の要素をハッシュ化→ set にあったら result に挿入」という処理をするので set にしてから渡すよりも速そう
    - 単純に重い処理が少ないし、空間計算量も小さくてキャッシュにも乗りやすそう

ということで、短い方をセットにした方がいいだろうということで step2 を書いてみた

### set と intersection を使わずに書きたい場合

- <https://discord.com/channels/1084280443945353267/1303257587742933024/1319664094235594824>
  - <https://discord.com/channels/1084280443945353267/1303257587742933024/1319664094235594824>
  - 片方がとても大きくて、片方とてもて小さい、かつ大きい方がソートされているとき
    - コードや実験結果がとても参考になる
  - 両方がソート済みの場合は両方の配列を頭から見ていって、一致した数が出てきたら採用する、という方式が使える

とても勉強になる

## step3（10分以内にさっとかける * 3回）
