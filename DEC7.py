user = int(input("Enter the numbers : "))
if user %2 ==0:
    print("the number is even")
else: 
    print("it's odd number")

#positive, negative
user1 = int(input("Enter the number: "))
if user1 >0: 
    print("it's positive number : ")
elif user1 ==0 : 
    print("it's zero")
else: 
    print("it's negative")

# largest of two numbers 
number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the second number: "))
print(max(number1,number2))
if number1 == number2:
    print("both are equal")


#leap year program 
user4 = int(input("enter the number you want: "))
if user4%4==0 and user4%100!=0 or user4 % 400 ==0: 
    print("it's leap year")
else: 
    print("it's not leap year")

# find the second largest number: 
numbers = [10, 5, 20, 8, 15]

largest = float()
second_largest = float()

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)

