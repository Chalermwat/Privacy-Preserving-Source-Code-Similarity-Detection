import math #line:1
import string #line:2
import itertools #line:3
import fractions #line:4
import heapq #line:5
import collections #line:6
import re #line:7
import array #line:8
import bisect #line:9
import sys #line:10
import random #line:11
import time #line:12
inf =10 **9 #line:13
class Coordinate :#line:16
    def __init__ (OO000O0OO00O0OO00 ,O0O000OO000O00OOO ,OO00O00000000000O ):#line:17
        OO000O0OO00O0OO00 .x =O0O000OO000O00OOO #line:18
        OO000O0OO00O0OO00 .y =OO00O00000000000O #line:19
def kock (OOO0O000000OO0OOO ,OO0O0O00OO00O0O00 ,O0OO0000OOOOO0OO0 ):#line:22
    if OOO0O000000OO0OOO ==0 :#line:23
        return #line:24
    OO0000O00O0O0O00O =Coordinate ((2 *OO0O0O00OO00O0O00 .x +O0OO0000OOOOO0OO0 .x )/3 ,(2 *OO0O0O00OO00O0O00 .y +O0OO0000OOOOO0OO0 .y )/3 )#line:26
    OOO0000OOOOO0OOOO =Coordinate ((OO0O0O00OO00O0O00 .x +2 *O0OO0000OOOOO0OO0 .x )/3 ,(OO0O0O00OO00O0O00 .y +2 *O0OO0000OOOOO0OO0 .y )/3 )#line:27
    O000OO00OOOOOO00O =Coordinate ((OOO0000OOOOO0OOOO .x -OO0000O00O0O0O00O .x )*math .cos (math .pi /3 )-(OOO0000OOOOO0OOOO .y -OO0000O00O0O0O00O .y )*math .sin (math .pi /3 )+OO0000O00O0O0O00O .x ,(OOO0000OOOOO0OOOO .x -OO0000O00O0O0O00O .x )*math .sin (math .pi /3 )+(OOO0000OOOOO0OOOO .y -OO0000O00O0O0O00O .y )*math .cos (math .pi /3 )+OO0000O00O0O0O00O .y )#line:33
    kock (OOO0O000000OO0OOO -1 ,OO0O0O00OO00O0O00 ,OO0000O00O0O0O00O )#line:35
    print (OO0000O00O0O0O00O .x ,OO0000O00O0O0O00O .y )#line:36
    kock (OOO0O000000OO0OOO -1 ,OO0000O00O0O0O00O ,O000OO00OOOOOO00O )#line:37
    print (O000OO00OOOOOO00O .x ,O000OO00OOOOOO00O .y )#line:38
    kock (OOO0O000000OO0OOO -1 ,O000OO00OOOOOO00O ,OOO0000OOOOO0OOOO )#line:39
    print (OOO0000OOOOO0OOOO .x ,OOO0000OOOOO0OOOO .y )#line:40
    kock (OOO0O000000OO0OOO -1 ,OOO0000OOOOO0OOOO ,O0OO0000OOOOO0OO0 )#line:41
def main ():#line:44
    O0OOOO0OOOO0O0O00 =int (input ())#line:45
    OOO0O00OOOOO0OO0O =Coordinate (0 ,0 )#line:47
    OOO0OOOOO000O0OO0 =Coordinate (100 ,0 )#line:48
    print (OOO0O00OOOOO0OO0O .x ,OOO0O00OOOOO0OO0O .y )#line:50
    kock (O0OOOO0OOOO0O0O00 ,OOO0O00OOOOO0OO0O ,OOO0OOOOO000O0OO0 )#line:51
    print (OOO0OOOOO000O0OO0 .x ,OOO0OOOOO000O0OO0 .y )#line:52
if __name__ =='__main__':#line:55
    main ()#line:56
