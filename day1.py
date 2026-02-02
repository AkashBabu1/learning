"""#1st challenge(get user input)
name =(input("Enter your name: "))
age =(input("Enter you age: "))
fav_hobby =(input("Enter you favourite hobby: "))
print(f"Hi, I'm {name} I'm {age} years old and I love {fav_hobby} ")"""
#2nd challenge (area of the rectangle)
"""length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
area= length*width
print(f'area of the rectangle is : {area}')"""

#3rd challenge(temperature in clesius from the user and convert it to fahrenheit)
"""temperature = int(input("could you tell me you temperature: "))
fahrenheit = (temperature*9/5)+32
print(fahrenheit)
"""
#4th challenge calculate the user current age
for i in range(2):
    print(i)
    user = int(input("Enter your birth year!: "))#user input:
    birth_year_cal =(2025 - user)#formula
    print("Hey my friend i got it your age is :",birth_year_cal)
#5th challenge
user = input("Enter any number : ")
integer = int(user)
point = float(user)
print(type(integer))
print(type(point))
print(type(user))

#6th challenge (create a program takes two numbers get output different formate.)
num1 = int(input("Enter any number you want: "))
num2 = int(input("Enter any number you want: "))
sum =(num1 + num2)#sum
diff= (num1-num2) #difference
prod = (num1*num2)#product
div =(num1 / num2)#divison
modulus=(num1% num2)#modulus
flr_div =(num1 // num2)#floor division
expo = (num1** num2)#exponantiation
print(f'{sum}\n{diff}\n{prod}\n{div}\n{modulus}\n{flr_div}\n{expo}')

#7th challenge
num = int(input("Enter any number: "))
square = (num**2)
cube = (num **3)
dob_half=((num*2)/2)
print(f'{square}\n{cube}\n{dob_half}')

#8th challenge
first_name = input("Enter you first name: ")
sec_name = input("Enter you second name: ")
print(first_name + sec_name)

#9th challenge
character = input("what do you thing about this world: ")
print(character.upper())
print(character.lower())
print(len(character))
print(character[0],character[-1])



