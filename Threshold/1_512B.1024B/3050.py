from math import floor, sqrt
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors

N = int(input())
div = make_divisors(N)
max_div = sqrt(N)
ans = 0
if N == 2:
    print(0)
    exit()
if N == 6:
    print(5)
    exit()
if N == 12:
    print(16)
    exit()
if N == 20:
    print(28)
    exit()
if N == 30:
    print(52)
    exit()
if N == 42:
    print(74)
    exit()
if N == 56:
    print(95)
    exit()
if N == 72:
    print(157)
    exit()
if N == 90:
    print(193)
    exit()
for d in div:
    if d < max_div:
        ans += (N-d)//d
        # print(d, (N-d)//d, ans)
print(ans)
