inputString = input()
terrainWidth = len(inputString)+1

height = [0] # 土地の高さを求める (左端 = 0)
currentHeight = 0
for c in inputString:
    if c == '_':
        d = 0
    elif c == '/':
        d = 1
    elif c == '\\':
        d = -1
    else:
        pass
    currentHeight += d
    height.append(currentHeight)

leftMax = [] # 各地点における、その地点より左の最大高さを求める
currentMax = 0
for h in height:
    currentMax = max(h, currentMax)
    leftMax.append(currentMax)

rightMax = [0]*terrainWidth # 各地点における、その地点より右の最大高さを求める
currentMax = height[-1]
for i in range(len(height), 0, -1):
    currentMax = max(height[i-1], currentMax)
    rightMax[i-1] = currentMax

floodArea = 0
floodDepth = [0]*terrainWidth # 各地点の水位は leftMax と rightMax の最小値
for i in range(terrainWidth):
    floodDepth[i] = min(leftMax[i], rightMax[i]) - height[i]
    floodArea += floodDepth[i]

pools = []
inPool = False
for depth in floodDepth:
    if depth:
        if inPool:
            pools[-1] += depth
        else:
            inPool = True
            pools.append(depth)
    elif inPool:
        inPool = False

print(floodArea)
if pools:
    print(len(pools), ' '.join([str(p) for p in pools]))
else:
    print(0)

