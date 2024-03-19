s = input()

st = []
leftn = 0

def pushv(s, x):
        tmp = s.pop()
        tmpsum = 0
        while tmp[0] != 'left':
                tmpsum += tmp[1]
                tmp = s.pop()
        else:
                tmpsum += x - tmp[1]
                s.append(('v', tmpsum))

for x in range(len(s)):
        if s[x] == '\\':
                st.append(('left', x))
                leftn += 1
        elif s[x] == '/':
                if leftn != 0:
                        pushv(st, x)
                        leftn -= 1

st = [x[1] for x in st if x[0] == 'v']

if len(st) != 0:
       print(sum(st))
       print(len(st), ' '.join([str(x) for x in st]))
else:
      print(0)
      print(0)