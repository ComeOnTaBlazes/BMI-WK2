#Calculation of BMI in m2 with user inputs

Weight = float(input("Enter weight in kg: "))
Height = float(input("Enter height in cm: "))

HeightM = (Height/100)**2

BMI = Weight / HeightM

print("Your BMI is",BMI," m2")