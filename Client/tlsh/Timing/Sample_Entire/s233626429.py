# ALDS1_3_D.

def show(a):
    # 配列の中身を出力する。
    _str = ""
    for i in range(len(a) - 1):
        _str += str(a[i]) + " "
    _str += str(a[len(a) - 1])
    print(_str)

def main():
    data = list(input())
    a = []  # '\\'の位置を格納していく。
    b = []  # 同じだが、池の集約に使う。
    ponds = []  # 池の面積のリスト(必要に応じて集約).
    Area = 0  # 総面積
    N = len(data)
    for i in range(N):
        if data[i] == '\\':
            a.append(i); b.append(i)
        elif data[i] == '/':
            if len(a) == 0: continue
            else:
                left = a.pop()  # '/'と対になる'\\'の位置
                Area += i - left
                ponds.append(i - left)
                # leftより右にあるbの元を先頭から見てあればカット、
                # その分だけpondsを集約する。
                while left < b[len(b) - 1]:
                    b.pop()
                    x = ponds.pop(); y = ponds.pop(); ponds.append(x + y)
    print(Area)
    ponds.insert(0, len(ponds))
    show(ponds)
    
if __name__ == "__main__":
    main()
