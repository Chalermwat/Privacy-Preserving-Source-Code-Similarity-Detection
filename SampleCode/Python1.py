import math

def mod(x, y):
    q = x // y
    r = x - (q * y)
    return r

def isPrime(number):
    for i in range(2,int(math.sqrt(number))+1):
        if mod(number,i)==0:
            return False
        
    return True

print(isPrime(2))
print(isPrime(4))
