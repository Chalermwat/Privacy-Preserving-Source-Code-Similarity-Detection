import argparse
import json
import fuzzyhash as fh


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

def displayProcessCode(normalized_code):
    line_list = normalized_code.split('\n')
    line_list = [i for i in line_list if i != '']
    for i in range(len(line_list)):
        print(f'Line {"{:03d}".format(i)} : {line_list[i]}')

parser = argparse.ArgumentParser(description='Generate Fussy Hash')
parser.add_argument('filepath', metavar='FilePath', type=str,
                    help='File path to source code')
parser.add_argument('--line', dest='line', type=int, default=10,
                    help='Number of Line to split (default: 10)')

args = parser.parse_args()

if __name__ == "__main__":
    static_var=False
    # prepro_code = removeMultilineComment(args.filepath)
    # process_code = processing(TMP_FILENAME,static_var)
    process_code = fh.processing(args.filepath,static_var)
    print('\n******************** Normalized Code ********************')
    displayProcessCode(process_code)
    print('*********************************************************\n')
    fuzzyHash = fh.genFuzzyHash(process_code)
    print('Fuzzy hash:',fuzzyHash)
    splitList = splitLine(process_code,args.line)
    fuzzyHashList = genFuzzyHashList(splitList)
    print(f"Split every {args.line} lines")
    print('FuzzyHashList:',json.dumps({'HashList':fuzzyHashList}))