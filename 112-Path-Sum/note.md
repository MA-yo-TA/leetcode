# 112. Path Sum

https://leetcode.com/problems/path-sum/

## step1（まず通す）

ノードを全部探索して、条件に該当するものが見つかったら return true すればいい。

ループで書くなら (node, sum_so_far) みたいに持ちたい。その場合は深さ優先探索でも幅優先探索でもいいが、該当するパスが見つかった時点で return できるので深さ優先探索の方が見るノード数が少なくて済むことが多そう。
他の方のコードでよく見かける `forntiers` という変数名を使ってみた。

再帰でも書ける（step1-2.py）。一本道だと再帰呼び出しの回数がノード数（最大 5000）になるので、注意が必要（Python の再帰呼び出し回数の上限はデフォルトだと 1000）

## step2（整形＆他の人のコードを読む）

- https://github.com/naoto-iwase/leetcode/pull/29#discussion_r2455081026
  - 「もし葉でtargetSumになるような経路を返却するとしたらどうでしょうか？設問としてはTrue/Falseなのですが、単純にTrue/Falseを得るよりはpathを実際に知るほうが意味があるのかなと思ったので...自分が面接だったら質問しそうです。」
    - 葉から根へ向かうのは親を辿っていけば一本道でたどり着くので、探索しながら各ノードの親を覚えておく `node_to_parent: dict[TreeNode, TreeNode` 辞書を作って、葉から順番に辿っていけば良さそう。
- https://discord.com/channels/1084280443945353267/1225849404037009609/1258455843226255361
  - 「引き算先にしちゃって、...のほうが素直ではないでしょうか。」
    - 確かにそう。

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if root is None:
            return False

        children_target_sum = target_sum - root.val
        if root.left is None and root.right is None:
            return children_target_sum == 0

        return self.hasPathSum(root.left, children_target_sum) or self.hasPathSum(
            root.right, children_target_sum
        )
```

## step3（10分以内にさっとかける \* 3回）
