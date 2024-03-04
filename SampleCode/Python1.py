import math

def isPrime(number):
    for i in range(2,int(math.sqrt(number))+1):
        if mod(number,i)==0:
            return False
        
    return True

def mod(x, y):
    """
    Returns:
    int: The remainder of x divided by y.
    """

    q = x // y
    r = x - (q * y)
    return r

print(isPrime(2))
print(isPrime(4))
