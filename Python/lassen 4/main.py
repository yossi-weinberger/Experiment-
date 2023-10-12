"""
weight = float(input("Please enter your weight: \n"))
height = float(input("Please enter your height (in meters): \n"))
bmi = int(weight / height**2)

print("\nYour BMI is: " + str(bmi))

if bmi < 18.5:
    print("You are underweight")
elif bmi > 18.5 and bmi < 25:
    print("Your weight is normal and and you are in good shape")
elif bmi > 25 and bmi < 30:
    print("You are overweight")
elif bmi > 30:
    print("You are obese, go see the doctor")

num = (input("type a nunber: \n"))
result = (int(num[0]))+(int(num[1]))
print(result)

num = int(input("type a nunber: \n"))
result = (num % 10) + (num // 10)
print(result)


age = int(input("type your age: \n"))
yaer = 120 - age
month = yaer * 12
weeks = month * 52
days = weeks * 7

print(f"You have left to live:\n {yaer} yaers \n {month} month \n {weeks} weeks \n {days} days")

"""
