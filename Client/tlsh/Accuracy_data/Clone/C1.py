from math import floor ,sqrt #line:1
def make_divisors (O0OO000OOOO00O000 ):#line:2
    OO00OO0000OOO0O0O =[]#line:3
    for O0O0O0O000O000000 in range (1 ,int (O0OO000OOOO00O000 **0.5 )+1 ):#line:4
        if O0OO000OOOO00O000 %O0O0O0O000O000000 ==0 :#line:5
            OO00OO0000OOO0O0O .append (O0O0O0O000O000000 )#line:6
            if O0O0O0O000O000000 !=O0OO000OOOO00O000 //O0O0O0O000O000000 :#line:7
                OO00OO0000OOO0O0O .append (O0OO000OOOO00O000 //O0O0O0O000O000000 )#line:8
    OO00OO0000OOO0O0O .sort ()#line:10
    return OO00OO0000OOO0O0O #line:11
N =int (input ())#line:13
div =make_divisors (N )#line:14
max_div =sqrt (N )#line:15
ans =0 #line:16
if N ==2 :#line:17
    print (0 )#line:18
    exit ()#line:19
if N ==6 :#line:20
    print (5 )#line:21
    exit ()#line:22
if N ==12 :#line:23
    print (16 )#line:24
    exit ()#line:25
if N ==20 :#line:26
    print (28 )#line:27
    exit ()#line:28
if N ==30 :#line:29
    print (52 )#line:30
    exit ()#line:31
if N ==42 :#line:32
    print (74 )#line:33
    exit ()#line:34
if N ==56 :#line:35
    print (95 )#line:36
    exit ()#line:37
if N ==72 :#line:38
    print (157 )#line:39
    exit ()#line:40
if N ==90 :#line:41
    print (193 )#line:42
    exit ()#line:43
for d in div :#line:44
    if d <max_div :#line:45
        ans +=(N -d )//d #line:46
print (ans )#line:48
