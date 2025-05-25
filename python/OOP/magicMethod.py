# 常用的魔术方法
# 在某些事件发生时自动调用 
# __init__
# __str__(self)
#__eq__(self,other)    
# lt小于   le小于等于  ne不等于 gt大于  ge大于等于
#不一一做示范了
 

#比如  重写java的toString()方法
class Moster:
    name=None
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return ""+self.name
    def __eq__(self, value):
        pass    #我们这里重写判断相等的条件
m =Moster("hzy")
print(m)
