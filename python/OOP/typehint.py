# 弱类型语言为了防止传参类型错误，所以添加了这个
# 对实际代码没有任何影响

def fun1(a:str):
    for ele in a:
        print(ele)
fun1("ddddd")

# 变量类型注解 
n1 :int = 4
n2 :float =5
is_pass :bool = False
name : str = "fdhsajhf"
my_list :list =[1]
my_tuple :tuple  =(1,)
my_set :set ={1}
my_dict :dict={"key":"value"}

my_list_:list[str] = ["df"]
my_dict_:dict[str,int] ={"key":5}

#注释中注解 
n2=5 # type: int  #pycharm中这个确实会有高亮，但是vscode没有高亮规则


# 函数的类型注解
# def fun()  ->int :
def fun1(a:int) ->int :
    return a*a


#类型注解只是提示性的，并不是器强制性的，所以并不会报错(如果是代码过程报错那不属于我所说的报错)，但仍然会运行


#Union  联合类型 
from typing import Union
n3 :Union[int,float] = 5
