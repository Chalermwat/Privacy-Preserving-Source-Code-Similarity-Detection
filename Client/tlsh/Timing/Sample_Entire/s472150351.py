def main():
    A = input().split()
    l = []
    operator = None
    for character in A:
        if character in ["+", "-", "*"]:
            if character == "+":
                l.append(l.pop()+l.pop())
            elif character == "-":
                l.append(-l.pop()+l.pop())
            else:
                l.append(l.pop()*l.pop())
        else:
            l.append(int(character))
    print(l[0])




if __name__ == "__main__":
    import os
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "-d":
            fd = os.open("input.txt", os.O_RDONLY)
            os.dup2(fd, sys.stdin.fileno())
            main()
    else:
        main()