#TEORIA DO LEKCJI
#A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,U,P,R,S,T,U,V,W,X,Y
#szyfr (litera+3)

#funkcja ord()-zwraca kod ASCII znaku
# print(ord("A"))
# print(ord("Z"))
#(w python kod ASCII wielkich liter A-Z są od 65 do 90)

#funkcja chr()- zwraca znak dla danego kodu
# print(chr(66))
# print(chr(75))

#zadanie: wypisz alfabet liter wielkich
# for i in range(65,91):
#   print(chr(i),end=" ")

#string w python-"lista"
napis=input("Podaj coś do zaszyfrowania:")
szyfr=""
# print(napis[0], napis[1], napis[2])
# print(len(napis))

for i in range(len(napis)):
  print(napis[i])
  szyfr=szyfr+chr(ord(napis[i]+3))
  print(szyfr)

for i in range(len(napis)):
  print(napis[i])
  szyfr=szyfr+chr((65+ord(napis[i]-65+3)%26))
  print(szyfr)