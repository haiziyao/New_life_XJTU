# 多态：参数为父类型 时，可以传子类对象
class Animal:
    name:None
    def __init__(self,name):
        self.name =name
    def cry(self):
        print(f"{self.name}  叫叫叫")
class Cat(Animal):
    def __init__(self,name):
        name ="cat"+name
        super().__init__(name)
class Dog(Animal):
    def __init__(self,name):
        name ='dog'+name
        super().__init__(name)
def cry(animal:Animal):
    animal.cry()
cat=Cat("lala")
cry(cat)