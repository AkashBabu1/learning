raining = input("Is it raining outside? ")
umbrella = input("Do you have an umbrella? ")

if raining.lower() == 'yes':
    print("Is that so!")
    
    if umbrella.lower() == 'yes':
        print("You can go outside.")
    else: 
        print("You need an umbrella!")
else: 
    print("I won't let you out!")
# check even or odd 
user = int(input("enter any number you want: "))
if user %2 ==0 :
    print("hey found it you entered even number: ",user)
else: 
    print("hey found that it's odd number: ",user)
#age eligibility: 
age = int(input("Enter you age: "))
if age >= 18:
    print("congrates! you can vote")
elif age<18:
    print("ho ho! you are too young: ")
else:
    print("enter the valid input: ")
#positive, negative, zero
number = int(input("enter any number you want :"))
if number >0:
    print("it's positive number: ",number)
elif number<0:
    print("it's negative number: ",number)
else:
    print("it's zero: ")

#find the largest number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1>num2 and num1>num3:
    print("number1 is greater: ",num1)
    if num1==num2 or num1 == num3:
        print("check some number same:")
    else:
        print("can you reenter the number:")
elif num2>num3:
    print("number2 is greater: ",num2)
else:
    print("number 3 is greater: ",num3)

#leap year program:
leap_year = int(input("Enter which year you want to check!: "))
if (leap_year%4 ==0 and leap_year%100 != 0) or(leap_year%400 == 0):
    print("its leap year: ",leap_year)
else: 
    print("It's not a leap year: ",leap_year)
#password checker:
password = "secret123"
user=input("Enter the your password: ")
if user == password:
    print("access granted")
else: 
    print("access denied")
#grading system
score = int(input("Enter your score: "))
if score >=90 :
    print("grade - A")
elif score>=80 and score<=89:
    print("grade - B")
elif score>=70 and score<=79:
    print("grade -C")
elif score <70:
    print("sorry to say this: you are fail: ")
else: 
    print("out of range:")
# odd or even adn divisible by 5
numbers = int(input("Enter any number: "))
if number %2 ==0:
    print("it's even")
elif number %5 == 0:
    print("it's divisible by 5")
else: 
    print("it's odd numeber")
    