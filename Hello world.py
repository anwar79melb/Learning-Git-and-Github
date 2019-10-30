# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("hello world")

print ("I like 6.00.1x!")

var = 'Panda'
if var == "panda":
   print("Cute!")
elif var == "Panda":
   print("Regal!")
else:
   print("Ugly...")
   
today = "started"
if today == "started":
    print("hello world")
else:
    print("no baby this is another day")
    
    
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

CTRL+C

num = 10
while num > 3:
    num -= 1
    print(num)

num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 

num = 10
for num in range (5):
    print (num)
print (num)

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')
        
for letter in 'hola':
    print(letter)

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

x = int (input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print (str(x) + ' is not a perfect cube')
else:
    print ('cube root of' + str(x) + ' is ' + str(x))
    
cube = 27
for guess in range (cube + 1):
    if guess**3 == cube:
        print ('Cube root of ', cube, ' is ', guess)


iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 


s = 'azcbobobegghakl'
currentString = s[0]
longestString = ""

wordLength = len(s)

num = 0

while num < (wordLength - 1):

    while s[num] <= s[num+1]:
        currentString = currentString + s[num+1]
        if (num+1) < (wordLength - 1):
            num += 1
        else:
            break

    if len(currentString) > len(longestString):
        longestString = currentString

    num += 1
    currentString = s[num]

print ("Longest substring in alphabetical order is:" , longestString)

letters = "ahdireurksjfhurMITJHOERHTSHOSRJNLSFHsjosfjoutorhjf"
word = input ("I will cheer for you! Enter a word: ")
times = int (input("Enthusiasm level (1:10): "))
i = 0
while i < len(word):
    char = word[i]
    if char in letters:
        print ("Give me an " + char + "! " + char)
    else:
        print ("Give me a " + char + "! " + char)
    i += 1
print ("What does that spell?")
for i in range (times):
    print (word, "!!!")

# other way
an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for char in word:
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a  " + char + "! " + char)
print("What does that spell?")
for i in range(times):
    print(word, "!!!")

# week 2, exercise 2
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    
    
# other ones
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

# other ones

# bisection search, example practice, week 3, practice 3
print("Please think of a number between 0 and 100!")
low = 0
high = 100
mid = (high+low)//2
while True:
    print("Is this your number ",mid,'?')
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if(answer == 'h'):
        high = mid
        mid = (high+low)//2        
    elif(answer == 'l'):
        low = mid
        mid = (high+low)//2
    elif(answer == 'c'):
        print('Game over. Your secret number was:',mid)
        break
    elif(answer != 'h' or answer != 'l' or answer != 'c'):
        print('Sorry, I did not understand your input.')
        
# my own code
print("Please think of a number between 0 and 100!")
low = 0
high = 100
mid = (high+low)//2
while True:
    print("Is this your number ",mid,'?')
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if(answer == 'h'):
        high = mid
        mid = (high+low)//2        
    elif(answer == 'l'):
        low = mid
        mid = (high+low)//2
    elif(answer == 'c'):
        print('Game over. Your secret number was:',mid)
        break
    elif(answer != 'h' or answer != 'l' or answer != 'c'):
        print('Sorry, I did not understand your input.')

# converting decimals to binary
num = 11 # this is the target number
if num < 0:
    inNeg = True
    num = abs (num)
else:
    isNeg = False
    result = ' '
if num == 0:
    result = '0'
while num > 0:
    result = str (num % 2) + result
    num = num // 2
if isNeg:
    result = '-' + result
    
# converitng decimal numbers between 0 and 1 to binary 
x = float (input("Enter a decimal number between 0 and 1: "))
p = 0
while ((2**p)*x)%1 != 0:
    print ("Reminder = " + str ((2**p)*x - int ((2**p)*x)))
    p +=1 
num = int (x*(2**p))
result = " "
if num == 0:
    result = '0'
while num > 0:
    result = str (num%2) + result
    num = num // 2
for i in range (p - len(result)):
    result = '0' + result
result = result [0:-p] + '.' + result [-p:]
print ("The binary representation of the decimal "+ "is " + str(result))
    
# Newton-Raphson methods for finding roots

epsilon = 0.01
y = 16.0
guess = y / 2.0
numGuesses = 0
while abs (guess**2 -y) >= epsilon:
    numGuesses +=1
    guess = guess - (((guess**2) - y)/(2*guess))
print ('numGuesses = ' + str (numGuesses))
print ('Square root of ' + str (y) + 'is about ' + str(guess))

# how to write or call a function

def is_even (i): # here def is 'keyword', is_even is function 'name', and i is parameter or arguments
    """
    Input: i, a positive int # this chunk of code is called 'specification or docstring'
    Returns True if i is even, otherwise False
    """
    print ("hi") # this line and next line is known as body of the function
    return i%2 == 0 # here return is 'keyword' and i%2 == 0 is the expression of the function
is_even (8) # this is called 'invoke' or 'calling' the function

# variable scoping
def f(x):
    x = x + 1
    print ("in f(x) : x = ", x)
    return x
x = 3
z = f(x)

# scope examples
# example 1
def f(y):
    x = 1
    x += 1
    print (x)
x = 5
f(x)
print (x)

# example 2
def g(y):
    print (x)
    print (x+1)
x = 5
g (x)
print (x)

# example 3
def h(y):
    x = x + 1
x = 5
h (x)
print (x) # this code will not work as x is not defined earlier

# trying a function inside another function
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print ('in g(x): x = ', x)
    h()
    return x
x = 3
z = g(x)

# new exercise
x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
g(x)

# keyword arguments
def printNames (firstName, lastName, reverse):
    if reverse:
        print (lastName + ', ' + firstName)
    else:
        print (firstName, lastName)
        
# binding default value
def printNames (firstName, lastName, reverse = False):
    if reverse:
        print (lastName + ', ' + firstName)
    else:
        print (firstName, lastName)
        
        
# Write an iterative function iterPower(base, exp) that calculates the 
# exponential by simply using successive multiplication. For example, 
# iterPower(base, exp) should compute by multiplying base times itself exp 
# times.

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    prod = 1
    while exp > 0:
       prod *= base
       exp -= 1
    return prod
    
# making the same function using recursive power
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return (base*recurPower(base, exp-1))

# The greatest common divisor of two positive integers is the largest 
# integer that divides each of them without remainder.
# Write an iterative function, gcdIter(a, b), that implements this idea.
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    c = min (a, b)
    while a%c != 0 or b%c != 0:
        c -= 1
    return c

# recursive method
# A clever mathematical trick (due to Euclid) makes it easy to find greatest 
# common divisors. Suppose that a and b are two positive integers:
# If b = 0, then the answer is a
# Otherwise, gcd(a, b) is the same as gcd(b, a % b)

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)

