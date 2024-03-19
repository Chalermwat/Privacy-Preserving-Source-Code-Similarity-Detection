# ALDS1_3_D Areas on the Cross-Section Diagram

s = input()
s = list(s)  # 地形リスト

s1 = []  # \ リスト


class S2:
    # 池の位置と大きさのリスト
    def __init__(self):
        self.point = []
        self.size = []

    def append(self, x, y):
        lake_size = y
        if not self.point:  # 一番最初の池の処理
            self.point.append(x)
            self.size.append(lake_size)
        else:
            if self.point[-1] < x:
                self.point.append(x)
                self.size.append(lake_size)
            else:
                while self.point[-1] > x:
                    # print('w self.point:{} x:{}'.format(self.point[-1], x))
                    self.point.pop()
                    lake_size += self.size[-1]
                    self.size.pop()
                    if not self.point:
                        break
                self.point.append(x)
                self.size.append(lake_size)
        # print('append point:{} append size:{}'.format(self.point, self.size))
        return self

    def pop(self):
        x = self.point.pop()
        y = self.size.pop()
        return x, y

    def sum_size(self):
        sum_size = sum(self.size)
        return sum_size


s2 = S2()

for i in range(len(s)):
    if s[i] is '\\':
        s1.append(i)
    elif s[i] is '/':
        if s1:  # S1が空ではない場合
            lake_point = s1.pop()
            lake_size = i - lake_point
            # print('point : {} size : {}'.format(lake_point, lake_size))

            s2.append(lake_point, lake_size)

total = s2.sum_size()
lake_num = len(s2.size)

# print('total size : {} number of lakes : {}\nlake size\n{}'.format(total, lake_num, s2.size))
print(total)
print(lake_num, end='')
for i in range(len(s2.size)):
    print('', s2.size[i], end='')
print('')


