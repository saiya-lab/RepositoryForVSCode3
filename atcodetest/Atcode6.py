#ABC083B-Some Sums
#整数の入力
# n = int(input())
# A = int(input())
# B = int(input())
# #n_1 = int(str(n)[-1])
# #n_2 = int(str(n)[-2])
# #n_3 = int(str(n)[-3])

# box = []
# for m in range(1, n+1):
#     if A<= m <=B:
#         box.append(m)


# print(sum(box))
#入力の受け取り
N, A, B = map(int, input().split())
#初期化
total = 0
#各桁の和の計算
for i in range(1, N+1):
    digit_sum = sum(map(int, str(i)))
    if A<= digit_sum <=B:
        total += i

print(total)

