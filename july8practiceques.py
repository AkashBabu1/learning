#while loop :
#count from 1 to 10
num = 1
while num <=10:
    print(num, end=" ")
    num +=1
#print even numbers from 2 to 20
print()
start = 2
while start <=20:
    if start % 2 == 0:
        print(start)
    start+=1

# guess the number game
secret_num = 12
guess= None
while secret_num!= guess:
    guess = int(input("enter the secret number: "))
    if secret_num == guess:
        print("ready to go: ")
    else:
        print("no worries try again: ")
# print table of a number 
user = int(input("Enter table you want: "))
end = int(input("where the table has to end: "))
cont =0
while cont < end:
    cont+=1
    out = user*cont
    print(f'{user}*{cont}={out}')

#countdown timer(start from 10 and countdown to 0)
cout = 10
while cout >=0:
    print(cout)
    cout-=1
#keep asking name until user types "stop"
secret1= 'stop'
user = None
while  secret1!=user:
    user = input("Enter the input: ")
    if user != secret1 :
        print("try again!")
# sum of digits
