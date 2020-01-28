#Calculation of BMI in m2 with user inputs

Weight = float(input("Enter weight in kg: "))
Height = float(input("Enter height in cm: "))

HeightMsq = (Height/100)**2

bmi = round(Weight / HeightMsq,2)

print("Your BMI is",bmi)