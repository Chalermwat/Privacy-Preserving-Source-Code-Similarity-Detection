
strSlopeFlat = list(input())

stack_total = []
starck_areas = []

for i,x in enumerate(strSlopeFlat):
    if x == '\\':
        stack_total.append(i)
    elif x == '/' :
        onearea = 0
        if len(stack_total) > 0:
            pos = stack_total.pop()
            onearea = (i-pos)
            while len(starck_areas)>0 and starck_areas[-1][0] > pos:
                tmp_pop = starck_areas.pop()
                onearea += tmp_pop[1]
            starck_areas.append([pos,onearea])

print(sum([y for x,y in starck_areas]))
results = [x[1]  for x in starck_areas if x[1] != 0]
print(len(results),*results)