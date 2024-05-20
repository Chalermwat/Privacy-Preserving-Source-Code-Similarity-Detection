import sys #line:1
write =sys .stdout .write #line:2
number_of_numbers =[]#line:4
numbers =[]#line:5
number_of_numbers =input ().split ()#line:7
number_of_numbers [0 ]=int (number_of_numbers [0 ])#line:8
number_of_numbers [1 ]=int (number_of_numbers [1 ])#line:9
for i in range (0 ,number_of_numbers [0 ]):#line:13
    line_nunmbers =[]#line:14
    line_numbers =input ().split ()#line:15
    for j in range (0 ,len (line_numbers )):#line:16
        line_numbers [j ]=int (line_numbers [j ])#line:17
    numbers .append (line_numbers )#line:18
right_end_numbers =[]#line:20
under_end_numbers =[]#line:21
for i in range (0 ,len (numbers )):#line:23
    right_end_numbers .append (sum (numbers [i ]))#line:24
for i in range (0 ,len (numbers [0 ])):#line:26
    under_end_number =0 #line:27
    for j in range (0 ,len (numbers )):#line:28
        under_end_number +=numbers [j ][i ]#line:29
    under_end_numbers .append (under_end_number )#line:30
for i in range (0 ,len (numbers )):#line:32
    for j in range (0 ,len (numbers [0 ])):#line:33
        write (str (numbers [i ][j ]))#line:34
        write (' ')#line:35
    print (right_end_numbers [i ])#line:36
for i in range (0 ,len (numbers [0 ])):#line:38
    write (str (under_end_numbers [i ]))#line:39
    write (' ')#line:40
print (sum (under_end_numbers ))