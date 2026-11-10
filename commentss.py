class A:

    a = 44

    def __init__(self, b, c):
        print("Uncodemy")
        print(b + c)

obj = A(44, 55)

class car:
    wheel = 6
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

    def display_info(self):
        print(f'{self.model}{self.brand} has {self.wheel} wheels')

car_obj = car("BMW", "X1")
car_obj.display_info()

    
