# Konversi suhu dari farenheit ke suhu lainnya
farenheit = float(input("Masukkan suhu dalam farenheit : "))
celcius = (5/9) * (farenheit - 32) 
reamur = (4/9) * (farenheit - 32)
kelvin = celcius + 273
print("Suhu dalam celcius adalah ",celcius)
print("Suhu dalam reamur adalah ",reamur)
print("Suhu dalam kelvin adalah ",kelvin)
print()

# Konversi suhu dari celcius ke suhu lainnya
celcius = float(input("Masukkan suhu dalam celcius : "))
farenheit = ((9/5) * celcius) + 32
reamur = (4/5) * celcius
kelvin = celcius + 273
print("Suhu dalam farenheit adalah ",farenheit)
print("Suhu dalam reamur adalah ",reamur)
print("Suhu dalam kelvin adalah ",kelvin)
print()

# Konversi suhu dari reamur ke suhu lainnya
reamur = float(input("Masukkan suhu dalam reamur : "))
celcius = (5/4) * reamur
farenheit = ((9/4) * reamur) + 32
kelvin = celcius + 273
print("Suhu dalam celcius adalah ",celcius)
print("Suhu dalam farenheit adalah ",farenheit)
print("Suhu dalam kelvin adalah ",kelvin)
print()

# Konversi suhu dari kelvin ke suhu lainnya
kelvin = float(input("Masukkan suhu dalam kelvin : "))
celcius = kelvin - 273
farenheit = ((9/5) * celcius) + 32
reamur = (4/5) * celcius

print("Suhu dalam celcius adalah ",celcius)
print("Suhu dalam farenheit adalah ",farenheit)
print("Suhu dalam reamur adalah ",reamur)
print()