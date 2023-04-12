#ZAGADNENIA POTRZEBNE NA SPRAWDZIAN3:
#napisy-> len,for, foreach,ord,chr
#indeksy, zakresy
# konwersje list<->
#list-sort reverse
#split, join
#algorytmy -> anagram, palindom, Boyer-Moore 

#PRZYKŁADOWE ZADANIA

#zadanie 1 czytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę

# x= input()
# print(x[0],x[-1])

#zadanie 2  wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej

# a=input()
# for i in range(1, len(a)-1):
#   print(a[i], end="")
# print()
# #druga wersja
# print(a[1:len(a)-1])

#zadanie 3 wypisz trzy ostatnie literki z wpisanego napisu w kolejności od końca

# b=input()
# for i in range(len(b)-1, len(b)-5,-1):
#   print(b[i], end="")
# print()

#opcja druga

# L=list(b)
# L.reverse()
# b="".join(L)
# for i in range(4):
#   print(L[i], end="")
# print()

#opcja trzecia

# print(b[len(b)-1:len(b)-5:-1])

#zadanie 4
#waga napisu to sum a kodów ascii jego liter zważ wpisany napis

# c=input()
# suma=0
# for i in c:
#   suma+=ord(i)
# print(suma)

#zadanie 5 policz ile jest literek a

#opcja 1
# e=input()
# ilosc=0

# for x in e:
#   if x== "A":
#     ilosc += 1
# print(ilosc)

#opcja 2
# print(e.count("A"))

#zadanie 6 podaj dominującą literkę we wpisanym napisie
#UWAGA NIECH TO BĘDZIE JEDNA LIERTKA

# g=input()
# maksik=0

# for x in g:
#   if g.count>maksik:
#     maksik =g.count(x)
#     literka = x
# print(literka, maksik)

#zadanie 7
#sprawdź czy w napisie występują trzy podciągi "LA"
# h=input()
# print(h.count("LAM"))

# h=input()
# ilosc=0
# for i in range(len(h)):
#   if h[i:i+2] == "LA":
#     ilosc+=1
#   if ilosc == 3:
#     print("TAK")
#   else:
#     print("NIE")


#zadania ze sprawdzianu w ramach ćwiczeń

#zadanie 1 Rozważmy wszystkie słowa, które posiadają dokładnie dwa t5akie same znaki oraz pozostałe znaki inne niż wspomniana para. Np. baza matka barszcz. Wypisz wsystkie znaki ze słowa, które znajdują się między parą takich samych znaków

# s=input()

# for i in range(len(s)):
#   if s.count(s[i])>1:
#     dubel=s[i]
# print(dubel)
# print(s.index(dubel, s.index(dubel)+1))
  
#zadanie2 Przekształć podane słowo do postaci paro-tylnej. Dzielimy słowona pary znaków od końca. Każdą parę wypisujemy w kolejności odwrotnej i w ten sposób tworzymy nowe słowo.

# s=input()
# L=list(s)
# L.reverse()
# s= "".join(L)
# print(s)

#zadanie 3 Sprawdź czy podane przez usera słowo jest niemalejące alfabetycznie, czyli każda kolejna literka w nim jest alfabetycznie nie mniejsza niż poprzednia

# s=input()
# for i in range(len(s)-1):
#   if s[i+1] < s[i]:
#     print("NIE JEST GIT")
#     exit(0)
# print()
