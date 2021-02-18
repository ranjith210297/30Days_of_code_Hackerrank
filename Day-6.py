t = int(input())
for t in range(t):
    #s = list(map(str,input().rstrip().split()))
    try:
        s=input()
    except(EOFError):
        break
    eve=""
    odd =""
    for i in range(len(s)):
        if i%2==0:
            eve += s[i]
        else:
            odd += s[i]
    print(eve+" "+odd)

#SOLUTION-2
# N = int(input())

# for i in range(0, N):

#     string = input()

#     for j in range(0, len(string)):
#         if j % 2 == 0:
#             print(string[j], end='')

#     print(" ", end='')

#     for j in range(0, len(string)):
#         if j % 2 != 0:
#             print(string[j], end='')

#     print("")