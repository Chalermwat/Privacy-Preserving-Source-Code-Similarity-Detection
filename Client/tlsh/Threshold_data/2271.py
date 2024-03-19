def part_sum(a,A):
    #初期化
    N=len(a)
    dp=[[-1 for i in range(A+1)] for j in range(N+1)]
    dp[0][0]=[]
    #DP
    for i in range(N):
        for j in range(A+1):
            if a[i]<=j: #i+1番目の数字a[i]を足せるかも
                if dp[i][j] != -1:
                    dp[i+1][j] = dp[i][j]
                elif dp[i][j-a[i]] != -1:
                    dp[i+1][j] = dp[i][j-a[i]]+[a[i]]
            else: #入る可能性はない
                dp[i+1][j]=dp[i][j]
    #生成可能な自然数の配列(辞書型)
    """
    num_list = {}
    for i in dp:
        for num,j in enumerate(i):
            if j != -1:
                num_list[num] = j
    return num_list
    """
    return dp[N][A]
a = int(input())
num = list(map(int,input().split()))
q = int(input())
ans = list(map(int,input().split()))
for i in ans:
    check = part_sum(num,i)
    #print(check)
    if check == -1:
        print("no")
    else:
        print("yes")
