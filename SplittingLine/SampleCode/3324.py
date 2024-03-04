d, n = map(int, input().split())
if d == 0:
    count = 0
    for i in range(1, 110):
        if i % 100 != 0:
            count += 1
            if count == n:
                print(i)
                break
        else:
            continue
        

if d == 1:
    count = 0
    for i in range(100, 20000, 100):
        if i % 100 == 0 and i % 10000 != 0:
            count+=1
            if count == n:
                print(i)
                break
        else:
            continue
        

if d == 2:
    count = 0
    for i in range(10000, 2000000, 10000):
        if i % 10000 == 0 and i % 1000000 != 0:
            count+=1
            if count == n:
                print(i)
                break
        else:
            continue


