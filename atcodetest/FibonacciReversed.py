#Atcoder beginner contest421
#X,Yの値を受け取る
# X = int(input())
# Y = int(input())

# def reverse_integer(X):
#     s = str(X)
#     reversed_s = s[::-1]
#     reversed_x =int(reversed_s)
#     return reversed_x

# def reverse_integer2(Y):
#     d = str(Y)
#     reversed_d = d[::-1]
#     reversed_y = int(reversed_d)
#     return reversed_y

# print(reverse_integer)
# print(reverse_integer2)

# f(x) を定義する関数
def f(x):
    # 整数を文字列に変換
    sx = str(x)
    # 文字列を反転
    rev_sx = sx[::-1]
    # 反転した文字列を整数に戻す
    return int(rev_sx)

# 入力 X, Y を読み込む
X, Y = map(int, input().split())

# 数列Aを格納するリストを初期化
a = [0] * 11  # インデックス1から10までを使用するため、サイズ11で作成

# a_1とa_2を設定
a[1] = X
a[2] = Y

# iが3から10までのa_iを計算
for i in range(3, 11):
    a[i] = f(a[i-1] + a[i-2])

# a_10 の値を出力
print(a[10])
