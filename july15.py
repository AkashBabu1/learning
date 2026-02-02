#break,continue,pass
#1. Print numbers from 1 to 100, but stop when you reach 25.
for numbers in range (1, 100):
    if numbers == 25: 
        break
    print(numbers,end = " ")
    print()
#2.Ask the user to enter numbers continuously. Stop asking if they enter -1

while (1):
    user = int(input("Enter the numbers continuosly: "))
    if user == -1:
        print("ho ho! miss you.")
        break
    print(user)

#3 Loop through a list of fruits, and break when you find "banana".
fruits = ["apple","carrot","orange","banana","dragon fruit"]
for get in fruits:
    if get is "banana":
        break
    print(get)

#4 Print all characters in a string, stop if character is "x".
company_name = "akash_dtox_creator"
for company in company_name: 
    if company is 'x':
        break
    print(company,end = " ")
print("--------------------------")
#5 in a countdown from 10 to 0, stop the loop if the number becomes 3.


for countdown in range(10,0,-1):
    if countdown == 3:
        break
    print(countdown)

#continue practice
#1.Print numbers from 1 to 10, skip printing number 5.
for i in range ( 1, 11):
    if i is 5:
        continue
    print(i)
print("----------------------------------")

#2. Print all even numbers between 1 and 20, but skip 10 and 14.
for even in range ( 0, 20,2):
    if even is 10 or even is 14:
        continue
    print(even)
print("------------------------------------------")

#3.Ask the user to input 5 names. Skip printing names that start with "a".
for i in range(1,5):
    user = input("Enter the name you want: ")
    if user.startswith('s'):
        continue
    print(user)
print("--------------------------------")

#4 Loop through numbers 1 to 50 and print only the ones not divisible by 3.
for div in range(1,51):
    if div % 3 == 0:
        continue
    print(div, "it's the not divisible by 3")

print("++++++++++++++++++++++++++++++++++++++")
#5. Loop through a string and skip printing all vowels.
a = ['a','e','i','o','u']
for i in ("thalapthy"):
    if i in a:
        continue
    print(i)

#pass practice questions
#1.Loop through a list of fruits. If fruit is "apple", use pass (do nothing), else print it.
frts = ['avacado','goova','apple','jam']
for fruit in frts:
    if fruit is 'apple':
        pass
    print(fruit)