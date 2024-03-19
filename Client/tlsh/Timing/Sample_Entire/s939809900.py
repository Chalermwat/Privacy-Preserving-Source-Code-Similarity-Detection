def push(x, top, S):
      S.append(x)
      top = top + 1

def pop(top):
      del S[top-1]
      top = top - 1

if __name__ == "__main__":
      stdin = input()
      stdin = stdin.split()
      n = len(stdin)
      S = []
      top = len(S)
      for i in range(0, n):
            if stdin[i] == '+':
                  #print("+++++ top value is {}".format(top))
                  b = S[top-1]
                  a = S[top-2]
                  pop(top)
                  S[top-1] = a + b
            elif stdin[i] == '-':
                  #print("----- top value is {}".format(top))
                  b = S[top-1]
                  a = S[top-2]
                  pop(top)
                  S[top-1] = a - b
            elif stdin[i] == '*':
                  #print(print("***** top value is {}".format(top)))
                  b = S[top-1]
                  a = S[top-2]
                  pop(top)
                  S[top-1] = a * b
            else:
                  push(int(stdin[i]), top, S)
                  #print("when push {} top value is {}".format(int(stdin[i]),top))
      print(S[top])