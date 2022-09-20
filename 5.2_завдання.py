import math
x=int(input("Введіть чотирицифрове число: "))
p=float(1000/x)
if p>1:
    print("Введено не чотирицифрове число")
else:
    x1=int(x//1000)
    x2=int((x//100)-(x1*10))
    x3=int(((x%100)-x1)/10)
    x4=int(x%10)
    if x1==x4 and x2==x3:
        print("Число є паліндромом")
    else:
        print("Число не є паліндромом")