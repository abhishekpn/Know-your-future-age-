print('AGE CALCULATOR MACHINE')
print("1.You can calculate  what is your age will be  in any paricular year \n"
      "2.You can calculate when you will be 100 years old ")

curr_year = 2020
value = str(input("Enter your Age OR Year of birth: "))
if len(value)<=2:
    print(f"This is your present age {value}")
    count = 100 - int(value)
    count = count + curr_year
    print(f"You will be 100 years old in year {count}")

elif len(value)>3:
    print(f"Your current age is {curr_year - int(value)}")
    count = int(value) + 100
    print(f"You will be 100 years old in {count}")
elif int(value) >= 100:
    print("You are already 100 years old")

else:
    print("Please check your input again ")

interestedYear = int(input("Enter the year you want too know your age: "))
if len(value)<=2:
    year = interestedYear - curr_year
    year = year + int(value)
    print(f"You will be {year} years old in {interestedYear} ")

elif len(value)>3:
    year = interestedYear - int(value)

    print(f"You will be {year} years old in {interestedYear} ")

