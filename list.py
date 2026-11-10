# a=[12,11,4.5,"India",True]
# #            01234567
# #   0  1  2   3       4

# print(a[2])
# print(a[3][4])
# a[1]=7
# print(a)
# print(len(a))

# # Exercise 1. Perform Basic List Operations
# numbers = [10,20,30,40,50]
# print("updated list",numbers)

# # Exercise 2. Perform List Manipulation
a= [10,20,30,40,50,60,70]
print("list",a)
a.append(10)
print("append",a)
a.insert(2,25)
print("insert",a)
a.remove(40)
print("remove",a)
a.pop()
print("pop",a)

# # Exercise 3. Sum and Average of All Numbers in a List
# b = [12,5,74,110]
# print(sum(b),'-sum of values')
# print(sum(b)/len(b),'-average of value')

# # # Exercise 4. Find Maximum and Minimum from List
b= [20,30,400,1000]
print(max(b),'max')
print(min(b),'min')

# # Exercise 5. Calculate the Product of All Elements
b= [2,30,4.5,900]
var=1
for i in b:
    var= var*i
    print(var,'product')

# # Exercise 6. Count Even and Odd Numbers
b= [1,3,4,9]
even=0
odd=0
for i in b:
    if i%2 ==0:
        even+=1
    else:
        odd+=1
print("Even numbers", even)
print("Odd numbers",odd)

# # Exercise 7. Reverse a List
b= [20,30,400,90]
b.reverse()
print("Reverse",b)

# # Exercise 8. Sort a List of Numbers
b= [280,30,500,900]
b.sort()
print("Sort",b)

# # Exercise 9. Create a Copy of a List
b= [20,300,400,900]
print(b)
c= b.copy()
print(c,"copied value")

# Exercise 10. Combine Two Lists
b= [10,30,400,900]
print(b)
combine= b+c
print(combine,'-combine')
