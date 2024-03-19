import sys
from collections import deque

def test():

	EleList = deque()
	sublist = []
	output = []
	areas_from_left = list(sys.stdin.readline())
	sum = 0
	depth = 0

	for element in areas_from_left:

		if element == '\\':
			depth += 1
			EleList.append(element)

		elif element == '_':
			if EleList:
				EleList.append(element)

		elif element == '/':
			depth -= 1
			if EleList:
				for pop_count in range(len(EleList)):
				
					pop_ele = EleList.pop()
					if pop_ele == '\\' and EleList:
						for i in range(pop_count+2):
							EleList.append('_')
						break
				lake = pop_count + 1
				sum += lake

				if len(EleList) == 0:
					if len(sublist) == 0:
						output.append(lake)
					else:
						tmp = 0
						for i in sublist:
							tmp += i[0]
						output.append(tmp + lake)
						sublist.clear()
				else:
					
					if not sublist or sublist[len(sublist)-1][1] < depth:
						sublist_element = [0,0]
						sublist_element[0] = lake
						sublist_element[1] = depth
						sublist.append(sublist_element)
					
					else:

						sublist_element = [lake,depth]

						while True:
							
							if not sublist:
								break

							tmp = sublist.pop()
							if tmp[1] > depth:
								sublist_element[0] += tmp[0]
							else:
								sublist.append(tmp)
								break

						sublist.append(sublist_element)
				#print(f"{output}{sublist}")

	output_sublist = []
	for tmp in sublist:
		output_sublist.append(tmp[0])

	output = output + output_sublist
	length = len(output)

	print(sum)
	if length != 0:
		print(f"{length} ",end='')
	else:
		print(length)
	

	for i in range(length - 1):
		print(f"{output[i]} ",end='')
	if output:
		print(output[length-1])

if __name__ == "__main__":
	test()
