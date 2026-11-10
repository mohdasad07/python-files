# a=(7,7,5.5,"uncodemy",True)
# # #           01234567
# # #  0 1 2      3        4
# print(a[1])
# print(a[1:4])
# print(a[::-1])

#  1.Basic Tuple Operations
a= (10,20,30,40, "India", True)
print(a[2])
print(a[2:5])
print("tuple",a)

# Exercise 2: The Trailing Comma
a= (5,)
print(a)

# Exercise 3: Tuple Repetition
a= (5,10,15)
b= a*3
print(b)

# Exercise 4: Tuple Concatenation
a= (12,4,6)
b=(10,20,30)
c = a+b
print(c)

# Exercise 5: Tuple Slicing
print(a[2])
print(c[0:3])

# Exercise 6: Tuple Reversal
print(c[::-1])

# Exercise 7: Counting
print(len(c))

# Exercise 8: Tuple Unpacking
b= (2,4,6)
x,y,z = b
print(x)
print(y)
print(z)

# Exercise 9: The Swap Trick
b = 3,4,5,6,70,80,90
a,b = b,a
print(a)
print(b)

# Exercise 10: Nested Tuple Access
nested= (5,6,8,"Asad",True,(9,7,8,"Asad",(1,1,1.6,"Asad",True),True))
#                                           0 1 2     3      4
#                            0 1 2   3             4                5
#        0 1 2  3       4                      5                                         
print(nested[5][1])
print(nested[5][4][3])
print(nested[5][4][2])
print(nested[5][4][3][3])

