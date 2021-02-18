#!/bin/python3

import math
import os
import random
import re
import sys





if __name__ == '__main__':
    n = int(input())
def decimalToBinary(n): 
    return bin(n).replace("0b", "")

bin_string = str(decimalToBinary(n))
consec_ones = bin_string.split("0")
ones_count = [len(i) for i in consec_ones]
print(max(ones_count))

'''
Method-2:

result = 0
maximum = 0

while num > 0:
    if num % 2 == 1:
        result += 1
        if result > maximum:
            maximum = result

    else:
        result = 0
    num //= 2
print(maximum)

'''