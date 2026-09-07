# 1.Print numbers 1 to 20 using a for loop
for i in range(1,21):
   print (i)

# 2.Print all even numbers between 1 and 50 using a for loop (hint: use range with step, or use if inside the loop)
for i in range (1,51):
    if i % 2 == 0:
        print (i)

# 3.Sum of numbers from 1 to 100 using a loop (keep adding to a running total)
sum=0
for i in range (1,101):
    sum += i     #sum=sum+1
print("sum of total numbers : ",sum)

# 4.Multiplication table of a number (take input, print its table 1×N to 10×N) using nested loop or single loop
n = int(input("Enter a number"))
for i in range (1,11):
        print (n*i)
        
# 5.Countdown from 10 to 1 using a while loop, then print "Liftoff!"
i=10
while i >= 1:
    print(i)
    i-=1
print("Liftoff!")

# 6.Print a right-angle triangle pattern of stars using nested loops (e.g., for size 5: row 1 has 1 star, row 2 has 2 stars, etc.)
for a in range (1,6):
    for b in range (a):
          print("*",end="")
    print()


# 7.Find the factorial of a number using a loop (5! = 5×4×3×2×1)
num = 5
i = 5
fact = 1
for i in range (1,6):
    fact = fact * i
print(fact)


# 8. Reverse a string using a for loop (don't use [::-1] — build it manually by looping through characters)
str = "Sneha"
rev = ""
for letter in str:
    rev = letter + rev
print(rev)
    
