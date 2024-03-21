weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

height_in_meters = height / 100
BMI = weight / (height_in_meters ** 2)
rounded_BMI = round(BMI, 1)

print("Your BMI is:", rounded_BMI)

if BMI < 16:
    print("You are severely underweight. BMI:", rounded_BMI)

elif 16 <= BMI < 18.5:
    print("You are underweight. BMI:", rounded_BMI)

elif 18.5 <= BMI < 24:
    print("You are healthy. BMI:", rounded_BMI)

elif 24 <= BMI < 30:
    print("You are overweight. BMI:", rounded_BMI)

elif BMI >= 30:
    print("You are obese. BMI:", rounded_BMI)
