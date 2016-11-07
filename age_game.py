#!/usr/bin/env python
# Years till 100
import sys

print ('Please enter alphabet only for the Name, NO NUMBER!!!')

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input('Enter Name:')

if len(sys.argv) > 2:
    age = int(sys.argv[2])
else:
    age = int(input('Enter Age:'))

sayHello = 'Hello ' + name + ','

if age == 100:
    sayAge = 'You are already 100 years old!'
elif age < 100:
    sayAge = 'You will be 100 in ' + str(100 - age) + ' years!'
else:
    sayAge = 'You turned 100 ' + str(age - 100) + ' years ago!'

print (sayHello, sayAge)