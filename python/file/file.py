# open(file,model='',buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None):
#model: r读取 w写入 a追加 b二进制模式 t文本模式（默认） +打开用于更新 x排他性创建

#f.read(size)
#f.readline()  字符串末尾保留换行符
#list(f) f.readlines() 返回一个lines的列表
#for line in f:
#f.write(str)
#f.flush()
#f.close()
#with open() as f:  文件会自动关闭

import os,time 
if os.path.exists(""):
    os.remove("")
else:
    pass

os.makedirs()
os.rmdir()

st = os.stat()  #获取文件相关信息
st.st_size() #文件大小
# 这边有很多方法，没用过，先不写那么多了
