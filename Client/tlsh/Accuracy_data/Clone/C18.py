class UnionFind :#line:1
  def __init__ (OO000OO00OOOO00OO ,O00O00OOO0000O0O0 ):#line:2
    OO000OO00OOOO00OO .n =O00O00OOO0000O0O0 #line:3
    OO000OO00OOOO00OO .parent =[OOOOOOOO0O0OO0O0O for OOOOOOOO0O0OO0O0O in range (O00O00OOO0000O0O0 )]#line:4
    OO000OO00OOOO00OO .rank =[1 ]*O00O00OOO0000O0O0 #line:5
    OO000OO00OOOO00OO .size =[1 ]*O00O00OOO0000O0O0 #line:6
  def find (O0OO000O0OOOO00O0 ,O00O00000OO0O00OO ):#line:8
    if O0OO000O0OOOO00O0 .parent [O00O00000OO0O00OO ]==O00O00000OO0O00OO :#line:9
      return O00O00000OO0O00OO #line:10
    else :#line:11
      O0OO000O0OOOO00O0 .parent [O00O00000OO0O00OO ]=O0OO000O0OOOO00O0 .find (O0OO000O0OOOO00O0 .parent [O00O00000OO0O00OO ])#line:12
      return O0OO000O0OOOO00O0 .parent [O00O00000OO0O00OO ]#line:13
  def unite (OOO000000OOOOO0O0 ,O00O0O00000OO00OO ,O00OO00000O0O00OO ):#line:15
    O00O0O00000OO00OO =OOO000000OOOOO0O0 .find (O00O0O00000OO00OO )#line:16
    O00OO00000O0O00OO =OOO000000OOOOO0O0 .find (O00OO00000O0O00OO )#line:17
    if O00O0O00000OO00OO !=O00OO00000O0O00OO :#line:18
      if OOO000000OOOOO0O0 .rank [O00O0O00000OO00OO ]<OOO000000OOOOO0O0 .rank [O00OO00000O0O00OO ]:#line:19
        OOO000000OOOOO0O0 .parent [O00O0O00000OO00OO ]=O00OO00000O0O00OO #line:20
        OOO000000OOOOO0O0 .size [O00OO00000O0O00OO ]+=OOO000000OOOOO0O0 .size [O00O0O00000OO00OO ]#line:21
      else :#line:22
        OOO000000OOOOO0O0 .parent [O00OO00000O0O00OO ]=O00O0O00000OO00OO #line:23
        OOO000000OOOOO0O0 .size [O00O0O00000OO00OO ]+=OOO000000OOOOO0O0 .size [O00OO00000O0O00OO ]#line:24
        if OOO000000OOOOO0O0 .rank [O00O0O00000OO00OO ]==OOO000000OOOOO0O0 .rank [O00OO00000O0O00OO ]:#line:25
          OOO000000OOOOO0O0 .rank [O00O0O00000OO00OO ]+=1 #line:26
  def group_size (O000OOOOO000OO00O ,O0O0O0OOO0OO00O0O ):#line:28
    return O000OOOOO000OO00O .size [O000OOOOO000OO00O .find (O0O0O0OOO0OO00O0O )]#line:29
N ,M =map (int ,input ().split ())#line:31
A ,B =[0 ]*M ,[0 ]*M #line:32
direct =[[]for _OOOO0OO0O000O0O00 in range (N )]#line:34
uf =UnionFind (N )#line:35
for i in range (M ):#line:37
    A [i ],B [i ]=map (int ,input ().split ())#line:38
    A [i ]-=1 #line:39
    B [i ]-=1 #line:40
    uf .unite (A [i ],B [i ])#line:41
ans =0 #line:43
for i in range (N ):#line:44
    ans =max (ans ,uf .group_size (i ))#line:45
print (ans )