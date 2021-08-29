# Day 6
# Sort an input string with even index first, space separator, followed by odd indices
T = int(input())
for i in range(0, T):
    S = input()
    print(S[::2], S[1::2],)
    

#Day 7
# Print the reverse of Aray Items, separated by space
#not using .reverse(). .  .
    import math
import os
import random
import re
import sys
                            # Use mapper to map input


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
A = map(str, arr[::-1])
print(" ".join(A))



# Day 8 MAPPING NAME AND NUMBER
#Key-Value pair mappings using a Map or Dictionary data structure
#Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for.

phonelist = {}
entries = int(input())

for n in range(entries):
    name, num = input().strip().split(' ')
    name, num = [str(name), int(num)]
    phonelist[name] = num

while True:
    try:  
        search = str(input())

        if search in phonelist:
            output = ''.join('%s=%r' % (search, phonelist[search]))
            print(output)
        else:
            print("Not found")
    except EOFError:
        break


    # DAY 9 >> RECURSION
    import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    if n == 1:
        return 1
    elif n < 1: return ("NA")
    else:
        return n * factorial(n-1)
    print(factorial)
     
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# DAY 10 
# #Incrementing count when the binary result of converting base ten number contains consecutive 1s
#!/bin/python3
#


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
current_conseq_1s = 0
max_conseq_1s = 0
while n > 0:
    remainder = n % 2
    if remainder == 1:
        current_conseq_1s +=1
        if current_conseq_1s > max_conseq_1s:
            max_conseq_1s = current_conseq_1s
            
    else:
        current_conseq_1s = 0
    n = n // 2
    
print(max_conseq_1s)



# Day 11
        #2D Arrays (Matrix)
# sumaion of an hour glass
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
 
    def get_sum(matrix, row, col):
        sum = 0
        sum += matrix[row-1][col-1]
        sum += matrix[row-1][col]
        sum += matrix[row-1][col+1]
        sum += matrix[row][col]
        sum += matrix[row+1][col-1]
        sum += matrix[row+1][col]
        sum += matrix[row+1][col+1]
        return sum
    
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
        max_hg_sum = -63
for i in range(1,5):
    for j in range(1,5):
        current_hg_sum = get_sum(arr, i, j)
        if current_hg_sum > max_hg_sum:
            max_hg_sum = current_hg_sum
            
print(max_hg_sum)



        # Day 12
        