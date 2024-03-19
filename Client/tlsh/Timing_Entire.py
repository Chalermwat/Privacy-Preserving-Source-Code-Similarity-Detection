import os
import time
import tlsh
import matplotlib.pyplot as plt
import fuzzyhash as fh

def genFuzzyHash(filename):
    with open(filename, 'r') as f:
        code_string = ''.join(f.readlines())
    return tlsh.hash(code_string.encode())


path = './Timing/Sample_Entire'
dir_list = os.listdir(path)
static_var=False
size_list = []
out_dict = {'size':[],'process':[],'hash':[]}
process_list = []
hash_list = []
out_list = []
for i in dir_list:
    filepath = path+'/'+i
    size_list.append(os.path.getsize(filepath))

    # With Normalized
    start_normalized = time.time()
    process_code = fh.processing(filepath,static_var)
    fuzzyHash = fh.genFuzzyHash(process_code)
    end_normalized = time.time()
    normalized_time = end_normalized-start_normalized
    process_list.append(normalized_time)

    # Without Nomalized
    start_hash = time.time()
    fuzzyHash = genFuzzyHash(filepath)
    end_hash = time.time()
    hash_time = end_hash-start_hash
    hash_list.append(hash_time)

    diffTIme = normalized_time-hash_time
    
    out_dict['size'].append(os.path.getsize(filepath))
    out_dict['process'].append(normalized_time)
    out_dict['hash'].append(hash_time)

    out_list.append((os.path.getsize(filepath),normalized_time))

my_dict = {'With Normalizing': process_list, 'Without Normalizing': hash_list}
fig, ax = plt.subplots()
ax.boxplot(my_dict.values())
ax.set_xticklabels(my_dict.keys())
plt.show()

from statistics import mean 

print('Max_normalized:',round(max(process_list),8))
print('Mean_normalized:',round(mean(process_list),8))
print('Min_normalized:',round(min(process_list),8))

print('Max:',format(max(hash_list),'.8f'))
print('Mean:',format(mean(hash_list),'.8f'))
print('Min:',format(min(hash_list),'.8f'))
