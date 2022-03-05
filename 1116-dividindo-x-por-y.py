n = int(input())
for x in range(0,n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    
    if b == 0:
        print("divisao impossivel")
    else: 
        print("{:.1f}".format(a/b))
