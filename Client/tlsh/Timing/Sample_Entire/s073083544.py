def main():
    sectionalview = input()
    stack = []
    a_surface = 0
    surfaces = []
    for cindex in range(len(sectionalview)):
        if sectionalview[cindex] == "\\":
            stack.append(cindex)
        elif sectionalview[cindex] == "/" and 0 < len(stack):
            if 0 < len(stack):
                left_index = stack.pop()
                a = cindex - left_index
                a_surface += a
                while 0 < len(surfaces):
                    if left_index < surfaces[-1][0]:
                        a += surfaces.pop()[1]
                    else:
                        break
                surfaces.append((cindex, a))
    t = [i[1] for i in surfaces]
    print(sum(t))
    print(" ".join(map(str, [len(t)] + t)))

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