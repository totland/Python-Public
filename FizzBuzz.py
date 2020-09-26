# Test Program 20200925
import sys
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + ' FizzBuzz')
    elif i % 3 == 0:
        print(str(i) + ' Fizz')
    elif i % 5 == 0:
        print(str(i) + ' Buzz')
    else:
        print (str(i))

