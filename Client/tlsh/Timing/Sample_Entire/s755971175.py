#input
A = list(input())
#print(A)
##    print(A[i],end = "")
#print(len(A))
sum = 0
#Stack
Stack1 = [] #各水たまりの面積
Stack2 = [] #
for i in range(len(A)):
    if A[i] == "\\":
        Stack1.append(i)
    elif A[i] == "/":
        if Stack1 != []:
            ip = Stack1.pop()
            tmp_sum = i-ip
            sum += i-ip

            xp, yp = ip,tmp_sum

            #-----------------------#
            if Stack2 == []:
                Stack2.append((i, tmp_sum))
            #-----------------------
            else:

                x, y = Stack2.pop()
                # x < ip(xp)
                while ( x- xp >= 0):
                    yp = y + yp
                    if Stack2 == []:
                        xp = x
                        Stack2.append((xp, yp))
                        break
                    else:
                        x, y = Stack2.pop()
                    #Stack2.append((xp, y + yp))
                else:
                    Stack2.append((x, y))
                    Stack2.append((xp, yp))

#print(Stack2)
print(sum)
if sum == 0:
    print(0)
else:
    print(len(Stack2), end=' ') #k
    for i in range(len(Stack2)):
        x, y = Stack2[i]
        if i < len(Stack2)-1:
            print(y, end=' ')
        else:
            print(y)
