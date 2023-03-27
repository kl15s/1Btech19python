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

c=input()
suma=0
for i in c:
  suma+=ord(i)
print(suma)
