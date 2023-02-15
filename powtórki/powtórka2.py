# a=int(input())
# b=int(input())
# s1=0
# s2=0
# for i in range(1,a):
#   if a%i==0:
#     s1+=i
# for j in range(1,b):
#   if a%j==0:
#     s2+=j

# if s1 == b+1 and s2 == a+1:
#   print("TAK")
# else:
#   print("NIE")

from math import gcd

licz1=int(input())
mia1=int(input))
licz2=int(input())
mia2=int(input())

#NWW mianowników
#iloczyn mianowników/NWD(mianowników)
wspolny= int(mia1 * mia2/ gcd(mia1,mia2))
