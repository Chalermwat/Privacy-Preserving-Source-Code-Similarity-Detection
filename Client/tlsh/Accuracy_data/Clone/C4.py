#!usr/bin/env python3
import sys #line:3
import operator #line:4
from math import floor #line:5
def string_to_list_spliter ():#line:8
    O0O0O0OOO00O0OO0O =[int (O00O00O0OOO0OOOOO )if isinstance (O00O00O0OOO0OOOOO ,int )==True else O00O00O0OOO0OOOOO for O00O00O0OOO0OOOOO in sys .stdin .readline ().split ()]#line:9
    return O0O0O0OOO00O0OO0O #line:10
def main ():#line:13
    O0O0OO0O00O0O00OO ={'+':operator .add ,'-':operator .sub ,'*':operator .mul ,'/':operator .truediv }#line:14
    while True :#line:16
        OOOO0O000OOOO0O00 =string_to_list_spliter ()#line:17
        if OOOO0O000OOOO0O00 [1 ]=='?':#line:18
            break #line:19
        elif OOOO0O000OOOO0O00 [1 ]=='+':#line:20
            print (O0O0OO0O00O0O00OO [OOOO0O000OOOO0O00 [1 ]](int (OOOO0O000OOOO0O00 [0 ]),int (OOOO0O000OOOO0O00 [2 ])))#line:21
        elif OOOO0O000OOOO0O00 [1 ]=='-':#line:22
            print (O0O0OO0O00O0O00OO [OOOO0O000OOOO0O00 [1 ]](int (OOOO0O000OOOO0O00 [0 ]),int (OOOO0O000OOOO0O00 [2 ])))#line:23
        elif OOOO0O000OOOO0O00 [1 ]=='*':#line:24
            print (O0O0OO0O00O0O00OO [OOOO0O000OOOO0O00 [1 ]](int (OOOO0O000OOOO0O00 [0 ]),int (OOOO0O000OOOO0O00 [2 ])))#line:25
        elif OOOO0O000OOOO0O00 [1 ]=='/':#line:26
            print (floor (O0O0OO0O00O0O00OO [OOOO0O000OOOO0O00 [1 ]](int (OOOO0O000OOOO0O00 [0 ]),int (OOOO0O000OOOO0O00 [2 ]))))#line:27
if __name__ =='__main__':#line:30
    main ()