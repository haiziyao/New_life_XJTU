# 类本身就是一个Class对象
class Moster:
    name=None
    def __init__(self,name):
        self.name=name
    def haha(self):
        print("haha")

Moster.haha(Moster)# 类访问非静态方法，需要把类对象传入
# 对于静态方法，不再赘述 @staticmethod
