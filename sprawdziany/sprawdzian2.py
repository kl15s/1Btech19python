n=0
suma=0

for i in range(2,201):
  x=int(input())
  if x%i==0:
    suma+=i
  suma-x
if x<=2:
  print("NIE")
else:
  for i in range(2,x):
    if x%i==0:
      print("NIE")
      break
    print("TAK")
  