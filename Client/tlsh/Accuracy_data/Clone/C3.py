#!/usr/bin/env python3
import sys #line:2
def solve (OO0O0O0O0OO0OO0O0 :int ,OOO0O0OOO00O000OO :int ,O0O0OO00O0OOO0OOO :int ):#line:5
    if (O0O0OO00O0OOO0OOO -OOO0O0OOO00O000OO )%2 ==0 :#line:6
        print ((O0O0OO00O0OOO0OOO -OOO0O0OOO00O000OO )//2 )#line:7
    else :#line:8
        if O0O0OO00O0OOO0OOO -1 >OO0O0O0O0OO0OO0O0 -OOO0O0OOO00O000OO :#line:9
            print (OO0O0O0O0OO0OO0O0 -O0O0OO00O0OOO0OOO +1 +((O0O0OO00O0OOO0OOO -OOO0O0OOO00O000OO -1 )//2 ))#line:10
        else :#line:11
            print (OOO0O0OOO00O000OO -1 +1 +((O0O0OO00O0OOO0OOO -OOO0O0OOO00O000OO -1 )//2 ))#line:12
    return 0 #line:13
def main ():#line:17
    def OOOOO000OO000O0OO ():#line:18
        for O0O0O00OO0OOO0000 in sys .stdin :#line:19
            for O00O0000000OOO000 in O0O0O00OO0OOO0000 .split ():#line:20
                yield O00O0000000OOO000 #line:21
    OOOO0000OOOOO00OO =OOOOO000OO000O0OO ()#line:22
    O0O0O0OOO00OO00O0 =int (next (OOOO0000OOOOO00OO ))#line:23
    OOOOOOOOO00000O00 =int (next (OOOO0000OOOOO00OO ))#line:24
    O0OO0O0O00000000O =int (next (OOOO0000OOOOO00OO ))#line:25
    solve (O0O0O0OOO00OO00O0 ,OOOOOOOOO00000O00 ,O0OO0O0O00000000O )#line:26
if __name__ =='__main__':#line:28
    main ()#line:29
