
class Stack:
    def __init__(self, n):
        self.A = [0 for i in range(n)]
        self.len = n
        self.top = 0

    def is_empty(self):
        return self.top == 0

    def is_full(self):
        return self.top == self.len - 1

    def push(self, x):
        if not self.is_full():
            self.top += 1
            self.A[self.top] = x

    def pop(self):
        if not self.is_empty():
            x = self.A[self.top]
            self.top -= 1
            return x

    def top_element(self):
        if not self.is_empty():
            return self.A[self.top]


if __name__ == '__main__':
    S1 = Stack(20005)  # for \
    S2 = Stack(10005)  # for ponds
    line = raw_input()
    for i in range(len(line)):
        if line[i] == '\\':
            S1.push(i)
        elif line[i] == '/':
            if S1.is_empty():
                continue
            j = S1.pop()
            cnt = 0  # total area of ponds that can be merged
            # no more ponds can be merged if S2.top_element()[0] < j, why?
            # because '/' is clearly increasing toward the stack top
            # and '\' is increasing toward the stack top, too
            # if not, there exists a pond that should have been merged
            while not S2.is_empty() and S2.top_element()[0] > j:
                cnt += S2.pop()[1]
            S2.push((j, cnt + i - j))
        else:
            pass

    l = []
    cnt = 0
    while not S2.is_empty():
        x = S2.pop()
        cnt += x[1]
        l.append(x)
    l.reverse()
    print cnt
    print len(l),
    for x in l:
        print x[1],
    print
