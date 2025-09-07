# ABC087B-Coins
# 500円玉をAマイ
#a = int(input())

#a_int = a * 500

#b = int(input())

#b_int = b * 100

#c = int(input())

#c_int = c * 50

#x_sum = a_int + b_int + c_int
#while all(x % 50 == 0 for x_sum in X):

#入力の受け取り
A = int(input())
B = int(input())
C = int(input())
X = int(input())

#初期化
count = 0

#組み合わせの計算
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if 500*a + 100*b + 50*c == X:
                count += 1

print(count)
