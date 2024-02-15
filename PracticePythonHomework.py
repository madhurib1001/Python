#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a program to print the given number is odd or even.
num=int(input("Enter Number: "))
if(num%2==0):
    print(num,"Number Is Even")
else:
    print(num,"Number Is Odd")


# In[4]:


#2. Write a program to find the given number is positive or negative
num=int(input("Enter Number: "))
if(num<0):
    print("Number Is Negative")
else:
    print("Number Is Positive")


# In[15]:


# 3. Write a program to check if the given number is palindrome or not.
num=int(input("Enter Number: "))
temp=num
reverse=0
while temp>0:
    remainder=temp % 10
    reverse=(reverse * 10) + remainder
    temp= temp //10
if num==reverse:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
    
    


# In[16]:


# 4. Write a program to find the sum of two numbers.
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
c=num1+num2
print(c)


# In[19]:


#5. Write a program to find if the given number is prime or not.
num=int(input("Enter Number: "))
flag=False
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            flag=True
            break
if flag:
    print("Number is not prime")
else:
    print("Number is prime")


# In[21]:


#6. Write a program to find a maximum of two numbers.
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
if(num1>num2):
    print(num1, "Is Greater Than", num2)
else:
     print(num2, "Is Less Than", num1)
    


# In[22]:


#7. Write a program to find a minimum of two numbers.
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
if(num1<num2):
    print(num1, "Is Less Than", num2)
else:
     print(num2, "Is Greater Than", num1)


# In[23]:


#8. Write a program to find a maximum of three numbers.
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
num3=int(input("Enter Third Number: "))
if(num1>num2 and num1>num3):
    print(num1,"is greater than",num2, "and",num3)
elif(num2>num1 and num2>num3):
    print(num2,"is greater than",num1,"and",num3)
elif(num3>num1 and num3>num2):
     print(num3,"is greater than",num1,"and",num2)
else:
    print("No Choice")


# In[24]:


#9. Write a program to find a minimum of three numbers.
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
num3=int(input("Enter Third Number: "))
if(num1<num2 and num1<num3):
    print(num1,"Is Less than",num2, "and",num3)
elif(num2<num1 and num2<num3):
    print(num2,"Is Less than",num1,"and",num3)
elif(num3<num1 and num3<num2):
     print(num3,"Is Less than",num1,"and",num2)
else:
    print("No Choice")


# In[26]:


#10. Write a program to find a factorial of a number.
num=int(input("Enter Number: "))
factorial=1
if num<0:
    print("Sorry factorial doesnot exist for negative number")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial=factorial*i
    print("The factorial of",num,"is", factorial)


# In[2]:


#11.star Pattern
for x in range(1,6):
    for y in range(1,6):
        print("*",end=" ")
    print()


# In[3]:


#12. Number pattern
for x in range(1,6):
    for y in range(1,6):
        print(x,end=" ")
    print()


# In[4]:


#13. number with increment pattern
for x in range(1,6):
    for y in range(1,6):
        print(y, end=" ")
    print()


# In[5]:


#14. reverse pattern
for x in range(5,0,-1):
    for y in range(5,0,-1):
        print(x,end=" ")
    print()


# In[9]:


#15. Number series pattern
n=5
k=1
for x in range(1,n+1):
    for y in range(1,n+1):
        print(format(k),end=" ")
        k+=1
    print()


# In[10]:


#16. odd Numbers
n=5
p=1
for x in range(1,n+1):
    for y in range(1,n+1):
        print(format(p),end=" ")
        p+=2
    print()


# In[11]:


#17. Even number pattern
n=5
p=2
for x in range(1,n+1):
    for y in range(1,n+1):
        print(format(p),end=" ")
        p+=2
    print()


# In[14]:


#18. add number serieswise pattern
for x in range(1,6):
    for y in range(1,4):
        print("{} {}".format(y,x),end=" ")
    print()


# In[1]:


#19. Sequence series
n=5
for x in range(1,n+1):
    p=x
    for y in range(1,n+1):
        print(format(p),end=" ")
        p+=n
    print()
        


# In[4]:


#20. reverse sequence pattern
n=5
for x in range(1,n+1):
    p=n-x+1
    for y in range(1,n+1):
        print(format(p),end=" ")
        p=p+n
    print()


# In[6]:


#21. 0 and 1 pattern
n=5
for x in range(1,n+1):
    for y in range(1,n+1):
        print(str((x+y)%2)+"",end=" ")
    print()


# In[8]:


#22. Capital ABCDE Pattern
for x in range (65,70):
    for y in range(1,6):
        print(chr(x),end=" ")
    print()


