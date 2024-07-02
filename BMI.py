# BMI (Body Mass Index)

weight = float(input("Masukkan berat badan (kg): "))
height_cm = float(input("Masukkan tinggi badan (cm) : "))
height_m = height_cm / 100

bmi = (weight / (height_m ** 2))
print (bmi)

if bmi > 27:
    print("Kelebihan berat badan tingkat tinggi.")
elif bmi >= 25:
    print("Kelebihan berat badan tingkat rendah.")
elif bmi >= 18.5:
    print("Normal.")
elif bmi >= 17:
    print("Kekurangan berat badan tingkat rendah.") 
else :
    print("Kekurangan berat badan tingkat tinggi.")  