N =int (input ())#line:1
T =[int (O0OOO000O0OO0OOOO )for O0OOO000O0OO0OOOO in input ().split ()]#line:2
A =[int (OO0O0O0OOO0OO0000 )for OO0O0O0OOO0OO0000 in input ().split ()]#line:3
mod =10 **9 +7 #line:4
mountain =[T [0 ]]#line:5
for i in range (1 ,N ):#line:6
    if T [i ]>T [i -1 ]:#line:7
        mountain .append (T [i ])#line:8
    else :#line:9
        mountain .append (-T [i ])#line:10
ans =1 #line:11
if N ==1 :#line:12
    if T [0 ]!=A [0 ]:#line:13
        print (0 )#line:14
        exit ()#line:15
for i in range (N -1 ,-1 ,-1 ):#line:16
    if i ==N -1 :#line:17
        if (A [i ]>mountain [i ])&(mountain [i ]>0 ):#line:18
            ans =0 #line:19
            break #line:20
        mountain [i ]=A [i ]#line:21
    elif mountain [i ]<=0 :#line:22
        if A [i ]>A [i +1 ]:#line:23
            if -mountain [i ]>=A [i ]:#line:24
                mountain [i ]=A [i ]#line:25
            else :#line:26
                ans =0 #line:27
                break #line:28
        else :#line:29
            mountain [i ]=-min (A [i ],-mountain [i ])#line:30
    else :#line:31
        if A [i ]>=mountain [i ]:#line:32
            continue #line:33
        else :#line:34
            ans =0 #line:35
            break #line:36
    if mountain [i ]<0 :#line:37
        ans =(-ans *mountain [i ])%mod #line:38
print (ans )