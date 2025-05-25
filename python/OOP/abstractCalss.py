#抽象类 
from abc import ABC
#继承了 ABC 就成为了抽象类， java也有抽象 abstract ,这里当作接口就好了
#抽象类不能实例化
#至少有一个抽象方法
class Animal(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmenthod
    def cry(self):
        pass