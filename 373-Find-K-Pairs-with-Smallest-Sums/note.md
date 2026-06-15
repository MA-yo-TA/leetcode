# 373. Find K Pairs with Smallest Sums

<https://leetcode.com/problems/find-k-pairs-with-smallest-sums/>

## step1（まず通す）

素朴に考えると全部の和をとってヒープに詰めて上位を取り出すことになるが和を取るところで m := nums1.length, n:= nums2.length として O(m*n) になって遅い。

もう少し考えると、2つの配列が昇順にソートされているし欲しいのは k smallest なので多く見積もっても書く配列の先頭から k 番目までだけ見れば良い。
そうなると、 和を取る部分は O(k^2) で制約的に k は m,n より一桁小さいのでだいぶマシ。
ヒープ化は線形時間かかるけど push, pop は 対数時間でいいのでヒープの長さが k になるまでは普通に push して、k を超えたら pushpop すると良さそう。
ただしこれでも O(k^2 log k) くらいあって k <= 10^4 とかなので 数百 ms ~ 数 s かかりそう。（実際 TLE した。）

他の方法を考える。
残っている中で最も小さいやつを順番に記録していくとすると

- 最初に和が一番小さいのは先頭同士
- それ以降で一番和が小さいのは、それまでに記録されたペアのどちらかのインデックスを1だけ大きくしたやつ（行列にすると今まで記録したペアの右か下）

これだとヒープに詰める log k がないのでその分早いか？
と思って書いたコードが

```python
class Solution:
    def find_next_smallest_pair(
        self,
        nums1: List[int],
        nums2: List[int],
        seen_index_pairs: Set[Tuple[int, int]],
        k_smallest_pairs: List[List[int]],
    ):
        next_smallest_index_pair = []
        next_smallest_sum = float("inf")
        for index_pair in seen_index_pairs:
            index1 = index_pair[0] + 1
            index2 = index_pair[1]
            if (
                (index1, index2) not in seen_index_pairs
                and index1 < len(nums1)
                and index2 < len(nums2)
            ):
                sum = nums1[index1] + nums2[index2]
                if sum < next_smallest_sum:
                    next_smallest_index_pair = [index1, index2]
                    next_smallest_sum = sum

            index1 = index_pair[0]
            index2 = index_pair[1] + 1
            if (
                (index1, index2) not in seen_index_pairs
                and index1 < len(nums1)
                and index2 < len(nums2)
            ):
                sum = nums1[index1] + nums2[index2]
                if sum < next_smallest_sum:
                    next_smallest_index_pair = [index1, index2]
                    next_smallest_sum = sum

        seen_index_pairs.add((next_smallest_index_pair[0], next_smallest_index_pair[1]))
        num1 = nums1[next_smallest_index_pair[0]]
        num2 = nums2[next_smallest_index_pair[1]]
        k_smallest_pairs.append([num1, num2])

    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        seen_index_pairs = set()
        seen_index_pairs.add((0, 0))
        k_smallest_pairs = [[nums1[0], nums2[0]]]
        while len(k_smallest_pairs) < k:
            self.find_next_smallest_pair(
                nums1, nums2, seen_index_pairs, k_smallest_pairs
            )

        return k_smallest_pairs

```

しかし、これは結局 k 回の while ループごとに 2k 個くらいの値を見てるのでまだ効率が悪い。

わからないので他の人のコードを見る。

- <https://github.com/shintaro1993/arai60/pull/14/changes#diff-39cc9cee3d79ce9bea375f8ce45d130675c35bfce12bf5471ba4a3b3dd897ad6R45>

**自分なりの解釈**

ヒープに常に現在の最小ペアが入っていることがわかっていればただ pop すればいい。

どうすればそ条件が満たせる？

> nums1 のすべての要素と nums2[0] の要素でペアを作り、初期値としてヒープに入れておく。ヒープから和の最小値のペアが取り出されるごとに、取り出したペアの nums1 の要素はそのままで、nums2 の要素は次のものにしたペアをヒープに追加する。ヒープには初期値として nums1 と nums2 のリストのサイズが小さいほうで初期化し、ヒープから一つ取り出すごとに一つ追加していくので、この処理の最中に使うメモリは初期化したサイズで考えてよさそうだと思います。全体としては、返却用のリストを作っているので空間計算量は O(k) になるでしょうか。

それはなぜ？

あるペアが次に最小になるのは、そのペアよりどちらかが若いものが全部チェックされたあとに限る。途中で考えていた発想は、そのペアよりどちらかが若いものが一つでも入っていれば可能性があるとしていたが条件が緩すぎた。少なくともそのペアより片方が若いものが全てチェックされるまではヒープに入れなくていい。

逆に、ペア両方を見るのは大変なので、ある程度はヒープの挿入・削除が対数時間なのに任せて「片方だけについてより若いもの全てがチェックされたら次の候補に入れる」とした方がロジックがわかりやすい。

## step2（整形＆他の人のコードを読む）

変数にしなくていいような箇所が多いので整理する。変数名も簡潔に。

## step3（10分以内にさっとかける * 3回）
