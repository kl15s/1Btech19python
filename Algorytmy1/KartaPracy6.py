#zadanie1 
# a=int(input())
# b=int(input())
# c=int(input())

# #arytnetyczny- jest stała różnica między liczbami w ciągu
# if b-a==c-b:
#   print("Jest arytmetyczny")
# #geometryczny- istnieje stały iloraz miedzy liczbami w ciągu
# if b/a==c/b:
#   print("Jest geometryczny")
# #rosnący
# if b>a and c>b:
#   print("Jest rosnący")
# #malejący
# if a>b and b>c:
#   print("Jest malejący")

#zadanie2
# suma=0

# for i in range(100,1000):
#   if i%8==0 and i%16!=0:
#   suma+=i
#   print(suma)

#zadanie3
 # for i in range(99,9,-1):
#   if i%7==0:
#     wielok=i
#     break

# ilość=0
# for i in range(1000,10000):
#   if % wielok==0:
#     ilość=ilość+1
#   print(ilość)

#zadanie4
ilość=0
suma=0

for i in range(10,100):
  cs= i/100 
  cd=i//10 or (i%100)//10 or (i//10)%
  cj=i%10
  if cd>=2*cj:
    ilość +=1
  print(ilość)

#zadanie5
