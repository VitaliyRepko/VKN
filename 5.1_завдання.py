import math
x=float(input("Введіть значення x: "))
y=0.0
if x>9:
    y=3.11+math.log10(2*x)+math.log(x+8, 3)
elif x<1:
    y=6.23*(x-0.7+math.pow(math.e, 3*x))
else:
    y=(1/x)+((2+x)/(math.pow(math.e, x)+math.pow(x, 2)))
print("Значення функції дорівнює:", y)