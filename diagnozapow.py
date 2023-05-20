#WSTĘP
#zadanie 1 oblicz sumę liczb 3-cyfrowych

# suma = 0 

# for i in range(100,1000):
#   suma += i 
# print(suma)

#zadanie 2 oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6

# suma=0
# ilosc=0

# for i in range(10,100):
#   if i%6==0:
#     suma+=i
#   if i%6==0:
#     ilosc+=1
# print(suma)
# print(ilosc)

#zadanie 3 znajdź najwiekszą liczbę wsród wylosowanych przez program liczb 4-cyfrowych

# from random import randint
# L=[randint(1000,10000) for i in range(5)]
# print(L)
# print(max(L))

#zadanie 4 podaj sumę cyfr w dowolnej liczbie

# a=int(input())
# suma=0

# while a>0:
#   suma+=a%10
#   a//=10
# print(suma)

#zadanie 5 znajdź najmniejszą liczbę we wpisanej przez usera liczbie 3-cyfrowej

# b=int(input())
# L=list(str(b))
# print(min(L))

#ALGORYTMY
#zadanie 1 sprawdź czy wpisana przez usera liczba jest pierwsza

# c=int(input())

# for i in range(2,c):
#   if c%i==0:
#     print("Liczba nie jest pierwsza")
# else:
#   print("Liczba jest pierwsza")

#zadanie 2 sprawdź czy wpisana przez usera liczba jest złożona

# n=int(input())

# for i in range(2,n):
#   if n%i==0:
#     print("Liczba jest złożona")
#   else:
#     print("Liczna nie jest złożona")

#zadanie 3 sprawdź czy wpisana prze usera liczba jest względnie pierwsza z 24

# def NWD(a,b):
#   while b!=0:
#     a,b=b,a%b
#   return a
# l=int(input("Podaj liczbę:"))
# NWD_l_24=NWD(l,24)
# if NWD_l_24==1:
#   print(l,"Liczba jest względnie pierwsza z 24")
# else:
#   print(l, "Liczba nie jest względnie pierwsza z 24")

#zadanie 4 Zakoduj szyfrem CEZARA i kluczem k słowo s.
# s=input()
# k=input()

# def encrypt(s, k):
#   encrypted = ""
# for letter in s:
#   if ord(letter) + k > ord('z'):
#     encrypted += chr(ord(letter) + k - 26)
#   else:
#     encrypted += chr(ord(letter) + k)
# encrypt(s, k)

#zadanie 5  Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę mieszaną.

# a=int(input("Podaj licznik v1:"))
# b=int(input("Podaj mianownik v1:"))
# c=int(input("Podaj licznik v2:"))
# d=int(input("Podaj mianownik v2:"))

# x,y=b,d
# iloczyn=x*y
# while x!=y:
#   if x>y:x=x-y
#   if y>x:y=y-x
# NWW=iloczyn//x
# e=(NWW//b)*a
# f=(NWW//d)*c
# g=e+f
# print(f"{a}/{b} + {c}/{d} = {e}/{NWW} + {f}/{NWW} = {g}/{NWW}")

#zadanie 6 Znajdź NWW dwóch wpisanych przez usera liczb

#odejmowanie NWW
# a=int(input("Podaj liczbę v1:"))
# b=int(input("Podaj liczbę v2:"))

# iloczyn = a*b
# while a != b:
#   if a>b:a = a-b
#   if b>a:b = b-a
# print(iloczyn//a)

#modulo

# a=int(input("Podaj liczbe v1:"))
# b=int(input("Podaj liczbe v2:"))

# iloczyn = a*b
# while b>0:
#   a,b = b,a%b
# print(iloczyn//a)

#NAPISY
#zadanie 1 Znajdź ilość liter C we wpisanym napisie
# a=input("Dawaj napis:")
# ilosc=0

# for i in (a):
#   if i=="c":
#     ilosc+=1
# print(ilosc)

#zadanie 2  Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp

# n=input("Podaj napis:")
# nr=True
# for i in range(len(n)-1):
#   if n[i] < n[i+1]:
#     nr=False
#     break
#   if nr:
#     print("Literki są w porządku nierosnacym")
#   else:
#     print("Literki nie są w porządku nierosnącym")

#zadanie 3  Podaj najdłuższy z 3 wpisanych przez usera wyrazów.

# a = input("Wyraz v1:")
# b = input("Wyraz v2:")
# c = input("Wyraz v3:")
# nw=a
# if len(b) > len(nw):
#   nw = b
# if len(c) > len(nw):
#   nw = c
# print("Najdłuższy wyraz to:", nw)