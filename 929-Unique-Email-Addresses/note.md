# 929. Unique Email Addresses

<https://leetcode.com/problems/unique-email-addresses/>

## step1（まず通す）

ひとまず、アドレスは制約を満たすようにバリデーションされている前提で考える。

パッと思いつくのは、

- まず `@` で local_name と domain_name に分ける
- local_name から、`+` で split して先頭だけをとってくる
- 残った部分から `.` を取り除く
- local_nameの残り@domain_name の形にして set に add

「一つのアドレスを 3 回くらい線形になめてハッシュテーブルに挿入」を 100 ループくらいなので、
配列の長さもアドレスの長さも 100 だとすると `(3 * 100 + set 化) * 100 ~ 数万-数十万` ステップくらい？ python だと1秒あたり100万-1000万ステップくらいなので数十 ms くらい？

実際 leetcode のジャッジで 57 ms くらいかかった。

## step2（整形＆他の人のコードを読む）

アドレス文字列を1度だけ先頭から見ていって処理すれば数倍は速いだろう。
やや複雑だし、2-3 倍くらいしか早くなってない。

### 自分で書き直したコードのバリエーション

```python
class Solution:
    def normalize(self, email: str) -> str:
        local_name = ""
        index = 0
        while index < len(email) and email[index] != "+":
            if email[index] == "@":
                return local_name + email[index:]
            if email[index] != ".":
                local_name += email[index]
            index += 1

        index = len(email) - 1
        while email[index] != "@":
            index -= 1

        return local_name + email[index:]

    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for email in emails:
            normalized_email = self.normalize(email)
            unique_emails.add(normalized_email)
        return len(unique_emails)
```

```python
class Solution:
    def normalize(self, email: str) -> str:
        local_name = ""
        index = 0
        while index < len(email) and email[index] != "@":
            if email[index] == "+":
                break
            if email[index] != ".":
                local_name += email[index]
            index += 1

        index = len(email) - 1
        while email[index] != "@":
            index -= 1

        return local_name + email[index:]

    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for email in emails:
            normalized_email = self.normalize(email)
            unique_emails.add(normalized_email)
        return len(unique_emails)
```

```python
class Solution:
    def normalize(self, email: str) -> str:
        local_name = ""
        index = 0
        after_plus = False
        while email[index] != "@":
            if not after_plus:
                if email[index] == "+":
                    after_plus = True
                elif email[index] != ".":
                    local_name += email[index]
            index += 1

        return local_name + email[index:]

    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for email in emails:
            normalized_email = self.normalize(email)
            unique_emails.add(normalized_email)
        return len(unique_emails)
```

### 他の人のコードを読む

- <https://github.com/naoto-iwase/leetcode/pull/14/changes>
  - replace の存在を忘れていた
    - この練習会で久しぶりにコードを書いているので結構組み込み型のメソッドとかを忘れている
    - 何かを調べるのではなくて全体を読む感じでドキュメントを眺めるのも有効かもしれない
  - インライン関数をよく見かける。 vs. クラスの別メソッドとして書くのトレードオフを理解したい
  - 正規表現は直感に沿うやり方
  - split で maxsplit 1 を指定する代わりに partition っていうメソッドもあるらしい
  - 不正な入力を弾くのは実用上大事そう
    - email address では何が「正しい」？
      - 思ったより使える文字種が多いしルールもまあまあ複雑なのでちゃんと書くと大変そう
        - RFC: <https://www.rfc-editor.org/info/rfc5322/> など
      - とはいえルールが明確なので地道に書いていけば良さそう
    - RFC違反のメールアドレスについて日本年金機構やドコモが注意喚起をしている
      - <https://www.nenkin.go.jp/denshibenri_kojin/n_net/attention/rfcmailaddress.html>
      - <https://www.docomo.ne.jp/service/docomo_mail/rfc_add/>
    - 違反してなくても `a!"\""@example.com` みたいなの（多分違反してない）をちゃんと処理できないソフトウェアもそこそこありそう？
      - だいたいライブラリを使うんだろうけど
    - この関数でやるよりは事前にやってて欲しい気がする
- <https://github.com/shintaro1993/arai60/pull/18>
  - ord （文字コード）には気をつけないといけない
    - a-z が連続しているとは限らない

問題の constraints だけだと
`.@example.com` が入力として許容されるのでおかしそう？

## step3（10分以内にさっとかける * 3回）
