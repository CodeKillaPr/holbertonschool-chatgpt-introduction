#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

args = sys.argv[1:]
for arg in args:
    print(arg)