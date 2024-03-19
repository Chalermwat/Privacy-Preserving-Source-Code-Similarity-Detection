length = int(input())
eles = [l for l in input().split()]
is_stable = 'Stable'

import copy
_copy = copy.deepcopy(eles)

for i in range(length):
    for j in range(length-1, 0, -1):
        if _copy[j][1] < _copy[j-1][1]:
            _copy[j], _copy[j-1] = _copy[j-1], _copy[j]

print(*_copy)
print(is_stable)

__copy = copy.deepcopy(eles)
for i in range(length-1):
    _min = i
    for l in range(i, length):
        if __copy[l][1] < __copy[_min][1]:
            _min = l
    if __copy[i][1] > __copy[_min][1]:
        __copy[i], __copy[_min] = __copy[_min], __copy[i]

print(*__copy)

for i in range(length -1):
    if _copy[i] != __copy[i]:
        is_stable = 'Not stable'

print(is_stable)