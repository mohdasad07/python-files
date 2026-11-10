a= lambda x,y,z: print(x+y+z)

a(11,2,7)


# Write a Python program to square and cube every number in a given list of integers using Lambda

a = [2, 3, 4, 5]

square = list(map(lambda x: x**2, a))
cube = list(map(lambda x: x**3, a))

print("Squares:", square)
print("cubes:", cube)

# Write a Python program to count the even and odd numbers in a given list of integers using Lambda.

a= [1,2,3,4,5,6]
even_numbers= list(filter(lambda x: x % 2 == 0, a))
odd_numbers= list(filter(lambda x: x % 2 != 0, a))
print(even_numbers)
print(odd_numbers)

#  Write a Python program to add two given lists using map and lambda.
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

c = list(map(lambda x, y: x + y, a, b))

print(c)

# Write a Python program to sort tuples using Lambda.
tup= (200,400,500,100,70,65,11)
tup1= list(tup)
sorting= sorted(tup1, key= lambda x:x)
print(tuple(sorting),'sorting')