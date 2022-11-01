#zad1
# for i in range(1,31):
#   print(i, end=" ")

#zad2
# for i in range(1,10,2):
#   print(i**2, end=" ")

#zad3
# for i in range(1516,10000,379):
#   print(i, end=" ")

#zad4
# for i in range(100,1000,5):
#   print(i, end=" ")

# for k in range(102,1000,6):
#   print(k, end=" ")

# for m in range(110,1000,11):
#   print(m, end=" ")

#zad5
# n=int(input("Ile liczb chcesz podać?"))
# suma=0

# for i in range(n):
#   y=int(input())
#   suma=suma+y
#   print(suma)

#zad6
# k=int(input())
# a=0

# for i in range(0,2*k,2):
#   a=a+i
#   print("Suma początkowych liczb parzystychv wynosi:")
#   print(a)

#zad7
# m=int(input())
# a=0

# for i in range(11,(m*2)+11,2):
#   a=a+i
#   print("Suma liczb początkowych nieparzystych wynosi:")
#   print(a)

#zad8
# W0=int(input("Podaj wartość początkową inwestycji:")) 
# L=int(input("Podaj lata inwestycji:"))
# Wk=0
# suma=Wk

# for i in range(0,L * 12):
#   Wk=suma*0.06*(1/12)
#   suma= suma+Wk
#   print("Końcowa wartość inwestycji wynosi:")
#   print(suma)

#zad9
# n=int(input("Podaj ilość liczb:"))
# a=21
# suma=0

# for i in range(0,n+1):
#   for t in range(0,i,a):
#     print(a)
#     suma=suma+a
#     a=a+100
#     print("Suma liczb wynosi:")
#     print(suma)

#zad10
# from cmath import sqrt

# for i in range(1,1000):
#   if i%10==sqrt(i):
#     print(i)
#   elif i%100==sqrt(i):
#     print(i)