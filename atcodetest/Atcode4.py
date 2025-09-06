#ABC081B - Shift only
#整数Nを入力として受け取る
N = int(input())

#N個の整数を入力として受け取る
A = list(map(int, input().split()))

#操作の回数を初期化
count = 0
#すべての整数が偶数である限りループを続ける
while all(a % 2 == 0 for a in A):
    #各整数を２で割る
    A = [a // 2 for a in A]
    #操作の回数をインクリメント→値を一つずつ増やすためのもの
    count += 1

print(count)
