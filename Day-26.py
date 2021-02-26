# Enter your code here. Read input from STDIN. Print output to STDOUT
ret = input()
n1 = list(map(int,ret.split()))

due = input()
n2 = list(map(int,due.split()))

d1,d2 = n1[0],n2[0]
m1,m2 = n1[1],n2[1]
y1,y2 = n1[2],n2[2]

if y1==y2 and m1==m2 and d1>d2:
    print(15*(d1-d2))
elif y1==y2 and m1>m2 and (d1>d2 or d1<d2):
    print(500*(m1-m2))
elif y1 > y2:
    print(10000)
else:
    print(0)