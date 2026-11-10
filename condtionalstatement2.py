# # # - WAP to find greatest of 3 numbers a=10,b=27,c=6.
# # # - WAP to check whether 10 is divisible in both 2 and 4.
# # # - WAP to check whether 8 is divisible in either 3 or 4.
# # a=1
# # b=2
# # c=6
# # if a>b and a>c:
# #     print("a is greater than b and c ")
# # elif b>c and b>a:
# #     print("b is greater than a and c")
# # else:
# #     print("c is greater than a and b")

# if 10%2 ==0and 10%4 ==0:
#     print("10 is divisible in both 2 and 4")
# else:
#     print("10 is not divisble in both 2 and 4")

# if 8%3==0 or 8%4==0:
#     print("8 is divisble in either 3 or 4")
# else:
#     print("8 is not divisble in either 3 or 4")

# marks = 20
# if marks>=76 and marks<=100:
#     print("Grade A")
# elif marks>= 51 and marks<= 75:
#     print("Grade B")
# elif marks>=26 and marks<= 50:
#     print("Grade C")
# else:
#     print("Grade D")
# number = 25
# if number>1:
#     print("number is positive")
# elif number< 1:
#     print("number is negative")
# else:
#     print("number is zero")

# number2 = 54
# if number2%2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

a= int(input("Enter the number 1:"))
b= int(input("Enter the number 2:"))
c= int(input("Enter the number 3:"))

if a>b and a>c:
    print("a is greater than b and c")
elif b>a and b>c:
    print("b is greater than a and c")
else:
    print("c is greater than b and a")

 