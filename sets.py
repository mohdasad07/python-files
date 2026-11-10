# a={5,5,1,2,0,6.5,"Uncodemy",True,False}
# print(len(a))

# a.add(46)
# print(a)
# a.remove(0)
# print(a)
# a.discard(46)
# print(a)

# Exercise 1: Basic Set Operations
a={1,2,4,7,8.5,10,"India", True}
print(len(a))

a.add(99)
print(a)
a.remove(7)
print(a)
a.discard(99)
print(a)

# Exercise 2: Clear All Elements
a.clear()
print(a)

# Exercise 3: Find the Length of a Set
a={5,5,1,4.5,"Asad",True,False}
print(len(a))

# Exercise 4: Check if a Set is Empty
if len(a) ==0:
    print("set is empty")
else:
    print("set is not empty")

# Exercise 5: Union of Sets
set1={1,2,3,4}
set2={3,4,5}
union_set=set1|set2
print("The number of sets",union_set)

# Exercise 6: Intersection of Sets
intersection_set = set1 & set2
print("Intersection sets" ,intersection_set)

# Exercise 7: Difference of Sets
difference_set= set1 - set2
print("Difference of sets",difference_set)

# Exercise 8: Symmetric Difference
symmetric_difference = set1^set2
symmetric_difference=set1.symmetric_difference(set2)
print("symetric difference",symmetric_difference)

# Exercise 9: Find Max and Min
print("max",max (set2))
print("min",min(set1))

# Exercise 10: Sum of Set Elements
a={100,300,200,400}
sum= sum(a)
print("Sum Value ", sum)