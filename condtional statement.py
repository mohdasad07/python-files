# a=10
# if a>=20:
#     print("A is greater than and equal to 200")
# else:
#  print("A is not greater than and equal to 200")

# age = 18
# if age>=18:
#    print("your eligiable for voting")
# else:
#    print("your not eligiable for voting")
age= int(input("enter the age")) # Typecasting
if age>=25:
    print("your eligiable for both")
elif age>=18 and age<21:
    print("your eligiable for voting")
else:
    print("your not eligiable for voting")