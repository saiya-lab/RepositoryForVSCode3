#Atcoder Beginner contest421
#部屋の数Nを読み込む
N = int(input())
#N人の住人名をリストとして読み込む
S = input().split()
#宛先の部屋番号と宛名yを読み込む
X, Y = input().split()
#部屋番号を0-based indexに変換
index = int(X) -1

if S[index] == Y:
    print("Yes")
else:
    print("No")

# print("Yes" if S[X-1] == Y else "No")
#
