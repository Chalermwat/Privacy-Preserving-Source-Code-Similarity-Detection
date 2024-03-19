from collections import defaultdict




BS, SL = '\\', '/'

diagram = list(input())

flood = defaultdict(int)
total = 0
stack = []

for cur, terrain in enumerate(diagram):
    if terrain == BS:
        stack.append(cur)
    elif terrain == SL and stack:
        first = stack.pop()
        water = cur-first
        total += water
        for (f_first, f_last) in list(flood):
            if first < f_first < cur:
                flood[(first, cur)] += flood.pop((f_first, f_last))
        flood[(first, cur)] += water

print(total)
print(' '.join(map(str, [len(flood)] + list(flood.values()))))

