def remainder(x, y):

        # Returns: int: The remainder of x divided by y.
    
        quotient    =     x   //    y

        remainder     =     x   -   (quotient  * y)

        return remainder

# This is the comment

import math

def Check(integer):

        # This is the comment


        for i in range(2,int(math.sqrt(integer))+1):

                                # This is the comment

                                if remainder(    integer,i   )   ==    0:


                                                                return False
            

        return True

# This is the comment

import math

# This is the comment

print(Check(2))

# This is the comment

print(Check(4))


