import math

# This method is Iterative way to find a element is Sorted array
# Algo : Binary Search
# prerequisite Array must be sorted.

def bin_search(arr,l,r,x):
    
   while(l <= r):

    mid = math.floor(l + (r - l)/2);
    if (arr[mid] == x):
        return mid
    elif (arr[mid] > x):
        r = mid-1
    else:
        l = mid+1

   return -1

arr = [2, 3, 4, 10, 40, 50, 53, 56, 69, 70]
x = 50
 
########### Function call ############

#
# @param arr : array with integers elements
# @param x : Element to find in array

result = bin_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print ("Element is present at index %d" %result)
else:
    print ("Element is not present in array")