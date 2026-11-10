def d(a,b):
    print("uncodemy")
    print(a*b)
d(5,6)

# Write a Python function to find the maximum of three numbers.
def m(a,b,c):
    result= max(a, b, c)
    print("Maximum number is",result)
m(10,40,30)

# Write a Python function to sum all the numbers in a list.
def total(numbers):
    a= sum(numbers)
    print("Sum of all numbers",a)
a= [10,20,30,40,50]
total(a)

# Write a Python function to multiply all the numbers in a list.
def total(numbers):
    a= 1
    for i in numbers:
        a = a * i

    print("Muliply all the numbers",a)
a = [10,20]
total(a)

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def m(number):
    a = 1
    for i in range(1,number + 1):
        a = a * i
    print("factorial number",a)
m(4)

# Write a Python program to print the even numbers from a given list.
def d(numbers):
    for i in numbers:
        if i % 2 == 0:
            print("Even numbers",i)
a= [15,17,30,11,22]
d(a)

