# 返り値を使う再帰をループで書くためのメンタルモデル

一番大事な考え方は次のとおり。

> 再帰は「関数が自分を呼んでいる」のではなく、未完了の作業をコールスタックに積んでいる。
> ループ化するときは、その未完了の作業を自分でスタックに積む。

特に返り値を使う再帰では、各関数呼び出しを次の情報を持つ「作業フレーム」と考える。

- 今どのノードを処理しているか
- 子の処理は終わったか
- 子から返ってきた値をどこに保存するか

## 再帰を依存関係として見る

今回の再帰は、抽象化すると次の形になっている。

```python
def solve(node):
    if node is None:
        return BASE

    left_result = solve(node.left)
    right_result = solve(node.right)

    return combine(node, left_result, right_result)
```

親の答えは、左右の子の答えが出るまで計算できない。

```text
左の答え ─┐
          ├─> 親の答え
右の答え ─┘
```

したがって、処理順は次のような postorder（帰りがけ順）になる。

```text
左 → 右 → 親
```

## 「入る」と「戻ってくる」を明示する

再帰呼び出しでは、同じノードを概念的に2回通る。

1. ノードに入ったとき
2. 子の処理を終えて戻ってきたとき

再帰では、言語のランタイムが「子を処理した後にどこから再開するか」をコールスタックに保存してくれる。

ループでは、それを `(node, children_done)` のような値として自分でスタックに保存する。

```python
def is_valid_bst(root):
    base = (True, float("inf"), float("-inf"))

    results = {None: base}
    stack = [(root, False)]

    while stack:
        node, children_done = stack.pop()

        if node is None:
            continue

        if not children_done:
            # 左右の処理後に、もう一度このノードへ戻ってくるための予約
            stack.append((node, True))

            # stack は後入れ先出しなので、左を先に処理するには
            # 右、左の順で積む。
            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            # この時点では、左右の結果がすでに results に入っている。
            left_valid, left_min, left_max = results[node.left]
            right_valid, right_min, right_max = results[node.right]

            results[node] = (
                left_valid
                and right_valid
                and left_max < node.val < right_min,
                min(left_min, right_min, node.val),
                max(left_max, right_max, node.val),
            )

    return results[root][0]
```

ここで、

```python
stack.append((node, True))
```

は次のような「続きの予約票」だと考える。

> 左右の子の処理が終わったら、このノードに戻って続きを実行する。

`children_done=False` は再帰関数に入った直後、`children_done=True` は再帰呼び出しから戻ってきた直後に対応する。

## 小さな木でスタックの動きを追う

次の木を考える。

```text
    2
   / \
  1   3
```

最初のスタックは次の状態。

```text
[(2, 入る)]
```

`2` に入ると、`2` の続きと左右の子を積む。

```text
[
    (2, 子の後),
    (3, 入る),
    (1, 入る),
]
```

スタックの末尾から取り出すので、実際の処理順は次のようになる。

```text
1 に入る
1 の子の後
3 に入る
3 の子の後
2 の子の後
```

ノードの答えを確定する順番は `1 → 3 → 2` となり、postorder になっている。

## 「返り値の置き場所」が必要

再帰では、子の返り値をローカル変数で受け取れる。

```python
left_result = solve(node.left)
```

ループでは子の処理と親の処理が別々のイテレーションになるため、返り値をどこかに保存する必要がある。

上の例では次の辞書がそれに当たる。

```python
results[node] = result
```

親を処理するときに、左右の子の結果を辞書から取得する。

```python
left_result = results[node.left]
right_result = results[node.right]
```

つまり、再帰からループへの機械的な対応は次のようになる。

| 再帰で暗黙に行われること | ループで明示するもの |
| --- | --- |
| 呼び出し中のノードを覚える | `stack` の `node` |
| 子の後に戻る場所を覚える | `children_done` |
| 子の返り値を受け取る | `results` |
| コールスタックから戻る | `stack.pop()` |

## 毎回、機械的に変換する必要はない

