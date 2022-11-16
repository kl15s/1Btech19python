#zad1
#1
# n=int(input())
# for i in range(n):
#   print("*-|", end=" ")
#2
#n=int(input())
# print("*-|"*n)

#zad2
# n=int(input())

# for i in range(1,n+1):
#   print("*"*i,end=" ")
#   if i%2==0:
#     print("--",end=" ")
#   else:
#     print("||",end=" ")

#zad3
# n=int(input())

# for i in range(1,n+1):
#   print("*",end=" ")
#   if i%2==0:
#     print("--"*i,end=" ")
#   else:
#     print("|"*i,end=" ")

#przykład(dodatkowy materiał nieobowiązkowy)

# n=int(input())

# for i in range(n):
#   for j in range(n):
#     print(f"({i},{j})", end=" ")
#   print()

#zad7(dodatkowy materiał nieobowiązkowy)
# n=int(input())

# for i in range(n):
#   for j in range(n):
#     if i==0 or j==0 or j==n-1 or i==n-1 or (i==n/2 and j==n/2):
#       print("*", end=" ")
#     else:
#       print("-",end=" ")
#   print()