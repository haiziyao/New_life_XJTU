class Person:
    name=None
    age:None
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("hahah")


# 父类的非私有 子类可以随便访问
class Student(Person):
    Class:None
    def __init__(self, name, age):
        super().__init__(name, age)
        print("lala")
class Teacher(Person):
    Class:None
stu = Student("lihua",8)

#py支持多继承  不像java那只支持单继承
#多继承的继承等级 class C（A，B）  左边的继承优先级高  有点逆天了多继承
