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
process_list = []
hash_list = []
compare_list = []
out_list = []
for i in dir_list:
    filepath = path+'/'+i

    # With Normalized
    start_normalized = time.time()
    process_code = fh.processing(filepath,static_var)
    fuzzyHash1 = fh.genFuzzyHash(process_code)
    end_normalized = time.time()
    normalized_time = end_normalized-start_normalized
    process_list.append(normalized_time)

    # Without Nomalized
    start_hash = time.time()
    fuzzyHash2 = genFuzzyHash(filepath)
    end_hash = time.time()
    hash_time = end_hash-start_hash
    hash_list.append(hash_time)

    # Comparison
    start_compare = time.time()
    tlsh.diffxlen(fuzzyHash1,fuzzyHash2)
    end_compare = time.time()
    comparison_time = end_compare-start_compare
    compare_list.append(comparison_time)

    diffTIme = normalized_time-hash_time
    out_list.append((os.path.getsize(filepath),normalized_time))

# my_dict = {'With Normalizing': process_list, 'Without Normalizing': hash_list}
my_dict = {'Comparison Time': compare_list}
fig, ax = plt.subplots()
ax.boxplot(my_dict.values())
ax.set_xticklabels(my_dict.keys())
plt.show()

from statistics import mean 

# print('Max_normalized:',round(max(process_list),8))
# print('Mean_normalized:',round(mean(process_list),8))
# print('Min_normalized:',round(min(process_list),8))

# print('Max_not:',format(max(hash_list),'.8f'))
# print('Mean_not:',format(mean(hash_list),'.8f'))
# print('Min_not:',format(min(hash_list),'.8f'))

print('Max_compare:',format(max(compare_list),'.8f'))
print('Mean_Max_compare:',format(mean(compare_list),'.8f'))
print('Min_Max_compare:',format(min(compare_list),'.8f'))
