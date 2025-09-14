
def calculate_score(hand, category):
    counts = [0] * 7
    for d in hand:
        counts[d] +=1
    # hand ダイス1から５
    # category 役の番号 0-12
    # counts = [0] これは、0 を7つ含むリストを作成しています。サイコロの目は1から6までですが、
    # リストのインデックスは0から始まります。インデックス0は使わず、
    # インデックス1から6をそれぞれサイコロの目の1から6に対応させることで、コードがより直感的になるcounts[1] には「1の目の出現回数」、
    # counts[2] には「2の目の出現回数」というように対応させることができます。for in hand handは手持ちのサイコロの目を格納したりすと
    # このforループはhandリストの各要素を順番に変数ｄに代入する
    # counts[d] += 1 ←出現回数を数える核心部分、ループが回るたびにｄにはhandリストから取り出されたサイコロの目が入るcounts[d]は、
    # 出現回数を表すカウンター。+=1はカウンターの値を１増やす操作、例えばdが５の場合、counts[5]の値が1増える、これにより5の目が出現するたびに
    # counts[5]がカウントアップされる
    if category <= 5:
        return counts[category + 1] * (category + 1)
    # category は現在評価している役の番号を表している、今問題ではカードの13種類の役が0から12までの番号で管理されている、
    # category=0は１の役を示していることから categoryの値は、対応するサイコロの目よりも1小さい値。
    # return counts[category + 1] * (category + 1) counts は、各サイコロの目の出現回数を格納したリストです。counts[category + 1]指定された目が何回出たか表す
    # コードは、**「指定された目が何回出たか」と「その目の値」**を掛けることで、AcesからSixesまでの各役の合計スコアを正確に計算しています。

    elif category == 6:
        return sum(hand)
    
    elif category == 7:
        for i in range(1, 7):
            if counts[i] >= 4:
                return sum(hand)
        return 0
    
    elif category == 8:
        has_3 = False
        has_2 = False
        for c in counts:
            if c == 3:
                has_3 = True
            if c == 2:
                has_2 = True
        return sum(hand) if has_3 and has_2 else 0
    
    elif category == 9:
        unique_dice = sorted(list(set(hand)))
        s_unique ="".join(map(str, unique_dice))
        if "1234" in s_unique or "2345" in s_unique or "3456" in s_unique:
            return 15
        return 0
    
    elif category == 10:
        if len(set(hand)) == 5 and (sum(hand) == 15 or sum(hand) == 20):
            return 30
        return 0
    
    elif category == 11:
        if len(set(hand)) == 1:
            return 50
        return 0
    
    elif category == 12:
        return sum(hand)
    
def solve(turn, used_mask):
    state = (turn, used_mask)
    if state in memo:
        return memo[state]
    
    if turn == 13:
        return 0
    
    max_score = 0

    for category in range(13):
        if not (used_mask & (1 << category)):
            pass
        return 0
    
def main():
    pass
if __name__ == '__main__':
    main()
