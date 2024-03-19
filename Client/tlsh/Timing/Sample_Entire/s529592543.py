def main():
    
    from collections import deque

    s = input()
    s1 = deque([])
    s2 = deque([])

    sum_ = 0
    
    for i, ch in enumerate(s):
        if ch == '\\' :
            s1.append(i)
            
        elif ch =='/' and len(s1) > 0:
            j = s1.pop()
            sum_ += i - j
            a = i- j
            while len(s2) > 0 and s2[-1][0] > j:
                a += s2.pop()[1]
            s2.append([j, a])
            
    ans = []
    
    while len(s2)>0:
        ans.append(s2.pop()[1])
        
    ans.reverse()
    print(sum(ans))
    ans.insert(0, len(ans))
    
    print(' '.join(map(str, ans)))

    
            
if __name__ == '__main__':
    main()
