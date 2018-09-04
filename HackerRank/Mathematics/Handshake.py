#!/bin/python3

import os
import sys
import math

#
# Complete the handshake function below.
#
def handshake(n):
    #
    # Write your code here.
    #
    return int(fact(n)/(fact(2)*fact(n-2)));

#
# creating own recursive fact method will create stackoverflow for large number.
# can optimize this function for larger input also using memoization.
def fact(value):
    if (value == 0):
        return 1
    else:
       return int(value*fact(value-1))

    #
    # returning the value of factorial using puthon inbuilt method
    # All Hackerrank test cases wil pass.  
    
    # return math.factorial(value)    
    

t = int(input())

for t_itr in range(t):
    n = int(input())

    result = handshake(n)
    print(result)

