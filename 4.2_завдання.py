import math
x=int(input("Введіть значення x: "))
y=int(input("Введіть значення y: "))
z=int(input("Введіть значення z: "))
a=int(input("Введіть значення a: "))
L=(x*math.cos(y)+z)-((math.tan(y)+math.pow(math.e, a))/math.pow(2, z+2.4))
print("Значення виразу дорівнює", L)
input()