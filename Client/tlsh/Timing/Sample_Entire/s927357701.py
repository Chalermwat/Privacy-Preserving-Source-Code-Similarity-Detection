def areas(updown: str):
    stack1, stack2 = [], []

    for i, c in enumerate(updown):
        if c == "\\":
            stack1.append(i)
        elif c == "/":
            if len(stack1) == 0:
                continue

            match = stack1.pop()

            # ToDo
            total = 0
            while stack2 and match < stack2[-1][0]:
                _, x = stack2.pop()
                total += x

            total += i - match
            stack2.append((match, total))

        elif c == "_":
            # 何もする必要がない
            pass
        else:
            raise Exception("Invalid Input")

    print(sum(x for _, x in stack2))
    print("{} {}".format(len(stack2), " ".join([str(x) for _, x in stack2])).strip())


# in1 = r"\\//"
# in2 = r"\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/" + "\\"

s = input().strip()
areas(s)

