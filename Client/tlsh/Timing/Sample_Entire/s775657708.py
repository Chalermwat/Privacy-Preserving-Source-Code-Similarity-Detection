from collections import deque

list = list(input())

queue = deque([]) 
queue2 = []
total = 0

for i in range(len(list)):
        if list[i] == '\\':
                queue.append(i)
        elif list[i] == '/' and len(queue) > 0:
                j = queue.pop()
                total += (i - j)
                temp = i - j
                while len(queue2) > 0 and queue2[len(queue2) - 1][0] > j:
                        temp += queue2[len(queue2) - 1][1]
                        queue2.pop()
                queue2.append([j, temp])
strResult = [str(len(queue2))]
for i in range(len(queue2)):
        strResult.append(str(queue2[i][1]))

print(total)
print(" ".join(strResult))
