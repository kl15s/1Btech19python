W = "AAAAABBCCCCDDDEEEEEEEFGGGH" #5A2B3C3D7EF3G
W += "."
H = ""
ilosc = 1
for i in range(len(W)-1):
  if W[i] == W[i+1]:
    ilosc = ilosc+1
  else:
    if ilosc>1:
     H += str(ilosc)
    H += W[i]
    ilosc = 1
print(H)
  