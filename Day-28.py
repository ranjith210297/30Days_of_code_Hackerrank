#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    unsortednames = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        if re.search("@gmail",emailID):
            unsortednames.append(firstName)
    for firstName in sorted(unsortednames):
        print(firstName)
    