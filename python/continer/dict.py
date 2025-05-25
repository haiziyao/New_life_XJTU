# key-value  
dict_a={
    'key1':'value1',
    'key2':'value2'
}

key = dict_a['key1'] # 根据key找出value

# 键可以是任何不可变类型，字符串和数字总是可以为键
# 如果一个tuple只包含字符串，数字或元组，那么它也可以是键
# 若元组包含了可变对象，不可作为键，list也不可以

for key in dict_a:
    print(dict_a[key])
for value in dict_a.values():
    print(value)
for key,value in dict_a.items():
    print(f"{key}={value}")
#空字典
dict_null = dict()
dict_null = {}

#key相同，后面的覆盖前面的 
dict_b={
    "a":"a",
    "a":"b"
}
print(dict_b["a"])


len(dict_a)

dict_a['key1']=value   #修改key的value，或者增加一对key：value

del dict_a['key1']

dict_a.pop("key1",'default')  #返回key的value 并移除

dict_a.keys()    #return all keys

bool = key in dict_a  #true or false 

dict_a.clear()       #clear the dict


#字典生成式
#list to dict\
books = ["书1","书2"]
authors =["作者1","作者2"]
result = { book:author+"这里啥都能加" for book,author in zip(books,authors) }
print(result)