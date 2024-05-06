#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

# Exclude the first element which is the script name
args = sys.argv[1:]
if len(args) > 0:
    f = factorial(int(args[0]))
    print(f)
else:
    print("No arguments provided")
