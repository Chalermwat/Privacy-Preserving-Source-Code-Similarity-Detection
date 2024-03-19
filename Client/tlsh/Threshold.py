import tlsh
import os
import fuzzyhash as fh
import matplotlib.pyplot as plt

path = './Threshold_data'
dir_list = os.listdir(path)
static_var=False
hash_list=[]
for i in dir_list:
    filepath = path+'/'+i

    # With Normalized
    process_code = fh.processing(filepath,static_var)
    fuzzyHash = fh.genFuzzyHash(process_code)
    hash_list.append((i,fuzzyHash))

print(hash_list)
score_list=[]
for i in range(len(hash_list)-1):
    for j in range(i+1,len(hash_list)):
        hash1 = hash_list[i][1]
        hash2 = hash_list[j][1]
        score = tlsh.diffxlen(hash1,hash2)
        score_list.append((hash_list[i],hash_list[j],score))

s=0
s_list=[]
for i in score_list:
    # if i[2] < 150 : print(i)
    print(i[2])
    s_list.append(i[2])
    s+=i[2]

from statistics import mean 

print('Max:',max(s_list))
print('Mean:',mean(s_list))
print('Min:',min(s_list))

plt.boxplot(s_list)
plt.show()






