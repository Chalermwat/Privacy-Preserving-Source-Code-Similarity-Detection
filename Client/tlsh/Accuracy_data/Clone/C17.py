import sys #line:2
import math #line:3
from bisect import bisect_left ,bisect_right ,insort_left ,insort_right #line:4
from collections import defaultdict ,deque ,Counter #line:5
from copy import deepcopy #line:6
from fractions import gcd #line:7
from functools import lru_cache ,reduce #line:8
from heapq import heappop ,heappush #line:9
from itertools import accumulate ,groupby ,product ,permutations ,combinations ,combinations_with_replacement #line:10
from math import ceil ,floor ,factorial ,log ,sqrt ,sin ,cos #line:11
from operator import itemgetter #line:12
from string import ascii_lowercase ,ascii_uppercase ,digits #line:13
sys .setrecursionlimit (10 **6 )#line:14
rs =lambda :sys .stdin .readline ().rstrip ()#line:15
ri =lambda :int (rs ())#line:16
rf =lambda :float (rs ())#line:17
rs_ =lambda :[_O00O00O0O0OOO0OOO for _O00O00O0O0OOO0OOO in rs ().split ()]#line:18
ri_ =lambda :[int (_O0O000O00O000O00O )for _O0O000O00O000O00O in rs ().split ()]#line:19
rf_ =lambda :[float (_OO0O0OO00OOO00000 )for _OO0O0OO00OOO00000 in rs ().split ()]#line:20
INF =float ('inf')#line:21
MOD =10 **9 +7 #line:22
N =ri ()#line:24
C =[0 ]*(N -1 )#line:25
S =[0 ]*(N -1 )#line:26
F =[0 ]*(N -1 )#line:27
for i in range (N -1 ):#line:28
    C [i ],S [i ],F [i ]=ri_ ()#line:29
dp =[0 ]*N #line:30
for i in range (N ):#line:31
    dp [i ]=0 #line:32
    for j in range (i ,N -1 ):#line:33
        dp [j +1 ]=C [j ]+max (S [j ],ceil (dp [j ]/F [j ])*F [j ])#line:34
    print (dp [N -1 ])