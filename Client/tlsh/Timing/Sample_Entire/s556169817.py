class card(object):
    def __init__(self, str):
        self.symbol = str[0]
        self.num = int(str[1:])
    
    def __lt__(self,obj):
        if(self.num < obj.num):
            return True
        else:
            return False
    def __gt__(self,obj):
        if(self.num > obj.num):
            return True
        else:
            return False

    def display_card(self):
        print("{0}{1}".format(self.symbol,self.num),end="")

n = int(input())
s = input()
org = list(map(card,s.split()))  

bub = list(org)
sel = list(org)

#####################################
"""
Bubble sort(bub[])
""" '''
for i in range(0,len(bub)):
    for j in range(len(bub)-1,i-1,-1):
        if(bub[j] < bub[j-1]):
            tmp = bub[j]
            bub[j] = bub[j-1]
            bub[j-1] = tmp
'''
flag = True
while(flag==True):
    flag = False
    for i in range(1,len(bub)):
        if(bub[i]<bub[i-1]):
            bub[i],bub[i-1] = bub[i-1],bub[i]
            flag = True


"""
selection sort(sel[])
"""

for i in range(0,len(sel)-1):
    minj = i
    for j in range(i,len(sel)):
        if(sel[j] < sel[minj]):
            minj = j
    sel[i],sel[minj] = sel[minj],sel[i]
       
"""
comp org(org[])
"""


# buble

for i in range(0,len(bub)):
    bub[i].display_card()
    if (i==len(bub)-1):
        print("\n",end="")
    else :
        print(" ",end="")
print("Stable")
# selec
                
for i in range(0,len(sel)):
    sel[i].display_card()
    if (i==len(sel)-1):
        print("\n",end="")
    else :
        print(" ",end="")
if(bub == sel): 
    print("Stable")
else:
    print("Not stable")