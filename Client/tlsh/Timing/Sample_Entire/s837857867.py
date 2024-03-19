def main():
    s = input()
    stack = []#¥をためるstack
    stack_sum = []#現状できている池のstack
    for i in range(len(s)):
        
        if s[i] == "\\":
            stack.append(i)#池の左側をためる
        elif s[i] == "/":
            if len(stack) != 0:#対応する左側がなかったらskip
                sum_t = 0
                last = stack.pop(-1)#lastからiまでの池を下では考える
                sum_t += (i-last-1)+1#[last,i]の池の計算
                if len(stack_sum) != 0:
                    for j in reversed(range(len(stack_sum))):#後ろからみる
                        if stack_sum[j][0] > last:#[last,i]ではった池でマージできるところをマージ
                            sum_t += stack_sum[j][1]
                            stack_sum.pop(j)
                stack_sum.append((last, sum_t))
    sum_ans = 0#全ての池の合計
    ans = []
    for i in range(len(stack_sum)):
        sum_ans +=stack_sum[i][1]
        ans.append(stack_sum[i][1])#池の容量だけ取り出す

    #print(sum_ans)
    #print(ans)
    print(sum(ans))
    print(len(ans),*ans)

if __name__ == "__main__":
    main()
#O(n^2)なのでO(n)でやるべき

