# 121. Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

## step1（まず通す）

先頭から見ていって、(それまでの最小値, 最大の上がり幅) を記録しながら進む。

## step2（整形＆他の人のコードを読む）

> prices が空の場合は、何を返すことが想定されているでしょうか。

https://discord.com/channels/1084280443945353267/1206101582861697046/1219181674038820945

> 空を返すのも一つですね。
> exception を投げるのも一つです。これはコードを追いにくくなるので、嫌うところは嫌います。
> 他に、abort する手もあります。
> https://en.cppreference.com/w/cpp/utility/program/abort
> Google は、user facing ではないパイプラインなどで LOG(FATAL) をよく使っていました。エラーメッセージを出して止めてしまうということです。
> https://rpg.ifi.uzh.ch/docs/glog.html
> こういうのは状況次第なのでどうしたらいいかを考えてみましょう。
> あと、問題を解いたら、同じのを解いている人のコメントを見るといいかもしれません。

https://discord.com/channels/1084280443945353267/1206101582861697046/1216960850267476071

自分としては、（この関数の使われ方にはもちろん依るが）0 でも良いのかなという気がした。
価格の時系列があって儲けが出ない時に 0 を返すことは規定されていて、であれば価格の時系列がない=売り買いできない→儲けが出ないという理屈。

> 関数型っぽい感覚

https://github.com/goto-untrapped/Arai60/pull/58#discussion_r1782742318

最初に書いたコードであまりいじるところがなかったので、step2.py は関数型っぽく書いてみた

## step3（10分以内にさっとかける \* 3回）


