# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_D
# Areas on the Cross-Section Diagram
# Result:
import sys

class Stack(object):
    def __init__(self):
        self.store = []

    def push(self, val):
        self.store.append(val)

    def pop(self):
        if self.is_empty():
            return None
        return self.store.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.store[len(self.store) - 1]

    def is_empty(self):
        if len(self.store) == 0:
            return True
        else:
            return False

    def to_list(self):
        return list(self.store)


### main
pools = []
s1 = Stack()
s2 = Stack()

line = sys.stdin.readline().rstrip()
area_sum = 0
idx = 0
for c in line:
    if c == '\\':
        s1.push(idx)
    elif c == '/':
        if not s1.is_empty():
            bs_idx = s1.pop()
            this_area_sum = idx - bs_idx
            area_sum += this_area_sum
            while (not s2.is_empty()) and (s2.top()[0] > bs_idx):
                this_area_sum += s2.pop()[1]
            s2.push((bs_idx, this_area_sum))
    else:
        pass
    idx += 1

print area_sum
s2_list = s2.to_list()
str = '%d' % (len(s2_list))
for e in s2.to_list():
    str += ' %d' % (e[1])
print str