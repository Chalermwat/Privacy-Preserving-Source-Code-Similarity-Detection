def part_sum (O0OOO0OOO0OOOO000 ,O00O00000O0OO0O0O ):#line:1
    OO00000OOOO00O00O =len (O0OOO0OOO0OOOO000 )#line:3
    OOOOOO00OOOOOO000 =[[-1 for OO0000OO0O00OO00O in range (O00O00000O0OO0O0O +1 )]for O0OOOO0O0O00O0O0O in range (OO00000OOOO00O00O +1 )]#line:4
    OOOOOO00OOOOOO000 [0 ][0 ]=[]#line:5
    for OOO0O0O00O00OOO00 in range (OO00000OOOO00O00O ):#line:7
        for O000O0O0O0OO0000O in range (O00O00000O0OO0O0O +1 ):#line:8
            if O0OOO0OOO0OOOO000 [OOO0O0O00O00OOO00 ]<=O000O0O0O0OO0000O :#line:9
                if OOOOOO00OOOOOO000 [OOO0O0O00O00OOO00 ][O000O0O0O0OO0000O ]!=-1 :#line:10
                    OOOOOO00OOOOOO000 [OOO0O0O00O00OOO00 +1 ][O000O0O0O0OO0000O ]=OOOOOO00OOOOOO000 [OOO0O0O00O00OOO00 ][O000O0O0O0OO0000O ]#line:11
                elif OOOOOO00OOOOOO000 [OOO0O0O00O00OOO00 ][O000O0O0O0OO0000O -O0OOO0OOO0OOOO000 [OOO0O0O00O00OOO00 ]]!=-1 :#line:12
                    OOOOOO00OOOOOO000 [OOO0O0O00O00OOO00 +1 ][O000O0O0O0OO0000O ]=OOOOOO00OOOOOO000 [OOO0O0O00O00OOO00 ][O000O0O0O0OO0000O -O0OOO0OOO0OOOO000 [OOO0O0O00O00OOO00 ]]+[O0OOO0OOO0OOOO000 [OOO0O0O00O00OOO00 ]]#line:13
            else :#line:14
                OOOOOO00OOOOOO000 [OOO0O0O00O00OOO00 +1 ][O000O0O0O0OO0000O ]=OOOOOO00OOOOOO000 [OOO0O0O00O00OOO00 ][O000O0O0O0OO0000O ]#line:15
    """
    num_list = {}
    for i in dp:
        for num,j in enumerate(i):
            if j != -1:
                num_list[num] = j
    return num_list
    """#line:24
    return OOOOOO00OOOOOO000 [OO00000OOOO00O00O ][O00O00000O0OO0O0O ]#line:25
a =int (input ())#line:26
num =list (map (int ,input ().split ()))#line:27
q =int (input ())#line:28
ans =list (map (int ,input ().split ()))#line:29
for i in ans :#line:30
    check =part_sum (num ,i )#line:31
    if check ==-1 :#line:33
        print ("no")#line:34
    else :#line:35
        print ("yes")#line:36
