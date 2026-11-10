# class A:
#     a = 100
# class B(A):
#     b = 200
# class C(B):
#     c = 300
# obj = C()
# print(obj.a)
# print(obj.b)
# print(obj.c)

class Cat:
    def speak(self):
       print("Meow")
class Dog:
    def speak(self):
        print("Woof")
animals=[Cat(),Dog()]
for animal in animals:
    animal.speak()

        