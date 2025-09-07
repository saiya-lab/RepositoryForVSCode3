#ABC088B-Card Game for Two
#入力の受け取り
N = int(input())
a = list(map(int, input().split()))
#↑各カードに書かれている数のリストaを受け取る

a.sort(reverse=True)
#リストaを降順にソートする

alice_score = sum(a[i] for i in range(0, N, 2))
bob_score = sum(a[i] for i in range(1, N, 2))
#ソートされたリストａを順番に処理し、Aliceとbobが交互にカードを選ぶようにする。Aliceが最初にカードを選び次にbobが選ぶ。このプロセスをリストの終わりまで繰り返す
print(alice_score - bob_score)
