import math
import time

# Method to find prime numbers
# Optimized implementation 
# Don't worry still not faster than, same implementation of C lang.

def prime(n):
    if(n == 1 and n == 2):
        return True
    if(n > 2 and n % 2 == 0):
        return False
        
    divisor = math.floor(math.sqrt(n))
    for d in range (3, 1 + divisor, 2):
        if(n%d == 0):
            return False
        return True

########## Driver Function ##########

t0 =  time.time()
for n in range(0, 101):
    print(n, prime(n))
t1 = time.time()
print (t1-t0)

   

