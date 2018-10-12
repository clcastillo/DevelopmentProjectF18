# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:30:05 2018

@author: user
"""


''' Project 1 '''

i = 1

while i <= 100:
    if i % 3 == 0 and i % 5 != 0:
        print('Fizz')
        
    elif i % 5 == 0 and i % 3 != 0:
        print('Buzz')
        
    elif i % 3 == 0 and  i % 5 == 0:
        print('FizzBuzz')
        
    else:
        print (i)
    
    i = i + 1
        

def project_1(n, m):
    ''' Project 1 optional/Bonus 1 '''
    while n <= m:
        if n % 3 == 0 and n % 5 != 0:
         print('Fizz')
         
        elif n % 5 == 0 and n % 3 != 0:
         print('Buzz')
         
        elif n % 3 == 0 and  n % 5 == 0:
         print('FizzBuzz')
         
        else:
         print (n)
         
        n = n + 1
        

project_1(1, 100)


def pgone(n, m):
    ''' Project 1 optional/Bonus 2 '''
    if n <= m:
        if n % 3 == 0 and n % 5 != 0:
         print('Fizz')
         
        elif n % 5 == 0 and n % 3 != 0:
         print('Buzz')
         
        elif n % 3 == 0 and  n % 5 == 0:
         print('FizzBuzz')
         
        else:
         print (n)
         
        return pgone(n+1, m)
 
pgone(1, 100)
        