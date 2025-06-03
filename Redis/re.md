### NoSQL概述

Not only SQL : 泛指非关系型数据库。以<font color=red>key-value</font>模式存储

* 不支持SQL标准
* 不支持ACID
* 远超于SQL性能

#### 使用场景

* 数据高并发的读写
* 海量数据的读写
* 对数据高扩展性的

#### NoSQL不适用场景

* 需要事务支持
* 需要即席查询

### Redis 概述

+ value 支持的类型相对更多 string list set zset hash
+ 数据支持push pop add remove 以及其他丰富操作
+ 支持不同排序方式
+ 缓存在内存中
+ 周期性保存在磁盘
+ master-slave

### Redis安装

不考虑windows，直接在linux上   

单线程+多路IO复用

<font color=red>需要c语言环境</font>

``` bash
yum install gcc
make
make install
#前台启动
redis-server
#后台启动
cd /opt #redis.conf
cp redis.conf /etc/redis.conf
vim redis.conf
daemonize no -> yes
redis-server /etc/redis.conf
ps -ef #查看进程
redis-cli #连接
ping 
shutdown #关闭
或者直接杀死进程
kill -9 kid
```

默认用的是6379端口