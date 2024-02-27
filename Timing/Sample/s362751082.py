N, K = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(K)]

MOD = 998244353
class Mint:
    __slots__ = ('value')

    def __init__(self, value=0):
        self.value = value % MOD
        if self.value < 0: self.value += MOD

    @staticmethod
    def get_value(x): return x.value if isinstance(x, Mint) else x

    def inverse(self):
        a, b = self.value, MOD
        u, v = 1, 0
        while b:
            t = a // b
            b, a = a - t * b, b
            v, u = u - t * v, v
        if u < 0: u += MOD
        return u

    def __repr__(self): return str(self.value)
    def __eq__(self, other): return self.value == other.value
    def __neg__(self): return Mint(-self.value)
    def __hash__(self): return hash(self.value)
    def __bool__(self): return self.value != 0

    def __iadd__(self, other):
        self.value = (self.value + Mint.get_value(other)) % MOD
        return self

    def __add__(self, other):
        new_obj = Mint(self.value)
        new_obj += other
        return new_obj
    __radd__ = __add__

    def __isub__(self, other):
        self.value = (self.value - Mint.get_value(other)) % MOD
        if self.value < 0: self.value += MOD
        return self

    def __sub__(self, other):
        new_obj = Mint(self.value)
        new_obj -= other
        return new_obj

    def __rsub__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj -= self
        return new_obj

    def __imul__(self, other):
        self.value = self.value * Mint.get_value(other) % MOD
        return self

    def __mul__(self, other):
        new_obj = Mint(self.value)
        new_obj *= other
        return new_obj
    __rmul__ = __mul__

    def __ifloordiv__(self, other):
        other = other if isinstance(other, Mint) else Mint(other)
        self *= other.inverse()
        return self

    def __floordiv__(self, other):
        new_obj = Mint(self.value)
        new_obj //= other
        return new_obj

    def __rfloordiv__(self, other):
        new_obj = Mint(Mint.get_value(other))
        new_obj //= self
        return new_obj

LR.sort(key=lambda x: x[1])
pl = pr = -1
LR2 = []
for l, r in LR:
    if LR2:
        pl, pr = LR2.pop()
        if l <= pl:
            LR2.append((l, r))
        elif l <= pr:
            LR2.append((pl, r))
        else:
            LR2.append((pl, pr))
            LR2.append((l, r))
    else:
        LR2.append((l, r))

dp = [Mint() for _ in range(N + 5)]
dp[1] += 1
dp[2] -= 1
for i in range(1, N):
    dp[i] += dp[i - 1]
    for l, r in LR2:
        nl = min(i + l, N + 1)
        nr = min(i + r, N + 1)
        dp[nl] += dp[i]
        dp[nr + 1] -= dp[i]
dp[N] += dp[N - 1]
print(dp[N])
