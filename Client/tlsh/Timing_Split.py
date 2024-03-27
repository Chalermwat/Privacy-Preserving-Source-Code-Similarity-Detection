import os
import time
import tlsh
import matplotlib.pyplot as plt
import fuzzyhash as fh

def genFuzzyHash(filename):
    with open(filename, 'r') as f:
        code_string = ''.join(f.readlines())
    return tlsh.hash(code_string.encode())

def splitLine(normalized_code,amountOfLine):
    line_list = normalized_code.split('\n')
    line_list = [i for i in line_list if i != '']
    out_list=[]

    if(len(line_list)<amountOfLine): amountOfLine=len(line_list)

    start=0
    end=start+amountOfLine

    while True:
        if(end>len(line_list)): 
            # print(start,end)
            if(end-start>amountOfLine):
                current_codeBlock = ''.join(line_list[start-1:end])
                # print(current_codeBlock)
                out_data = (start,end,current_codeBlock)
                out_list.append(out_data)
            break

        # print(start,end)
        current_codeBlock = ''.join(line_list[start:end])
        if(end-start>=amountOfLine):
            if(len(current_codeBlock)>50): 
                # print(current_codeBlock)
                out_data = (start,end,current_codeBlock)
                out_list.append(out_data)
                start+=1
                end=start+amountOfLine
            else:
                end+=1
        else:
            end+=1
    # print(line_list,len(line_list))
    return out_list

def genFuzzyHashList(split_list):
    out_map = {}
    for i in split_list:
        hash = fh.genFuzzyHash(i[2])
        if hash=='TNULL': continue
        key = f'S{i[0]}E{i[1]}'
        out_map[key] = hash
    return out_map


path = './Timing/Sample_Split'
dir_list = os.listdir(path)
static_var=False
process_list = []
size_list = []
compare_list = []
out_list = []
for i in dir_list:
    filepath = path+'/'+i
    file_size = os.path.getsize(filepath)
    size_list.append(file_size)

    # With Normalized
    start_normalized = time.time()
    process_code = fh.processing(filepath,static_var)
    splitList = splitLine(process_code,10)
    fuzzyHashList = genFuzzyHashList(splitList)
    end_normalized = time.time()
    normalized_time = end_normalized-start_normalized
    process_list.append(normalized_time)

    out_list.append((file_size,normalized_time))

# my_dict = {'With Normalizing': process_list}
# fig, ax = plt.subplots()
# ax.boxplot(my_dict.values())
# ax.set_xticklabels(my_dict.keys())

out_list.sort()
x = []
y = []
for i in out_list:
    x.append(i[0])
    y.append(i[1])
plt.plot(x,y)
plt.show()

from statistics import mean 

print('Max_normalized:',round(max(process_list),8))
print('Mean_normalized:',round(mean(process_list),8))
print('Min_normalized:',round(min(process_list),8))

