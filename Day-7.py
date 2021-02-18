
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    l = arr[::-1]
    s=""
    for i in l:
        s += str(i)+" "
    print(s)