for i in range(1,6):
    for j in range(i):
        print('*',end= " ")
        for k in range(5,0,-1):
            print('1',end=" ")
    print()

for rep in range(6):
    print()
    for j in range(rep):
        print("*11111",end=" ")
print("------------------------------------")

count_composite = 0
prime = 0

while (1):
    user = int(input("Enter the number you want: "))
    composite = 0
    for i in range(2,user):
        if user%i == 0:
            composite= 1
            break
    if user==-1 :
        break
    elif composite ==1:
       count_composite += 1
       print("this is composite number: ",user) 
    else:
        prime +=1
        print("this is prime number : ", user) 

number = input("enter the number:  ")
for i in number:
    print(i)
