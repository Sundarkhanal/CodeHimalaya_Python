n=int(input())
flag = False
for i in range(2,n,1):
    if n%i==0:
        flag = True
if flag:
    print("Not a prime number")
else:
    print("Prime number")
