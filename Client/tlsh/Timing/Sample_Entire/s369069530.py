data = input()
#data = '\\\\///\\_/\\/\\\\\\\\/_/\\\\///__\\\\\\_\\\\/_\\/_/\\'
diff = {'\\':-1, '_':0, '/':1}
height = [0]
[height.append(height[-1]+diff[i]) for i in data]
bottom = min(height)
height = [h-bottom for h in height]

m = max(height)
water = [m for h in height]

height00 = [0] + height + [0]
water00 = [0] + water + [0]

roop = True
forward = 1
while roop:
	temp = water00[:]
	for i in range(1,len(water00)-1)[::forward]:
		water00[i] = max(height00[i],min(water00[i-1:i+2]))
	roop = temp != water00
	forward *= -1

water = water00[1:-1]
depth = [w-h for w,h in zip(water,height)]

paddles = [0]
for d1,d2 in zip(depth[:-1],depth[1:]):
	if d1==0 and d2>0:
		paddles.append(0)
	paddles[-1] += min(d1,d2) + 0.5*abs(d1-d2)

paddles = [int(p) for p in paddles[1:]]
print(sum(paddles))
print(len(paddles), *paddles)