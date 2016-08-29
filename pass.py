#!/usr/bin/env python
# Guru King secure program that uses security.
import sys

validPassword = 'secret' #this is our password.

inputPassword = input('Please Enter Password: ')

if inputPassword == validPassword:
    print ('You have access!')
else:
    print ('Access denied!')
    print ('Try Again or Contact your Software Team')
    sys.exit(0)

print ('Welcome!')