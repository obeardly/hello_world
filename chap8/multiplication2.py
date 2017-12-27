#!/usr/bin/env python

#Try It Out Excercise Chapter 8 Ex 2

table = int(raw_input('What multiplication table would you like? '))
level = int(raw_input('To what number do you want your multiplication table? '))
for i in range(1, (level + 1)):
  print i * table
