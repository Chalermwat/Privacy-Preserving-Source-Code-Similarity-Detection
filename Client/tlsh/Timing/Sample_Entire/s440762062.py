def is_stable(output_str, same_num_str):
    if len(same_num_str)>0:
        for i in range(len(same_num_str)):
            if output_str.find(same_num_str[i]) == -1:
                return "Not stable"
    return "Stable"
    
data_num = int(input())
cards = input().split(" ")
cards2 = cards[:]
cnt = 0
num_1 = 0
num_2 = 0
same_num_str = []
output_str = ""
judge_stbl = ""
for i in range(data_num):
    
    for j in range(data_num-1, i,-1):
        if int(cards[j][1:]) < int(cards[j-1][1:]):
            cards[j], cards[j-1] = cards[j-1], cards[j]
        elif int(cards[j][1:]) == int(cards[j-1][1:]):
            same_num_str.append(cards[j-1]+" "+cards[j])    
            
output_str = " ".join(cards) 
judge_stbl = is_stable(output_str, same_num_str)

print(output_str + "\n" + judge_stbl)

same_num_str = []
output_str = ""
judge_stbl = ""

for i in range(data_num):
    min_idx = i
    for j in range(i, data_num):
        if int(cards2[j][1:]) < int(cards2[min_idx][1:]):
            min_idx = j
        elif int(cards2[j][1:]) == int(cards2[min_idx][1:]) and j != min_idx:
            same_num_str.append(cards2[min_idx]+" "+cards2[j])    

    if i != min_idx:
        cards2[i], cards2[min_idx] = cards2[min_idx], cards2[i]

output_str = " ".join(cards2) 
judge_stbl = is_stable(output_str, same_num_str)

print(output_str + "\n" + judge_stbl)