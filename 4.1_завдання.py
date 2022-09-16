import math
x=int(input("Введіть значення x: "))
f=float((pow(math.e, x+math.sqrt(x)+math.cos(x)))*(2.9*x-(math.cos(x)/math.sin(x)))/(pow(3, 0.7*x+math.sqrt(x))))
print("Значення функції дорівнює", f)
input()