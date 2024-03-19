class stack():
    def __init__(self):
        self.S = []
        
    def push(self, x):
        self.S.append(x)
        
    def pop(self):
        return self.S.pop()
        
    def isEmpty(self):
        if len(self.S) == 0:
            return True
        else:
            return False

areas = input()

S1 = stack()
S2 = stack()

for i, info in enumerate(areas):
    if info == '/':
        if S1.isEmpty():
            continue
        left = S1.pop()
        menseki = i - left
        while True:
            if S2.isEmpty():
                S2.push([menseki, left])
                break
            if S2.S[-1][1] < left:
                S2.push([menseki, left])
                break
            menseki += S2.pop()[0]
    elif info == '\\':
        S1.push(i)

ans = [m[0] for m in S2.S]
print(sum(ans))
if len(ans) == 0:
    print(len(ans))
else:
    print(len(ans), ' '.join(list(map(str, ans))))
