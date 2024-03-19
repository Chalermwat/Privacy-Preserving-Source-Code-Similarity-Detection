s = input()
st1=[]
st2=[]
st3=[]
n=len(s)
lv = 0
for i in range(n):
	c=s[i]
	if c=='\\':
		lv-=1
		st1.append(i)
	elif c=='/':
		lv+=1
		if len(st1) > 0:
			a = i - st1.pop()
			if len(st2)==0 or st2[len(st2)-1]>=lv:
				st3.append(a)
			else:
				t=0	
				while len(st2)>0 and st2[len(st2)-1]<lv:
					st2.pop()
					t+=st3.pop()
				st3.append(a+t)		
			st2.append(lv)
		else:
			if len(st2) > 0:
				st2.pop()
				st2.append(lv)
				
st=''
total=0
n = len(st3)
st+=str(n)
for i in range(n):
	st+=' '+str(st3[i])
	total+=(st3[i])
print(total)
print(st)

