# Stages of life
age = int(input("Insert the age of the person: "))
if age < 2:
    print("The person is a baby")
elif age >= 2 and age < 4:
    print("The person is a kid")
elif age >=4 and age < 13:
    print("The person is a child")
elif age >= 13 and age < 20:
    print("The person is a teenager")
elif age >= 20 and age < 65:
    print("The person is an adult")
else:
    print("The person is a elder")
