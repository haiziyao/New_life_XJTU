``` bash
sh 文件  #可以直接执行shell脚本

```



``` bash
set  #显示当前所有变量

# 语法
变量名=值  #绝对不能有空格
unset  变量   #撤销变量
readonly  变量  #静态变量，不能unset

#quick test 
#!/bin/bash     
A=100
echo $A
echo "$A"
unset A
readonly B=2
echo $B
C=`date`    #Tab 上面那个键  这里的意思是date是一个命令，
# 是在把date所得到的结果赋值给C
D=$(date)

echo "tomcat_home=$TOMCAT_HOME"

#注释  :<<!  内容 ！
:<<!   !


#运行时候传入参数
$n   $0  : 是程序本身   $1  :等其他是传入的其他参数
$*  把所有参数看作为一个整体
$@  表示所有参数，只不过不看成一个整体
$#  表示传入参数的个数

```

``` bash
 #运算符
 $((运算表达式))
 $[运算表达式]
 expr 表达式

res=$((2+3*4))
res=$[2*3+5]
res='espr 2*3+6'


```

``` bash
#条件判断
#单分支
if [ condition ] # condition其前后都要有空格
then 
 	命令
fi
#多分支
if [ 条件判断 ]
then 
	代码
elif [ 条件判断 ]
then
	代码
fi

#符号的介绍
	#字符串比较
		#  =  判断是否相等
	#整数的比较
		# -lt 小于
		# -le 小于等于
		# -eq 等于
		# -gt 大于
		# -ge 大于等于
		# -ne 不等于
	#按照文件权限判断
    	# -r -w -x
    #文件类型
    	# -f  文件存在而且是一个常规文件
    	# -e 文件存在
    	# -d 文件存在而且是一个目录
    	
```



```  bash
#case语句

case $vary in
``value1``)
 代码
;;
``value2``)
;;
*)
;;
esac

```

``` bash
#for 循环
for value in V1 V2 V3 V4
do
代码
done

for (( 初始值;循环控制条件;变量变化 ))
```

``` bash
#while
while [ 条件判断 ]
do
代码
done

```

``` bash
#read 读取控制台输入
read(选项)(参数)
  -p  #指定读取值时的提示符
  -t  #指定读取值时的等待的时间，单位是秒,
  read -t 5 -p "请输入一个数" value
  
```

``` bash
#basename 返回路径的最后的部分,常常用于获取文件名字
basename [pathname] [suffix]
basename /home/aa/test.txt # 返回 test.txt
basename /home/aa/test.txt .txt #返回 test

dirname /home/aa/test.txt  #返回/home/aa
```

``` bash
#自定义函数
[ function ] funname[()]
{
	Action;
	[return int;]
}

#例子
function getSum(){
	SUM=$[$n1+$n2]
	echo "和是$SUM"
}
```

``` bash
#实战练习————备份数据库

```