機械的変換は汎用的だが、問題の定式化を変えるともっと簡単になることがある。

元の実装は、子から親へ情報を返している。

```text
子の最小値・最大値 → 親
```

BST の条件は、「このノード以下で許される値の範囲」を親から子へ渡す形にもできる。

```text
親が持つ許容範囲 → 子
```

```python
def is_valid_bst(root):
    stack = [(root, float("-inf"), float("inf"))]

    while stack:
        node, lower, upper = stack.pop()

        if node is None:
            continue

        if not lower < node.val < upper:
            return False

        stack.append((node.right, node.val, upper))
        stack.append((node.left, lower, node.val))

    return True
```

この形では、スタック上の各作業がそれ単体で完結している。

```text
このノードの値が (lower, upper) の範囲内か調べる
```

子の答えを待つ必要がないため、「戻ってくる」状態や結果保存用の辞書も不要になる。

## inorder が狭義単調増加であることとの同値関係

LeetCode 98 では、valid BST は各ノードについて次の条件を満たす木として定義されている。

- 左部分木のすべての値は、そのノードの値より小さい。
- 右部分木のすべての値は、そのノードの値より大きい。
- 左右の部分木も valid BST である。

このように厳密不等号で定義された有限の二分木では、次の2つは同値になる。

> valid BST である
>
> ⇔
>
> inorder traversal で得られる値の列が狭義単調増加である

ここでいう狭義単調増加は、隣り合うすべての値について次が成り立つことを指す。

```text
a[0] < a[1] < a[2] < ...
```

### valid BST なら inorder は狭義単調増加

inorder traversal は、各ノードを次の順番で走査する。

```text
左部分木 → ノード自身 → 右部分木
```

valid BST では、左部分木のすべての値がノード自身より小さく、右部分木のすべての値がノード自身より大きい。また、左右の部分木も valid BST である。

したがって、inorder で得られる列全体が狭義単調増加になる。

### inorder が狭義単調増加なら valid BST

あるノードを根とする部分木の inorder は、必ず次の順番になる。

```text
左部分木の全ノード → ノード自身 → 右部分木の全ノード
```

この列が狭義単調増加なら、左部分木のすべての値はノード自身より小さく、右部分木のすべての値はノード自身より大きい。

また、各部分木の inorder は列全体の連続した部分列なので、それぞれも狭義単調増加である。同じ議論を部分木に再帰的に適用できるため、木全体が valid BST になる。

この同値関係を使うと、直前に訪問した値だけを覚えて判定できる。

```python
def is_valid_bst(root):
    stack = []
    node = root
    previous = None

    while node is not None or stack:
        while node is not None:
            stack.append(node)
            node = node.left

        node = stack.pop()

        if previous is not None and previous >= node.val:
            return False

        previous = node.val
        node = node.right

    return True
```

`previous >= node.val` を不正とする点が重要である。例えば `1, 2, 2, 3` は広義には昇順だが、狭義単調増加ではないため、LeetCode 98 の定義では valid BST ではない。

なお、「重複値は右部分木だけに許す」のような別の定義では、inorder が広義単調増加であることだけでは配置規則を判定できない。今回この同値関係がきれいに成り立つのは、問題文が左右の大小関係を厳密不等号で定義しているためである。

## 考える順番

返り値を使う再帰をループにするときは、次の順番で考える。

1. 親の計算には、子の返り値が必要か。
2. 必要なら、処理順は基本的に postorder になる。
3. `(node, 入る／戻る)` をスタックに持たせて機械的に変換する。
4. 各呼び出しの返り値を `results[node]` などに保存する。
5. その後で、子から返す値を「親から子へ渡す引数」に変えられないか考える。

今回の問題では、次の2通りがある。

- 機械的変換：`children_done` と `results` を使う。
- 問題に合わせた変換：許容範囲を親から子へ渡す。

まずは機械的変換を確実にできるようにする。そのうえで、より単純な定式化がないかを探す。

特に、

> `children_done=True` は、再帰呼び出しから戻ってきた場所

と捉えると混乱しにくい。
