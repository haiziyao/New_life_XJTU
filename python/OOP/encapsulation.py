#私有化 双下划线开头命名就是私有化
class Clerk:
    name:None
    __job:None
    __salary: None
    def __init__(self,name,job,salary):
        self.name=name
        self.__job=job
        self.__salary=salary
    def get_salary(self):
        return self.__salary
boss=Clerk("damahou","chishi",888)
print(boss.name)
print(boss.get_salary())
#python 奇特现象
boss.__salary=999
print(boss.__salary) #此__salary 并不是salary 这里的__属于属性名的一部分 ,而 Clerk里面则是用__作为隐式判定
# 而实际上变量仍然是 salary 而非 __salary