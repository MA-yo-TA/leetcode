# 142. Linked List Cycle II

<https://leetcode.com/problems/linked-list-cycle-ii/>

## step1（まず通す）

141 において set で書いたのならば、ほぼ同じコードで良い

迷ったポイントは、

```python
            if current_node in visited_nodes:
                return current_node

        return None
```

と書くか

```python
            if current_node in visited_nodes:
                break

        return current_node
```

と書くかだが、下は読み手にとって戻り値が正しいのかを理解するのにワンテンポ余計にかかる感じがしたので、「もう一回たどり着いたノードがあればそれがサイクルの先頭、そういうものがなかった時は None を返す」とより素直に読めそうな上を採用した。

Floyd の方法だが、[典型コメント集](https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?usp=sharing)にあった「逆再生」の説明は自分にとってはやや理解に時間がかかったので、自分にとってわかりやすい別の説明を考えてみた。

```txt
fast と slow が「サイクルの中にいて、両者の（周回を考慮した）位置がサイクルの長さの整数倍だけ離れている」とき、両者の位置は一致するし、一致したなら「」の条件が満たされている。

なので、fast と slow が出会ったとき fast - slow の差 = slow の位置 (2倍なので) は サイクルの長さの整数倍である。

そこで、出会ったタイミングで slow だけをスタート地点に戻し、今度は両者同じ速さで進めると、スタートからずっと両者の距離はサイクルの長さの整数倍が保たれていて、slow が最初にサイクルに踏み入った地点で「」の条件が満たされるので両者は出会う。逆にサイクルに踏み入るまでは出会うことはない。
```

ちょっと書くことが増えるので、注意しないと読みづらくなりそうと感じた。

## step2（整形＆他の人のコードを読む）

## step3（10分以内にさっとかける * 3回）
