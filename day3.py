# Leap year checker: divisible by 4, EXCEPT century years (÷100) unless also ÷400
year = int(input("Enter year:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,"is a leap year")
        else:
            print(year,"is not leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not leap year")


# 2.Grade calculator using proper elif ordering (A: 90+, B: 75-89, C: 50-74, Fail: <50)
marks=int(input("Enter your marks to calculate grade :"))
if marks >= 90:
    print("A Grade")
elif marks >= 75 and marks <=89:
    print("B Grade")
elif marks >=50 and marks <=74:
    print("C Grade")
else:
    print("Fail")


# 3.Largest of 3 numbers using if/elif/else (no max() this time — write the logic yourself)
a = int(input("Enter 1st number : ")) 
b = int(input("Enter 2nd number : ")) 
c = int(input("Enter 3rd number : ")) 
if a > b:
    if a > c:
        print(a,"is largest number")
    else:
        print(c,"is largest number")
else:
    if b > c:
        print(b,"is largest number")
    else:
        print(c,"is largest number")


# 4.Simple login system: check username and password against fixed values, print "Login successful" or "Login failed"
user = input("Enter Username : ")
passwd = input("Enter Password : ")
if user == "admin" and passwd == "password" :
    print("Login Successful!")
else:
    print("Login Failed!")


# 5.Number classifier: positive / negative / zero
num = int(input("Enter a number : "))
if num > 0:
    print(num,"is positive number")
elif num < 0:
    print(num,"is negative number")
else:
    print(num,"is zero")


# 6.Vowel or consonant checker for a single letter
ch = input("Enter a character")
if ch in "aeiouAEIOU":    
    print(ch ,"is vowels")
else :
    print(ch ,"is consonents")


# 7.Simple traffic light system: take input "red"/"yellow"/"green", print what action to take (stop/wait/go)
colour = input("Enter Traffic signal colour red/yellow/green")
if colour == "red":
    print("STOP")
elif colour == "yellow":
    print("WAIT")
elif colour == "green":
    print("GO")
else:
    print("Invalid Input")


# 8.Ticket pricing: take age as input — child (under 12): $5, senior (60+): $7, adult: $10 — print ticket price
age = int(input("Enter your age : "))
if age < 12:
    print("Ticket price for child id $5")
elif age < 60:
    print("Ticket price for adults is $10")
else:
    print("Ticket price for senior is $7")