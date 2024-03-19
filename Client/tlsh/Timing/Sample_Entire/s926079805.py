high_water_marks = {}
areas = []

depth = 0
offset = 0
for i in input():
  if i == "/":
    depth -= 1
    if depth in high_water_marks:
      hwm = high_water_marks[depth]
      new_area = [hwm, offset - hwm]
      while len(areas) > 0 and areas[-1][0] > hwm:
        a = areas.pop()
        new_area[1] += a[1]
      areas.append(new_area)
  elif i == "_":
    pass
  else:
    high_water_marks[depth] = offset
    depth += 1

  offset += 1

total = 0
for a in areas: total += a[1]
print(total)
sizes = [a[1] for a in areas]
sizes.insert(0, len(areas))
print(" ".join(map(str, sizes)))