import sys

input = sys.stdin.readline

S = input().strip()

stack = []
ponds = []

for idx, s in enumerate(S):
    if s == "\\":
        stack.append(idx)
    elif s == "/" and stack:
        _first = stack.pop()
        pond = idx - _first
        ponds.append((_first, pond))

    # concatnate ponds
    while len(ponds) > 1:
        _cur, _size = ponds.pop()
        _prev, _prev_size = ponds.pop()

        if _cur < _prev:
            ponds.append((_cur, _prev_size + _size))
        else:
            ponds.append((_prev, _prev_size))
            ponds.append((_cur, _size))
            break

ans = []
for idx, size in ponds:
    ans.append(size)
if not ans:
    print(0)
    print(0)
else:
    print(sum(ans))
    print("{} ".format(len(ans)) + " ".join([str(s) for s in ans]))

