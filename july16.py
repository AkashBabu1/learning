user =(input("Enter the input: "))# input
for i in range(len(user)):#loop range
    print(user[:i])

for outer in range(1,5):
    print()
    for inner in range(5,0,-1):
        print("I",end = " ")

for square in range(1,6):
    print()
    for j in range(1,6):
        if square == 1 and j== 1 or square ==2 and j==2 or square == 3 and j== 3 or square == 4  and j== 4 or square == 5  and j== 5:
            print("$",end=" ")
        elif square== 1 or square == 5 or j == 1 or j == 5:
            print('*',end = " ")
    
        else:
            print(" ",end=" ")

for mount in range (5):
    print()
    for space in range(5,mount,-1):
        print("m",end= " ")
    for mountq in range(mount):
        print(mount,end=" ")

for mount in range (5):
    print()
    for space in range(5,mount,-1):
        print("m",end= "")
    for mountq in range(mount):
        print(mount,end=" ")
for l in range (1,5):
    print()
    for k in range(1,5):
        if l==1 or l ==4 or k==1 or k== 4:
            print("I",end = " ")
        else:
            print(" ",end =" ")

for rev in range(5):
    print()
    for again in range(rev):
        print("*",end= " ")