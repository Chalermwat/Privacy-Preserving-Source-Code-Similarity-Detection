from math import sqrt ;#line:1
count =int (input ());#line:3
data =[];#line:4
for n in range (count ):#line:5
    data .append (int (input ()));#line:6
def prime_number (OO0O00OOO0O0OO0O0 ):#line:8
    OOOOOOO00O0000OOO =get_max_divisor (OO0O00OOO0O0OO0O0 );#line:9
    O000O0OO000OO0OO0 =get_prime (OOOOOOO00O0000OOO );#line:10
    O00O0O00OO000OO00 =0 ;#line:11
    for OOO0O00O0O0O000O0 in OO0O00OOO0O0OO0O0 :#line:12
        OOO000OOO00O00O00 =1 ;#line:13
        for OO0O0OO000OO00000 in O000O0OO000OO0OO0 :#line:14
            if OOO0O00O0O0O000O0 <OO0O0OO000OO00000 :#line:15
                OOO000OOO00O00O00 =0 ;#line:16
                break ;#line:17
            elif OOO0O00O0O0O000O0 ==OO0O0OO000OO00000 :#line:18
                break ;#line:19
            elif OOO0O00O0O0O000O0 %OO0O0OO000OO00000 ==0 :#line:20
                OOO000OOO00O00O00 =0 ;#line:21
                break ;#line:22
        O00O0O00OO000OO00 +=OOO000OOO00O00O00 ;#line:23
    return O00O0O00OO000OO00 ;#line:24
def get_max_divisor (OOO0O00O0OOO0OOOO ):#line:26
    OOO00O00O00O00O00 =OOO0O00O0OOO0OOOO [0 ];#line:27
    for OOO0OOOOOO00O000O in OOO0O00O0OOO0OOOO [1 :]:#line:28
        if OOO0OOOOOO00O000O >OOO00O00O00O00O00 :#line:29
            OOO00O00O00O00O00 =OOO0OOOOOO00O000O ;#line:30
    return int (sqrt (OOO00O00O00O00O00 ))+1 ;#line:31
def get_prime (OO0O00000O0O00000 ):#line:33
    OO00O0OOO00O00OO0 =[];#line:34
    for O0OO0O000O00O0OOO in range (2 ,OO0O00000O0O00000 +1 ):#line:35
        O00OOO0O0OOOOO0O0 =True ;#line:36
        for OO00O0OO0OOOOOOO0 in OO00O0OOO00O00OO0 :#line:37
            if O0OO0O000O00O0OOO %OO00O0OO0OOOOOOO0 ==0 :#line:38
                O00OOO0O0OOOOO0O0 =False ;#line:39
        if O00OOO0O0OOOOO0O0 :#line:40
            OO00O0OOO00O00OO0 .append (O0OO0O000O00O0OOO );#line:41
    return OO00O0OOO00O00OO0 ;#line:42
print (prime_number (data ));#line:44
