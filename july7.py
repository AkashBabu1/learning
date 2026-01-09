#varible practice
x = y = z = "tamil"
print(x)
print(y)
print(z)

months =["jan","feb","march"]
z,y,x= months
print(z)
print(x)
print(y)
print(x,y,z)
print(months)

language = "python "
connector = "is "
opinion = "learn"
print(language+connector+opinion)

def mul(a,b):
    """this is for multiplication"""
    print(a*b)
mul(1,3)
print(mul.__doc__)

high_demand = "ain"
High_demand = "ai automation"
print(high_demand)
print(High_demand)
high_demand = "consistency"
print(high_demand)
print(high_demand)

best,worst,right = ("ai automation","not taking action","take action")
print(worst,'\n',best,'\n',right)


#data types
"""numeric,set, dictionary,boolean,sequence"""
fingers =10
fig_length = 1.1
most_use_finger = "35"
alpha_numeric = 1j
print(type(fingers))
print(type(fig_length))
print(type(most_use_finger))
print(type(alpha_numeric))
a = complex(alpha_numeric)
print(type(a))
b = int(most_use_finger)
print(type(b))

#dictionary data type noindexing,ordered,mutable,noduplicate keys
family = {'dad':'appa','mom':"amma",1:3}
print(type(family))
print(family)
print(family['dad'])
#set data type unordered,immutable,noduplicate,noindexing
ai_tools = {"n8n","make.com","relevance","base44"}
print(type(ai_tools))
print(ai_tools)
#list data type ordered,mutable,duplicate,indexing
wishes = ["businees","calisthenics","mental health","give rest to my parents"]
print(wishes)
print(type(wishes))
#tuple datatype ordered,mutable,duplicate,indexing

action =("consistent action", "perpectual learners","ignore short time pleasure")
print(action)
print(type(action))

"""operators in python 
    arithmatic(+-*%//),assingment operator(+=-=),identity operator(is,isnot)
    membership operator(in,notin),logical operator(and,not,or)bitwise operator"""
#arithmatic operator
subject = 5
mark = 100
print(subject + mark,"- additon")
print(subject - mark,"- subraction")
print(subject / mark,"- divison")
print(subject // mark,"- floor division")
print(subject * mark,"- multiplication")
print(subject ** mark,"- exponantial")
print(subject % mark,"- modulas")

#assingment operator
subject+=1
print(subject)
subject +=mark
print(subject)
subject /=mark
print(subject)
#logical operator(and,or, not)
print(subject>4 and subject <200)
print(not(subject>2 or subject<2))
#identity operator(is,isnot)
print(subject is mark)
print(subject is not mark)
#membership operator(in not in )
brand = "DETOX"
print("q" in brand,"- I'm membership operator")
#operator precedence
print(2*(23+3)/3)


#slicing(we can specify the indexes where to start and where to end)
sweets = ["paalkova","maisurepawk","rasakula",1,2,34,0,34]
print(sweets)
print(sweets[-1])
print(sweets[3])
print(sweets[::2])
print(sweets[::-1])
print(sweets[-1::])
 