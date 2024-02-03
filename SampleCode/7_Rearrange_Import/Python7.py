import argparse
import ssdeep

parser = argparse.ArgumentParser(description='Generate Fussy Hash')
parser.add_argument('filepath', metavar='FilePath', type=str,
                    help='File path to source code')

args = parser.parse_args()
import os
def genFuzzyHash(filename):
    with open(filename, 'r') as f:
        code_string = ''.join(f.readlines())
    print(code_string)
    return ssdeep.hash(code_string)
import re
if __name__ == "__main__":
    fuzzyHash = genFuzzyHash(args.filepath)
    print('Fuzzy hash:',fuzzyHash)
import time