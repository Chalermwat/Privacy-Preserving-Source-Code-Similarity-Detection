from collections import deque

section = raw_input( )
depth = 0
area = 0
depthArr = deque( )
areaArr = deque( )

for i, ground in enumerate( section ):
	if "\\" == ground:
		depth += 1
		depthArr.append( i )
	elif 0 < depth and "/" == ground:
		if len( depthArr ):
			j = depthArr.pop( )
			pool =  i - j
			area += pool

			while len( areaArr ):
				preJ, prePool = areaArr.pop( )
				if j <= preJ:
					pool += prePool
				else:
					areaArr.append( ( preJ, prePool ) )
					break
			areaArr.append( ( j, pool ) )

print( area )
output = []
output.append( len( areaArr ) )
for arr in areaArr:
	output.append( arr[1] )
print( " ".join( map( str, output ) ) )