class Pond:
    def __init__(self, down_x, area):
        super().__init__()
        self.down_x = down_x
        self.area = area


s = []
ponds = []
all_area = 0
x = 0
for c in input():
    if "\\" == c:
        s.append(x)
    elif "/" == c and s:
        down_x = s.pop()
        area = x - down_x
        all_area += area
        while ponds and ponds[-1].down_x > down_x:
            area += ponds[-1].area
            ponds.pop()
        ponds.append(Pond(down_x, area))
    x += 1
print(all_area)
if ponds:
    print(len(ponds), ' '.join(map(lambda pond: str(pond.area), ponds)))
else:
    print(0)

