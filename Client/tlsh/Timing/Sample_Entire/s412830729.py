s=input()
d_in={'/':1,'\\':-1,'_':0}
stack_h=[]
pairs_x=[]
for i in range(len(s)):
  if d_in[s[i]]==-1:
    stack_h.append(i)
  elif d_in[s[i]]==1:
    if len(stack_h)!=0:
      pairs_x.append([stack_h.pop(),i+1])
stack_ans=[]
for i in range(len(pairs_x)):
  pair_i=pairs_x.pop()
  if len(stack_ans)==0:
    stack_ans.append(pair_i)
  elif pair_i[1]<=stack_ans[-1][0]:
    stack_ans.append(pair_i)
area=[0]*len(stack_ans)
sum_area=0
for i in range(len(stack_ans)):
  p=stack_ans.pop()
  h=0
  for j in range(p[0],p[1]):
    area[i]+=h
    h-=d_in[s[j]]
  sum_area+=area[i]

print(sum_area)
if len(area)==0:
  print(0)
else:
  print(len(area),end=' ')
  print(' '.join(map(str,area)))
