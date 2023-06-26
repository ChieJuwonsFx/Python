sisi = int(input("Masukkan jumlah sisi segitiga yang ingin anda buat : "))

count = 1
space = int(sisi/2)

while True :
    if (count%2):
        print (" "* space + "*"*count)
        count += 1
        space -= 1
        
    else :
        count += 1 
        continue

    if count > sisi:
        break

count = count - 2
space = 1
while True :
    if (count%2):
        print (" "* space + "*"*count)
        count -= 1
        space += 1
       
    else :
        count -= 1 
        continue

    if count == 0 :
        break
   