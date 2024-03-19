# -*- coding: UTF-8 -*-
#Stable Sort
import copy

def bubble_sort(bubble_N,bubble_A):
    #バブルソート
    flag = 1
    bi = 0
    # Sort処理（自分メモ：flagが0になったらループを抜ける）
    while flag:
        flag = 0
        for bj in reversed(range(bi + 1, bubble_N)):
            if bubble_A[bj][1:2] < bubble_A[bj - 1][1:2]:
                tmp = bubble_A[bj - 1]
                bubble_A[bj - 1] = bubble_A[bj]
                bubble_A[bj] = tmp
            flag = 1
        bi += 1

def selection_sort(selection_N,selection_A):
    #選択ソート
    for si in range(selection_N):
        cnt_flg = 0
        minj = si
        for sj in range(si, selection_N):
            if selection_A[sj][1:2] < selection_A[minj][1:2]:
                minj = sj
                cnt_flg = 1
        tmp = selection_A[si]
        selection_A[si] = selection_A[minj]
        selection_A[minj] = tmp

#標準入力から
N = int(input()) #要素数
B_A = list(input().split()) #バブルソート対象（スペース区切り→配列に展開）
S_A = copy.deepcopy(B_A) #選択ソート対象（コピー）

bubble_sort(N,B_A) #バブルソート実施
selection_sort(N,S_A) #選択ソート実施
ans_bubble = ' '.join(map(str,B_A)) #配列を文字列に戻す
ans_selection = ' '.join(map(str,S_A)) #配列を文字列に戻す

#バブルソート結果の出力（常にStable）
print(ans_bubble)
print("Stable")

#選択ソート結果の出力（バブルソート結果と比較してStable判断）
print(ans_selection)
if ans_bubble == ans_selection:
    print("Stable")
else:
    print("Not stable")

