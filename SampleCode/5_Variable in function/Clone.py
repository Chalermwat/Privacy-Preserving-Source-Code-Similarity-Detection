import math

def mod(a, b):
    quotient = a // b
    remainder = a - (quotient * b)
    return remainder

def isPrime(n):
    for index in range(2,int(math.sqrt(n))+1):
        if mod(n,index)==0:
            return False
        
    return True

print(isPrime(2))
print(isPrime(4))
