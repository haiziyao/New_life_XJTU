#类与对象  属性 行为方法 
class Cat:
    Name=None
    Age=None
cat1 = Cat()
cat1.Name="haha"
cat1.age =4
print(cat1.Age)
print(cat1.age)  #这个自定义属性  确实比java离谱多了

# 对象的布尔值
# False 数值0 None 空字符串 空列表 空字典 空元组  空集合   ：这些对象的布尔值 都是false 
print(bool(False))
print(bool({}))
#作用  方便于我们判断 变量是否为None  不像java一样，干啥都得 str.isNull()  ??好像是这个？？三个月没写java忘完了

content =""
if content:
    print("aaa")

#成员方法 
# def 方法名(self,形参列表):
#   方法体 
class Person:
    name=None
    age = None
    def get_name(self,age):
        print(self.age)
        print(age)
    @staticmethod   #静态方法可以不给self
    def getname( ):
        print("haha")
person=Person()
person.age="aa"
# 这些东西都是很简单的OOP了，过一遍就好了  slef 就是 java的this
person.get_name("bb")
person.getname()


#构造方法
class Dog:
    name:None
    age:None
    def __init__(self,name,age):
        self.name=name
        self.age=age
dog1=Dog("damahou",9)
print(dog1.age)

#构造器拓展  多参数
