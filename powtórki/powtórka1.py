#pierwiastek

# from math import sqrt:
# print(sqrt(576))
# print(576**(1/2))
# print(8**(1/3))

#if
#operatory porównań == >= <= >< !=(-różne)

#pętla z liczbami 3 cyfrowymi podzielnymi przez 13 i 4

# for i in range(100,1000):
#   if i%13==0 and i%4!=0:
#     print(i, end=" ")

#łączenie warunków-są dwie opcje:

#pierwszy:
#a,b,c=3,5,7
# if a<b<c:
#   print("")

#drugi:
# a,b,c=3,5,7
# if a<b and b<c:
#   print("")

#pętle
# dzielniki
# n=24
# for i in range(1,25):
#   if n%i==0:
#     print(i)

#suma
# suma=0
# for i in range(1,25):
#   if n%i==0:
#     print(i)
#     suma=suma+i
#     ilość=ilość+1
#     print("suma","suma")
#     print("ilość","ilość")

#oblicz sumę k poczatkowych liczb trzycyfrowych
#100+101+102+103...
#we:3
#wy:406(100+101+102+103)

# k=3
# suma=0
# ilość=0

# for i in range(100,1000):
#   suma=suma+i
#   ilość=ilość+1

#   if ilość==k:
#     break
#     print(suma)

                    #LUB
# k=3
# suma=0
# for i in range(100,1000+k):
#   suma=suma+i
#   print(suma)

#oblicz sumę n początkowych wyrazów ciągu fibonacciego

# n=int(input())
# a,b=0,1
# for i in range(n):
#   a,b=b,a+b
#   suma=suma+b
#   print(suma)

# jak wyodbyć 
# ostatnie 2 cyfry z liczby, 
# albo cyfrę setek?
# n = 12345
# print((n%1000)//100)
  