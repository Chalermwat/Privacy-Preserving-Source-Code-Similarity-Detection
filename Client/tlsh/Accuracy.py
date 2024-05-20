import os
import re
import tlsh
import matplotlib.pyplot as plt
import fuzzyhash as fh
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score

def genFuzzyHash(filename):
    with open(filename, 'r') as f:
        code_string = ''.join(f.readlines())
    return tlsh.hash(code_string.encode())


original_path = './Accuracy_data/Original'
clone_path = './Accuracy_data/Clone'
original_filelist = os.listdir(original_path)
clone_filelist = os.listdir(clone_path)

o_list = []
c_list = []

for o in original_filelist:
    test_number = re.findall(r'[0-9]+', o)

    o_path = original_path +'/' + o
    o_list.append((int(test_number[0]),o_path))

for c in clone_filelist:
    test_number = re.findall(r'[0-9]+', c)

    c_path = clone_path +'/' + c
    c_list.append((int(test_number[0]),c_path))

o_list.sort()
c_list.sort()

# print(o_list)
# print(c_list)

static_var=False
data = {
    "OriginalFile": [],
    "CloneFile": [],
    "Score": [],
    "Predict": [],
    "Truth Value": []
}
for o in o_list:
    o_process_code = fh.processing(o[1],static_var)

    # with open(o[1], 'r') as fo:
    #     o_process_code = ''.join(fo.readlines())
    fuzzyHash_O = fh.genFuzzyHash(o_process_code)
    for c in c_list:
        c_process_code = fh.processing(c[1],static_var)

        # with open(c[1], 'r') as fc:
        #     c_process_code = ''.join(fc.readlines())
        fuzzyHash_C = fh.genFuzzyHash(c_process_code)

        score = tlsh.diffxlen(fuzzyHash_O,fuzzyHash_C)
        data["OriginalFile"].append(o[1])
        data["CloneFile"].append(c[1])
        data["Score"].append(score)
        data["Predict"].append(1 if score <145 else 0)
        data["Truth Value"].append(1 if c[0]==o[0] else 0)

df = pd.DataFrame(data)
print(df) 

# df.to_csv('out.csv', index=False)  

print(df[df["Predict"] != df["Truth Value"]])
# print(df[df["Truth Value"]==1])

print("Accuracy")
print(accuracy_score(df["Truth Value"], df["Predict"]))
print("Precision")
print(precision_score(df["Truth Value"], df["Predict"], average='binary'))
print("Recall")
print(recall_score(df["Truth Value"], df["Predict"], average='binary'))

# static_var=False
# process_list = []
# hash_list = []
# compare_list = []
# out_list = []
# for i in dir_list:
#     filepath = path+'/'+i

#     # With Normalized
#     start_normalized = time.time()
#     process_code = fh.processing(filepath,static_var)
#     fuzzyHash1 = fh.genFuzzyHash(process_code)
#     end_normalized = time.time()
#     normalized_time = end_normalized-start_normalized
#     process_list.append(normalized_time)

#     # Without Nomalized
#     start_hash = time.time()
#     fuzzyHash2 = genFuzzyHash(filepath)
#     end_hash = time.time()
#     hash_time = end_hash-start_hash
#     hash_list.append(hash_time)

#     # Comparison
#     start_compare = time.time()
#     tlsh.diffxlen(fuzzyHash1,fuzzyHash2)
#     end_compare = time.time()
#     comparison_time = end_compare-start_compare
#     compare_list.append(comparison_time)

#     diffTIme = normalized_time-hash_time
#     out_list.append((os.path.getsize(filepath),normalized_time))

# # my_dict = {'With Normalizing': process_list, 'Without Normalizing': hash_list}
# my_dict = {'Comparison Time': comparison_time}
# fig, ax = plt.subplots()
# ax.boxplot(my_dict.values())
# ax.set_xticklabels(my_dict.keys())
# plt.show()

# from statistics import mean 

# # print('Max_normalized:',round(max(process_list),8))
# # print('Mean_normalized:',round(mean(process_list),8))
# # print('Min_normalized:',round(min(process_list),8))

# # print('Max_not:',format(max(hash_list),'.8f'))
# # print('Mean_not:',format(mean(hash_list),'.8f'))
# # print('Min_not:',format(min(hash_list),'.8f'))

# print('Max_compare:',format(max(compare_list),'.8f'))
# print('Mean_Max_compare:',format(mean(compare_list),'.8f'))
# print('Min_Max_compare:',format(min(compare_list),'.8f'))
