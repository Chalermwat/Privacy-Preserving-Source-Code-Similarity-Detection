
N = int(raw_input())
line = raw_input()

num_list1 = line.split()

num_list2 = line.split()


flag = 1
while flag==1:
    flag =0
    for j in range(N-1,0,-1):
        if int(num_list1[j][1:]) < int(num_list1[j-1][1:]):
            a = num_list1[j]
            num_list1[j] = num_list1[j-1]
            num_list1[j-1] = a
           
            flag =1

print " ".join(num_list1)
print "Stable"



for i in range(0,N,1):
   
    minj =i
    for j in range(i,N,1):
        if int(num_list2[j][1:]) < int(num_list2[minj][1:]):
            minj = j
            
    num_list2[i], num_list2[minj] = num_list2[minj], num_list2[i]
print " ".join(num_list2)


if num_list1 == num_list2: 
    print "Stable"
else:
    print "Not stable"