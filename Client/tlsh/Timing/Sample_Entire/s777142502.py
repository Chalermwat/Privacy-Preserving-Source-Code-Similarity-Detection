from operator import add


class SegmentTree():
    """
    update, get を提供するSegmentTree

    Attributes
    ----------
    __n : int
        葉の数。2 ^ i - 1
    __dot :
        Segment function
    __e: int
        単位元
    __node: list
        Segment Tree
    """
    def __init__(self, A, dot, e):
        """
        Parameters
        ----------
        A : list
            対象の配列
        dot :
            Segment function
        e : int
            単位元
        """
        n = 2 ** (len(A) - 1).bit_length()
        self.__n = n
        self.__dot = dot
        self.__e = e
        self.__node = [e] * (2 * n)
        for i in range(len(A)):
            self.__node[i + n] = A[i]
        for i in range(n - 1, 0, -1):
            self.__node[i] = self.__dot(self.__node[2 * i], self.__node[2 * i + 1])
    
    def update(self, i, c):
        i += self.__n
        node = self.__node
        node[i] = c % MOD
        while i > 1:
            i //= 2
            node[i] = self.__dot(node[2 * i], node[2 * i + 1]) % MOD

    def get(self, l, r):
        vl, vr = self.__e, self.__e
        l += self.__n
        r += self.__n
        while (l < r):
            if l & 1:
                vl = self.__dot(vl, self.__node[l]) % MOD
                l += 1
            l //= 2
            if r & 1:
                r -= 1
                vr = self.__dot(vr, self.__node[r]) % MOD
            r //= 2
        return self.__dot(vl, vr) % MOD
    

MOD = 998244353
N, K = map(int, input().split())
move = [tuple(map(int, input().split())) for _ in range(K)]
move.sort()

st = SegmentTree([0] * N, add, 0)
st.update(0, 1)
for i in range(1, N):
    cnt = 0
    for l, r in move:
        L = max(0, i - r)
        R = i - l
        if R >= 0:
            cnt += st.get(L, R + 1)
    st.update(i, cnt)

print(st.get(N - 1, N))
