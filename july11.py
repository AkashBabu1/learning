"""# for loops 
# question
sum = 0#sum=
user = int(input("Enter the input: "))#input
for start in range (1,user+1):#loop 1,input
    sum = sum+start#sum
print("this is the averavge value = ",sum/user)

#question 2
n = int(input("Enter any table you want : "))
for i in range (1,n+1):
    print(f'{n} * {i} = {n*i}')

#question3 
start = int(input("Enter the starting number: "))
ending = int(input("Enter the ending number: "))
for i in range (start,ending+1):
    if i % 2 == 0 : 
        print("it's even number- ",i)
    else:
        print(i, "it's odd number")"""

#question3
factorial = int(input("enter the number you want: "))
sum = 1
for i in range (1 , factorial):
    sum = sum * i
print(sum)



for star in range(5,0,-1):
    for j in range(star):
        print("8",end= " ")
    print()
    

for assending in range(1,5+1):
    print()
    for ord in range(assending):
        print(ord,end= " ")

for same in range(6):
    print()
    for same1 in range(same):
        print(same,end = "")
count= 0
for cnt in range(5):
    print()
    for k in range(cnt+1):
        print(count,end = "")
        count+=1


for outlp in range(1,6):
    print()
    for space in range(6,outlp,-1):
        print( " ",end = " ")
    for inloop in range(1,outlp+1):
        print(inloop,end= " ")\
        
for mount in range (1,6):
    print()
    for spac in range(6,mount,-1):
        print("",end= " ")
    for inn in range(mount):
        print(mount,end = " ")