round=10
sum=0
welcome_text='# Welcome #'
end_text="### End ###"

print(welcome_text)
for i in range(round):
    if(i%2==0):
        sum+=i

print(sum)
print(end_text)