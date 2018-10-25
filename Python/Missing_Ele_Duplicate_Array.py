import math
import time

# This Method use to find missing element in an array
# Which is duplicate to another array
# Method is basically do a XOR of each element in each array and find missing element in one array

def missingElementInDuplicateArray(arr,arr1,m,n):

    res = 0  
    for i in range (0,m):
        res = res ^ arr[i]

    res1 = 0
    for i in range (0,n):
        res1 = res1 ^ arr1[i]
    res2 = res ^ res1
    print(res2)

# result can be calculated in single res value and print res.
#    for i in range (0,m):
#        res = res ^ arr[i]

#    for i in range (0,n):
#        res = res ^ arr1[i]
#    
#    print(res) 

########## Driver Function ###########

arr = [1,2,3,6,8,4,10,100,18,20,25,50]
arr1 = [2,8,6,1,4,10,50,100,3,20,18]

# M = len(arr)
# N = len(arr1)

missingElementInDuplicateArray(arr,arr1,len(arr),len(arr1))

# Another way to call method by storing length of arr in variables and then send.
# missingElementInDuplicateArray(arr,arr1,M,N)

