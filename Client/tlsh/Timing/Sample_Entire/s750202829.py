# encoding: utf-8


def calc_area(startIndex, endIndex, terrain):
    level = terrain[startIndex]
    area = 0
    for i in xrange(startIndex, endIndex):
        area += (level - terrain[i]) + 0.5 * (terrain[i] - terrain[i + 1])
    return int(area)


def check_area(terrain):
    i = 0
    startIndex = 0
    endIndex = 0
    while i < len(terrain) - 1:
        if terrain[i + 1] - terrain[i] < 0:
            startIndex = i
            break
        i += 1
    for j in xrange(i + 1, len(terrain)):
        if terrain[i] == terrain[j]:
            endIndex = j
            return startIndex, endIndex
    else:
        return 0, 0


def main():
    string = list(raw_input())
    terrain = []
    height = 0
    for c in string:
        terrain.append(height)
        if c == "\\":
            height -= 1
        elif c == "/":
            height += 1
    terrain.append(height)

    waterAreaRight = []
    while True:
        i, j = check_area(terrain)
        if i == j:
            break
        waterAreaRight.append(calc_area(i, j, terrain))
        terrain = terrain[j:]

    terrain = terrain[::-1]
    waterAreaLeft = []
    while True:
        i, j = check_area(terrain)
        if i == j:
            break
        waterAreaLeft.append(calc_area(i, j, terrain))
        terrain = terrain[j:]
    waterAreaRight.extend(waterAreaLeft[::-1])

    print sum(waterAreaRight)
    print len(waterAreaRight),
    if len(waterAreaRight) > 0:
        print " ".join(map(str, waterAreaRight))

main()