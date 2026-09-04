# 1.Take two numbers as input, print results of + - * / // % **
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print("Addition:",(a+b))
print("Subtraction:",(a-b))
print("Multiplication:",(a*b))
print("Division:",(a/b))
print("Floor division",(a//b))
print("Modulus:",(a%b))
print("Power:",(a**b))

# 2.BMI calculator: BMI = weight / (height ** 2)
w=4
h=5
bmi=w/(h**2)
print("BMI=",bmi)

# 3.Check if a number is even or odd using %
n=13
labels = ["odd number", "even number"]
is_even=(n%2==0)
print(n, "is", labels[is_even])

# 4.Km to miles converter: miles = km * 0.621371
km=5
miles=km*0.621371
print(km,"km =",miles)

# 5.Check if a number is divisible by both 3 and 5 (and)
num=15
result = (num%3==0 and num%5==0)
print(num," is divisible by both 3 and 5:",result)

# 6.Take three numbers, find the largest using comparisons (no if/else yet)
x=4
y=7
z=13
largest = max(x,y,z)
print("largest number is: ",largest)

# 7.Rupees to dollars converter (pick a fixed rate)
rupee=float(input("Enter amount in rupee"))
rate=83.00
dollars=rupee/rate
print(rupee, "INR=", round(dollars, 2), "USD")

# 8.Take a year, check divisibility by 4 using %
year = int(input("Enter a year:"))
print(year, " is divisible by 4", year%4==0)
