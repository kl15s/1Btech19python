#zadanie1
# a=input()
# b=input()
# reszta=0

# for i in b:
#   L=list(b)
#   if a==L[a+reszta]:
#     print("TAK")
#   else:
#     print("NIE")

#zadanie2
a=input()
napis="BAZA"

for i in range(len(a)):
  L=list(a)
  P=list(napis)
  
  if P==L: 
    print("TAK")
  else:
    print("NIE")