# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def isprime(n):
    if n == 1:      
        return "Not prime"
    for k in range(2,int(math.sqrt(n))+1):
        if n%k == 0:
            return "Not prime"
    return "Prime"
    
t = int(input())
for i in range(t):
    n = int(input())
    print(isprime(n))