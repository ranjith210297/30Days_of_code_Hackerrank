import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    summ=0
    maxx = -99
    for row in range(len(arr)):
        for col in range(len(arr)):
            if row+2<len(arr) and col+2<len(arr):
                summ = arr[row][col]+arr[row][col+1]+arr[row][col+2]+arr[row+1][col+1]+arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2]
                if summ>maxx:
                    maxx = summ
                
print(maxx)