#list tuple 都可以
# 语法：序列[起始索引：结束索引：步长]  左闭右开
str = "hello,world"
str_slice = str[0:5:1]
print(str_slice) #hello
print(str[:5:])  #默认规则 起始索引默认0  结束索引默认最后  步长默认为1
#负数截取
str[-1:-6:-1]  #这个非常有意思 即是截取(-6,-1] 这个左开右闭优点反常识
