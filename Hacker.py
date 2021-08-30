        # Day 1
        # String Output

        # Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.
print (input_string)



    # Day 2
    # Datatypes


i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.

# Print the sum of the double variables on a new line.

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
#print(s)

j = int(input())
f = float(input())
z = str(input())

m = i + j
print (m)
g = d + f
print (g)

print (s+z)




    # Day 2
    # Operators

    #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    
    tip = float((meal_cost * tip_percent)/100)
    tax = float((meal_cost * tax_percent)/100)
    
    total_cost = meal_cost + tip + tax
    
    print (round(total_cost))


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)



    # Day 3
    # Intro to conditional statements

    #!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
if N%2==0:
    if N in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
    
else: print ("Weird")



    # Day 4
    # Class vs Instance

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge
        if self.initialAge >=0:
            self.age = initialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        
        if self.age >= 13:
            if self.age <18:
                print("You are a teenager.")
            else:
                print("You are old.")
        else:
            print("You are young.")
            
    def yearPasses(self):
        # Increment the age of the person in here
        self.age +=1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")


    # Day 5
    # Loops

    #!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
for i in range(1, 11):
    result = n*i
    print(n, 'x', i, '=', result)
else:
    pass



    # Day 6
    # Let's Review
    # Sort an input string with even index first, space separator, followed by odd indices
T = int(input())
for i in range(0, T):
    S = input()
    print(S[::2], S[1::2],)
    

#Day 7
# Arrays
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



# Day 8 
# Dictionaries and Maps
# MAPPING NAME AND NUMBER
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


    # DAY 9 >> 
    # RECURSION 3
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
    # Binary numbers
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
        # Inheritance
    
class Person():
    def __init__(self, firstName, lastName, idNumber):
	    self.firstName = firstName
	    self.lastName = lastName
	    self.idNumber = idNumber


    def printPerson(self):
	    print("Name:", self.lastName + ",", self.firstName)
	    print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
        
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        
        sum = 0
        for score in scores:
            sum += score
        average = sum/len(scores)
        
        if average < 40:
            return "T"
        elif average < 55:
            return "D"
        elif average < 70:
            return "P"
        elif average < 80:
            return "A"
        elif average < 90:
            return "E"
        else:
            return "O"
    
    
    
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())




    # Day 13: 
    # Abstract Classes

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        Book.price = price
        
    def display(self):
        print('Title: ' + self.title)
        print('Author: ' + self.author)
        print('Price: ' + str(self.price))
    

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()




        # Day 14
        #Scope  
        # ... Difference between max and min numbers in an array
class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
        self.maximumDifference = 0
    
    def computeDifference(self):
        maxVal = 0
        minVal = 101
        
        for element in self.__elements:
            if element < minVal:
                minVal = element
            if element > maxVal:
                maxVal = element
                
        self.maximumDifference = maxVal - minVal

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)



    # Day 15 
    # Linked List
    