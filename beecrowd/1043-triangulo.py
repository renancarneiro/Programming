a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)

if (b - c) < a and a < (b + c):
    if (a - c) < b and b < (a + c):
        if (a - b) < c and  c < (a + b):
            perimetro = a + b + c
            print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((a + b) * c) / 2
    print("Area = {:.1f}".format(area))
