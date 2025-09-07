S = input().strip()[::-1]
#4つの文字列を逆純にする
words = ["dream", "dreamer", "erase", "eraser"]
words = [word[::-1] for word in words]

#文字列の探索
while len(S) > 0:
    matched = False
    for word in words:
        if S.startswith(word):
            S = S[len(word):]
            matched = True
            break
    if not matched:
        break

if len(S) == 0:
    print("YES")
else:
    print("NO")

#while len(S) > 0:: Sが空でない限りループを続けます。
# matched = False: この変数は、Sの現在の先頭がwordsのいずれの単語とも一致しない場合にFalseのままとなります。
# for word in words:: wordsリストの各単語に対してループを実行します。
# if S.startswith(word):: Sが現在のwordで始まっているかどうかを確認します。
# S = S[len(word):]: もしSがwordで始まっていれば、そのwordの部分をSから取り除きます。
# matched = True: Sがwordで始まっていたので、matchedをTrueに設定します。
# break: 一致した単語が見つかったので、内側のforループを抜けます。
# if not matched:: もしSの現在の先頭がwordsのどの単語とも一致しなかった場合、この条件がTrueとなります。
# break: 一致する単語がないため、whileループを終了します
