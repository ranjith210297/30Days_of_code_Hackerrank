import sys
num = int(input())
phone_book={}
for i in range(num):
    inp = str(input()).split(" ")
    name = inp[0]
    number = int(inp[1])
    phone_book[name] = number
    
try:
    while True:
        name = input()
        if name in phone_book:
            print(name+"="+str(phone_book[name]))
        else:
            print("Not found")
except EOFError:
    pass
           