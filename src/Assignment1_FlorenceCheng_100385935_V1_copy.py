#Assignment 2
#Florence Cheng 100385935

from math import pi
import datetime
x = 1234567890
y = pi
z = .723
today = datetime . datetime .now ()

s = 'String Formatting'
ruler = '-'
question_mark = '?'

#Question 1

print(f'\t\t\t{ruler*(len(s)+4)}')
print(f'\t\t\t| {s} |')
print(f'\t\t\t{ruler*(len(s)+4)}')
print(f'| 25 width left-aligned string output s = {s}')
print(f'| 25 width left-aligned string output s padded with ? s = {s}{question_mark*8}.')
print(f'| 25 width right-aligned string output s =\t   {s}.')
print(f'| 25 width right-aligned string output s padded with ? s = {question_mark*8}{s}.\n')

#Question 2

n = 'Number Formatting'
print(f'\t\t{ruler*(len(n)+4)}')
print(f'\t\t| {n} |')
print(f'\t\t{ruler*(len(n)+4)}')
print(f'| Integer x with thousand separator x = {x:,}')
print(f'| Integer x in binary = {x:b}')
print(f'| Floating-point with 10-decimal y = {y:.10f}')
print(f'| Floating-point in scientific format y = {y:.5e}')
print(f'| Floating-point as percentage z = {z:.2%}\n')

#Question 3

dt = 'Date & Time Formatting'
print(f'\t\t{ruler*(len(dt)+4)}')
print(f'\t\t| {dt} |')
print(f'\t\t{ruler*(len(dt)+4)}')
print(f'| Date in the format YY-MM-DD {today:%y-%m-%d}')
print(f'| Date in the format YYYY-MM-DD {today:%Y-%m-%d}')
print(f'| Date in with the day & month name {today:%A %d, %B %Y}')
print(f'| Time in the format HH-MM-SS {today:%H:%M:%S}')
print(f'| Date in the format YYYY-MM-DD HH-MM-SS {today:%Y-%m-%d %H:%M:%S}')