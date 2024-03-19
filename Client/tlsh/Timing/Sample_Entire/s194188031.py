f = list(input())
s = []

for i, v in enumerate(f):
    if v == '\\':
        s.append([v, i])
    elif v == '/' and len(s) > 0:
        n = s.pop()
        if n[0] == '\\':
            t = i-n[1]
            s.append(['.', t])
        elif len(s) > 0:
            j = len(s)-1
            n1 = n[1]
            while j >= 0 and s[j][0] == '.':
                #print(n1, s[j][1])
                n1 += s[j][1]
                j -= 1
            if j >= 0:
                m = s[j]
                # print(m)
                n1 += i-m[1]
                s = s[:j]
                s.append(['.', n1])
            else:
                # print("err")
                s.append(n)

        else:
            s.append(n)
    #print(v, s, i)


a = [v[1] for v in s if v[0] == '.']
print(sum(a))
a.insert(0, len(a))
print(" ".join([str(v) for v in a]))

