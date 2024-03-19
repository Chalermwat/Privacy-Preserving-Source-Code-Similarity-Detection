import math
import sys
import itertools
from collections import deque
# import numpy as np

def main():
  S = sys.stdin.readline()
  len_S = len(S)

  index = 0 # 操作しているSのインデックス
  DOWN = [] # 下り文字をスタック
  POOL = [] # 水たまりごとの面積
  area = 0 # 総面積

  for s in S:
    if s == '\\':
      DOWN.append(index)

    elif s == '/' and len(DOWN) > 0:
      pool_start = DOWN.pop()
      pool_end = index
      tmp_area = pool_end - pool_start
      area += tmp_area

      while True:
        if len(POOL) == 0:
          break
        if POOL[-1]['start'] > pool_start and POOL[-1]['end'] < pool_end:
          tmp_area += POOL[-1]['area']
          POOL.pop()
        else:
          break

      POOL.append({'start': pool_start, 'end': pool_end, 'area': tmp_area})

    index += 1

  print(area)
  if len(POOL) > 0:
    print(len(POOL), end=" ")
    for i in range(len(POOL)-1):
      print(POOL[i]['area'], end=" ")
    print(POOL[-1]['area'])
  else:
    print(0)

if __name__ == '__main__':
  main()
