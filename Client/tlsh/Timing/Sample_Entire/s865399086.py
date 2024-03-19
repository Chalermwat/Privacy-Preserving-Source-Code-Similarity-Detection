from collections import deque

section = raw_input( )
area = 0
depthPosArr = deque( )
depthPosPoolArr = deque( )

for ipos, ground in enumerate( section ):
	if "\\" == ground:
		depthPosArr.append( ipos )
	elif "/" == ground:
		if len( depthPosArr ):
			jpos = depthPosArr.pop( )
			pool =  ipos - jpos
			area += pool

			while len( depthPosPoolArr ):
				preJPos, prePool = depthPosPoolArr.pop( )
				if jpos <= preJPos:
					pool += prePool
				else:
					depthPosPoolArr.append( ( preJPos, prePool ) )
					break
			depthPosPoolArr.append( ( jpos, pool ) )

print( area )
output = []
output.append( len( depthPosPoolArr ) )
for arr in depthPosPoolArr:
	output.append( arr[1] )
print( " ".join( map( str, output ) ) )