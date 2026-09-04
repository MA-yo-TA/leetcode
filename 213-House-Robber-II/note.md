# 213. House Robber II

https://leetcode.com/problems/house-robber-ii/

## step1（まず通す）

輪になっていない場合（198. House Robber）は、目の前の家までで盗める最高額は以下二つの max だった:

- 目の前から盗まない→一つ前の家までの最高額
- 目の前から盗む→二つ前の家までの最高額 + 今の家で盗める額

輪になっていると、リストの先頭と末尾以外は今までと同じだが、先頭と末尾は両方から盗むことはできないので、

1. 先頭を入れてもよくて目の前の家までで盗める最高額
2. 2つ目の家からから始めて（先頭を含めずに）目の前の家までで盗める最高額

の2つを計算し続け、最後の家の 2 と一つ前の家の 1 を比較することになる。

## step2（整形）

append するより最初にlen(nums) の長さを確保した配列用意してから値を入れていく方が見やすいかも。（漸化式っぽい見た目になるので）
→書いてみたが別にそんなことはなかった。初期化の行が増えるだけみづらいかも。

```python
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        max_monies_from_begin = [0] * len(nums)
        max_monies_from_begin[0] = nums[0]
        max_monies_from_begin[1] = max(nums[0], nums[1])

        max_monies_without_begin = [0] * len(nums)
        max_monies_without_begin[1] = nums[1]
        for i in range(2, len(nums)):
            max_monies_from_begin[i] = max(
                max_monies_from_begin[i - 1],
                max_monies_from_begin[i - 2] + nums[i],
            )
            max_monies_without_begin[i] = max(
                max_monies_without_begin[i - 1],
                max_monies_without_begin[i - 2] + nums[i],
            )

        return max(max_monies_from_begin[-2], max_monies_without_begin[-1])
```

198. House Robber と同じく、配列は不要で2つ前まで覚えていればいいのでそれで書く。

## step3（10分以内にさっとかける \* 3回）

prev と prevprev を return するのは違和感あったので変数名を変えた（これでもあんまりいいとは思わないが）

## step4

> 同じロジックを 2 回書くより、ロジックを関数にくくりだし、開始インデックスと終了インデックスを 2 種類渡して max を取るほうがシンプルになると思いました。

これで書いてみる

実質的な初期値（`nums[begin]` など）をあらかじめ代入して range(begin + 2, end) でループするか、仮の初期値 0 を入れておいて range(begin, end) でループするかは迷う。みて意味がわかりやすいのは前者な気がするが、配列のインデックスの範囲を気にする必要がありちょっと煩雑か。