# using methods of recursive solution in strings
# checking palindrome

def isPalindrome (s):

    def toChars (s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
        
    def isPal (s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal (s[1:-1])
    return isPal (toChars(s))
# this is called divide and conquer of algorithm

# the easier one
given = 'ablewasiereisawelba'

print(given == given[::-1])

# exercise using bisection search in week 3
# finding an alphabet in a string using recursive method

# def isIn(char, aStr):
#    if _____ and ______:  # base case
#       return False
#   test = _____
#   if _____:  # check letter in the middle
#       return True
#   if _____:  # 'char' is in lower half
#       return isIn(_____)
#   else:      # 'char' is in upper half
#       return isIn(_____)

# the complete solution
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 1 and char == aStr:
        return True
    elif len(aStr) == 1 and char != aStr:
        return False
    elif len(aStr) == 0:
        return False
    else:
        if char == aStr [len(aStr)//2]:
            return True
        elif char < aStr [len (aStr)//2]:
            return isIn (char, aStr [0: (len(aStr)//2)])
        else:
            return isIn (char, aStr [len(aStr)//2:len(aStr)])
            
# A regular polygon has n number of sides. Each side has length s.

#   The area of a regular polygon is: 

#   The perimeter of a polygon is: length of the boundary of the polygon

# Write a function called polysum that takes 2 arguments, n and s. 
# This function should sum the area and square of the perimeter of the regular 
# polygon. The function returns the sum, rounded to 4 decimal places.

from math import tan, pi # imports library 'tan' and 'pi' from 'math' module
def polysum (n, s):
    area = round ((0.25*n*s**2)/tan(pi/n), 4) # uses of round() function is: round (element, no of decimal places)
    perimeter = round (((n*s)**2),4)
    result = area + perimeter
    return result
    
# other method
import math
def polysum2 (n, s):
    area = round ((0.25*n*s**2)/math.tan(math.pi/n), 4)
    perimeter = round (((n*s)**2),4)
    result = area + perimeter
    return result
    
# Pset 2
# all example in pset 2 is not done yet 
total_paid = 0.00 
i=1 
while (i <= 12):
    monthly_interest_rate = (annualInterestRate) / 12.0 
    minimum_monthly_payment = (monthlyPaymentRate) * (balance) 
    monthly_unpaid_balance = (balance) - (minimum_monthly_payment) 
    balance = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance) 
    print('Month: '+str(i)) 
    print('Minimum monthly payment: '+str(round(minimum_monthly_payment,2))) 
    print('Remaining balance: '+str(round(balance,2))) 
    total_paid += minimum_monthly_payment 
    i+=1 
    print('Total paid: '+str(round(total_paid,2))) 
    print('Remaining balance: '+str(round(balance,2)))

# week 3
# manipulating Tuples
def get_data (aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[1],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min (nums)
    max_nums = max (nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)
(small, large, words) = get_data (((1, 'mins'), (3, 'yours'), (5, 'ours'), (7, 'mine')))
