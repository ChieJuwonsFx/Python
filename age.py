#Menghitung umur

import datetime as dt

print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal lahir\t : "))
bulan = int(input("Bulan lahir\t : "))
tahun = int(input("Tahun lahir\t : "))

print()
print (f"Hasil : ")
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365.25
umur_bulan_sisa = (umur_hari.days % 365.25) // 30.4167
umur_hari_sisa = (umur_hari.days % 365.25) % 30.4167

print(f"Umur anda adalah hari : {type(umur_tahun)} tahun, {umur_bulan_sisa:.0f} bulan, {umur_hari_sisa:.0f} hari.")