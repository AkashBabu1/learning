"""#for loop examples
user =int(input("Enter the number that you want: "))
s=0
for i in range(1,user+1):
    s+=i
print(i)
avrage=s/i
print(avrage)
print(s)

#write a program to print the multiplication table of n
user = int(input("Enter the table you want: "))
stop = int(input("enter the stoping range you want: "))
for i in range(1,stop+1):
    result = user*i
    print(f'{user}*{i}={result}')

#factorial
user = int(input("enter the factorial number that you want: "))
s=1
for i in range(1,user+1):
    s*=i
print(s)
"""

"""#write the program to print foloowing paten.
for i in range(1,5+1):
    print()
    for j in range(1,i):
        print(j, end=" ")

#write a program to print(*)
for i in range(1,5):
    print()
    for j in range(i):
        print("*",end="")

#write a program to print the same number : 
for i in range(1,6):
    print()
    for j in range(i):
        print(i, end=' ')"""

"""#write a hollow square *
n=5


#write a program 
for i in range(n):
    for j in range(n):
        # border
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        # diagonal from top-left to bottom-right
        elif i == j:
            print("$", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 5  # size of the square

for i in range(n):
    for j in range(n):
        # border
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        # main diagonal (left to right)
        elif i == j:
            print("$", end=" ")
        else:
            print(" ", end=" ")
    print()

n = 5
for i in range(n):
    for j in range(n):
        # special case: top-left corner
        if i == 0 and j == 0:
            print("$", end=" ")
        # border
        elif i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        # main diagonal (left to right)
        elif i == j:
            print("$", end=" ")
        else:
            print(" ", end=" ")
    print()
n = 5
for i in range(n):
    for j in range(n):
        # special case: top-left corner
        if i == 0 and j == 0:
            print("$", end=" ")
        # border
        elif i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        # main diagonal (left to right)
        elif i == j:
            print("$", end=" ")
        else:
            print(" ", end=" ")
    print()
n = 5
for i in range(n):
    for j in range(n):
        # special case: top-left corner
        if i == 0 and j == 0 or i == n-1 and j == n-1:
            print("$", end=" ")
        # border
        elif i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        # main diagonal (left to right)
        elif i == j:
            print("$", end=" ")
        else:
            print(" ", end=" ")
    print()
"""
"""def add (a,b):
    print(a+b)
add(2,3)
add (34,54)
def sub(c,d):
    return c-d
#armstrong number 

n = int(input("enter the number: "))
#write a program using for loop
num = int(input("enter the numebr: "))
fact=1
for i in range (1,num+1):
    fact = fact*i
print("this is your factorial:", fact)"""

#prime number: 
"""user = int(input("Enter the number that you want: "))
iscomposite=0

for i in range(2,user):
    if user%i ==0:
        iscomposite =1
        break
if iscomposite ==1:
    print("number of composite")
else: 
    print("number is prime")"""
"""
babu_family = ['akash','anush','ashini']

print(babu_family[-2::])
print(babu_family[0:3])

#function:"""

def show():
    var = "good morning"
    def show1():
        p= "puliyan"
        print(p)
    show1()
    return var

print(show())

