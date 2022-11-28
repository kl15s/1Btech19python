#PRE
# print (list(range(2,8,1)))
# print(list(range(8,1,-1)))
# for i in range(3,10):
#   print(i)


# pętla liczb dwucyfrowych od 10 do 21
# for i in range(10,22):
#   print(i)

# pętla liczb dwucyfrowych nieparzystych od 15 do 31
# for i in range(15,33,2):
  # print(i, end=" ")
  
# pętla liczb dwucyfrowych malejąco (step ujemny)
# for i in range(99,9,-1):
#   print(i,end=" ")

# pętla liczb dwucyfrowych malejąco (step dodatni)
# for i in range(10,100,1):
#   print(109-i,end=" ")
  
#pętla liczb 3-cyfrowych podzielnych przez 20
# for i in range(100,1000,20):
#   print(i,end=" ")

#zad1
# n= int(input())
# for i in range(n):
#   print(i**3+3,end=" ")

#zad2
# for i in range(105,1000,15):
#   print(i,end=" ")

# for i in range (100,1000):
#   if i %15==0
#   print(i,end=" ")

#zad3
# n=int(input())
# for i in range(1,n+1):
#   if n%i==0:
#     print(i, end=" ")

#dzielniki właściwe
# n=int(input())
# for i in range(2,n):
#   if n%i==0:
#     print(i, end=" ")

#zad4
# s=0
# for i in range(10,100):
#   s=s+i
# print(s)

#zad5
# n = int(input("W ile gramy?"))

# suma = n*(n+1)//2
 
# for i in range(n-1):
#   a = int(input()) 
#   suma = suma - a

# print("Brakuje:", suma)

#napisz pętle sumującą liczby dwucyfrowe parzyste

# suma=0
# for i in range(10,100,2):
#   suma= suma + i
# print(suma)


#zad6
#Fibo wg literatury 0,1,1,2,3,5,8,13,21,34
#Fibo nasze 1,2,3,5,8,13.....

# n=int(input())
# a,b=0,1
# for i in range(n):
#   a,b=b,a+b
#   print(b,end=" ")
