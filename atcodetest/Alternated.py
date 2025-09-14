S = input()
N = len(S) // 2

# パターン1: ABAB...
# Aが偶数番目、Bが奇数番目に配置されるパターン
count1 = 0
for i in range(N):
    # Aの理想的な位置: 2*i
    # Bの理想的な位置: 2*i+1
    if S[2*i] == 'B':
        count1 += 1
    if S[2*i+1] == 'A':
        count1 += 1

# パターン2: BABA...
# Aが奇数番目、Bが偶数番目に配置されるパターン
count2 = 0
for i in range(N):
    # Aの理想的な位置: 2*i+1
    # Bの理想的な位置: 2*i
    if S[2*i] == 'A':
        count2 += 1
    if S[2*i+1] == 'B':
        count2 += 1

print(min(count1, count2))
