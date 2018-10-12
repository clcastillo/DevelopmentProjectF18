# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 23:11:57 2018

@author: george
"""

##
## Write a program that prints the numbers from 1 to 100. But for multiples of 3 print “Fizz”, instead of multiples of 5 print “Buzz”, and for multiples of both 3 and 5 print “FizzBuzz”.
## Optional/Bonus
## Make a function that does this from n to m instead of 1 to 100
## Do this without using a looping statement
##

# n and m can be any integer
n = 0
m = 100

def print_with_loop(n, m):
    for num in range(n, m):
        print(num)
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")

def print_recursion(n, m):
    print(n)
    if(n != m):
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        print_recursion(n + 1, m)

print('Loop way')
print_with_loop(n, m)

print('\nRecursion Way')
print_recursion(n, m)