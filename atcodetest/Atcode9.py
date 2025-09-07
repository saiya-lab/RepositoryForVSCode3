#ABC085C-Otoshidama
N, Y = map(int, input().split())
#↓forのループを使ってお札のすべての可能な組み合わせを探索
for x in range(N+1):
    for y in range(N+1-x):
        z = N - x - y
        if 10000*x + 5000*y + 1000*z == Y:
            print(x, y, z)
            exit()
#インタラクティブシェルの終了
#適切な組み合わせが見つからなかった場合の出力
print(-1, -1, -1)
