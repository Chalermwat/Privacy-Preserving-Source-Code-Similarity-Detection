#安定なソート
#4つの絵柄と9つの数字から成る36枚のカード
def bubble(nums,N):
    for i in range(N-1): #先頭が確定するまで調べる（確定したら先頭の次の値が先頭になる）
        j = N-1
        while j > i:
            if nums[j-1][1] > nums[j][1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            j = j - 1 #交換したら次の値に移動する
    return nums

def selection(nums,N):
    for i in range(N-1):
        minj = i
        for j in range(i+1,N): #配列を探索し、最小値を見つける
            if nums[minj][1] > nums[j][1]:
                minj = j
        if minj != i:
            nums[minj], nums[i] = nums[i], nums[minj]
    return nums

N = int(input())
nums = input().split()
nums2 = nums.copy()
#numsをそのまま二つのソートで使うと、後のソートでは先のソートの影響を受けるので、コピーしておく
#あるいは、numsではなくnums[:]を引数とする

result1 = bubble(nums,N)
print(' '.join(map(str,result1)))
print("Stable")
result2 = selection(nums2,N)
print(' '.join(map(str,result2)))
print("Stable" if result1 == result2 else "Not stable")

