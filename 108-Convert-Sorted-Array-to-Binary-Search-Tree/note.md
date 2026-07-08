# 108. Convert Sorted Array to Binary Search Tree

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

## step1（まず通す）

元の配列がソートされているので、二分探索する要領で左右配列の分かれ目（中間）を繋いでいけばいい
再帰で書くのがわかりやすい。

## step2（整形＆他の人のコードを読む）

ループでも書く。部分配列を毎回スタックに詰めるのは効率が悪いので、区間の先頭と末尾のインデックスだけ持つようにする。step1.py は毎回配列をスライスしているのでちょっと遅い。スライスする長さは木の階層ごとに半分ずつになっていくのでn := len(nums) としたとき時間計算量は O(n log n)。

- https://github.com/naoto-iwase/leetcode/pulls
  - 「（再帰の base case は）1も含めると直感で倍速くなる。(二分木の構造または本問の再帰構造より）」
    - 確かにそうだ。葉の左右の子（None）に対する関数呼び出しがなくなるので。
- https://github.com/shintaro1993/arai60/pull/28/changes#diff-5db3d349f04f651e2faacefca7e2937a523f2fd8c8b6cbd30ad1e7ed699f8d3aR36
  - 添え字の再帰

```python
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def interval_to_BST(head, tail) -> Optional[TreeNode]:
            if head == tail:
                return None

            center = (tail + head) // 2
            return TreeNode(
                val=nums[center],
                left=interval_to_BST(head, center),
                right=interval_to_BST(center + 1, tail),
            )

        return interval_to_BST(0, len(nums))
```

- https://github.com/shintaro1993/arai60/pull/28/changes#diff-5db3d349f04f651e2faacefca7e2937a523f2fd8c8b6cbd30ad1e7ed699f8d3aR91
  - 添え字の範囲について。「自分は、0 と len(nums) で始めるのが好きだと思った。」私も同じ好み。

## step3（10分以内にさっとかける \* 3回）
