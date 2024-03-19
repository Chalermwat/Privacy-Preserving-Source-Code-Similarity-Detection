import queue

inpstr = input()
stack = queue.LifoQueue()
stack_areas = queue.LifoQueue()

cnt = 0  # 位置
area = 0  # 総面積
for s in inpstr:
	if s == '\\':
		stack.put(cnt)
	elif s == '/':
		if not stack.empty():
			i = stack.get()
			area = area + cnt - i
			# 個々の面積の再計算
			temp = [i, cnt - i]  # 今回の面積と開始位置
			if stack_areas.empty():
				stack_areas.put(temp)
			else:
				for j in range(0, stack_areas.qsize()):
					temp2 = stack_areas.get()
					if i > temp2[0]:
						stack_areas.put(temp2)
						break
					else:
						temp[1] = temp[1] + temp2[1]
				stack_areas.put(temp)
	elif s == '_':
		pass  # 何もしない、結果cntだけ増える
	cnt = cnt + 1

print(area)
# stackから出力用のリストに変換
areas = []
while not stack_areas.empty():
	areas.append(stack_areas.get()[1])
#print(areas)
areas.append(len(areas))
areas.reverse()
print(' '.join([str(n) for n in areas]))

