import sys
write=sys.stdout.write

number_of_numbers=[]
numbers=[]

number_of_numbers=input().split()
number_of_numbers[0]=int(number_of_numbers[0])
number_of_numbers[1]=int(number_of_numbers[1])



for i in range(0,number_of_numbers[0]):
    line_nunmbers=[]
    line_numbers=input().split()
    for j in range(0,len(line_numbers)):
        line_numbers[j]=int(line_numbers[j])
    numbers.append(line_numbers)

right_end_numbers=[]
under_end_numbers=[]

for i in range(0,len(numbers)):
    right_end_numbers.append(sum(numbers[i]))

for i in range(0,len(numbers[0])):
    under_end_number=0
    for j in range(0,len(numbers)):
        under_end_number+=numbers[j][i]
    under_end_numbers.append(under_end_number)

for i in range(0,len(numbers)):
    for j in range(0,len(numbers[0])):
        write(str(numbers[i][j]))
        write(' ')
    print(right_end_numbers[i])

for i in range(0,len(numbers[0])):
    write(str(under_end_numbers[i]))
    write(' ')

print(sum(under_end_numbers))