# In[10]:


#22. Capital ABCDE Pattern
for x in 'ABCDE':
    for y in 'ABCDE':
        print(x,end=" ")
    print()


# In[11]:


#23. Star pattern
for x in range(1,6):
    for y in range(1,x+1):
        print("*",end=" ")
    print()


# In[12]:


#24. even triangle pattern
p=2
for x in range(5,0,-1):
    for y in range(6,x,-1):
        print(format(p),end=" ")
        p+=2
    print()


# In[16]:


#25. sequence triangle pattern
p=1
for x in range(5,0,-1):
    for y in range(6,x,-1):
        print(format(p),end=" ")
        p+=1
    print()


# In[17]:


#26. sequence of table
for x in range(1,6):
    for y in range(1,x+1):
        print(format(x*y),end=" ")
    print()


# In[18]:


# 27. Fibonacci Series pattern
n=5
n1=0
n2=1
r=n1+n2
for x in range(0,n):
    for y in range(0,x+1):
        print(str(r)+"",end=" ")
        r=n1+n2
        n1=n2
        n2=r
    print()


# In[19]:


#28. A,B Pattern
for x in range(65,70):
    for y in range(65,x+1):
        print(chr(x),end=" ")
    print()


# In[20]:


#29. Reverse star pattern
for x in range(1,6):
    for y in range(6,x,-1):
        print("*",end=" ")
    print()


# In[24]:


#30. ABCD reverse pattern
decr=9
for x in range(4,0,-1):
    for y in range(x,5):
        print(" ",end=" ")
    for z in range(1,decr+1):
        print(chr(z+64),end=" ")
    decr-=2
    print()


# In[1]:


#31. Print day while choosing number from user input
num=input("Enter The day number:")
if(num=='1'):
    print("Sunday")
elif(num=="2"):
    print("Monday")
elif(num=="3"):
    print("Tuesday")
elif(num=="4"):
    print("Wed")
elif(num=="5"):
    print("Thursday")
elif(num=="6"):
    print("Friday")
else:
    print("No Choice")


# In[2]:


#32. Markswise grade
num=int(input("Enter Your Marks:"))
if(num>=90):
    print("Your Grade is A")
elif(num>80 and num<=90):
    print("Your grade is B")
elif(num>=60 and num<=80):
    print("Your grade is C")
elif (num<60):
    print("Your grade is D")
else:
    print("Fail")


# In[4]:


#33. Price of bike with tax
num=int(input("Enter price of bike:"))
if(num>100000):
    a=num*15/100
    print(a)
    AC=a+num
    print(AC)
elif(num>50000 and num<=100000):
    b=num*10/100
    print(b)
    AC1=b+num
    print(AC1)
elif(num<=50000):
    c=num*5/100
    print(c)
    AC2=c+num
    print(AC2)
else:
    print("No Choice")


# In[5]:


#34. Above 75 percentage of student can sit for exam
totaldays=int(input("Enter total number of days:"))
absdays=int(input("Enter absent days:"))
totalpresent=totaldays-absdays
per=totalpresent/totaldays*100
if(per<75):
    print("Student cannot sit for exam")
else:
    print("elligible for exam")


# In[6]:


#35. 
num=int(input("Enter the number of days:"))
if(num==5):
    c=num*2
    print(c)
elif(num>6 and num<10):
    c=num*3
    print(c)
elif(num>11 and num<15):
    c=num*4
    print(c)
elif(num>15):
    c=num*5
    print(c)
else:
    print("none")


# In[8]:


#36. 
num=int(input("Enter the kilometers:"))
if(num==10):
    c=num*11
    print(c)
elif(num>90 and num<10):
    c=num*10
    print(c)
elif(num>90):
    c=num*9
    print(c)

else:
    print("none")


# In[16]:


#37. Create simple calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid Input")


# In[20]:


#38. Python Program to calculate the square root

num = int(input("Enter number")) 
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))


# In[21]:


#39. # Python Program to find the area of triangle

a = 5
b = 6
c = 7
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# In[22]:


#40. # Python program to swap two variables

x = 5
y = 10
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# In[23]:


#41.  Python program to find H.C.F of two numbers

def compute_hcf(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))


# In[24]:


#42. # Python program to check if year is a leap year or not

