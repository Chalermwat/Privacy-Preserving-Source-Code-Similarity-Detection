from typing import List


class Info:
    def __init__(self, arg_start, arg_end, arg_area):
        self.start = arg_start
        self.end = arg_end
        self.area = arg_area


if __name__ == "__main__":
    LOC: List[int] = []
    POOL: List[Info] = []
    all_symbols = input()
    loc = 0
    total_area = 0

    for symbol in all_symbols:
        if symbol == '\\':
            LOC.append(loc)

        elif symbol == '/':
            if len(LOC) == 0:
                continue

            tmp_start = int(LOC.pop())
            tmp_end = loc
            tmp_area = tmp_end - tmp_start
            total_area += tmp_area

            while len(POOL) > 0:
                # \  / : (tmp_start, tmp_end)
                #  \/ : (POOL[-1].start, POOL[-1].end)
                if tmp_start < POOL[-1].start and POOL[-1].end < tmp_end:
                    tmp_area += POOL[-1].area
                    POOL.pop()
                else:
                    break

            POOL.append(Info(tmp_start, tmp_end, tmp_area))

        else:
            pass

        loc += 1

    print(f"{total_area}")
    print(f"{len(POOL)}", end="")
    while len(POOL) > 0:
        print(f" {POOL[0].area}", end="")
        POOL.pop(0)
    print()

