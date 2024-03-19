diagram = input()

water_all = 0
water = 0
ip = 0
stack1 = []
stack2 = []

for i, symbol in enumerate(diagram):
    if symbol == '\\': # 一つのバックスラッシュはこう書くらしい
        stack1.append(i)
    elif symbol == '/':
        if stack1 != []:
            ip = stack1.pop()
            water = i - ip
            water_all += water
            
            if stack2 != []:
                while stack2[-1][0] > ip:
                    i2, water2 = stack2.pop()
                    water += water2
                    if stack2 == []:
                        break
                stack2.append([ip, water])
            else:
                stack2.append([ip, water])

s = str(len(stack2))
waters = [str(i[1]) for i in stack2]
if len(waters)!=0:
    s += ' ' + ' '.join(waters)

print(water_all)
print(s)
