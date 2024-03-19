import collections
import sys

S1 = collections.deque()
S2 = collections.deque()
S3 = collections.deque()

for i, j in enumerate(sys.stdin.readline()):
    if j == '\\':
        S1.append(i)
    elif j == '/':
        if S1:
            left_edge = S1.pop()
            new_puddle = i - left_edge
            while True:
                if S2:
                    if S2[-1] > left_edge:
                        S2.pop()
                        new_puddle += S3.pop()
                    else:
                        break
                else:
                    break
            S2.append(left_edge)
            S3.append(new_puddle)
        else:
            pass


print(sum(S3))

print(len(S3), *S3)