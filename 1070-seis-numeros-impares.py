x = int(input())
y = x
for n in range(1,6):
    if x % 2 == 0:
        x = x + 1
        print(x)
    if x % 2 != 0:
        if x == y:
            print(y)    
        x = x + 2 
        print(x)
    
