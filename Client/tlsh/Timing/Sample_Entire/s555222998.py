from copy import  deepcopy
def bubble_sort(lst):
    size=len(lst)
    for i in xrange(size):
        for j in reversed(range(i+1,size)):
            if lst[j].num<lst[j-1].num:
                tmp=lst[j]
                lst[j]=lst[j-1]
                lst[j-1]=tmp
def selection_sort(lst):
    size=len(lst)
    for i in xrange(size):
        mn=i
        for j in xrange(i+1,size):
            if lst[mn].num>lst[j].num:
                mn=j
        tmp=lst[i]
        lst[i]=lst[mn]
        lst[mn]=tmp
class pock:
    def __init__(self,val):
        self.val=val
        self.num=int(val[1:])
    def __gt__(self,other):
        return self.num>other.num


num=raw_input().strip()
inp=raw_input().strip().split()
arr=[]
for ii in inp:
    arr.append(pock(ii))
bubb=deepcopy(arr)
bubble_sort(bubb)
insec=deepcopy(arr)
selection_sort(insec)
print " ".join(pp.val for pp in bubb)
print "Stable"

print " ".join(pp.val for pp in insec)
ok=1
ln=len(arr)
for i  in xrange(ln):
    if(bubb[i].val!=insec[i].val):
        ok=0
        break
if ok==1:
    print "Stable"
else:
    print "Not stable"

