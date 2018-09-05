#
# Complete the maximumDraws function below.
#

def maximumDraws(n):
    #
    # Write your code here.
    #
        if(n==0):
            return 0
        else:
            return n+1
   
#
# This Function code is part of HackerRank and to be used in HackerRank environemnt.
#

''' if __name__ == '__main__':
      fptr = open(os.environ['OUTPUT_PATH'], 'w')

      t = int(input())

      for t_itr in range(t):
          n = int(input())

          result = maximumDraws(n)

          fptr.write(str(result) + '\n')

      fptr.close()
'''

############# Driver Function ############

t = int(input("Enter Number of testcases"))
type(t)

while(t!=0):

    n = int(input("Enter number of pair of socks"))
    type(n)

    print(maximumDraws(n))
    t = t-1    