year = int(input("Enter year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))


# In[28]:


#43. # Multiplication table  in Python

num = int(input("Enter number for finding table: "))

for i in range(1, 11):
    print(num, 'x', i, '=', num*i)


# In[2]:


#44. To check given number is palindrom or not
str="JavaJ"
rev=reversed(str)
if list(str)==list(rev):
    print("String is palindrome")
else:
    print("String is not palindrome")


# In[13]:


#45. Factorial using recurssion
def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
num=int(input("Enter Number: "))
print("The factorial of",num,"is",fact(num))


# In[14]:


#46. Find simple interest
def si(p,t,r):
    si=p*t*r/100
    return si
si(5000,4,2)


# In[15]:


#47. Print 10 times "Hello" in loop
for i in range(10):
    print("Hello")


# In[21]:


#48. Print fibonacci series
a=0
b=1
n=int(input("Enter Number:"))
print(a)
print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)


# In[32]:


#49. Find sum of numbers using python
def sumofnumbers(n):
    if n==1:
        return n
    else:
        return n + sumofnumbers(n-1)
num=int(input("Enter Number:"))
output=sumofnumbers(num)
#print("The sum of natural numbers {} is".format(num,output))
print("sum of first {} natural number is {}".format(num,output))


# In[33]:


#50.# make calculator
def addition(a,b):
    return a+b #local variable
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def division(a,b):
    return a/b
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
def calc(a,b):
    print("The addition is :" ,addition(num1,num2))
    print("The substraction is :" ,sub(num1,num2))
    print("The multiplication is :" ,multi(num1,num2))
    print("The division is :" ,division(num1,num2))
calc(num1,num2)


# In[34]:


#51. Classes and object
class A:
    name="Madhuri"
    age=21
    def display(self):
        name1="Mayuri"
        age=21
        print("Hello")
ob=A()
ob.display()
ob.name
A.age


# In[35]:


#52. Non-parameterized constructor
class Student:
    print("Hii this is class using default constructor")
    def __init__(self):
        print("Hii this constructor is explicitly defined")
s1=Student()


# In[37]:


#53. Non and parameterized constructor
class Student:
    def __init__(self): #without parameter
        print("Hii this is constructor without any parameter")
    def __init__(self,name):   #with  para
        print("Hii this is constructor with parameter")
        print("Hello" ,name)
s1=Student("Priya")
    


# In[38]:


#54. Static variable
class A:
    x = 10 #static variable 
    def show(self):
        #self.x=15  #instance variable 
        self.x=self.x+4
        print (self.x,A.x)
ob=A()
ob.show()
ob.show()
ob.show()
ob.show()
ob.show()
A().show()


# In[41]:


#55. wap to create person class include attributre name ,country,dob determine the person age
from datetime import date
class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def calculateage(self):
            today=date.today() #function-today
            age=today.year-self.dob.year
            if today<date(today.year,self.dob.month,self.dob.day):
                age-=1
                return age
person1=person("Mayuri","Mumbai",date(2000,7,2))
print(person1.name)
print(person1.country)
print(person1.dob)
print(person1.calculateage())


# In[42]:


#56. Multiple Inheritance: When a child class inherits from multiple parent classess,it is called multiple
class mother:
    mothername=""
    def mother(self):
        print(self.mothername)
    #base class2
class father:
    fathername=""
    def father(self):
        print(self.fathername)
#derived class
class son(mother,father):
    def parents(self): #method
        print("Father:",self.fathername)
        print("Mother:",self.mothername)
#driver's code
s1=son()
s1.fathername="ABC"
s1.mothername="XYZ"
s1.parents()


# In[43]:


#57.Multilevel Inheritance: Features of the base class and the derieved class are further inherited into
class First:
    def input(self):
        self.a=int(input("Enter First Number:"))
        self.b=int(input("Enter Second Number:"))
class Second(First):
    def add(self):
        self.z=self.a+self.b
class Third(Second):
    def result(self):
        print("Sum of two numbers",self.z)
obj=Third()
obj.input()
obj.add()
obj.result()


# In[44]:


#58. Hierarchical 
class First:
    def __init__(self):
        self.x=10
        self.y=20
class second(First):
    def findsum(self):
        self.z=self.x+self.y
        print("Sum is:",self.z)
class third(First):
    def findsub(self):
        self.z=self.x-self.y
        print("Sub is:",self.z)
obj1=second()
obj1.findsum()
obj2=third()
obj2.findsub()
    


# In[45]:


#59. #polymorphism
# Method Overriding
class Parent():
    def __init__(self):
        self.n="Parent In"
    def show(self):
        print(self.n)
class child(Parent):
    def __init__(self):
        self.n="In child"
    def show(self):
        print(self.n)
ob1=Parent()
ob2=child()
ob1.show()
ob2.show()


# In[46]:


#60. operator overloading
#assignment,arithemtic/unary-negative positiv,comparison
print(2+8)
print("a"+"b")
print("Akansha"*2)
print(3*4)

