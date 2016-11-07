#!/usr/bin/env python
#guru guess the number game
#by OLANO TEAH BLOH
import random

answer = random.randint(1, 10)
num = 0

while num != answer:
    num = float(input('Guess what number am I thinking about? '))

    if num != answer:
        print ('Wrong!')

print ('Correct!')