# 元素不可重复的,存储顺序与添加时间无关  
set_a = {100,100}  
print(f"{type(set_a)}  {set_a}")

set_null = set()
print(set_null)

set_aa   ={}    # 字典类型 
print(type(set_aa))  

a={1,2,3,5,7,9}
b={1,2,4,6,8,0}

len(a)  #返回长度

print( 1 in a)  #ele 是否在 set 中 : ele in set

a.add(11)   # set.add(ele)
a.remove(11) # set.remove(ele)  如果集合中不存在ele，则报错KeyError
a.pop()   # set.pop()   随机删除一个数据

c=a.union(b)  # set.union(set)  求并集
d=a|b           #求交集
 
print( a.intersection(b))  #求交集
print( a&b )   

print( a.difference(b) ) #求差集
print( a-b )