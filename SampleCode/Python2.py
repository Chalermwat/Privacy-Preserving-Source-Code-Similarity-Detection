def remainder(x, y):

    # Returns: int: The remainder of x divided by y.
    
    quotient    =     x   //    y

    remainder     =     x   -   (quotient  * y)

    return remainder

import math

def Check(integer):

        for i in range(2,int(math.sqrt(integer))+1):

                if remainder(    integer,i   )   ==    0:

                      return False
            
        return True

import math

print(Check(2))

print(Check(4))


