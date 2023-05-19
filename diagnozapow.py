#WSTĘP
#zadanie 1 oblicz sumę liczb 3-cyfrowych

# suma=0
# for i in range(100,1000):
#   suma+=i
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
#   exit(0)
# print("Liczba jest pierwsza")

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

#zadanie 4 