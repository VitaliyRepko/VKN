A=int(input("Введіть чотирицифрове число: "))
a1=int(A/1000)
a2=int((A-(a1*1000))/100)
a3=int((A-((a1*1000)+(a2*100)))/10)
a4=int((A-((a1*1000)+(a2*100)+(a3*10))))
B=float(pow(a1*a2*a3*a4, 1/4))
print("Середнє арифметчине цифр:", B)
input()
