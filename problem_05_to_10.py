#5. Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f"The sum of first {n} natural numbers is: {sum}")

#6. Write a program to find the factorial of a given number using for loop.
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is: {factorial}")

#Write a program to print the following star pattern.
 #*
#***
#***** for n = 3
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

#Write a program to print the following star pattern:
#*
#**
#*** for n = 3
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print("*" * i)

#9. Write a program to print the following star pattern.
#* * *
#* * for n = 3
#* * *
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print("* " * n)
    else:
        print("* " * (n - 1))

#. Write a program to print multiplication table of n using for loops in reversed
#order.
n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n*i}")