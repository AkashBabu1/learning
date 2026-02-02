#combined practice questions(variabes+operators+loops)
#1. Print the Sum of First 10 Even Numbers
for i in range(1,10+1):
    if i %2 == 0:
        print(i)

#2  Print the Factorial of a Number-Ask the user for input and calculate factorial using a loop.
user = int( input("Enter the factorial number: "))
s = 1
for i in range( 1,user+1):
    s= i*s
print(s)

#3Find the Largest of Three Numbers Take 3 user inputs and use comparison operators and logic.
num1,num,num3 = (input("Enter the intergers : "))
print(max(num,num1,num3))

#Check if a Number is Prime
user1 = int(input("Enter the input: "))
comps= 0
for  i in range (2,user1):
    if user1%i ==0 :
        comps =1
        break
if comps == 1 :
    print("it compos")
else:
    print("its prime")

print("-----------------------------------")
#5. Print a Table of Squares (1 to 10) Use a loop, variables, and exponentiation operator **.
count= 11
for table in range (1,11):
    print(table**count)