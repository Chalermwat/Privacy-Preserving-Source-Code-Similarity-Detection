areaStr = list(input())
N = len(areaStr)
tmpArea = []
totalArea = 0
eachArea = []
"""
for i in range(N):
    if areaStr[i] == "\\":
        tmpArea.append(i)
    elif areaStr[i] == "/":
        if len(tmpArea) != 0:
            totalArea += (i - tmpArea.pop())
    else:
        pass
    
"""


tmpArea = []
totalArea = 0
for i in range(N):
    if areaStr[i] == "\\":
        tmpArea.append(i)
    elif areaStr[i] == "/":
        if len(tmpArea) != 0:
            j = tmpArea.pop()
            
            totalArea += (i - j)
            a = i - j
            while(len(eachArea) > 0 and eachArea[len(eachArea) - 1][0] > j):
                a +=  eachArea.pop()[1]
               
            eachArea.append([j, a])
    else:
        pass
    

print(totalArea)
print(len(eachArea), end = "")
if len(eachArea) > 1:
    for i in range(len(eachArea)-1):
        print("", end = " ")
        print(eachArea[i][1], end = "")
if len(eachArea) >= 1:
    print("", end = " ")
    print(eachArea[len(eachArea)-1][1])
    
else:
    print("")






