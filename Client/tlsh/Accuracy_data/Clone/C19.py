d ,n =map (int ,input ().split ())#line:1
if d ==0 :#line:2
    count =0 #line:3
    for i in range (1 ,110 ):#line:4
        if i %100 !=0 :#line:5
            count +=1 #line:6
            if count ==n :#line:7
                print (i )#line:8
                break #line:9
        else :#line:10
            continue #line:11
if d ==1 :#line:14
    count =0 #line:15
    for i in range (100 ,20000 ,100 ):#line:16
        if i %100 ==0 and i %10000 !=0 :#line:17
            count +=1 #line:18
            if count ==n :#line:19
                print (i )#line:20
                break #line:21
        else :#line:22
            continue #line:23
if d ==2 :#line:26
    count =0 #line:27
    for i in range (10000 ,2000000 ,10000 ):#line:28
        if i %10000 ==0 and i %1000000 !=0 :#line:29
            count +=1 #line:30
            if count ==n :#line:31
                print (i )#line:32
                break #line:33
        else :#line:34
            continue #line:35
