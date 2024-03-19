def push(S, top, x):
      S.append(x)
      top = top + 1

def pop(S, top):
      t = int(S[top-1])
      del S[top-1]
      top = top -1
      return t

if __name__ == "__main__":
      top = 0
      inpt = (input()).split()
      n = len(inpt)
      S = []
      for i in range(0,n):
            if inpt[i] == "+":
                  b = pop(S, top)
                  a = pop(S, top)
                  c = a + b
                  push(S, top, c)
            elif inpt[i] == "-":
                  b = pop(S, top)
                  a = pop(S, top)
                  c = a - b
                  push(S, top, c)
            elif inpt[i] == "*":
                  b = pop(S, top)
                  a = pop(S, top)
                  c = a * b
                  push(S, top, c)
            else :
                  push(S, top, int(inpt[i]))
      print(S[top-1])