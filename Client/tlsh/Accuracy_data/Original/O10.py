from math import sqrt;

count = int(input());
data = [];
for n in range(count):
    data.append(int(input()));

def prime_number(data):
    max_divisor = get_max_divisor(data);
    divisor_primes = get_prime(max_divisor);
    count = 0;
    for n in data:
        ok = 1;
        for p in divisor_primes:
            if n < p:
                ok = 0;
                break;
            elif n == p:
                break;
            elif n % p == 0:
                ok = 0;
                break;
        count += ok;
    return count;

def get_max_divisor(data):
    maxN = data[0];
    for n in data[1:]:
        if n > maxN:
            maxN = n;
    return int(sqrt(maxN)) + 1;

def get_prime(max_divisor):
    primes = [];
    for n in range(2, max_divisor + 1):
        is_prime = True;
        for p in primes:
            if n % p == 0:
                is_prime = False;
        if is_prime:
            primes.append(n);
    return primes;

print(prime_number(data));
