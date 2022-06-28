#!/usr/bin/python3
"""Write a program that prints all numbers
from 0 to 98 in decimal and in hexadecimal"""
for number in range(0, 98):
    print("{} = {}".format(number, hex(number)))
