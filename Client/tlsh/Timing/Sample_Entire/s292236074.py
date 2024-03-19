import sys


def read_heights():
    current = 0
    heights = [current]
    for c in sys.stdin.read().strip():
        current += {
            '/': 1,
            '\\': -1,
            '_': 0
        }[c]
        heights.append(current)
    return heights


heights = read_heights()

height_index = {}
for i, h in enumerate(heights):
    height_index.setdefault(h, []).append(i)

flooded = [False] * len(heights)
floods = []

# search from highest points
for h in sorted(height_index.keys(), reverse=True):
    indexes = height_index[h]
    for i in range(len(indexes) - 1):
        start = indexes[i]
        stop = indexes[i + 1]
        if start + 1 == stop or flooded[start] or flooded[stop]:
            continue
        if any(heights[j] >= h for j in range(start + 1, stop)):
            continue
        # flood in (start..stop)
        floods.append((start, stop))
        for j in range(start, stop):
            flooded[j] = True

floods.sort()

areas = []
for start, stop in floods:
    area = 0
    top = heights[start]
    for i in range(start + 1, stop + 1):
        h = heights[i]
        area += top - h + (heights[i - 1] - h) * 0.5
    areas.append(int(area))

print(sum(areas))
print(' '.join([str(v) for v in [len(areas)] + areas]))

