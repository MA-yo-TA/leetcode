# 53. Maximum Subarray

https://leetcode.com/problems/maximum-subarray/

k## step1（まず通す）

パッと思いつくのは、まず累積和を計算して、開始位置と終了位置について全探索。
ただし時間計算量が O(n^2) かかるので、`1 <= nums.length <= 10^5` だと長くて数十秒以上とかかかりそう。

問題を、「時系列データの増減を表したデータから、最大の上がり幅を求める」ものととらえてみた。
それで折れ線グラフをいろいろ書いて思いついた、より効率のいい方法として、累積和を計算したあとそれを前から見ていって

- 暫定的な最小値
- 「暫定最小値からの上がり幅」の暫定的な最大値

を更新していくというのがありそう。

Follow up を見ると devide and conquer でもっと上手いやり方があるということだが、リストを二つに割った時に解が両方にまたがる場合の処理などがパッとわからないので ↑ を書く。

## step2（整形＆他の人のコードを読む）

> nums が空の場合をどうしようか考え、sum 関数に空のリストを与えると0が返ってきて、こちらが使い勝手がいいかと思い0を返すようにしました。

https://github.com/shintaro1993/arai60/pull/36/changes#diff-4fa770c6b4c347fb912a16b384c6d437771e66e5af0ca845cfe46915ec4df0a4R9

自分のコードだと float("-inf") が返るようになっており、これは使う人を驚かせてしまうかも。（int かと思ったらそうじゃないというのも込みで）

用途によっては、リストが空 = 時系列データがない = 上がり幅は未定義ってことで None とかを返してもいいかもしれない。

> やっぱり初期値は nums[0] より -math.inf の方が考えやすい。

https://github.com/shintaro1993/arai60/pull/36/changes#diff-4fa770c6b4c347fb912a16b384c6d437771e66e5af0ca845cfe46915ec4df0a4R60

math.inf を知らなかった

> - アルゴリズムの選択
> - subarrayは連続しているので、貪欲的に解けそうだなと感じた。
> - 和が最大なsubarrayが、負の整数を跨いでいる場合が厄介。これを重点的に考察した。
> - そこまでの積み重ねのリターンが負の整数分差し引いても上回る場合、跨ぐ価値があると考察した。
> - 一般化して、nums[i]を第i世代の生涯収支とみなし、負になったら子供に相続させるのを取りやめるという例えがはまった。
> - この例えで、（相続分を含めた）財産が最大だった世代の財産を答えればよい。

https://github.com/naoto-iwase/leetcode/pull/37/changes

非常に面白い喩え。

ここで気になったのが、なんで 0 を閾値にしてリセットするのかということ。数列全体にオフセットを加えれば同じじゃないかと一瞬思ったが、1世代しかいないときを例にとるとその資産額は、0 からの差分で捉える（時系列グラフの時刻 0 の値が 0）なので、ということか。

```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_subarray_sum = -float("inf")
        accumulated = 0
        for num in nums:
            accumulated += num
            max_subarray_sum = max(accumulated, max_subarray_sum)
            accumulated = max(0, accumulated)

        return max_subarray_sum
```

> 各区間 `[L, R]` について、次の4つを返すようにします：
>
> 1. `total`: 区間全体の和
> 2. `best_prefix`: 区間の先頭から始まる最大部分和
> 3. `best_suffix`: 区間の末尾で終わる最大部分和
> 4. `best_subarray`: 区間内部の最大部分和
>
> これならマージができます。左右を `A`（左）と `B`（右）とすると、
>
> - `total = A.total + B.total`
> - `best_prefix = max(A.best_prefix, A.total + B.best_prefix)`
> - `best_suffix = max(B.best_suffix, B.total + A.best_suffix)`
> - `best_subarray = max(A.best_subarray, B.best_subarray, A.best_suffix + B.best_prefix)` ←これが“中央をまたぐ”
>
> ベースケースは単一要素 `x` のとき
> `total = best_prefix = best_suffix = best_subarray = x`。

https://github.com/naoto-iwase/leetcode/pull/37/changes#diff-52347f58ca1366895729356e24b384b058a947b881fb21e28e844969b8396244R55

分割統治はわかっていなかったが、こうすればできるのか。

## step3（10分以内にさっとかける \* 3回）

step1.py と同じアルゴリズムで書く
