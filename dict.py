# Exercise 1: Basic Dictionary Operations
# a={"name":"Asad","age":"35"}
# a["location"]= "Bangalore"
# print(a)
# a["name"]="Asad khan"
# print(a)
# del a["age"]
# print(a)

# Exercise 2: Dictionary Operations
# Exercise 3: Dictionary from Two Lists
# Exercise 4: Clear Dictionary
# Exercise 5: Merge Dictionaries
# Exercise 6: Access Nested Dictionary
# Exercise 7: Access ‘history’ Key From a Nested Dictionary
# Exercise 8: Initialize Dictionary with Default Values
# Exercise 9: Rename a Key of Dictionary
# Exercise 10: Delete a List of Keys

# Exercise 2: Dictionary Operations
a={"name":"Asad","age":35,"city":"Bangalore"}
print(a["name"])

# Exercise 3: Dictionary from Two Lists
a= ["name","age","city"]
b= ["Asad","35","Bangalore"]
a = dict(zip(a, b))
print(a)

# Exercise 4: Clear Dictionary
a = {"name": "Asad","age": 35,"city": "Bangalore"}
a.clear()
print(a)

#  Exercise 5: Merge Dictionaries
a = {"name": "Asad","age": 35}
b= {"city": "Bangalore"}
a.update(b)
print(a)

#  Exercise 6: Access Nested Dictionary
a = {"name": "Asad","details": {"age": 36,"city": "Bangalore"}}
print(a["details"]["age"])
print(a["details"]["city"])

#  Exercise 7: Access ‘history’ Key From a Nested Dictionary
a = {"name": "Asad","Marks": {"history": 85,"Maths": "65","Science":45}}
print(a["Marks"]["history"])

# # Exercise 8: Initialize Dictionary with Default Values
a= ["English","Maths","History"]
marks= dict.fromkeys(a,45)
print(marks)

# Exercise 9: Rename a Key of Dictionary
a = {"name": "Asad","age": 35,"city": "Bangalore"}
a["location"] = a.pop("city")
a.pop("age")
print(a)

# Exercise 10: Delete a List of Keys
a = {"name": "Asad","age": 35,"city": "Bangalore"}
del a["city"]
del a["age"]
print(a)

