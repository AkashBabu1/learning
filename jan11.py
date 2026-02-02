"""i=1
s=0
while(i<=10):
    print(i)
    s=s+i
    i=i+1
print(s)
print(s/i)

#print(horizontal astrisks)
i=0
while (i<=20):
    print("*",i ,end=" ")
    i=i+1
print()
#write a program to calculate the sum of numbers from m to n
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))
s=0
while (m<=n):
    s=m+s
    m=m+1
print(s)

#write the program to read numbers until-1 is also count negative , positive, and zeros by the user;

positive =0
negative =0
zeros =0

while True:
    user = int(input("Enter the number that you wish: "))
    if user ==-1:
        break
    if user >0:
        positive= positive +1
    elif user==0:
        zeros= zeros +1
    else:
        negative= negative +1
     
    
print(positive)
print(negative)
print(zeros)"""

#write a program the whether the given number is amstrong number

"""user1 = str(input("enter the value: "))
length = len(user1)
a=0
while int(user1) !=0:
    for a in str(user1):
        a= int(a)**length

if user1 ==a:
    print("yeah it's the armstrong number")
else: 
    print("it's not a armstrong number")
print(a)"""
 #for loop-Write a program to print the multiplication table of n, where n is entered by the user.
"""user = int(input("Enter the table that want to know: "))
count = int(input("Enter until which one you want to print: "))
for i in range (count+1):
    ans = user*i
    print(f'{user}*{i}={ans}')"""
#factorial using for loop
"""user = int(input("Enter the number that you want: "))
fact = 1
for i in range(1, user+1):
    fact= i*fact
print(fact)"""
#wirte a program the given number is prime number or composite

"""user1 = int(input("Enter the value: "))
composite = 0
for i in range(2,user1):
    if user1%i == 0: 
        composite = 1
        break
if composite ==1:
    print("it's the composite number")
else:
    print("it's the prime number")"""
#write the program print the following pattern

for i in range(1,6):
    print("pass",i,end =" ")
    for j in range(1,6):
        print(j, end =" ")
    print()

for i in range(5):
    print()
    for j in range(6):
        print("*",end=" ")
    
for i in range(7):
    print()
    for j in range(i):
        print("*",end= "")

for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j, end=" ")

#write a program the following pattern
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(i, end=" ")
#write a program the following pattern
for i in range(5):
    print()
    for j in range(1,i+1):
        print(j,end=" ")
#write a program to print the following the pattern.
for i in range(1,6):
    print()
    for k in range(6,i,-1):
        print("", end=" ")
    for j in range(1,i+1):
        print(j,end='')