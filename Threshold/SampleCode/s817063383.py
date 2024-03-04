import heapq
import copy
N, K = map(int, input().split())
V = list(map(int, input().split()))

max_val = 0
left_hq = list()
left_val = 0
for left in range(N+1):
    if left > 0:
        heapq.heappush(left_hq,V[left-1])
        left_val += V[left-1]
        all_hq = copy.deepcopy(left_hq)
        all_val = left_val
        for right in range(N+1):
            if right+left > K or right+left > N :
                continue
            if right > 0:
                heapq.heappush(all_hq,V[-right])
                all_val += V[-right]
            
            temp_hq = copy.deepcopy(all_hq)
            temp_val = all_val
            for i in range(K-left-right):
                if len(temp_hq) == 0:
                    break
                else:
                    minus = heapq.heappop(temp_hq)
                    if minus > 0:
                        break
                    temp_val -= minus
                    
            if temp_val > max_val:
                max_val = temp_val
print(max_val)
