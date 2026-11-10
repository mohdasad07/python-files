i=1
# while i<=5:
#     print(i,end= " ")
#     i+=1
# Exercise 1: Print first 10 natural numbers using while loop
# Exercise 2: Calculate sum of all numbers from 1 to a given number
# Exercise 3: Print multiplication table of a given number
# Exercise 4: Count the total number of digits in a number

# i=1
# while i <= 20:
#     print(i,end =" ")
#     i = i + 1
# Exercise 2: Calculate sum of all numbers from 1 to a given number

# num = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= num:
# #     sum = sum + i
# #     i = i + 1
# # print(sum)
# #  Exercise 3: Print multiplication table of a given number
# num= int(input("enter the number"))
# i=1
# while i <=10:
#     print(num,"*",i,"=" , num * i)
# #     i+=1
# Exercise 4: Count the total number of digits in a number
num = int(input("Enter the number"))
count =0
while num > 0:
    num= num//20
    count +=1

print("Total number of digit:", count)


    

