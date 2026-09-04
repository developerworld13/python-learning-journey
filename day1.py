#Print your name, age, and city using variables
name = "Developer"
age = 20
city = "Pune"
print("Name",name)
print("Age",age)
print("City",city)


#Swap two variables' values (try without a temp variable: a, b = b, a)
a=1
b=2
a,b=b,a
print(a)
print(b)

#Temperature converter — Celsius to Fahrenheit: F = (C * 9/5) + 32
C=30
F = (C * 9/5) + 32
print(str(C))
print(str(F))

#Simple calculator — take two numbers, print add/subtract/multiply/divide results
add = a+b
sub = a-b
mul = a*b
div = a/b
print("addition",add)
print("subtraction",sub)
print("multiplication",mul)
print("division",div)


#Area of a rectangle: 
l=5
w=9
area_rect = l*w
print("Area of Rectangle",area_rect)

#Area of a circle: area = 3.14159 * radius ** 2
r=13
area_circle = 3.14159 *r ** 2
print("Area of Circle",area_circle)


#Print the type of 5 different values (a string, int, float, bool, and a list)
string="name"
inte=6
float=5.5
bool=True
print(string)
print(inte)
print(float)
print(bool)


#Take a string number like "20", convert to int, add 10, print result
s=str(90)
i=int (s)
result=i+10
print(result)

#Use input() to ask the user's name, then print "Hello, <name>!"
name = input("Enter your name:")
print(f"Hello {name}!")

#Calculate simple interest: SI = (principal * rate * time) / 100
p=10000
ra=6
t=4
SI=(p*ra*t)/100
print(f"Simple Interest={SI}")