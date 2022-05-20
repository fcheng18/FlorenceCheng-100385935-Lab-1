'''
My first program in Python
Florence Cheng
ID# 100385935
'''
from html.entities import name2codepoint
import math
#from math import pi
#print('Hello, World')
name = ''
name = input('Please input your name: ')

#print('Welcom {name} to Computing Analytics!')
print('Welcome '+name+ ' to Computing for Data Analytics')
print(f'Welcome {name.upper()}    to Computing for Data Analytics')
print(f'Welcome {name.title()}  to Computing for Data Analytics')
x = math.pi
#x = pi
print(f'The value of PI with nine decimal places is  {x:.9F}')
print(dir(math))


name_2 = input ('What is your name?')
print(f'Welcome {name_2}!')