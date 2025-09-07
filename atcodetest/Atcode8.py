#ABC085B-Kagami Mochi
#↓餅の枚数Nを受け取る
N = int(input())
d = [int(input()) for _ in range(N)]
#↑各餅の直径のリストdを受け取る

Mochi_diameters = len(set(d))
#setを使ってリストの中の直径のリストを受け取る
print(Mochi_diameters)
